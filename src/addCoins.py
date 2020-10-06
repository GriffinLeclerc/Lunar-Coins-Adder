import os
import sys
import platform
import xml.etree.ElementTree as ET

if len(sys.argv) != 2:
    print("Please specify a number of coins to add.")
    exit(-1)

# Path selection for us WSL users
path = ""
if(platform.system() == "Linux"):
    path = "/mnt/c/Program Files (x86)/Steam/userdata/131301348/632360/remote/UserProfiles"
else:
    path = r"C:\Program Files (x86)\Steam\userdata\131301348\632360\remote\UserProfiles"

# Get all the user profile xmls
for filename in os.listdir(path):
    if not (filename.endswith('.xml')): continue
    fullname = os.path.join(path, filename)
    tree = ET.parse(fullname)

    # Add the desired amount of coins to the existing coin total
    coinsNode = tree.getroot().find("coins")
    coins = int(coinsNode.text)
    coins += int(sys.argv[1])
    coinsNode.text = str(coins)

    # Write back to the xml
    tree.write(fullname)

