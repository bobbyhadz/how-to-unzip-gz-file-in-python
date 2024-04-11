# How to unzip a .gz file using Python

import gzip
import shutil

with gzip.open('example.json.gz', 'rb') as file_in:
    with open('example.json', 'wb') as file_out:
        shutil.copyfileobj(file_in, file_out)
        print('example.json file created')
