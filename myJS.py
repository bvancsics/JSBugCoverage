import subprocess as sp


def npm_install():
    install_cmd = "npm install"
    sp.call(install_cmd, shell=True)


def get_tests():
    test_cmd = "/work/tests.js ./test > tests.json"
    sp.call(test_cmd, shell=True)


def perTest_run():
    perTest_cmd = "/work/pertest.js"
    sp.call(perTest_cmd, shell=True)


def pertestJS_modify(pertesJS_file, coverage_command):
    with open(pertesJS_file, 'r') as file :
      filedata = file.read().replace( '[COV_COMMAND]', str(coverage_command))

    with open(pertesJS_file, 'w') as file:
      file.write(filedata)


def pertestJS_reset(pertesJS_file, coverage_command):
    with open(pertesJS_file, 'r') as file :
      filedata = file.read().replace( str(coverage_command), '[COV_COMMAND]' )

    with open(pertesJS_file, 'w') as file:
      file.write(filedata)