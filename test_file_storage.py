#!/usr/bin/python3

from models.engine import file_storage

FileStorage = file_storage.FileStorage
fs = FileStorage()
print(fs)
b = fs.reload()
print(b)
