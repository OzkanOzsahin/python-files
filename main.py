__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
from zipfile import ZipFile
###
# --- Make sure the imports are on the top of the file ---
###

base_path = os.getcwd()
cache_path = os.path.join(base_path, "files\cache")
data_path = os.path.join(base_path, "data.zip")

# 1



def clean_cache():
    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)
    os.mkdir(cache_path)


# 2

def cache_zip(zip, cache):
    with ZipFile(zip, "r") as zipObj:
         zipObj.extractall(cache)
###
# Use the zipfile module to extract the zip file in a small amount of code.
###

# 3

def cached_files():
    cached_files_list = []
    for path in os.listdir(cache_path):
        full_path = os.path.join(cache_path, path)
        cached_files_list.append(full_path)
    return cached_files_list



# 4

def find_password(list_of_files):
    for file in list_of_files:
        with open(file) as f:
            for line in f:
                if "password" in line:
                    split_line = line.split(" ", 1)
                    return split_line[1].replace("\n", "")


# This block is only executed when run from "main", and not when imported.
if __name__ == "__main__":
    clean_cache()
    cache_zip(data_path, cache_path)
    cached_files()
    print(find_password(cached_files()))
