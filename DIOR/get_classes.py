# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
import os

path = "Annotations"

clses=['',]
files= os.listdir(path)
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
                
print(clses)
