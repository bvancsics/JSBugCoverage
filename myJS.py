import subprocess as sp


def npm_install():
    install_cmd = "npm install"
    sp.call(install_cmd, shell=True)


def get_tests(tests_folder):
    test_cmd = "/work/tests.js "+str(tests_folder)+" > ./tests.json"
    sp.call(test_cmd, shell=True)


def test_run(per_test_coverage, coverage_command, tests_folder):
    get_tests(tests_folder)
    if str(per_test_coverage) == "True":
        perTest_run(coverage_command)
    else:
        allTest_run(coverage_command)


def perTest_run(coverage_command):
    perTest_cmd = "/work/pertest.js -t ./tests.json -r perTest_results.txt -c \""+str(coverage_command)+"\""
    sp.call(perTest_cmd, shell=True)


def allTest_run(coverage_command):
    sp.call(coverage_command, shell=True)