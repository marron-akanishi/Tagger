import os
import numpy as np
import cv2
import shutil
import json

study_list = {}

# http://blog.aidemy.net/entry/2017/12/17/214715
def scratch_image(img, filpV=True, flipH=True, thr=True, filt=True):
    # 水増しの手法を配列にまとめる
    methods = [filpV, flipH, thr, filt]
    # ぼかしに使うフィルターの作成
    filter1 = np.ones((3, 3))
    # オリジナルの画像データを配列に格納
    images = [img]
    # 手法に用いる関数
    scratch = np.array([
        lambda x: cv2.flip(x, 0),
        lambda x: cv2.flip(x, 1),
        lambda x: cv2.threshold(x, 100, 255, cv2.THRESH_TOZERO)[1],
        lambda x: cv2.GaussianBlur(x, (5, 5), 0),
    ])
    # 加工した画像を元と合わせて水増し
    doubling_images = lambda f, imag: np.r_[imag, [f(i) for i in imag]]

    for func in scratch[methods]:
        images = doubling_images(func, images)
    return images

for tag in range(0,14):
    folder = "./"+str(tag)+"/"
    file_count = len(os.listdir(folder))
    for filepath in os.listdir(folder):
        _, filename = os.path.split(filepath)
        # 学習データの水増し
        name, ext = os.path.splitext(filename)
        if file_count < 300:
            images = scratch_image(cv2.imread(folder+filepath), True, True, True, True)
        elif file_count < 470:
            images = scratch_image(cv2.imread(folder+filepath), False, True, True, True)
        elif file_count < 650:
            images = scratch_image(cv2.imread(folder+filepath), False, False, True, True)
        else:
            images = scratch_image(cv2.imread(folder+filepath), False, False, False, True)
        for i, img in enumerate(images):
            newpath = folder+name+str(i)+ext
            cv2.imwrite(newpath, img)
            newpath = "./files/study" + newpath[1:]
            study_list[newpath] = tag
        os.remove(folder+filepath)

jsonfile = open("./study.json","w")
json.dump(study_list, jsonfile, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
jsonfile.close()