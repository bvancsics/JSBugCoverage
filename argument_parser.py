import argparse
import os
import sys


def arg_parser():
    for i in range(len(sys.argv)):
        if sys.argv[i] == "-cB" or sys.argv[i] == "--checkout-buggy-version":
            return get_checkout_bug_parent_arguments()
        elif sys.argv[i] == "-cF" or sys.argv[i] == "--checkout-fixed-version":
            return get_checkout_fixed_arguments()
        elif sys.argv[i] == "-cFOTC" or sys.argv[i] == "--checkout-fixed-only-test-change":
            return get_checkout_fixed_only_test_arguments()

        elif sys.argv[i] == "-bR" or sys.argv[i] == "--buggy-results":
            return get_buggy_test_arguments()
        elif sys.argv[i] == "-fR" or sys.argv[i] == "--fixed-results":
            return get_fixed_test_arguments()
        elif sys.argv[i] == "-fOTCR" or sys.argv[i] == "--fixed-only-test-change-results":
            return get_fixed_only_test_change_test_arguments()

        elif sys.argv[i] == "-cmp" or sys.argv[i] == "--compare-buggy-and-fixed-results":
            return get_compare_arguments()

    print("Options:")
    print("\t-cB or --checkout-buggy-version")
    print("\t-cF or --checkout-fixed-version")
    print("\t-cFOTC or --checkout-fixed-only-test-change")
    print("\t-bR or --buggy-results")
    print("\t-fR or --fixed-results")
    print("\t-fOTCR or --fixed-only-test-change-results")
    print("\t-cmp or --compare-buggy-and-fixed-results")
    exit()


# *********************** checkout *************************

def get_checkout_bug_parent_arguments():
    parser = argparse.ArgumentParser(description = '   ')
    parser.add_argument('-cB',  '--checkout-buggy-version', action='store_true', help = '     ')

    parser.add_argument('-r',   '--repo',   required = True, help = 'project repo')
    parser.add_argument('-f',   '--folder', required = True, help = 'clone/checkout folder')
    parser.add_argument('-H',   '--hash',   required = True, help = 'fix hash')

    param_dict = {}
    args = parser.parse_args()
    param_dict["checkout-buggy-version"] = args.checkout_buggy_version
    param_dict["folder"] = args.folder
    param_dict["hash"] = args.hash
    param_dict["repo"] = args.repo
    return param_dict



def get_checkout_fixed_arguments():
    parser = argparse.ArgumentParser(description = '   ')
    parser.add_argument('-cF', '--checkout-fixed-version', action='store_true', help = '     ')

    parser.add_argument('-r',   '--repo',           required = True, help = 'project repo')
    parser.add_argument('-f',   '--folder',         required = True, help = 'clone/checkout folder')
    parser.add_argument('-H',   '--hash',           required = True, help = 'fix hash')

    param_dict = {}
    args = parser.parse_args()
    param_dict["checkout-fixed-version"] = args.checkout_fixed_version
    param_dict["folder"] = args.folder
    param_dict["hash"] = args.hash
    param_dict["repo"] = args.repo
    return param_dict


def get_checkout_fixed_only_test_arguments():
    parser = argparse.ArgumentParser(description = '   ')
    parser.add_argument('-cFOTC', '--checkout-fixed-only-test-change', action='store_true', help = '     ')

    parser.add_argument('-r',   '--repo',           required = True, help = 'project repo')
    parser.add_argument('-f',   '--folder',         required = True, help = 'clone/checkout folder')
    parser.add_argument('-H',   '--hash',           required = True, help = 'fix hash')
    parser.add_argument('-i',   '--include',        required = True, help = 'include (test)regex')
    parser.add_argument('-pF',  '--patchFolder',    required = True, help = 'fixed patches folder')

    param_dict = {}
    args = parser.parse_args()
    param_dict["checkout-fixed-only-test-change"] = args.checkout_fixed_only_test_change
    param_dict["folder"] = args.folder
    param_dict["hash"] = args.hash
    param_dict["repo"] = args.repo
    param_dict["include"] = args.include
    param_dict["patchFolder"] = args.patchFolder
    return param_dict


