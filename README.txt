The credentials.py file contains two dictionaries: 

login = {
    'username' : 'YOUR_USERNAME',
    'password' : 'YOUR_PASSWORD'
}

path = {
'print' : 'ABSOLUTE_PATH_TO_FILES_TO_PRINT'
}

As we import credentials at the top of the printToLibrary.py script,
we can access the 'username' value with: credentials.login["username"]

In order to run the script, fill in the 'YOUR_USERNAME' and 'YOUR_PASSWORD'
fields with your ssc login credentials. Fill in the 
'ABSOLUTE_PATH_TO_FILES_TO_PRINT' with the absolute path to the folder
containing the documents you want to print, e.g. 'C:\\Users\\UBCStudent\\Desktop\\Print'.
