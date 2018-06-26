import json
import subprocess as sp


def get_test_json(test_command, json_name):
    get_json_cmd = test_command+" > "+str(json_name)
    sp.call( get_json_cmd, shell=True)


def get_test_stat(json_name):
    test_stat = {}
    try:
        json_data = json.load( open(json_name) )
        test_stat = get_test_stat_from_god_json(json_data, test_stat)
    except:
        test_stat = get_test_stat_from_bad_json(json_name)

    print("Number of tests: "+str(test_stat["tests"]))
    print("\tpasses: "+str(test_stat["passes"]))
    print("\tfailures: "+str(test_stat["failures"]))
    print("\tpending: "+str(test_stat["pending"]))
    return test_stat


def get_test_stat_from_god_json(json_data, test_stat):
    test_stat["tests"] = json_data["stats"]["tests"]
    test_stat["passes"] = json_data["stats"]["passes"]
    test_stat["pending"] = json_data["stats"]["pending"]
    test_stat["failures"] = json_data["stats"]["failures"]
    return test_stat


def get_test_stat_from_bad_json(json_name):
    test_stat = {}
    with open(json_name, 'r', encoding='utf-8') as infile:
        for line in infile:
            if line.count("\"tests\": ") and line.count("[")==0 :
                test_stat["tests"] = int(line.split(",")[0].split(": ")[1])
            elif line.count("\"passes\": ") and line.count("[")==0 :
                test_stat["passes"] = int(line.split(",")[0].split(": ")[1])
            elif line.count("\"pending\": ") and line.count("[")==0 :
                test_stat["pending"] = int(line.split(",")[0].split(": ")[1])
            elif line.count("\"failures\": ") and line.count("[")==0 :
                test_stat["failures"] = int(line.split(",")[0].split(": ")[1])
    return test_stat


def results_comapre(buggy_test_stat, fixed_test_stat):
    if buggy_test_stat["failures"] != fixed_test_stat["failures"]:
        print("There is difference")
    else:
        print("There isn't difference")
