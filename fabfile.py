from fabric.api import *
env.user = 'ubuntu'
env.hosts = ["35.174.205.38"]
env.key_filename = "/home/ubuntu/.ssh/id_rsa"


def hello():
    target = run('ls -t ./AirBnB_Clone_V2/versions/')
    print(target.split())
