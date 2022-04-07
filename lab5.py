#!/usr/bin/python3
#T.J. Tillo
#SY402 Section 5521
#Lab 5

#Used the example found here for the base code: https://github.com/BeagleD/SY402-Spring-22/blob/main/Lab5.py
#I moved the code that creates and parses gethashes.txt to the "try" statement to get the code to run successfully.

import os
import sys
import hashlib
import datetime

new=[]
missing=[]
modified=[]
old_files={}
new_files={}

ignore_list = ['dev', "proc", "run", "sys", "tmp", "var/lib", "var/run",".wine"]
now = datetime.datetime.now()

def main():
   for root, dirs, files in os.walk(".", topdown=True): #from geeksforgeeks.org

     for item in ignore_list:
            if item in dirs:
                dirs.remove(item)
     testlist = root.split("/")
     for directory in testlist:
         if (directory in ignore_list) and (directory in root.split()):
             continue

         else:
             for f in files:
                 current_file = os.path.join(root,f)

                 if current_file not in old_files:
                     print("New File: ", current_file)
                 H = hashlib.sha256()
                 try:
                     with open(current_file, "rb") as FIN:
                         H.update(FIN.read())
                         hash = H.hexdigest()
                         new_files[current_file]=hash
                         if old_files[current_file]!=hash:
                             print("File Changed: ", current_file)
                        ### Mostly taken from stackoverflow ; strftime is from W3schools###
                         with open("gethashes.txt", "a+") as myfile:
                             myfile.write(current_file),myfile.write(","),myfile.write(now.strftime("%Y-%m-%d %H:%M:%S")),myfile.write(","),myfile.write(H.hexdigest()),myfile.write("\n")
                         gethashes = open("gethashes.txt", "r")
                         gethashes = gethashes.readlines()
                         for line in gethashes:
                             filename=line.split(",")[0]
                             filehash =line.split(",")[2].rstrip("\n")
                             old_files[filename]=filehash
                
                 except:
                     print(current_file)

def compare():
    for file in old_files:
        if file not in new_files:
            print("File missing: ", file)


if __name__ == "__main__":
   main()
   compare()
