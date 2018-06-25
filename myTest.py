import json
import subprocess as sp


def get_test_json(test_command, json_name):
    get_json_cmd = test_command+" > "+str(json_name)
    sp.call( get_json_cmd, shell=True)


def get_test_stat(json_name):
    test_stat = {}
    json_data = json.load( open(json_name) )
    test_stat["tests"] = json_data["stats"]["tests"]
    test_stat["passes"] = json_data["stats"]["passes"]
    test_stat["pending"] = json_data["stats"]["pending"]
    test_stat["failures"] = json_data["stats"]["failures"]

    print("Number of tests: "+str(test_stat["tests"]))
    print("\tpasses: "+str(test_stat["passes"]))
    print("\tfailures: "+str(test_stat["failures"]))
    print("\tpending: "+str(test_stat["pending"]))
    return test_stat


def results_comapre(befor_json, after_json):
    before_failed_tests = get_failed_tests(befor_json)
    after_failed_tests = get_failed_tests(after_json)

    if len(before_failed_tests) != len(after_failed_tests):
        print("There is difference")
    else:
        print("There isn't difference")


def get_failed_tests(json_file):
    tests = set()
    json_data = json.load( open(json_file) )
    for test in json_data["failures"]:
        tests.add(test["fullTitle"])
    return tests
