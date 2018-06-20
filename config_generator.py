import argparse
import subprocess as sp
import os

"""
python3 config_generator.py
    -d ./data.csv
    -f ./CheckoutFolder
    -pF ./ExpressPatches/
"""

def arg_parser():

    parser = argparse.ArgumentParser(description = 'ide jon valami')
    parser.add_argument('-d', '--data', required = True, help = 'data csv file')
    parser.add_argument('-f', '--folder', required = True, help = 'clone/checkout folder')
    parser.add_argument('-pF', '--patchFolder', required = True, help = 'fixed patches folder')
    parser.add_argument('-oC', '--only-checkout', action='store_true', help = 'only checkout buggy version')
    parser.add_argument('-pTC', '--per-test-coverage', action='store_true', default=False, help = 'run per-test coverage')

    param_dict = {}
    args  = parser.parse_args()
    param_dict["data"] = args.data
    param_dict["folder"] = args.folder
    param_dict["patchFolder"] = args.patchFolder
    param_dict["only-checkout"] = args.only_checkout
    param_dict["per-test-coverage"] = args.per_test_coverage


    check_fixed_folder_exist(param_dict["patchFolder"])
    return param_dict


def check_fixed_folder_exist(fixed):
    if not os.path.isdir(fixed):
        print(str(fixed)+" doesn't exist")
        exit()


def get_attributes_from_data_csv(line):
    return line.split(";")[0], line.split(";")[1], line.split(";")[2], line.split(";")[3], line.split(";")[4]


def config_writer(repo, commit_hash, cmd, tests, include, param_dict):
    o_file=("CONFIG_"+str(commit_hash))
    F=open(o_file, "w")
    F.write("repo="+str(repo)+"\n")
    F.write("hash="+str(commit_hash)+"\n")
    F.write("folder="+str(param_dict["folder"])+"/"+str(commit_hash)+"\n")
    F.write("patchFolder="+str(param_dict["patchFolder"])+"\n")
    F.write("command="+str(cmd)+"\n")
    F.write("include="+str(include)+"\n")
    F.write("tests="+str(tests)+"\n")
    F.write("only-checkout="+str(param_dict["only-checkout"])+"\n")
    F.write("per-test-coverage="+str(param_dict["per-test-coverage"]))
    F.close()


def data_csv_reader(param_dict):
    F = open(param_dict["data"], "r")
    lines = F.readlines()

    for x in range(1, len(lines)):
        line = lines[x].split("\n")[0]

        if line.startswith("#"):
            # Ignore lines that start with #
            pass
        else:
            repo, commit_hash, cmd, tests, include = get_attributes_from_data_csv(line)
            config_writer(repo, commit_hash, cmd, tests, include, param_dict)
            run_cmd = "python3 main.py -cF "+"CONFIG_"+str(commit_hash)
            sp.call(run_cmd, shell=True)
    F.close()


param_dict = arg_parser()
data_csv_reader(param_dict)

