import os
import json

filelist = json.load(open("./study.json"))

for filepath in filelist.keys():
    os.remove(filepath)

os.remove("./study.json")