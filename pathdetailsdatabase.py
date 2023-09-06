import sqlite3

# Establish a connection to the SQLite database
connection = sqlite3.connect("database.db")
cursor = connection.cursor()


# Create the "paths" table
#cursor.execute("CREATE TABLE IF NOT EXISTS paths (id INTEGER PRIMARY KEY AUTOINCREMENT,path TEXT NOT NULL UNIQUE)")
# Create the "music_info" table
#cursor.execute("CREATE TABLE IF NOT EXISTS music_info (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT NOT NULL,artist TEXT)")

# DISPLAYING paths TABLE
#cursor.execute("PRAGMA table_info(paths)")
#for x in cursor:
#   print(x)


# DELETING DATA IN paths TABLE
#cursor.execute("DELETE FROM paths WHERE  path= ?", ("path_of_directory",))


#DELETING ALL DATA IN USERLOGIN TABLE
#cursor.execute("Delete FROM paths")

#DELETING ALL DATA IN music_info TABLE
#cursor.execute("Delete FROM music_info")


# CHECKING TABLE DATA
cursor.execute("SELECT * FROM music_info")
for x in cursor:
    print(x)

# Commit the changes and close the connection
#If use user create,delete,truncate,update queries from above and want to save changes in database then uncomment below line
#connection.commit()
connection.close()
