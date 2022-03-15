import os
import glob

def delete():
    files = glob.glob('./records/*')
    for f in files:
        os.remove(f)