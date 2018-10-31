import datetime
import os

author = "" #Setting up a global variable that we can use throughout 

def create_journal():
    name = input("Name your journal:   ")

    cwd = os.getcwd()
    
    path = cwd + "/" + name    

    try:  
        os.mkdir(path)
    except OSError:  
        print ("Creation of the directory %s failed" % path)
    else:  
        print ("Successfully created the directory %s " % path)


def open_journal():
    os.chdir(os.getcwd())
    journal_list = os.listdir()
    
    print("Current Journals: " + str(len(journal_list)))
    for journal in journal_list:
        print(journal)
        
    name = input("Name of journal:  ")
    cwd = os.getcwd()
    path = cwd + "/" + name
    os.chdir(path)

    directory_list = os.listdir()
    print("Current Entries: " + str(len(directory_list)))
    for entry in directory_list:
        print(entry)

def fetch_content():
    content = input("Write till your heart's content :)")
    return content

def add_page():
    title = input("Name your entry:  ")
    filename = title.replace(" ","") + ".txt" #Adding .txt so we can create the page
    
    add_content(title)
    

def remove_page():
    title = input("What's the title of your entry?  ")
    filename = title.replace(" ","") + ".txt"
    os.remove(filename)

def add_content():
    title = input("What's the title of your entry?  ")
    content = fetch_content()
    filename = title.replace(" ","") + ".txt"
    entry = open(filename, "a")
    entry.write(author + "\n")
    entry.write(title + "\n")
    entry.write(str(datetime.datetime.now()) + "\n")
    
    count = 0
    prev_index = 0
    for i in range(0, len(content) - 1):
        if content[i] == " ":
            entry.write(content[prev_index:i])
            count += 1
            prev_index = i
        if count == 10:
            count = 0
            entry.write("\n")
  
            
    entry.close()

def controls():
    print("What would you like to do?: ")
    print("1: Create a journal")
    print("2: Open a journal")
    print("3: Create an entry")
    print("4: Add to an entry")
    print("5: Remove an entry")
    option = input("Your choice:  ")
    print("-----\n-----")

    if option == "1" or option == 1:
        create_journal()
    elif option == "2" or option == 2:
        open_journal()
    elif option == "3" or option == 3:
        add_page()
    elif option == "4" or option == 4:
        add_content()
    elif option == "5" or option == 5:
        remove_page()
    else:
        print("Please answer based on your choices")
        controls()

    choice = input("Do you need to do anything else? (y/n)")
    if choice == "y" or choice == "yes":
        controls()
    else:
        print("See you later!")

author = input("What's your name?  ")
controls()
        
        
        
        
        
        
        
    



















    
    
