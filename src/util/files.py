import os

def path(url):
    return url.replace('~', os.getenv('HOME'))
