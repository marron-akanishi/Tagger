import os
import shutil
import json

folder = "./done/"

jsonlist = open("./list.json")
filelist = json.load(jsonlist)
jsonlist.close()

for files in filelist.keys():
    temp, filename = os.path.split(files)
    movedir = folder+str(filelist[files])+"/"
    if os.path.exists(movedir) == False:
        os.mkdir(movedir)
    shutil.move(files,movedir+filename)