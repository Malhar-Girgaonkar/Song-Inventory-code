============================================================================================================================================================================================
                                                                                         READ FOR INFORMATION
============================================================================================================================================================================================


Project Description:
.......................
This a simple and fun application that i have made to solve a little personal problem of having huge ammount of downloaded mp3 songs but no proper management.I like to keep my music data secure for future incase something happens to my hardwaare and for this i made this application that takes a folder and stores it's path in a database and goes in that folder and reads all the mp3 files and extracts their metadata using the eyed3 python module and then stores this data in an database created with sqlite3.

============================================================================================================================================================================================

Usage:
......
1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the main script: `python Login.py`.

============================================================================================================================================================================================

First time?Learn to setup the project
-------------------------------------
-If you are running the program first time or downloaded the program just now.Do folowing to set up the project.
	-First run requirements.py to install python modules needed
	-Second check if there is a file named userinfo.db in same folder as login.py
		-If not then run databasecreatelite.py present in app data/database to create userinfo.db using sqlite3
		-If yes then skip
	-if all of this is done successfully then check if userinfo.db is working properly by following steps
		-run the sqlite3conn.py file and it must give following output
			-output=('admin', 'Admin@123')
		-**IMPORTANT*=If you dont want to enter your data and just use application use following administrative credentials
			-username=admin
			-password=Admin@123
-**IMPORTANT**=Everytime you run the program make sure to open the project file in VScode and then move ahead
-Gateway file for program is Login.py from where program will direct you ahead
-Incase of any errors and database issue do following
	-Make sure you opened project file in VScode as thhe file paths in program use relative path and can give error if not run from project directory
	-For database error like "userinfo.db denied access" make sure userinfo.db is having read,write permissions in properties under security
	-For userinfo.db not found just run the databasecreatelite.py file in app data/Database directory
	-If error is unknown search it on https://openai.com/blog/chatgpt or google.I am sure someone would have answered the question :)

	

============================================================================================================================================================================================

Features:
..........
- Helps keep personal music data like song name, artist name,etc safe incase of sstem failure or loss of data.
- Helps use secure DBMS service.

============================================================================================================================================================================================

Technology stack:
	-CTkMessagebox
	-customtkinter (and its submodules)
	-tkinter (and its submodules)
	-mysql.connector
	-eyed3
	-os
	-shutil
	-sqlite3
	-Backend


============================================================================================================================================================================================

License:
........
This project is MIT License.
Feel free to use it at your will :)
A thanks in heart is all i need ;)
 
============================================================================================================================================================================================

Contact:
.......
For any questions or feedback, please contact:
- Email: malhargirgaonkar@gmail.com