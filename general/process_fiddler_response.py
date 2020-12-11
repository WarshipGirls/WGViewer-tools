import os
import json

import chardet
import zlib
from ast import literal_eval

i = 390
while i < 391:
    filename = f'{i}_.txt'
    if not os.path.exists(filename):
        i += 1
        continue
    with open(filename, 'rb') as f:
        raw = f.read()

    byte_data = zlib.decompress(raw)
    try:
        data = literal_eval(byte_data.decode('ascii'))  # encoding type determined by chardet
    except ValueError:
        # Still failed for passLevel.json
        string = str(byte_data)
        replaced = string.replace('false','{}')
        dataform = str(replaced).strip("'<>() ").replace('\'', '\"')
        data = json.loads(dataform)
    print("\n")
    print(f"==================== {i} ====================")
    print(data)
    print("=============================================\n")
    i += 1
