import os
import glob

def delete_plots():
    files = glob.glob('./plots/*')
    for f in files:
        os.remove(f)