import json

def diff_between_jsons():
    befor_data = json.load( open('../before.json') )
    after_data = json.load( open('../after.json') )

    if int(befor_data["stats"]["failures"]) < int(after_data["stats"]["failures"]):
        return True

    return False
