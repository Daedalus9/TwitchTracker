def help():
    helpFile=open('./var/help.txt', 'r')
    for line in helpFile:
        print(line[:-1])
    helpFile.close()