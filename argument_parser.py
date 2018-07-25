import argparse
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

        elif sys.argv[i] == "-I" or sys.argv[i] == "--info":
            return get_info_arguments()

    print("Options:")
    print("\t-cB or --checkout-buggy-version")
    print("\t-cF or --checkout-fixed-version")
    print("\t-cFOTC or --checkout-fixed-only-test-change")
    print("\t-bR or --buggy-results")
    print("\t-fR or --fixed-results")
    print("\t-fOTCR or --fixed-only-test-change-results")
    print("\t-cmp or --compare-buggy-and-fixed-results")
    print("\t-I or --info")
    exit()


# *********************** checkout *************************

def get_checkout_bug_parent_arguments():
    parser = argparse.ArgumentParser(description = '   ')
    parser.add_argument('-cB',  '--checkout-buggy-version', action='store_true', help = '     ')

    parser.add_argument('-r',   '--repo',   required = True, help = 'project repo')
    parser.add_argument('-f',   '--folder', required = True, help = 'clone/checkout folder')
    parser.add_argument('-b',   '--bug-ID',         required = True, help = 'bug ID')

    param_dict = {}
    args = parser.parse_args()
    param_dict["checkout-buggy-version"] = args.checkout_buggy_version
    param_dict["folder"] = args.folder
    param_dict["bug-ID"] = args.bug_ID
    param_dict["repo"] = args.repo
    return param_dict



def get_checkout_fixed_arguments():
    parser = argparse.ArgumentParser(description = '   ')
    parser.add_argument('-cF', '--checkout-fixed-version', action='store_true', help = '     ')

    parser.add_argument('-r',   '--repo',           required = True, help = 'project repo')
    parser.add_argument('-f',   '--folder',         required = True, help = 'clone/checkout folder')
    parser.add_argument('-b',   '--bug-ID',         required = True, help = 'bug ID')

    param_dict = {}
    args = parser.parse_args()
    param_dict["checkout-fixed-version"] = args.checkout_fixed_version
    param_dict["folder"] = args.folder
    param_dict["bug-ID"] = args.bug_ID
    param_dict["repo"] = args.repo
    return param_dict


def get_checkout_fixed_only_test_arguments():
    parser = argparse.ArgumentParser(description = '   ')
    parser.add_argument('-cFOTC', '--checkout-fixed-only-test-change', action='store_true', help = '     ')

    parser.add_argument('-r',   '--repo',           required = True, help = 'project repo')
    parser.add_argument('-f',   '--folder',         required = True, help = 'clone/checkout folder')
    parser.add_argument('-b',   '--bug-ID',         required = True, help = 'bug ID')

    param_dict = {}
    args = parser.parse_args()
    param_dict["checkout-fixed-only-test-change"] = args.checkout_fixed_only_test_change
    param_dict["folder"] = args.folder
    param_dict["bug-ID"] = args.bug_ID
    param_dict["repo"] = args.repo
    return param_dict


# *********************** test *************************

def get_buggy_test_arguments():
    parser = argparse.ArgumentParser(description = '   ')
    parser.add_argument('-bR',  '--buggy-results', action='store_true', help = '     ')

    parser.add_argument('-r',   '--repo',           required = True, help = 'project repo')
    parser.add_argument('-f',   '--folder',         required = True, help = 'clone/checkout folder')
    parser.add_argument('-b',   '--bug-ID',         required = True, help = 'bug ID')
    parser.add_argument('-tC',  '--test-command',   required = True, help = 'test command')

    parser.add_argument('-pTC', '--per-test-coverage', action='store_true', default=False, help = 'run per-test coverage')
    parser.add_argument('-CC',  '--coverage-command', default="None", help = '(istanbul) coverage command')
    parser.add_argument('-pC',  '--pre-command', default="None", help = 'required pre-command')

    param_dict = {}
    args = parser.parse_args()
    param_dict["buggy-results"] = args.buggy_results
    param_dict["folder"] = args.folder
    param_dict["bug-ID"] = args.bug_ID
    param_dict["repo"] = args.repo
    param_dict["test-command"] = args.test_command

    param_dict["per-test-coverage"] = args.per_test_coverage
    param_dict["coverage-command"] = args.coverage_command
    param_dict["pre-command"] = args.pre_command

    return param_dict


