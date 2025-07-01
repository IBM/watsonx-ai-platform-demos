# to keep this repo clean, we download the data from the internet and save it to the data folder

import requests
from pathlib import Path


# this is the overview page of all tutorials available on the website
# https://www.ibm.com/support/pages/node/627743


# This is the list of links that we will download
links = [
    "https://public.dhe.ibm.com/ps/products/db2/info/vr115/pdf/en_US/db2_perf_tune_115.pdf",
    "https://public.dhe.ibm.com/ps/products/db2/info/vr115/pdf/en_US/db2_sec_guide_115.pdf",
    "https://public.dhe.ibm.com/ps/products/db2/info/vr115/pdf/en_US/db2_txt_search_115.pdf",
    "https://public.dhe.ibm.com/ps/products/db2/info/vr115/pdf/en_US/db2_sys_mon_guide_115.pdf",
    "https://public.dhe.ibm.com/ps/products/db2/info/vr115/pdf/en_US/db2_part_clust_115.pdf",
    "https://public.dhe.ibm.com/ps/products/db2/info/vr115/pdf/en_US/db2_data_mov_115.pdf"
]

# download the data in to this folder 
data_folder = Path(__file__).parent 

# create the folder if it doesn't exist
data_folder.mkdir(parents=True, exist_ok=True)  

# download the data
for link in links:
    response = requests.get(link)
    file_path = data_folder / link.split("/")[-1]
    with open(file_path, "wb") as file:
        file.write(response.content)        




