import numpy as np 
import pandas as pd 
from streetview import search_panoramas
from streetview import get_streetview
import os 
import re

target = pd.read_csv("./santa_rosa.csv",  index_col=0)
for header in range(2007,2025):
    target[str(header)] = ""

filenames = os.listdir("./images/")

for file in filenames:
    #do some regex, idk
    file_symbols = re.split(":|_|-",file)
    index = file_symbols[1] 
    year = file_symbols[8]
    target.loc[str(index), str(year)] =  "./images/" + file 

target.to_csv("./santa_rosa_with_paths.csv")

