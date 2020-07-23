import os
import datetime


def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

def is_file_outdated(filename):
    return modification_date(filename) < datetime.datetime.now()
