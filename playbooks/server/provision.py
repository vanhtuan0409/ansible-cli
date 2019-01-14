import fire
from libs.paths import resolv_relative

class Provision(object):
    def install_dep(self, env, target=None):
        return {
            "playbook": resolv_relative(__file__, "install_dep.yml"),
            "vars": {
                "env": env,
                "target": target,
            }
        }
