import subprocess as sp


def npm_install():
    install_cmd = "npm install"
    sp.call(install_cmd, shell=True)


def get_tests(tests_folder):
    test_cmd = "/work/tests.js "+str(tests_folder)+" > ./tests.json"
    sp.call(test_cmd, shell=True)


def perTest_run(coverage_command):
    perTest_cmd = "/work/pertest.js -t ./tests.json -r results.txt -c \""+str(coverage_command)+"\""
    sp.call(perTest_cmd, shell=True)


def get_cov_json(coverage_command, json_name):
    json_command = cut_command(coverage_command)
    get_json_cmd = json_command+" > "+str(json_name)
    sp.call( get_json_cmd, shell=True)


def cut_command(coverage_command):
    return coverage_command.replace("istanbul cover --report json-summary ", "").replace(" -- ", " ").replace(" --no-exit ", " ")

