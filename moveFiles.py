__author__ = 'Brenda'

import os


def start(files, dir):
    for file in files:
        # See if directory exists before moving files
        if checkDirectory(file) is False:
            print("MAKING DIRECTORY")
            os.makedirs(file.destination)

        # Move Files
        if file.destination:
            os.rename(file.directory, str(file.destination + "\\" + file.original))


def checkDirectory(file):
    if file.destination:
        if os.path.isdir(file.destination + "//") is False:
            return False
