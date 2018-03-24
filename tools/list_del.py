import os
import json
import cv2

folder = "./static/images/"
listfile = open("./list.json","r")
filelist = json.load(listfile)
listfile.close()
newlist = {}

for filename in filelist.keys():
    if os.path.exists(filename):
        newlist[filename] = filelist[filename]

listfile = open("./list_new.json","w")
json.dump(newlist, listfile, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
listfile.close()