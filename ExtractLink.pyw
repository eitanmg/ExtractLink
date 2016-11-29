#---------------------------------------------------Imports-----------------------------------------------
from Tkinter import *
import tkFileDialog as filedialog
import mailbox
from datetime import datetime
from os import listdir
from os.path import isfile, join
import re
import tkMessageBox
import tldextract
import os, shutil
#---------------------------------------------------End of Imports-----------------------------------------

dir_path = os.path.dirname(os.path.realpath(__file__)) # get current working directory

#---------------------------------------------------Code---------------------------------------------------

def browsefuncinput():
    filename = filedialog.askdirectory()
    path_input.delete('1.0', END)
    path_input.insert('1.0', filename)


def browsefuncoutput():
    filename = filedialog.askdirectory()
    pathoutput_input.delete('1.0', END)
    pathoutput_input.insert('1.0', filename)


def browsewhitelist():
    filename = filedialog.askopenfilename()
    whitelist_input.delete('1.0', END)
    whitelist_input.insert('1.0', filename)


def ValidateInput():
    inputTextBox = path_input.get('1.0', END).strip('\n')
    outputTextBox = pathoutput_input.get('1.0', END).strip('\n')
    if (inputTextBox == "") or (outputTextBox == ""):
        return False
    return True


def delete_files_in_folder():
    emails_folder = dir_path + '\Emails'
    results_folder = dir_path + '\Results'

    num_of_files_in_emails = len(os.walk(emails_folder).next()[2])
    num_of_files_in_results = len(os.walk(results_folder).next()[2])

    if num_of_files_in_emails == 0 and num_of_files_in_results == 0:
        tkMessageBox.showinfo("No files to delete", "No files to delete")
    else:
        try:
            for the_email_file in os.listdir(emails_folder):
                email_file_path = os.path.join(emails_folder, the_email_file)
                if os.path.isfile(email_file_path):
                    os.unlink(email_file_path)
            for results_the_file in os.listdir(results_folder):
                results_file_path = os.path.join(results_folder, results_the_file)
                if os.path.isfile(results_file_path):
                    os.unlink(results_file_path)
            # elif os.path.isdir(file_path): shutil.rmtree(file_path) # uncomment delete also folders in this path
            tkMessageBox.showinfo("Done", "files deleted successfully" + '\n' + str(num_of_files_in_emails) + ' deleted from Emails folder' + '\n' + str(num_of_files_in_results) + ' deleted from Results folder')
        except Exception as e:
            tkMessageBox.showinfo("An error occurred", e)


def readFilesInFolder():
    isWhiteListOn = True
    if whitelist_input.get('1.0', END).strip('\n') == "":
        isWhiteListOn = False
    validationAnswer = ValidateInput()
    lines_seen = set()
    excludeSigns = ['.PNG', '.jpg', '.JPG', '.pdf', '.PDF']
    if validationAnswer is True:
        todayDateAndTime = datetime.now()
        onlyfiles = [f for f in listdir(path_input.get('1.0', END).strip('\n')) if isfile(join(path_input.get('1.0', END).strip('\n'), f))]
        resultFile = open(pathoutput_input.get('1.0', END).strip('\n') + '//Results - ' + todayDateAndTime.strftime('%Y-%m-%d %H-%M-%S') + '.txt', 'a')
        for p in onlyfiles:
            with open(path_input.get('1.0', END).strip('\n') + '//' + p ,'r') as rawFile:
                content = rawFile.readlines()
                for line in content:
                    answer = checkIfContainURL(line)
                    if answer != 'NoUrlsInLine':
                        for a in answer:
                            if a.endswith(('.png', '.PNG', '.jpg', '.JPG', '.jpeg', '.JPEG', '.PDF', '.pdf', '.gif', '.GIF')):
                                pass
                            else:
                                if isWhiteListOn is True:
                                    iswhitelist = checkIfWhiteList(a)
                                    if iswhitelist is False:
                                        if a not in lines_seen:
                                            resultFile.write(a + '\n')
                                            lines_seen.add(a)
                                else:
                                    if a not in lines_seen:
                                        resultFile.write(a + '\n')
                                        lines_seen.add(a)

        resultFile.close()
        tkMessageBox.showinfo("Done", "All done" + '\n\n' + 'The file: ' + '\n\n' + resultFile.name + '\n\n' + 'created successfully in Results folder')
    else:
        tkMessageBox.showinfo("Error", "Choose a valid path")


