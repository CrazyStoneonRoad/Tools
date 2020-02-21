# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
import os


def pretty_xml(element, indent, newline, level=0):
    if element is not None:
        if (element.text is None) or element.text.isspace():
            element.text = newline + indent * (level + 1)
        # else:
        #     element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
    temp = list(element)
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):
            subelement.tail = newline + indent * (level + 1)
        else:
            subelement.tail = newline + indent * level
        pretty_xml(subelement, indent, newline, level=level + 1)



'''
annotation
    folder XXXXXXXXXXXXXXX DIOR
    filename
    source
        database
        annotation XXXXXXXXXXXXXXX DIORann
        image XXXXXXXXXXXXXXX DIORim
        flickrid XXXXXXXXXXXXXXX NULL
    owner XXXXXXXXXXXXXXX
        flickrid NULL
        name smwn
    size
        width
        height
        depth
    segmented
    object
        name
        pose
        truncated XXXXXXXXXXXXXXX 0
        difficult XXXXXXXXXXXXXXX 0
        bndbox
            xmin
            ymin
            xmax
            ymax
'''
path = "Annotations-imcompleted"
Opth = "Annotations"
files= os.listdir(path)
for file in files:
    if not os.path.isdir(file):
        tree = ET.parse(path+"/"+file)
        root = tree.getroot()

        folder = ET.Element('folder')
        folder.text = 'DIOR'
        root.insert(0,folder)


        source = root.find('.//source')
        annotation = ET.Element('annotation')
        annotation.text = 'DIORann'
        image = ET.Element('image')
        image.text = 'DIORim'
        flickrid = ET.Element('flickrid')
        flickrid.text = 'NULL'
        source.append(annotation)
        source.append(image)
        source.append(flickrid)


        owner = ET.Element('owner')
        flickrid = ET.SubElement(owner,'flickrid')
        flickrid.text = 'NULL'
        name = ET.SubElement(owner,'name')
        name.text = 'smwn'
        root.insert(3,owner)

        objects = root.findall('.//object')
        for object in objects:
            truncated = ET.Element('truncated')
            truncated.text = '0'
            difficult = ET.Element('difficult')
            difficult.text = '0'
            object.insert(2,truncated)
            object.insert(3,difficult)

        pretty_xml(root,'\t','\n')
        tree.write(Opth+"/"+file)
