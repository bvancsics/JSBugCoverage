import subprocess as sp



def npm_install():
    install_cmd = "npm install"
    sp.call(install_cmd, shell=True)