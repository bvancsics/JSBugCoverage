import myTest
import myJS
import os
import subprocess as sp


# ****************** checkout **********************

def is_checkout(param_dict, checkout_command_types):
    for checkout_command in checkout_command_types:
        if checkout_command in param_dict.keys():
            return True
    return False


def checkout(param_dict):
    if "checkout-buggy-version" in param_dict.keys():
        checkout_buggy_version(param_dict["repo"], param_dict["folder"], param_dict["hash"])
    elif "checkout-fixed-version" in param_dict.keys():
        checkout_fixed_version(param_dict["repo"], param_dict["folder"], param_dict["hash"])
    elif "checkout-fixed-only-test-change" in param_dict.keys():
        checkout_fixed_version_only_tests(param_dict["repo"], param_dict["folder"], param_dict["hash"],
                                          param_dict["include"], param_dict["patchFolder"])


def checkout_buggy_version(repo, folder, fixed_hash):
    clone_repo(repo, folder)
    checkout_cmd = "git checkout "+str(fixed_hash)+"^1"
    sp.call(checkout_cmd, shell=True)


def checkout_fixed_version(repo, folder, fixed_hash):
    clone_repo(repo, folder)
    checkout_cmd = "git checkout "+str(fixed_hash)
    sp.call(checkout_cmd, shell=True)


def checkout_fixed_version_only_tests(repo, folder, fixed_hash, include, patchFolder):
    checkout_buggy_version(repo, folder, fixed_hash)
    patch_apply(patchFolder, fixed_hash, include)


def patch_apply(patchFolder, fixed_hash, include):
    fixed_patch_file = os.path.abspath(patchFolder+"/"+fixed_hash)
    apply_cmd = "git apply --include=\""+str(include)+"\" "+str(fixed_patch_file)+".patch"
    sp.call(apply_cmd, shell=True)


def clone_repo(project_repo, folder):
    if os.path.isdir(folder):
        rm_cmd = "rm -R "+str(folder)
        sp.call(rm_cmd, shell=True)

    os.makedirs(folder)

    os.chdir(folder)
    clone_cmd = "git clone "+str(project_repo)
    sp.call(clone_cmd, shell=True)
    os.chdir( os.listdir( "./" )[0] )


# ***************** test results ********************

def is_test(param_dict, test_results_command_types):
    for test_results_command in test_results_command_types:
        if test_results_command in param_dict.keys():
            return True
    return False

def test(param_dict):
    if "buggy-results" in param_dict.keys():
        buggy_test_results(param_dict["repo"], param_dict["folder"], param_dict["hash"], param_dict["test-command"])
    elif "fixed-results" in param_dict.keys():
        fixed_test_results(param_dict["repo"], param_dict["folder"], param_dict["hash"], param_dict["test-command"])
    elif "fixed-only-test-change-results" in param_dict.keys():
        fixed_only_test_change_results(param_dict["repo"], param_dict["folder"], param_dict["hash"],
                                       param_dict["test-command"], param_dict["include"], param_dict["patchFolder"])

    myJS.test_run(param_dict["per-test-coverage"], param_dict["coverage-command"], param_dict["test-folders"], param_dict["pre-command"])


def buggy_test_results(repo, folder, fixed_hash, test_command):
    checkout_buggy_version(repo, folder, fixed_hash)
    myJS.npm_install()
    myTest.get_test_json(test_command, "../buggy-results.json")
    myTest.get_test_stat("../buggy-results.json")


def fixed_test_results(repo, folder, fixed_hash, test_command):
    checkout_fixed_version(repo, folder, fixed_hash)
    myJS.npm_install()
    myTest.get_test_json(test_command, "../fixed-results.json")
    myTest.get_test_stat("../fixed-results.json")


def fixed_only_test_change_results(repo, folder, fixed_hash, test_command, include, patchFolder):
    checkout_fixed_version_only_tests(repo, folder, fixed_hash, include, patchFolder)
    myJS.npm_install()
    myTest.get_test_json(test_command, "../fixed-only-test-change-results.json")
    myTest.get_test_stat("../fixed-only-test-change-results.json")


# ************ compare **************

def is_compare(param_dict, compare_results_command_types):
    for compare_results_command in compare_results_command_types:
        if compare_results_command in param_dict.keys():
            return True
    return False


def compare(param_dict):
    if "compare-buggy-and-fixed-results" in param_dict.keys():
        compare_test_results(param_dict["repo"], param_dict["folder"], param_dict["hash"],
                             param_dict["test-command"], param_dict["include"], param_dict["patchFolder"])


def compare_test_results(repo, folder, fixed_hash, test_command, include, patchFolder):
    checkout_buggy_version(repo, folder, fixed_hash)
    myJS.npm_install()
    myTest.get_test_json(test_command, "../buggy-results.json")
    buggy_test_stat = myTest.get_test_stat("../buggy-results.json")


    patch_apply(patchFolder, fixed_hash, include)
    myJS.npm_install()
    myTest.get_test_json(test_command, "../fixed-results.json")
    fixed_test_stat = myTest.get_test_stat("../fixed-results.json")

    myTest.results_comapre(buggy_test_stat, fixed_test_stat)


# ************ info **************


def is_info(param_dict, info_command_types):
    for info_command in info_command_types:
        if info_command in param_dict.keys():
            return True
    return False


def info(param_dict):
    if "info" in param_dict.keys():
        get_info(param_dict["bug-ID"], param_dict["repo"], param_dict["hash"])


def get_info(ID, repo, commit_hash):
    print("Bug ID:\t\t"+str(ID))
    print("Repository:\t"+str(repo))
    print("Commit hash:\t"+str(commit_hash))
    commit_link = str(repo).replace(".git", "")+str("/commit/"+str(commit_hash))
    print("Commit link:\t"+str(commit_link))
