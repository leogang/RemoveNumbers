import os

def rename_files():
    #Get file names from a folder
    file_list = os.listdir("/Users/animaltalk/Downloads/prank")
    print file_list
    saved_path = os.getcwd()
    print "Current Working directory is " + saved_path
    os.chdir(r"/Users/animaltalk/Downloads/prank")
    
    #For each file, rename filename
    for file_name in file_list:
            print "Old Name - " + file_name
            os.rename(file_name, file_name.translate(None, "0123456789"))
            print "New Name - " + file_name.translate(None, "0123456789")
           
    os.chdir(saved_path)
    
rename_files()
