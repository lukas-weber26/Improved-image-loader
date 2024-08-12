import numpy as np 
import pandas as pd 
from streetview import search_panoramas
from streetview import get_streetview
import os 
import concurrent.futures 

pool = concurrent.futures.ThreadPoolExecutor(max_workers = 40)
google_cloud_key = os.environ['GCP_KEY']
data = pd.read_csv("./santa_rosa.csv")
os.mkdir("images")

def pull_year(latitude, longitude, panos):
    for p in panos:
        if (p.date != None):
            name = "Index:" + str(index) + "_Lat:" + str(latitude) + "_Long:" + str(longitude) + "_Date:" + str(p.date) + ".jpg"
            image = get_streetview(pano_id=p.pano_id,api_key=google_cloud_key)
            img_name = 'images/' + name
            image.save(img_name , "jpeg")

for index in data.index:
    latitude = data['Latitude'][index]
    longitude = data['Longitude'][index]
    print(index)
    panos = search_panoramas(lat=latitude, lon=longitude)
    pool.submit(pull_year, latitude, longitude, panos) 

pool.shutdown(wait=True)
print("Download complete!")
        
