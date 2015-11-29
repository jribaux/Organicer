__author__ = 'Brendan'

# Imports
import os.path

import regAnalyse
import finalDestination
import moveFiles


print("Starting Application...")

# This will cause problems 100%
directory = "C:\\Users\\" + os.getlogin() + "\\Downloads"

# Get Directory Listing
print("Obtaining Directory")

DirectoryTargets = os.listdir(directory)
print(DirectoryTargets)

# Analyse the files naming
# - Determine rar'ige and potentially extract
regAnalyse.analayseList(DirectoryTargets, directory)

# Go File by File Ranking them ( Low score aka s03e43.Bobs.Burgers.SCENENAME.03) Check if its a weird format
# Find if its extractable preview its contents and extract specific types of data *.mkv *.mp3 *.mp4
# Just extract the shit and delete the leftovers?

# Use this information to group it with similar files
# Extension specific Folders? .doc and .docx together
finalDestination.pointNewDest(regAnalyse.files, directory)
regAnalyse.showFileObjects()

# Move the File clean up unused files
moveFiles.start(regAnalyse.files, directory)