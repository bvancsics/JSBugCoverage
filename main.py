import argument_parser
import myGit

"""
Examples:

python3 main.py -fOTCR -r https://github.com/expressjs/express -f ./ASD-1 -H 12626aed35a6d1ef4466fa0d67613a53db8b1149 -tF "test/ test/acceptance/" -tC "node_modules/.bin/_mocha --require test/support/env --reporter json test/ test/acceptance/" -CC "istanbul cover --report json-summary node_modules/.bin/_mocha -- --require test/support/env --reporter json --check-leaks test/ test/acceptance/" -i test/* -pF /data/MeroScript/expressjs_express/patches

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