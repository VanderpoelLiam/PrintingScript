import credentials
import os
import time
import send2trash
from selenium import webdriver
from pyautogui import typewrite, press, prompt, click

def filenameMeetsRequirements(filename):
    """Checks if filename is one of the allowed filetypes that can be
    printed.
    Inputs:
        filename, String
            Name of file including filetype extention.
    Outputs:
        Boolean
            Whether or not the requirement is satisfied.
    """
    return filename.endswith(".xlam") or filename.endswith(".xls") or filename.endswith(".xlsb") or filename.endswith(".xlsm") or filename.endswith(".xlsx") or filename.endswith(".xltm") or filename.endswith(".xltx") or filename.endswith(".pot") or filename.endswith(".potm") or filename.endswith(".potx") or filename.endswith(".ppam") or filename.endswith(".pps") or filename.endswith(".ppsm") or filename.endswith(".ppsx") or filename.endswith(".ppt") or filename.endswith(".pptm") or filename.endswith(".pptx") or filename.endswith(".doc") or filename.endswith(".docm") or filename.endswith(".docx") or filename.endswith(".dot") or filename.endswith(".dotm") or filename.endswith(".dotx") or filename.endswith(".rtf") or filename.endswith(".pdf") or filename.endswith(".bmp") or filename.endswith(".dib") or filename.endswith(".gif") or filename.endswith(".jfif") or filename.endswith(".jif") or filename.endswith(".jpe") or filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".tif") or filename.endswith(".tiff") or filename.endswith(".xps")

def getFilesToPrint(flag):
    """Returns a list of the files in the print directory provided by
    credentials.path["print"] that satisfy the requirements in the
    filenameMeetsRequirements method. The output contains either a list of the
    absolute paths to each file, or the absolute path to the folder followed by
    all the filenames
    Inputs:
        flag, Boolean
            If True, return list of absolute paths to files
            If False, return list with the absolute path to the folder as the
            first entry, followed by all the filenames
    Outputs:
        filesToPrint, list
            List of Strings of the absolute path to the files to print.
    """
    filesToPrint = []
    if flag:
        for folderPath, subfolders, filenames in os.walk(credentials.path["print"]):
            for filename in filenames:
                if filenameMeetsRequirements(filename):
                    filesToPrint.append(os.path.join(folderPath, filename))
    else:
        for folderPath, subfolders, filenames in os.walk(credentials.path["print"]):
            filesToPrint.append(folderPath)
            for filename in filenames:
                if filenameMeetsRequirements(filename):
                    filesToPrint.append(filename.split(".")[0])
    return filesToPrint

def credentialsNotValid():
    return credentials.login["username"] == 'YOUR_USERNAME' or \
        credentials.login["password"] == 'YOUR_PASSWORD' or \
        credentials.path["print"] == 'ABSOLUTE_PATH_TO_FILES_TO_PRINT'

def signIn(browser):
    usernameInput = browser.find_element_by_id("inputUsername")
    passwordInput = browser.find_element_by_id("inputPassword")
    usernameInput.send_keys(credentials.login["username"])
    passwordInput.send_keys(credentials.login["password"])

    logInBtn = browser.find_element_by_name("$Submit$0")
    logInBtn.click()

def uploadFiles(browser, files):
    webPrintBtn = browser.find_element_by_id("linkUserWebPrint")
    webPrintBtn.click()

    submitBtm = browser.find_element_by_link_text("Submit a Job »")
    submitBtm.click()

    monoDuplePrinter = browser.find_element_by_id("printer-10156")
    monoDuplePrinter.click()

    optionsBtn = browser.find_element_by_class_name("right")
    optionsBtn.click()

    uploadDocs = browser.find_element_by_class_name("right")
    uploadDocs.click()

    uploadFromBtn = browser.find_element_by_id("upload-from")
    uploadFromBtn.click()
    time.sleep(0.5)

    for i, filename in enumerate(files):
        if i == 0:
            print(filename)
            typewrite(filename)
            time.sleep(0.5)
            press('enter')
        else:
            print("UPLOADING FILE: " + filename)
            typewrite('"' + filename + '" ')
            
    time.sleep(0.5)
    press('enter')

    uploadAndComplete = browser.find_element_by_class_name("right")
    uploadAndComplete.click()

def clearPrintFolder(files):
    for filename in files:
        print("DELETING FILE: " + filename.split("\\")[-1])
        send2trash.send2trash(filename)

def printNow(browser):
    printerIdMap = ['library\WOODWARD-RP1', 'library\HUMANITIES-RP2',\
                    'library\KOERNER-RP2', 'library\EDUCATION-RP1',\
                    'library\LAW-RP1', 'library\IKB-RP1']

    num = prompt("If you want to print now, select the printer you wish to print\n \
          to from the list below:\n \
          1: Woodward Library, near Ref Desk\n \
          2: Koerner Level 2, near HSS Reference Desk\n \
          3: Koerner Level 3, opposite of Circ Desk\n \
          4: Education Library, near Circulation Desk\n \
          5: Law Library, Main level copy room\n \
          6: IKB Level 3, Library side\n\
          For example, to select the 'Woodward Library, near Ref Desk\n\
          printer, enter '1' and press OK or enter.\n\
          Press Cancel or enter nothing to skip this step.")

    if not(num is None or num == ""):
        try:
            num = int(num)
            if 1 > num or num > 6:
                raise ValueError

            printer = printerIdMap[num-1]
            print(printer)

            for filename in files:
                print("PRINTING FILE: " + filename)
                assert(False)
                browser.find_element_by_link_text('Held in a queue').click()
                browser.find_element_by_link_text(printer).click()
        except ValueError:
            printNow(browser)


def main():
    if credentialsNotValid():
        print("You need to fill in the credentials.py file.")
        print("Please look at the README for instructions.")
        return

    files_abs   = getFilesToPrint(True)
    files_names =  getFilesToPrint(False)

    if len(files_abs) == 0:
        print("There are no files to print.")
        return

    browser = webdriver.Firefox()
    browser.get('https://payforprint.ubc.ca:9192/user')



    try:
        signIn(browser)
        uploadFiles(browser, files_names)
        print("======================================================================")
        print("|| YOUR FILES HAVE BEEN UPLOADED TO THE LIBRARY MONO DUPLEX PRINTER ||")
        print("======================================================================")
        print("\n")

        # TODO fix this method
        # printNow(browser)
    except:
        print("There has been an issue, your files may not have been uploaded.")
    finally:
        time.sleep(5)
        assert(False)
        clearPrintFolder(files_abs)
        #browser.quit()

if __name__ == '__main__':
    main()
