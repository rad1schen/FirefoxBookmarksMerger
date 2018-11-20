import json
from collections import defaultdict
import tkinter as tk
from tkinter import filedialog

output = []

print("Please open a .json bookmark file")

while True:
    root = tk.Tk()
    root.withdraw()

    input_file = filedialog.askopenfilename()

    input_data = json.load(open(input_file,"r",encoding="utf8"))

    for i in range(0,len(input_data['children'])):
        try:
            output+=input_data['children'][i]['children']
        #dont stop at objects without children key
        except KeyError:
            continue
        

    multiples=input("Do you want to add another .json bookmark file? y/n [n]")
    if multiples != "y":
        break

d = defaultdict(list)

for i in output:
    try:
        d[i['uri']].append(i)
    #dont stop at objects without URI key
    except KeyError:
        continue

merged = []
for key, val in d.items():
    merged.append(val[0])

data = {
  "guid": "root________",
  "title": "",
  "index": 0,
  "dateAdded": 1432159479739000,
  "lastModified": 1511199631405000,
  "id": 1,
  "type": "text/x-moz-place-container",
  "root": "placesRoot",
  "children": [
      {"guid": "unfiled_____",
      "title": "Unfiled Bookmarks",
      "index": 0,
      "dateAdded": 1432159479739000,
      "lastModified": 1511199631405000,
      "id": 5,
      "type": "text/x-moz-place-container",
      "root": "unfiledBookmarksFolder",
      "children": []
      }
      ]
  }

#assign new id and index numbers
newid = 54
newindex = 0
for i in merged:
    i['index'] = newindex
    i['id'] = newid
    newindex = newindex +1
    newid = newid+1

data['children'][0]['children'] = merged

#output as merged_bookmarks.json
with open("merged_bookmarks.json", "w") as write_file:
    json.dump(data, write_file)

print("Done")
    
