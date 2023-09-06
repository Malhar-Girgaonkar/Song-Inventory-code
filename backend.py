import sqlite3
import os
import shutil
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
from customtkinter import filedialog
import eyed3


class Backend():
    def __init__(self) -> None:
        #check if database.db is exists or else call create_database
        self.db_exists = self.check_database_exists()
        if not self.db_exists:
            self.create_database()


    def check_database_exists(self):
        #returns true if database exists and false otherwise
        try:
            conn = sqlite3.connect('database.db')
            conn.close()
            return True
        except sqlite3.OperationalError:
            return False


    def get_directory_name(self):
        #file dialogue to select directory of songs
        self.folderpath=filedialog.askdirectory()
        return(self.folderpath)


    def store_path(self,path):
        #store in database
        try:
            # Store in database
            conn = sqlite3.connect("database.db")
            mycursor = conn.cursor()
            query = "INSERT INTO paths(path) VALUES (?)"
            values = (path,)
            mycursor.execute(query, values)
            conn.commit()
            conn.close()
            # Display successfull message
            msg2=CTkMessagebox(title="Success", message="Path Stored",icon="check", option_1="Ok")
            if msg2.get()=="Ok":
                msg2.destroy()
        except sqlite3.Error as e:
            # Handle any errors that occur during the process
            msg2=CTkMessagebox(title="Error", message=e,icon="cancel", option_1="Ok")
            if msg2.get()=="Ok":
                msg2.destroy()


    def create_database(self):
        try:
            conn=sqlite3.connect("database.db")
            cursor = conn.cursor()
            print("\n\nCREATING TABLE\n\n")
            # Create the "paths" table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS paths (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    path TEXT NOT NULL UNIQUE
                )
            ''')
            # Create the "music_info" table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS music_info (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    artist TEXT,
                )
            ''')
            # Commit the table creation
            conn.commit()
            conn.close()
            print("executed create table")
        except sqlite3.Error as e:
            msg2=CTkMessagebox(title="Error", message=e,icon="cancel", option_1="Ok")
            if msg2.get()=="Ok":
                msg2.destroy()

    def song_exists_in_database(self, title, artist):
        conn = sqlite3.connect("database.db")
        mycursor = conn.cursor()
        query = "SELECT id FROM music_info WHERE title = ? AND artist = ?"
        values = (title, artist)
        mycursor.execute(query, values)
        existing_song = mycursor.fetchone()
        conn.close()
        return existing_song is not None

    def read_metadata_from_mp3(self, mp3_file_path):
        try:
            audiofile = eyed3.load(mp3_file_path)
            if audiofile.tag is not None:
                title = audiofile.tag.title
                artist = audiofile.tag.artist
                return title, artist
            else:
                return None, None,
        except Exception as e:
            print(f"Error reading metadata from {mp3_file_path}: {e}")
            return None, None

    # Methodto iterate through all MP3 files in a folder and store their metadata
    def read_metadata_from_folder(self, folder_path):
        mp3_files = [f for f in os.listdir(folder_path) if f.endswith('.mp3')]
        for mp3_file in mp3_files:
            mp3_file_path = os.path.join(folder_path, mp3_file)
            title, artist= self.read_metadata_from_mp3(mp3_file_path)
            if title is not None:
                # Store the metadata in your database
                self.store_metadata_in_database(title, artist)
                
    # Add a method to store metadata in your database
    def store_metadata_in_database(self, title, artist):
        if not self.song_exists_in_database(title, artist):
            try:
                conn = sqlite3.connect("database.db")
                mycursor = conn.cursor()
                query = "INSERT INTO music_info (title, artist) VALUES (?, ?)"
                values = (title, artist)
                mycursor.execute(query, values)
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                # Handle any errors that occur during the process
                msg2=CTkMessagebox(title="Error", message=e,icon="cancel", option_1="Ok")
                if msg2.get()=="Ok":
                    msg2.destroy()
        else:
            # Song with the same title and artist already exists in the database, skip it
            print(f"Song '{title}' by '{artist}' already exists in the database. Skipping...")



