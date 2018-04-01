# This script helps you print quickly to UBC printers.

Before the script can be run fill in the following fields in credentials.py:
```python
login = {
    'username' : 'YOUR_USERNAME',
    'password' : 'YOUR_PASSWORD'
}

path = {
'print' : 'ABSOLUTE_PATH_TO_FILES_TO_PRINT'
}
```

Fill in the 'YOUR_USERNAME' and 'YOUR_PASSWORD' fields with your ssc login credentials. Fill in the 'ABSOLUTE_PATH_TO_FILES_TO_PRINT' with the absolute path to the folder containing the documents you want to print, e.g. 'C:\\Users\\UBCStudent\\Desktop\\Print'.

The script can now be run by typing the following into the cmd line:

python printToLibrary.py

## The script in action

![The script in action](https://github.com/VanderpoelLiam/PrintingScript/blob/master/printingScriptInAction.gif)
