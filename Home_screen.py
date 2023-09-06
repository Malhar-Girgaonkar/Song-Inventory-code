from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
from customtkinter import filedialog
import tkinter as tk
import mysql.connector
import subprocess
import sqlite3
import os
import shutil
from backend import Backend




ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
appWidth, appHeight = 880,700

class MyFramegreeting(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #label1 for Greeting
        self.uname=ctk.CTkLabel(self, text="Home Page",anchor="center",text_color="Green",font=("Helvetica",30,"italic"))
        self.uname.grid(row=0,column=0,columnspan=2,padx=20,pady=20,sticky="ew")

class MyFrameInfo(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #Label for frame
        self.frame_header=ctk.CTkLabel(self, text="Information",anchor="w",text_color="blue",font=("Helvetica",25,"italic"))
        self.frame_header.grid(row=0,column=0,padx=20,pady=20,sticky="ew")
        #label for Info
        self.text="""\
This application is used to do the following:

- Store metadata of songs in a database
- Keep track of downloaded songs
- Display information like title, artist, genre
- Useful for managing your music library
"""
        self.Info=ctk.CTkLabel(self, text=self.text,anchor="w",font=("Helvetica",20,"italic"))
        self.Info.grid(row=1,column=0,padx=20,pady=20,sticky="ew")

class Myframework(ctk.CTkFrame):
    def get_directory(self):
        #redirects to backend.py
        self.directory_name=self.bk.get_directory_name()
        #print("folder:",self.directory_name)
        self.label_directorypath.configure(text=self.directory_name)

    def store_directory(self):
        #redirects to backend.py
        self.bk.store_path(self.directory_name)

    def read_data(self):
        self.bk.read_metadata_from_folder(self.directory_name)

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #backend instance bk
        self.bk=Backend()
        #Label for getting directory name
        self.label_getdirectory=ctk.CTkLabel(self, text="Select folder: ",anchor="w",font=("Helvetica",20,"italic"))
        self.label_getdirectory.grid(row=0,column=0,padx=20,pady=20,sticky="ew")
        #button for Redirect to get_directory
        self.btngetdirectory=ctk.CTkButton(self,text="Select",command=self.get_directory)
        self.btngetdirectory.grid(row=0, column=1,padx=20, pady=20,sticky="ew")
        #Label for adding directory path to database
        self.label_storedirectory=ctk.CTkLabel(self, text="Store folder path: ",anchor="w",font=("Helvetica",20,"italic"))
        self.label_storedirectory.grid(row=1,column=0,padx=20,pady=20,sticky="ew")
        #button for Redirect to get_directory
        self.btngetdirectory=ctk.CTkButton(self,text="Store",command=self.store_directory)
        self.btngetdirectory.grid(row=1, column=1,padx=20, pady=20,sticky="ew")
        #Label to show selected directory path
        self.label_showdirectorypath=ctk.CTkLabel(self, text="Selected path: ",anchor="w",font=("Helvetica",20,"italic"))
        self.label_showdirectorypath.grid(row=2,column=0,padx=20,pady=20,sticky="ew")
        self.label_directorypath=ctk.CTkLabel(self, text="...",anchor="w",font=("Helvetica",15,"italic"))
        self.label_directorypath.grid(row=2,column=1,padx=20,pady=20,sticky="ew")
        #Label for reading all metadata of all files in given directory
        self.label_readmetadata=ctk.CTkLabel(self, text="Read Metadata: ",anchor="w",font=("Helvetica",20,"italic"))
        self.label_readmetadata.grid(row=4,column=0,padx=20,pady=20,sticky="ew")
        #button for Redirect to gread_data
        self.btnreadmetadata=ctk.CTkButton(self,text="Start",command=self.read_data)
        self.btnreadmetadata.grid(row=4, column=1,padx=20, pady=20,sticky="ew")






class Homepageapp(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Home Page")
        
        # Calculate the coordinates for centering the window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_position = (screen_width - appWidth) // 2
        y_position = (screen_height - appHeight) // 2

        # Set the geometry of the window to open it at the center
        self.geometry(f"{appWidth}x{appHeight}+{x_position}+{y_position}")
        self.resizable(True, True)
        self.attributes('-topmost', True)

        #frame Greeting  frame
        self.greeting_frame = MyFramegreeting(master=self)
        self.greeting_frame.grid(row=0, column=0,columnspan=2,rowspan=1,padx=20,pady=20,sticky="nsew")

        #frame for information display
        self.info_frame=MyFrameInfo(master=self)
        self.info_frame.grid(row=1, column=0,columnspan=1,rowspan=1,padx=20,pady=20,sticky="nsew")
        #frame for buttons
        self.work_frame=Myframework(master=self)
        self.work_frame.grid(row=1, column=1,columnspan=1,rowspan=1,padx=20,pady=20,sticky="nsew")



if __name__=="__main__":
    Homepage_app=Homepageapp()
    Homepage_app.mainloop()