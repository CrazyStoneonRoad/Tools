# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
import os
import shutil
import sys

NO = int( sys.argv[1])
clses = ['bg',]
nos = [0,]

path = "Annotations"
Opth = "selected"
if not os.path.exists(Opth):
    os.mkdir(Opth)

files= os.listdir(path)
for file in files:

    if not os.path.isdir(file):
        tree = ET.parse(path+"/"+file)
        root = tree.getroot()

        objects = root.findall('.//object')
        if len(objects) == 1:
            object = objects[0]

            name = object.find('name')
            cls = name.text

            if cls not in clses:
                clses.append(cls)
                nos.append(0)

            if nos[clses.index(cls)]<(NO):
                shutil.copyfile("JPEGImages/"+file[:-4]+'.jpg', Opth+"/"+cls+'-'+file[:-4]+'.jpg')
                nos[clses.index(cls)] = nos[clses.index(cls)] + 1
                # if NO > 0:
                #     continue
                # NO = NO - 1
            else:
                continue

for file in files:

    if not os.path.isdir(file):
        tree = ET.parse(path+"/"+file)
        root = tree.getroot()

        objects = root.findall('.//object')
        for object in objects:

            name = object.find('name')
            cls = name.text

            if cls not in clses:
                clses.append(cls)
                nos.append(0)
            if nos[clses.index(cls)]<(NO):
                shutil.copyfile("JPEGImages/"+file[:-4]+'.jpg', Opth+"/"+cls+'-'+file[:-4]+'.jpg')
                nos[clses.index(cls)] = nos[clses.index(cls)] + 1

print(clses)