def get_fixed_test_arguments():
    parser = argparse.ArgumentParser(description = '   ')
    parser.add_argument('-fR',  '--fixed-results', action='store_true', help = '     ')

    parser.add_argument('-r',   '--repo',           required = True, help = 'project repo')
    parser.add_argument('-f',   '--folder',         required = True, help = 'clone/checkout folder')
    parser.add_argument('-b',   '--bug-ID',         required = True, help = 'bug ID')
    parser.add_argument('-tC',  '--test-command',   required = True, help = 'test command')

    parser.add_argument('-pTC', '--per-test-coverage', action='store_true', default=False, help = 'run per-test coverage')
    parser.add_argument('-CC',  '--coverage-command', default="None", help = '(istanbul) coverage command')
    parser.add_argument('-pC',  '--pre-command', default="None", help = 'required pre-command')


    param_dict = {}
    args = parser.parse_args()
    param_dict["fixed-results"] = args.fixed_results
    param_dict["folder"] = args.folder
    param_dict["bug-ID"] = args.bug_ID
    param_dict["repo"] = args.repo
    param_dict["test-command"] = args.test_command

    param_dict["per-test-coverage"] = args.per_test_coverage
    param_dict["coverage-command"] = args.coverage_command
    param_dict["pre-command"] = args.pre_command

    return param_dict

def get_fixed_only_test_change_test_arguments():
    parser = argparse.ArgumentParser(description = '   ')
    parser.add_argument('-fOTCR',  '--fixed-only-test-change-results', action='store_true', help = '     ')

    parser.add_argument('-r',   '--repo',           required = True, help = 'project repo')
    parser.add_argument('-f',   '--folder',         required = True, help = 'clone/checkout folder')
    parser.add_argument('-b',   '--bug-ID',         required = True, help = 'bug ID')
    parser.add_argument('-tC',  '--test-command',   required = True, help = 'test command')

    parser.add_argument('-pTC', '--per-test-coverage', action='store_true', default=False, help = 'run per-test coverage')
    parser.add_argument('-CC',  '--coverage-command', default="None", help = '(istanbul) coverage command')
    parser.add_argument('-pC',  '--pre-command', default="None", help = 'required pre-command')

    param_dict = {}
    args = parser.parse_args()
    param_dict["fixed-only-test-change-results"] = args.fixed_only_test_change_results
    param_dict["folder"] = args.folder
    param_dict["bug-ID"] = args.bug_ID
    param_dict["repo"] = args.repo
    param_dict["test-command"] = args.test_command

    param_dict["per-test-coverage"] = args.per_test_coverage
    param_dict["coverage-command"] = args.coverage_command
    param_dict["pre-command"] = args.pre_command

    return param_dict


# *********************** compare *************************

def get_compare_arguments():
    parser = argparse.ArgumentParser(description = '   ')
    parser.add_argument('-cmp',  '--compare-buggy-and-fixed-results', action='store_true', help = '     ')

    parser.add_argument('-r',   '--repo',           required = True, help = 'project repo')
    parser.add_argument('-f',   '--folder',         required = True, help = 'clone/checkout folder')
    parser.add_argument('-b',   '--bug-ID',         required = True, help = 'bug ID')
    parser.add_argument('-tC',  '--test-command',   required = True, help = 'test command')

    param_dict = {}
    args = parser.parse_args()
    param_dict["compare-buggy-and-fixed-results"] = args.compare_buggy_and_fixed_results
    param_dict["folder"] = args.folder
    param_dict["bug-ID"] = args.bug_ID
    param_dict["repo"] = args.repo
    param_dict["test-command"] = args.test_command

    return param_dict

# *********************** compare *************************

def get_info_arguments():
    parser = argparse.ArgumentParser(description = '   ')
    parser.add_argument('-I',   '--info', action='store_true', help = '     ')

    parser.add_argument('-b',   '--bug-ID',         required = True, help = 'bug ID')
    parser.add_argument('-r',   '--repo',           required = True, help = 'project repo')

    param_dict = {}
    args = parser.parse_args()
    param_dict["info"] = args.info
    param_dict["bug-ID"] = args.bug_ID
    param_dict["repo"] = args.repo

    return param_dict