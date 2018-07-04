import argparse
import subprocess as sp


def arg_parser():

    parser = argparse.ArgumentParser(description = 'ide jon valami')
    parser.add_argument('--data', required = True, help = 'data csv file')
    parser.add_argument('--task', required = True,
                        choices=["checkout-buggy-version",
                                 "checkout-fixed-version",
                                 "checkout-fixed-only-test-change",
                                 "buggy-results",
                                 "fixed-results",
                                 "fixed-only-test-change-results",
                                 "compare-buggy-and-fixed-results",
                                 "info"])
    parser.add_argument('--per-test-coverage', action='store_true', default=False, help = 'run per-test coverage')

    param_dict = {}
    args  = parser.parse_args()
    param_dict["data"] = args.data
    param_dict["task"] = args.task
    param_dict["per-test-coverage"] = args.per_test_coverage
    return param_dict


def get_attributes_from_data_csv(line):
    cmd_param_dict = {}
    cmd_param_dict["bug-ID"] = line.split(";")[0]
    cmd_param_dict["repo"] = line.split(";")[1]
    cmd_param_dict["folder"] = line.split(";")[2]
    cmd_param_dict["test-command"] = "\""+line.split(";")[3]+"\""
    cmd_param_dict["coverage-command"] = "\""+line.split(";")[4]+"\""
    cmd_param_dict["test-folders"] = "\""+line.split(";")[5]+"\""
    cmd_param_dict["pre-command"] = "\""+line.split(";")[6]+"\""
    return cmd_param_dict


def do_command(param_dict, cmd_param_dict):
    cmd = ""
    if param_dict["task"] == "checkout-buggy-version":
        cmd = "-cB -r "+cmd_param_dict["repo"]+\
              " -f "+cmd_param_dict["folder"]+\
              " -b "+cmd_param_dict["bug-ID"]
    elif param_dict["task"] == "checkout-fixed-version":
        cmd = "-cF -r "+cmd_param_dict["repo"]+\
              " -f "+cmd_param_dict["folder"]+\
              " -b "+cmd_param_dict["bug-ID"]
    elif param_dict["task"] in ["cFOTC", "checkout-fixed-only-test-change"]:
        cmd = "-cFOTC -r "+cmd_param_dict["repo"]+\
              " -f "+cmd_param_dict["folder"]+\
              " -b "+cmd_param_dict["bug-ID"]

    elif param_dict["task"] in ["bR", "buggy-results"]:
        cmd = "-bR -r "+cmd_param_dict["repo"]+\
              " -f "+cmd_param_dict["folder"]+\
              " -b "+cmd_param_dict["bug-ID"]+\
              " -tC "+cmd_param_dict["test-command"]+\
              " -CC "+cmd_param_dict["coverage-command"]+\
              " -tF "+cmd_param_dict["test-folders"]
        if str(param_dict["per-test-coverage"]) == "True":
            cmd += "--per-test-coverage"+\
                   " -pC "+cmd_param_dict["pre-command"]
    elif param_dict["task"] in ["fR", "fixed-results"]:
        cmd = "-fR -r "+cmd_param_dict["repo"]+\
              " -f "+cmd_param_dict["folder"]+\
              " -b "+cmd_param_dict["bug-ID"]+\
              " -tC "+cmd_param_dict["test-command"]+\
              " -CC "+cmd_param_dict["coverage-command"]+\
              " -tF "+cmd_param_dict["test-folders"]
        if str(param_dict["per-test-coverage"]) == "True":
            cmd += " --per-test-coverage "+\
                   " -pC "+cmd_param_dict["pre-command"]
    elif param_dict["task"] in ["fOTCR", "fixed-only-test-change-results"]:
        cmd = "-fOTCR -r "+cmd_param_dict["repo"]+\
              " -f "+cmd_param_dict["folder"]+\
              " -b "+cmd_param_dict["bug-ID"]+\
              " -tF "+cmd_param_dict["test-folders"]+\
              " -tC "+cmd_param_dict["test-command"]+\
              " -CC "+cmd_param_dict["coverage-command"]
        if str(param_dict["per-test-coverage"]) == "True":
            cmd += " --per-test-coverage "+\
                   " -pC "+cmd_param_dict["pre-command"]

    elif param_dict["task"] in ["cmp", "compare-buggy-and-fixed-results"]:
        cmd = "-cmp -r "+cmd_param_dict["repo"]+\
              " -f "+cmd_param_dict["folder"]+\
              " -b "+cmd_param_dict["bug-ID"]+\
              " -tC "+cmd_param_dict["test-command"]

    elif param_dict["task"] in ["I", "info"]:
        cmd = "-I -b "+str(cmd_param_dict["bug-ID"])+\
              " -r "+cmd_param_dict["repo"]

    return cmd


def data_csv_reader(param_dict):
    F = open(param_dict["data"], "r")
    lines = F.readlines()

    for x in range(1, len(lines)):
        line = lines[x].split("\n")[0]

        if line.startswith("#"):
            # Ignore lines that start with #
            pass
        else:
            cmd_param_dict = get_attributes_from_data_csv(line)
            cmd = "python3 main.py "+str(do_command(param_dict, cmd_param_dict))
            print()
            print(cmd)
            print()
            sp.call(cmd, shell=True)
    F.close()


#*******************************************

param_dict = arg_parser()
data_csv_reader(param_dict)