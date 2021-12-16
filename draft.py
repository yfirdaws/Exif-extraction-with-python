
import pandas as pd
#import numpy as np 
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS
import glob
import csv
import os

#loading files
for f in glob.glob(r'\\nagisfs03\per\Firdaws.Yahya\shared\NS 40004/*.JPG'): 
  fle=f #replace with filename
  filename=os.path.splitext(fle)[0] #remove.jpg from file name
  im=Image.open(fle)
 
  # dictionary to store metadata keys and value pairs.
  exif = {}

  # iterating over the dictionary 
  for tag, value in im._getexif().items():

  #extarcting all the metadata as key and value pairs and converting them from numerical value to string values
      if tag in TAGS:
          exif[TAGS[tag]] = value  

  print()
  print("Displaying all the metadatas of the image: \n")
  print(exif)
#creating dataframe
df=pd.DataFrame([exif])
#inserting filename to first column
df.insert(0,'Image',filename)
df.head()
#df.to_csv('Exif data.csv')