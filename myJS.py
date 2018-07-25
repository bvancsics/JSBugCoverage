import json
import myTest
import subprocess as sp


def npm_install():
    install_cmd = "npm install"
    sp.call(install_cmd, shell=True)


def test_run(per_test_coverage, coverage_command, test_command, pre_command):
    myTest.get_test_names(test_command)
    if str(per_test_coverage) == "True":
        precommand_run(pre_command)
        perTest_run(coverage_command)
    else:
        allTest_run(coverage_command)
    get_cov_stat()


def perTest_run(coverage_command):
    perTest_cmd = "/work/pertest.js -t ./tests.json -r perTest_results.txt -c \""+str(coverage_command)+"\""
    sp.call(perTest_cmd, shell=True)


def allTest_run(coverage_command):
    sp.call(coverage_command, shell=True)


def precommand_run(precommand):
    if len(precommand) > 0:
        sp.call(precommand, shell=True)


def get_cov_stat():
    cov_stat = {}
    try:
        json_data = json.load( open("./coverage/coverage-summary.json") )
        cov_stat["lines"] = get_cov_stat_from_god_json(json_data, "lines")
        cov_stat["statements"] = get_cov_stat_from_god_json(json_data, "statements")
        cov_stat["functions"] = get_cov_stat_from_god_json(json_data, "functions")
        cov_stat["branches"] = get_cov_stat_from_god_json(json_data, "branches")
        print("Number of function:\t"+str(cov_stat["functions"]["total"]))
        print("\tcovered:\t"+str(cov_stat["functions"]["covered"]))
        print("\tcovered (%):\t"+str(cov_stat["functions"]["pct"]))
    except:
        pass


def get_cov_stat_from_god_json(json_data, type):
    cov_stat_of_type = {}
    cov_stat_of_type["total"] = json_data["total"][type]["total"]
    cov_stat_of_type["covered"] = json_data["total"][type]["covered"]
    cov_stat_of_type["skipped"] = json_data["total"][type]["skipped"]
    cov_stat_of_type["pct"] = json_data["total"][type]["pct"]
    return cov_stat_of_type