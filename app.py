# ajaxはPOST、それ以外はGET
import os
import sys
import glob
import json
import flask
import datetime

# 自身の名称を app という名前でインスタンス化する
app = flask.Flask(__name__)
tagfile = open("./taglist.json")
tagjson = json.load(tagfile)
tagfile.close()
listfile = open("./list.json")
listjson = json.load(listfile)
listfile.close()

def GetListData(num):
    num = int(num)
    if num == -1:
        for i, key in enumerate(sorted(listjson.keys())):
            if listjson[key] == -1:
                return i, key
    else:
        key = sorted(listjson.keys())[num]
        return num, key

def GetTagName(tagid):
    tagid = int(tagid)
    return tagjson[str(tagid-1)]

# ここからウェブアプリケーション用のルーティングを記述
# トップページ
@app.route('/')
def Index():
    tagcount = []
    for i in range(0,len(tagjson)):
        tagcount.append(0)
    for key in listjson.keys():
        tagcount[listjson[key]+1] += 1
    return flask.render_template('index.html', all=len(listjson), list=tagcount)

@app.route('/view', methods=['GET'])
def TagView():
    listid, imagefile = GetListData(flask.request.args.get('id'))
    return flask.render_template('view.html', id=listid, max=len(listjson)-1, image=imagefile, taglist=tagjson, tag=tagjson[str(listjson[imagefile])])

@app.route('/settag', methods=['POST'])
def SetTag():
    imagename = flask.request.form['image']
    tagid = flask.request.form['tagid']
    imageid = int(flask.request.form['id'])
    listjson[imagename] = int(tagid)
    with open("./list.json","w") as ftp:
        json.dump(listjson, ftp, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    if imageid < len(listjson)-1:
        return "/view?id="+str(imageid+1)
    else:
        return "end"

if __name__ == '__main__':
    # debug server
    app.debug = False # デバッグモード
    app.jinja_env.filters['GetTagName'] = GetTagName
    app.run(host='0.0.0.0') # どこからでもアクセス可能に