def checkIfWhiteList(url):
    with open(whitelist_input.get('1.0', END).strip('\n'), 'r') as whitelistfile:
        whitelist_content = whitelistfile.read().splitlines()  # 'read the whitelist file into line
        domain_raw = tldextract.extract(url)
        domain = "{}.{}".format(domain_raw.domain, domain_raw.suffix)
        if domain.strip('\n') in whitelist_content:
            return True
        else:
            return False


def checkIfContainURL(line):
    urls = re.findall("((http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?)", line) #regex to find URL
    if len(urls) > 0:
        listOfUrls = []
        for url in urls:
            listOfUrls.append(url[0])
        return listOfUrls
    return 'NoUrlsInLine'

#---------------------------------------------------End of Code-----------------------------------------------------


#---------------------------------------------------Test Code-----------------------------------------------------

# urls = re.match("(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?", line).group() #regex to find URL
#(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?
#http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+
# def removeDuplicates(resultFile):
#     lines_seen = set()  # holds lines already seen
#     dupFileContent = open(resultFile.name, "a+")
#     dupFileContentLines = dupFileContent.readlines()
#     for line in dupFileContentLines:
#         if line not in lines_seen:  # not a duplicate
#             dupFileContent.write(line)
#             lines_seen.add(line)
#     dupFileContent.close()

#
# def checkIfContainURL(line):
#     urls = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", line) #regex to find URL
#     if len(urls) > 0:
#         listOfUrls = []
#         for url in urls:
#             x = re.match("(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?", url).group()
#             listOfUrls.append(x)
#         return listOfUrls
#     return 'NoUrlsInLine'
#---------------------------------------------------End Test of Code-----------------------------------------------------


#-------------------------------------------------Tkinter GUI--------------------------------------------------------
root = Tk()

root.title("ExtractLink")

input_label = Label(root, text="Choose input folder", font=("Calibri", 12))
input_label.grid(row=0, column=0)
browse_button = Button(root, text="Browse", font="12", fg="blue", relief=GROOVE, command=browsefuncinput)
browse_button.grid(row=11, column=1, padx=20, columnspan=1)
path_input = Text(width=40, height=2, bd=2, relief=GROOVE)
path_input.grid(row=11, column=0)
path_input.insert('1.0', dir_path + '\Emails')

output_label = Label(root, text="Choose output folder", font=("Calibri", 12))
output_label.grid(row=16, column=0)
output_browse_button = Button(root, text="Browse", font="12", fg="blue", relief=GROOVE, command=browsefuncoutput)
output_browse_button.grid(row=21, column=1, padx=20, columnspan=1)
pathoutput_input = Text(width=40, height=2, bd=2, relief=GROOVE)
pathoutput_input.grid(row=21, column=0)
pathoutput_input.insert('1.0', dir_path + '\Results')

whitelist_label = Label(root, text="Choose Whitelist file (Recommended)", font=("Calibri", 12))
whitelist_label.grid(row=25, column=0)
whitelist_browse_button = Button(root, text="Browse", font="12", fg="blue", relief=GROOVE, command=browsewhitelist)
whitelist_browse_button.grid(row=31, column=1, padx=20, columnspan=1)
whitelist_input = Text(width=40, height=2, bd=2, relief=GROOVE)
whitelist_input.grid(row=31, column=0)
whitelist_input.insert('1.0', dir_path + '\Whitelist.txt')

start_button = Button(root, text="Start", font="12", fg="blue", relief=GROOVE, command=readFilesInFolder)
start_button.grid(row=90, column=0, padx=20)

delete_button = Button(root, text="Delete Previous", font="12", fg="red", relief=GROOVE, command=delete_files_in_folder)
delete_button.grid(row=90, column=1, padx=20)

root.update()
root.minsize(root.winfo_width(), root.winfo_height())

root.mainloop()
#-------------------------------------------------End of Tkinter GUI--------------------------------------------------------