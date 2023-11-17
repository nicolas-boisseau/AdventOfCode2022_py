import os
from urllib import request

def DownloadIfNotExists(url):
    # Download the file from `url` and save it locally under `file_name`:
    file_name = url.split('/')[-1] + ".txt"

    if os.path.exists(file_name):
        return

    r = request.Request(url)

    session = os.getenv("ADVENTOFCODE_SESSION")
    r.add_header("Cookie", f"session={session}")
    with request.urlopen(r) as response, open(file_name, 'wb') as out_file:
        data = response.read()
        out_file.write(data)
