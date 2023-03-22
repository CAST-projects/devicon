import os
import json

folder_path = "./icons" # replace with the path to the folder you want to list

os.remove(folder_path+"/list.json")

folder_contents = os.listdir(folder_path)
folder_contents.sort()

folder_contents.remove(".DS_Store")
# listdir() method returns a list of all files and folders in the given folder_path

json_output = json.dumps({"allicons":folder_contents})
# dumps() method converts the folder_contents list to a JSON-formatted string

print(json_output)
# prints the JSON output to the console

with open(folder_path+"/list.json", "w") as f:
    f.write(json_output)
