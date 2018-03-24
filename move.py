import os
import shutil
import json

folder = "./files/"

jsonfile = open("./list.json")
filelist = json.load(jsonfile)
jsonfile.close()
study_list = {}
test_list = {}

for count, filepath in enumerate(filelist.keys()):
    _, filename = os.path.split(filepath)
    # 10%をテスト用にする
    if count % 10 == 1:
        movedir = folder+"test/"+str(filelist[filepath])+"/"
        test_list[movedir+filename] = filelist[filepath]
    else:
        movedir = folder+"study/"+str(filelist[filepath])+"/"
        study_list[movedir+filename] = filelist[filepath]
    # フォルダー作成
    if os.path.exists(movedir) == False:
        os.mkdir(movedir)
    # ファイルコピー
    shutil.copyfile(filepath, movedir+filename)

jsonfile = open("./study.json","w")
json.dump(study_list, jsonfile, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
jsonfile.close()
jsonfile = open("./test.json","w")
json.dump(test_list, jsonfile, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
jsonfile.close()