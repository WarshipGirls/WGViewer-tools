import requests
import hashlib
import time


def get_url_end(now_time=str(int(round(time.time() * 1000)))):
    url_time = now_time
    md5_raw = url_time + 'ade2688f1904e9fb8d2efdb61b5e398a'
    md5 = hashlib.md5(md5_raw.encode('utf-8')).hexdigest()
    return md5

# L_ / M_ / S_ + NORMAL_ / BROKEN_ + ship_cid(mid part) + _1 _2 (optional for diff skins)
pic_name = "L_BROKEN_1039"
prefix = f"http://bshot.moefantasy.com/2/ccbResources/model/{pic_name}.mukaR?md5="

url = prefix + get_url_end()

r = requests.get(url)
output_name = pic_name + ".mukaR"
with open(output_name, 'wb') as f:
    f.write(r.content)
