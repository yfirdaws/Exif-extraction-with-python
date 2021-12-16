import pandas as pd
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS
import glob
import csv
import os

#loading files
for f in glob.glob(r'\\nagisfs03\per\Firdaws.Yahya\shared\NS 40004/*.JPG'): 
  head, tail = os.path.split(f)
  fle=tail #replace with filename
  filename=os.path.splitext(fle)[0] #remove.jpg from file name
  im=Image.open(fle)
 
  # dictionary to store metadata keys and value pairs.
  exif = {}

  imm=im._getexif()

  # iterating over the dictionary 
  if imm:
    for tag, value in imm.items():
      
    #extarcting all the metadata as key and value pairs and converting them from numerical value to string values
        if tag in TAGS:
            exif[TAGS[tag]] = value  
    print()
    print(filename)
    print("Displaying all the metadatas of the image: \n")
    print(exif)
  else:
      print(filename)
      print("Sorry, image has no exif data.")

#creating dataframe
#df=pd.DataFrame([exif])
#inserting filename to first column
#df.insert(0,'Image',filename)
#df.head()
#df.to_csv('Exif data.csv')