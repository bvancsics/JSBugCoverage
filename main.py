import argument_parser
import myGit

"""
Examples:

python3 main.py --checkout-buggy-version --repo https://github.com/expressjs/express -f ./ASD -H 12626aed35a6d1ef4466fa0d67613a53db8b1149

python3 main.py --buggy-results --repo https://github.com/expressjs/express -f ./ASD -H 12626aed35a6d1ef4466fa0d67613a53db8b1149 -c "node_modules/.bin/_mocha --require test/support/env --reporter json test/ test/acceptance/"

python3 main.py --compare-buggy-and-fixed-results --repo https://github.com/expressjs/express -f ./ASD -H 12626aed35a6d1ef4466fa0d67613a53db8b1149 -c "node_modules/.bin/_mocha --require test/support/env --reporter json test/ test/acceptance/" -pF /work/data/expressjs_express/patches/ -i test/*
"""


checkout_command_types = ["checkout-buggy-version", "checkout-fixed-version", "checkout-fixed-only-test-change"]
test_results_command_types = ["buggy-results", "fixed-results", "fixed-only-test-change-results"]
compare_results_command_types = ["compare-buggy-and-fixed-results"]

param_dict = argument_parser.arg_parser()

if myGit.is_checkout(param_dict, checkout_command_types):
    myGit.checkout(param_dict)
elif myGit.is_test(param_dict, test_results_command_types):
    myGit.test(param_dict)
elif myGit.is_compare(param_dict, compare_results_command_types):
    myGit.compare(param_dict)
