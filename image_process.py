import pandas as pd 
import numpy as np
from PIL import Image 


def HSVToGreen(path):
    img = Image.open(path)
    im = np.asarray(img.convert('HSV'))
    greenCount = 0
    current = 0

    for i in range(640):
        for j in range(640):
            current = (im[i,j,0])
            if (current > 57 and current < 98):
                greenCount += 1 / (640*640) 

    return 100 * greenCount  


def RGBToGreen(path):
    img = Image.open(path)
    im = np.asarray(img.convert('RGB'))
    greenCount = 0;

    for i in range(640):
        for j in range(640):
            r = im[i,j,0]/256;
            g = im[i,j,1]/256;
            b = im[i,j,2]/256;
            gmr = g - r
            gmb = g - b
            diff = gmr*gmb

            if (gmr > 0/256 and diff > 2/256): 
                greenCount += (diff / (640*640))

    return 100* greenCount  


data = pd.read_csv("./santa_rosa_with_paths.csv")


for header in range(2012,2021):
    data["HSV_Green_" + str(header)] = ""
    data["RGB_Green_" + str(header)] = ""


for index in data.index:
    for year in range(2012,2021):
        path = data[str(year)][index]
        if (path != "" and path != np.nan and str(path) != "nan"):
            data.loc[index, "HSV_Green_" + str(year)] =  HSVToGreen(str(path))
            data.loc[index, "RGB_Green_" + str(year)] =  RGBToGreen(str(path))


data.to_csv("./santa_rosa_processed.csv")
print("Done profiling.")
