import requests
import os
from urllib.parse import urlparse, unquote
import sys


def download(url):
    print("[-] Parsing URL")
    a = urlparse(url)
    print("[-] Getting URL")
    filename = os.path.basename(a.path)
    print("[-] Making file")
    with open(filename, "w") as f:
        print("[-] Downloading...")
        f.write(requests.get(url).text)
    
    print("[!] Done!")

try:
    download(sys.argv[1])
except IndexError:
    print("[Error] URL not provided")