# *********************** test *************************

def get_buggy_test_arguments():
    parser = argparse.ArgumentParser(description = '   ')
    parser.add_argument('-bR',  '--buggy-results', action='store_true', help = '     ')

    parser.add_argument('-r',   '--repo',       required = True, help = 'project repo')
    parser.add_argument('-f',   '--folder',     required = True, help = 'clone/checkout folder')
    parser.add_argument('-H',   '--hash',       required = True, help = 'fix hash')
    parser.add_argument('-c',   '--command',    required = True, help = 'test command')

    param_dict = {}
    args = parser.parse_args()
    param_dict["buggy-results"] = args.buggy_results
    param_dict["folder"] = args.folder
    param_dict["hash"] = args.hash
    param_dict["repo"] = args.repo
    param_dict["command"] = args.command

    return param_dict


def get_fixed_test_arguments():
    parser = argparse.ArgumentParser(description = '   ')
    parser.add_argument('-fR',  '--fixed-results', action='store_true', help = '     ')

    parser.add_argument('-r',   '--repo',       required = True, help = 'project repo')
    parser.add_argument('-f',   '--folder',     required = True, help = 'clone/checkout folder')
    parser.add_argument('-H',   '--hash',       required = True, help = 'fix hash')
    parser.add_argument('-c',   '--command',    required = True, help = 'test command')

    param_dict = {}
    args = parser.parse_args()
    param_dict["fixed-results"] = args.fixed_results
    param_dict["folder"] = args.folder
    param_dict["hash"] = args.hash
    param_dict["repo"] = args.repo
    param_dict["command"] = args.command

    return param_dict

def get_fixed_only_test_change_test_arguments():
    parser = argparse.ArgumentParser(description = '   ')
    parser.add_argument('-fOTCR',  '--fixed-only-test-change-results', action='store_true', help = '     ')

    parser.add_argument('-r',   '--repo',           required = True, help = 'project repo')
    parser.add_argument('-f',   '--folder',         required = True, help = 'clone/checkout folder')
    parser.add_argument('-H',   '--hash',           required = True, help = 'fix hash')
    parser.add_argument('-c',   '--command',        required = True, help = 'test command')
    parser.add_argument('-i',   '--include',        required = True, help = 'include (test)regex')
    parser.add_argument('-pF',  '--patchFolder',    required = True, help = 'fixed patches folder')

    param_dict = {}
    args = parser.parse_args()
    param_dict["fixed-only-test-change-results"] = args.fixed_only_test_change_results
    param_dict["folder"] = args.folder
    param_dict["hash"] = args.hash
    param_dict["repo"] = args.repo
    param_dict["command"] = args.command
    param_dict["include"] = args.include
    param_dict["patchFolder"] = args.patchFolder

    return param_dict


# *********************** compare *************************

def get_compare_arguments():
    parser = argparse.ArgumentParser(description = '   ')
    parser.add_argument('-cmp',  '--compare-buggy-and-fixed-results', action='store_true', help = '     ')

    parser.add_argument('-r',   '--repo',           required = True, help = 'project repo')
    parser.add_argument('-f',   '--folder',         required = True, help = 'clone/checkout folder')
    parser.add_argument('-H',   '--hash',           required = True, help = 'fix hash')
    parser.add_argument('-c',   '--command',        required = True, help = 'test command')
    parser.add_argument('-i',   '--include',        required = True, help = 'include (test)regex')
    parser.add_argument('-pF',  '--patchFolder',    required = True, help = 'fixed patches folder')

    param_dict = {}
    args = parser.parse_args()
    param_dict["compare-buggy-and-fixed-results"] = args.compare_buggy_and_fixed_results
    param_dict["folder"] = args.folder
    param_dict["hash"] = args.hash
    param_dict["repo"] = args.repo
    param_dict["command"] = args.command
    param_dict["include"] = args.include
    param_dict["patchFolder"] = args.patchFolder

    return param_dict