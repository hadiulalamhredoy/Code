# Question: Write a python program to print the contents of a directory using the OS module.

""" Instructions: 1. Install the OS 
                    2. Specify the directory you want to list
                        3. List all files and directories in the specified path
                            4. Print each file and directory name """
                            
import os

directory_path = '/Users/h/Desktop/cse106'

contents = os.listdir(directory_path)

print(contents)