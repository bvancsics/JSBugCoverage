import argparse
import os
import sys


def arg_parser():

    parser = argparse.ArgumentParser(description = 'ide jon valami')

    for i in range(len(sys.argv)):
        if sys.argv[i] == "-cF" or sys.argv[i] == "--configFile":
            parser.add_argument('-cF', '--configFile', help = 'config file')
            args_conf = parser.parse_args()
            return arg_from_file(args_conf.configFile)

    parser.add_argument('-r', '--repo', required = True, help = 'project repo')
    parser.add_argument('-f', '--folder', required = True, help = 'clone/checkout folder')
    parser.add_argument('-H', '--hash', required = True, help = 'fix hash')
    parser.add_argument('-c', '--command', required = True, help = 'coverage command')
    parser.add_argument('-pF', '--patchFolder', required = True, help = 'fixed patches folder')



    param_dict = {}
    args                = parser.parse_args()
    param_dict["folder"] = args.folder
    param_dict["hash"] = args.hash
    param_dict["repo"] = args.repo
    param_dict["command"] = args.command
    param_dict["patchFolder"] = args.patchFolder

    check_fixed_folder_exist(param_dict["patchFolder"])

    return param_dict


def arg_from_file(configFile):
    param_dict = {}
    with open(configFile, "r") as infile:
        for line in infile:
            arg = line.split("\n")[0].split("=")[0]
            val = line.split("\n")[0].split("=")[1]
            param_dict[arg] = val
    return param_dict


def check_fixed_folder_exist(fixed):
    if not os.path.isdir(fixed):
        print(str(fixed)+" doesn't exist")
        exit()