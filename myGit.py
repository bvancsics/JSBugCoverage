import myJS
import os
import shutil
import subprocess as sp


def git_clone(project_repo, folder):
    if os.path.isdir(folder):
        shutil.rmtree(folder)
    else:
        os.makedirs(folder)

    os.chdir(folder)
    clone_cmd = "git clone "+str(project_repo)
    sp.call(clone_cmd, shell=True)
    os.chdir( os.listdir( "./" )[0] )


def git_chechout(hash, include, command, only_checkout, fixed_patch_file):
    checkout_cmd = "git checkout "+str(hash)+"^1"
    sp.call(checkout_cmd, shell=True)

    if only_checkout == "True":
        exit()

    myJS.npm_install()
    myJS.get_cov_json(command, "../before.json")

    apply_cmd = "git apply --include=\""+str(include)+"\" "+str(fixed_patch_file)+".patch"
    sp.call(apply_cmd, shell=True)

    myJS.npm_install()
    myJS.get_cov_json(command, "../after.json")
