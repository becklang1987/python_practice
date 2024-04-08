import re
import sys
import paramiko
paramiko.SSHClient


from PIL import Image
import os

def picrefact(test):
    os.chdir(test)
    for pic in os.listdir():
        f ,e = os.path.splitext(pic)
        outfile = f + ".jpg"
        print(f)
        print(e)
        if e == ".png":
                with Image.open(pic) as im:
                    im= im.rotate(-90).resize((200,200)).convert('RGB')
                    im.save(outfile)


    return
picrefact(sys.argv[1])
