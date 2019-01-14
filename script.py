import os
import sys
import fire
from libs.colors import Color
from libs.gen_ansible_cmd import gen_cmd
from libs.os_exec import exec_cmd

class AnsibleParams(object):

    BOOTSTRAP = ''
    PROVISION_FOLDER = ''
    RAW = False
    DEBUG = False
    VERBOSE = False

# Auto load playbooks from directory
class AnsibleFire(object):

    def __init__(
        self,
        raw=False,
        debug=False,
        verbose=False,
    ):
        AnsibleParams.RAW = raw
        AnsibleParams.DEBUG = debug
        AnsibleParams.VERBOSE = verbose
        dirs = [
            item
            for item in os.listdir('./playbooks')
            if os.path.isdir('./playbooks/' + item)
        ]

        loadable = [
            item
            for item in dirs
            if (
                os.path.isfile('./playbooks/{0}/provision.py'.format(item)) and
                os.path.isfile('./playbooks/{0}/__init__.py'.format(item))
            )
        ]

        for item in loadable:
            mod = __import__('playbooks.{0}.provision'.format(item), fromlist=['Provision'])
            setattr(self, item, getattr(mod, 'Provision')())

if __name__ == "__main__":
    params = None
    print Color.YELLOW
    params = fire.Fire(AnsibleFire)
    print Color.ENDC

    if not params or not isinstance(params, dict):
        sys.exit(0)

    if "vars" not in params:
        params["vars"] = {}

    print Color.RED
    cmd = gen_cmd(params)
    print cmd
    print Color.ENDC

    exec_cmd(cmd)
