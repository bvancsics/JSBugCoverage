import json
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove


def diff_between_jsons():
    befor_data = json.load( open('../before.json') )
    after_data = json.load( open('../after.json') )

    if int(befor_data["stats"]["failures"]) < int(after_data["stats"]["failures"]):
        return True
    return False


def get_failed_test():
    failed_test_names = set()
    befor_data = json.load( open('../before.json') )
    for failed_test in befor_data["failures"]:
        failed_test_names.add( str(failed_test["fullTitle"].replace(" ", ".")) )
    return failed_test_names


def failed_test_filtering(failed_test_names):
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open("./tests.json") as old_file:
            for line in old_file:
                if not _search(failed_test_names, line):
                    new_file.write( line )

    remove("./tests.json")
    move(abs_path, "./tests.json")


def _search(failed_test_names, line):
    for failed_test in failed_test_names:
        new_line = line.replace(" ", ".")
        if new_line.count( "\""+failed_test.replace(" ",".").replace("\"","\\\"")+"\"," ):
            return True
    return False
