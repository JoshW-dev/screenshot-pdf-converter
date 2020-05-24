import os
import glob
os.remove("screenshot.png")
for filename in glob.glob(".\page*"):
    os.remove(filename)
