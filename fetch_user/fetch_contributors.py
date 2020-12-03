import json
import urllib.request


def get_data_from_url(url: str) -> list:
    contents = urllib.request.urlopen(url).read().decode()
    return json.loads(contents)


def get_contributors() -> set:
    url = "https://api.github.com/repos/WarshipGirls/WGViewer/contributors"
    user_list = get_data_from_url(url)
    res = set()
    for user in user_list:
        res.add(user['login'])
    return res

def get_commenters() -> set:
    url = "https://api.github.com/repos/WarshipGirls/WGViewer/issues/2/comments"
    comment_list = get_data_from_url(url)
    res = set()
    for comm in comment_list:
        res.add(comm['user']['login'])
    return res
