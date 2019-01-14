import os

def resolv_relative(cwd, path):
    dir_path = os.path.dirname(os.path.realpath(cwd))
    return os.path.join(dir_path, path)
