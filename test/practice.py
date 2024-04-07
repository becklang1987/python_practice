import sys
import os
from PIL import Image
import  re


def convertpic(tt):
    for pic in os.listdir(os.getcwd()):
        f,e = os.path.splitext(pic)
        print(re.search(r'^(ic).*', f))
        if re.search(r'^(ic).*',f) != None:
            with Image.open(pic) as ff:
                ff=ff.rotate(-90).resize((128,128))
                ff.save("/opt/icons"+f+".jpg")
    return

convertpic("tt")
