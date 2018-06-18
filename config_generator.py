import argparse
import subprocess as sp
import os

def arg_parser():

    parser = argparse.ArgumentParser(description = 'ide jon valami')
    parser.add_argument('-d', '--data', required = True, help = 'data csv file')
    parser.add_argument('-f', '--folder', required = True, help = 'clone/checkout folder')
    parser.add_argument('-pF', '--patchFolder', required = True, help = 'fixed patches folder')
    parser.add_argument('-oC', '--only-checkout', default=False, help = 'only checkout buggy version')

    param_dict = {}
    args  = parser.parse_args()
    param_dict["data"] = args.data
    param_dict["folder"] = args.folder
    param_dict["patchFolder"] = args.patchFolder
    param_dict["only-checkout"] = args.only_checkout

    check_fixed_folder_exist(param_dict["patchFolder"])
    return param_dict


def check_fixed_folder_exist(fixed):
    if not os.path.isdir(fixed):
        print(str(fixed)+" doesn't exist")
        exit()


def get_attributes_from_data_csv(line):
    return line.split(";")[0], line.split(";")[1], line.split(";")[2], line.split(";")[3]


def config_writer(repo, commit_hash, cmd, include, folder, patchFolder, only_checkout):
    o_file=("CONFIG_"+str(commit_hash))
    F=open(o_file, "w")
    F.write("repo="+str(repo)+"\n")
    F.write("hash="+str(commit_hash)+"\n")
    F.write("folder="+str(folder)+"/"+str(commit_hash)+"\n")
    F.write("patchFolder="+str(patchFolder)+"\n")
    F.write("command="+str(cmd)+"\n")
    F.write("include="+str(include)+"\n")
    F.write("only-checkout="+str(only_checkout))
    F.close()


def data_csv_reader(param_dict):
    F = open(param_dict["data"], "r")
    lines = F.readlines()

    for x in range(1, len(lines)):
        line = lines[x].split("\n")[0]
        repo, commit_hash, cmd, include = get_attributes_from_data_csv(line)
        config_writer(repo, commit_hash, cmd, include, param_dict["folder"], param_dict["patchFolder"], param_dict["only-checkout"])
        run_cmd = "python3 main.py -cF "+"CONFIG_"+str(commit_hash)
        sp.call(run_cmd, shell=True)
    F.close()


param_dict = arg_parser()
data_csv_reader(param_dict)

