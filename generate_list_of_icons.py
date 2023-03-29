import os
import json
from os.path import expanduser

folder_paths = ["./icons","~/github/resources/familyIcons","~/github/resources/genericIcons","~/github/resources/techportal"]

for folder_path in folder_paths: # replace with the path to the folder you want to list

    real_folder_path = expanduser(folder_path)

    try:
        os.remove(real_folder_path+"/list.json")
    except:
        pass

    folder_contents = os.listdir(real_folder_path)
    folder_contents.sort()

    folder_contents.remove(".DS_Store")
    # listdir() method returns a list of all files and folders in the given folder_path

    #strip .svg
    folder_contents = [w.replace(".svg","") for w in folder_contents]

    json_output = json.dumps({"allicons":folder_contents})
    # dumps() method converts the folder_contents list to a JSON-formatted string

    print(json_output)
    # prints the JSON output to the console

    with open(real_folder_path+"/list.json", "w") as f:
        f.write(json_output)
