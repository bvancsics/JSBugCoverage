import argumentum_parser
import myGit
import myJS
import os
import other

# python3 main.py -r "https://github.com/expressjs/express" -f ./ProbaCheckout -H "2e1284beb6210444932d050b9d31d3908afb7591" -c "nyc --reporter json ./node_modules/.bin/mocha " -pF "./ExpressPatches"

param_dict = argumentum_parser.arg_parser()
fixed_patch_file = os.path.abspath(param_dict["patchFolder"]+"/"+param_dict["hash"])


myGit.git_clone(param_dict["repo"], param_dict["folder"])
myGit.git_chechout(param_dict["hash"], param_dict["include"], param_dict["command"],
                   param_dict["only-checkout"], str(fixed_patch_file))


if other.diff_between_jsons():
    myJS.get_tests()
    myJS.perTest_run(param_dict["command"])
