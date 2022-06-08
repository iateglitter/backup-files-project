import os
import shutil
path = input("enter number of days")
source = input("enter number of days")
destination = input("enter number of seconds")
listOfFiles = os.listdir()
for days in listOfFiles:
    shutil.copy(source+"/"+days,destination+"+")
