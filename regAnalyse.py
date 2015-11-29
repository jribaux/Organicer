__author__ = 'Brenda'

# This is where the magic happens

import re
import os

import fileObject

#REGULAR EXPRESSIONS
versionReg = r'\d+(?:\.\d+){2,}'
nameReg = r"(.+?)\.[^\.]+$"
extensionReg = r"\.[0-9a-z]+$"

files = []

# Repeat
def analayseList(DirectoryTarget, directory):
    for target in DirectoryTarget:
        # Create Object
        file = fileObject.FileObject()
        file.directory = (directory + "\\" + target)
        file.original = target
        if os.path.isfile(directory + "\\" + target):
            file.name = nameRegex(target)
            file.version = versionRegex(target)
            file.type = extensionRegex(target)
        else:
            file.type = "Directory"
        files.append(file)


def versionRegex(DirectoryTarget):
    search = re.findall(versionReg, DirectoryTarget)
    if search:
        return search[0]
    else:
        return None


def extensionRegex(DirectoryTarget):
    search = re.findall(extensionReg, DirectoryTarget)
    if search:
        return search[0]
    else:
        return None


def nameRegex(DirectoryTarget):
    search = re.findall(nameReg, DirectoryTarget)
    if search:
        return stripString(search[0].split(versionRegex(DirectoryTarget))[0])
    else:
        return None


def stripString(str):
    return str.replace(".", " ").replace("-", " ").replace("_", " ")

def showFileObjects():
    if files:
        try:
            for i in files:
                if i.original:
                    print("Original Name: " + i.original)
                if i.name:
                    print("Simple Name: " + i.name)
                if i.version:
                    print("Version: " + i.version)
                if i.type:
                    print("Type: " + i.type)
                if i.directory:
                    print("Directory: " + i.directory)
                if i.destination:
                    print("Destination: " + i.destination)
                if i.group:
                    print("Group: " + i.group)
                print("\n")
        except:
            print("Something went wrong in displaying file Objects")
            return


