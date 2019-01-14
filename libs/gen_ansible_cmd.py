import os

def gen_cmd(opts):
    cmd = "ansible-playbook {0}".format(opts["playbook"])
    for key, value in opts["vars"].iteritems():
        if value and not isinstance(value, bool):
            cmd += " --extra-vars {0}={1}".format(key, value)
    return cmd
