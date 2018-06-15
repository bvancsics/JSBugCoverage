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


def git_chechout(hash, include, fixed_patch_file):
    checkout_cmd = "git checkout "+str(hash)+"^1"
    sp.call(checkout_cmd, shell=True)

    apply_cmd = "git apply "+str(fixed_patch_file)+".patch --include="+str(include)
    sp.call(apply_cmd, shell=True)