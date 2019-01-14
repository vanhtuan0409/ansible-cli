import os
import yaml
import fire
import re

INVENTORY_CONFIG = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "./inventory.yml"
)
ROOT_SSH_CONFIG_PATH = "{0}/.ssh/config".format(os.path.expanduser("~"))
MARKER = "# {0} - GROKKING ONLINE SSH HOSTS"
BEGIN = MARKER.format('BEGIN')
END = MARKER.format('END')

def load_server_config():
    with open(INVENTORY_CONFIG, 'r') as f:
        data = yaml.load(f)
        f.close()
        return data


def gen_config(data, key_path):
    config_str = ""
    for env, hosts in data['all']['children'].iteritems():
        for host_name, host_info in hosts['hosts'].iteritems():
            config_str += """Host {0} {1}
    HostName {2}
    User root
    IdentityFile {3}
""".format(host_name, host_info['ansible_host'], host_info['ansible_host'], key_path)
    return config_str

def write_config_to_file(config, destination):
    with open(destination, "r+") as f:
        current_content = f.read()
        new_content = replace_marker(current_content, config, BEGIN, END)
        f.truncate(0)
        f.write(new_content)
        f.close()


def replace_marker(source, replace_str, begin_mark, end_mark):
    pattern = re.compile('{0}.*?{1}'.format(begin_mark, end_mark), re.DOTALL)
    replace_str = begin_mark + '\n' + replace_str + end_mark
    if pattern.search(source):
        return pattern.sub(replace_str, source)
    return source + '\n' + replace_str

def gen_ssh_config(key_path):
    data = load_server_config()
    config = gen_config(data, key_path)
    write_config_to_file(config, ROOT_SSH_CONFIG_PATH)

if __name__ == "__main__":
    fire.Fire(gen_ssh_config)
