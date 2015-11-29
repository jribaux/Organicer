__author__ = 'Brenda'


def loadConfig():
    print("Reading Configuration File")
    return str(open("destinationConfig.txt").read()).split("\n")

def pointNewDest(files, dir):
    destination = loadConfig()

    for file in files:
        for i in range(0, destination.__len__()):
            if destination[i] == "*Ext:":
                for ext in destination[i+1].split(";"):
                    if file.type == ext:
                        file.group = destination[i-1]
                        file.destination = dir + destination[i+2]





