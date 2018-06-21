import subprocess as sp


def npm_install():
    install_cmd = "npm install"
    sp.call(install_cmd, shell=True)


def get_tests(tests_folder):
    test_cmd = "/work/tests.js "+str(tests_folder)+" > ./tests.json"
    sp.call(test_cmd, shell=True)


def get_test_results():
    sp.call("/work/results.js -t ../before.json -r ./before_results.txt", shell=True)
    sp.call("/work/results.js -t ../after.json -r ./after_results.txt", shell=True)


def test_run(per_test_coverage, coverage_command):
    if per_test_coverage == "True":
        perTest_run(coverage_command)
    else:
        allTest_run(coverage_command)


def perTest_run(coverage_command):
    perTest_cmd = "/work/pertest.js -t ./tests.json -r perTest_results.txt -c \""+str(coverage_command)+"\""
    sp.call(perTest_cmd, shell=True)


def allTest_run(coverage_command):
    sp.call(coverage_command, shell=True)


def get_cov_json(coverage_command, json_name):
    json_command = cut_command(coverage_command)
    get_json_cmd = json_command+" > "+str(json_name)
    sp.call( get_json_cmd, shell=True)


def cut_command(coverage_command):
    tmp = coverage_command.split(" node_modules/")[1]
    return "node_modules/"+str(tmp).replace(" -- ", " ")
