import os
import json
import cv2

folder = "./static/images/"
filelist = {}
resize = False

for files in os.listdir(folder):
    temp, ext =  os.path.splitext(files)
    if ext == ".png" or ext == ".jpg":
        if resize:
            img = cv2.imread(folder+files)
            orgWidth, orgHeight = img.shape[:2]
            size = (int(orgHeight/2), int(orgWidth/2))
            img = cv2.resize(img, size)
            cv2.imwrite(folder+files,img)
        filelist[folder+files] = -1

listfile = open("./list.json","w")
json.dump(filelist, listfile, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
listfile.close()