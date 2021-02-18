import json
import random


tests = {
	"FPGA-u250": {
		"team": "devops",
		"git_repo": "https://github.com/shlumper/jukoexample.git",
		"test_cmd_path": "/root/jukoexample",
		"image": "deepcontainerregistry.azurecr.io/base_python_image:0.1",
		"test_list": {
         
			"basic": {
				"required_mem": "1024",
				"artifact_paths": [
					"/root/cl_cifar10/verif/common/tools/index.html"
				],
            "test_commands": {}
			}
		}
	}
}

for number in range(100):
   rand = random.randint(0,50)
   tests["FPGA-u250"]["test_list"]["basic"]["test_commands"]["fib" + str(number)] = "python calculate.py " + str(rand)


print(json.dumps(tests, indent=4, sort_keys=True))