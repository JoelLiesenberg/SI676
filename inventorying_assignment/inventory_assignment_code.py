import os
import shutil
import hashlib
import csv
import datetime

def get_checksum(filePath, checksum_type):
    checksum_type = checksum_type.lower()

    with open(filePath, 'rb') as f:
        bytes = f.read()
        if checksum_type == 'md5':
            hash_string = hashlib.md5(bytes).hexdigest()
        elif checksum_type == 'sha256':
            hash_string = hashlib.sha256(bytes).hexdigest()
        else:
            raise('{} is not a hash function supported by this program. You must ask for MD5.')
    return hash_string

dir_string = os.path.join('data', 'webfiles-samples')

file_info = []

file_count = 0

for folderName, subfolders, filenames in os.walk(dir_string):
    for filename in filenames:
        file_count += 1
        index = file_count
        filename = filename
        folder = folderName
        path = os.path.join(folderName, filename)
        size = os.path.getsize(path)
        extension = os.path.splitext(filename)[1]
        modify_datetime = datetime.datetime.strftime(datetime.datetime.fromtimestamp(os.path.getmtime(path)), "%Y-%m-%dT%H:%M:%S%Z")
        md5hash = get_checksum(path, 'md5')
        file_info.append([
            index,
            path,
            filename,
            extension,
            size,
            modify_datetime,
            md5hash
        ])
        

headers = [
    'index',
    'path',
    'filename',
    'extension',
    'size',
    'modify_datetime',
    'md5hash'
]

with open('file-inventory.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for file in file_info:
        writer.writerow(file)