import argument_parser
import myGit

"""
Examples:


"""


checkout_command_types = ["checkout-buggy-version", "checkout-fixed-version", "checkout-fixed-only-test-change"]
test_results_command_types = ["buggy-results", "fixed-results", "fixed-only-test-change-results"]
compare_results_command_types = ["compare-buggy-and-fixed-results"]
info_command_types = ["info"]

param_dict = argument_parser.arg_parser()

if myGit.is_checkout(param_dict, checkout_command_types):
    myGit.checkout(param_dict)
elif myGit.is_test(param_dict, test_results_command_types):
    myGit.test(param_dict)
elif myGit.is_compare(param_dict, compare_results_command_types):
    myGit.compare(param_dict)
elif myGit.is_info(param_dict, info_command_types):
    myGit.info(param_dict)