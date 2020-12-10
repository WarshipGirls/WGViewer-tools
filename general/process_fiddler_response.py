import os
import zlib
from ast import literal_eval

i = 0
while i < 155:
    filename = f'{i}_.txt'
    if not os.path.exists(filename):
        i += 1
        continue
    with open(filename, 'rb') as f:
        raw = f.read()

    byte_data = zlib.decompress(raw)
    data = literal_eval(byte_data.decode('ascii'))  # encoding type determined by chardet
    print("\n")
    print(f"==================== {i} ====================")
    print(data)
    print("=============================================\n")
    i += 1