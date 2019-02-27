from os import listdir
from os.path import isfile, join


class Muct:
    def __init__(self, path, sub_path):
        self._path = path
        self._sub_path = sub_path

    def get_all_image_path(self):
        onlyfiles = [f for f in listdir(
            self._path+"/"+self._sub_path) if isfile(join(self._path+"/"+self._sub_path, f))]
        return onlyfiles
