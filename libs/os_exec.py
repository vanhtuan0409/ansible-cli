import subprocess

def exec_cmd(cmd):
    process = subprocess.Popen(cmd, shell=True)
    return process.communicate()

