import subprocess as sp


def npm_install():
    install_cmd = "npm install"
    sp.call(install_cmd, shell=True)


def get_tests():
    test_cmd = "/work/tests.js ./test > tests.json"
    sp.call(test_cmd, shell=True)


def perTest_run(coverage_command):
    perTest_cmd = "/work/pertest.js -t ./tests.json -r results.txt -c \""+str(coverage_command)+"\""
    sp.call(perTest_cmd, shell=True)

