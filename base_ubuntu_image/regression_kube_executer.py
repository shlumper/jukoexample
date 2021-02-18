import os
import subprocess
import sys 
import json
from datetime import datetime
import logging
import shutil
from pathlib import Path


# running this locally 
# python regression_kube_consumer.py "job3" optimizer localhost /tmp/deleteme/ 
logger = logging.getLogger('regression_kube_executer')

debug_level = logging.INFO
print("*** running in debug mode - debug level="+str(debug_level)+" ***")

logging.basicConfig(format='%(asctime)s - %(name)s - %(lineno)s - %(funcName)s() - %(levelname)s - %(message)s', level=debug_level)
logging.getLogger("adal-python").setLevel(logging.WARNING)


def export_dir(src, dst):
    src = os.path.abspath(src)
    artifact_name = src.split("/")[-1]
    new_dst = os.path.join(dst, artifact_name)
    print("starting exporting:", src, new_dst)

    if os.path.isfile(src):
        shutil.copy(src, new_dst)
        print("copying:", src, new_dst)
    elif not os.path.exists(src):
        f = open(new_dst, "a")
        f.write("this file was created by regression kube, this artifact path was not exists")
        f.close()
        print("file not exists, creating empty one:", src, new_dst)
    else:
        os.makedirs(new_dst, exist_ok=True)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(new_dst, item)
            print("copying:", s, d)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks=True)
            elif os.path.isfile(s):
                shutil.copy(s, d)
            else:
                shutil.copy2(s, d)

job_name = sys.argv[1] # "job1"
commit = sys.argv[2] # "optimizer_shl6fix_mushon_tests"
test_result_path = sys.argv[3] #/kube_mnt/job5/test_outputs
test_name = sys.argv[4] #test name
test_cmd = sys.argv[5] #command line - "ls -la"
suite = sys.argv[6] #Basic
test_cmd_path = sys.argv[7] #Basic
artifacts_paths = []
if sys.argv[8]:
    artifacts_paths = sys.argv[8].split(",")
git_repo = sys.argv[9] #Basic


logging.info("parameters:")
logging.info("job_name: " + job_name)
logging.info("commit: " + commit)
logging.info("test_result_path: " + test_result_path)
logging.info("test_name: " + test_name)
logging.info("test_cmd: " + test_cmd)
logging.info("test_cmd_path: " + test_cmd_path)
logging.info("artifacts_paths: " + str(artifacts_paths))

def run_command(command, stdout_file_name):
    logging.info("stdout_file_name - " + stdout_file_name)
    with open(stdout_file_name, 'wb') as f: 
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for c in iter(lambda: process.stdout.read(1), b''):  
            sys.stdout.write(str(c.decode('cp1252')))
            f.write(c)
    return_code = process.poll()
    logging.info("return code: " + str(return_code))
    return str(return_code)
    
startTime = datetime.now()
logging.info("startTime" + str(startTime))

result = {}
result["job_name"] = job_name
result["suite"] = suite
result["test_name"] = test_name
result["commit"] = commit
result["test_cmd"] = test_cmd

output_file_name = suite + "." + result["test_name"].replace(" ","_")
logging.info("output_file_name: " + output_file_name)
stdout_file_name = test_result_path + "/stds/" + output_file_name + ".stdout.txt"
logging.info("stdout_file_name: " + stdout_file_name)

os.makedirs(test_result_path, exist_ok=True)
os.makedirs(test_result_path + "/stds/", exist_ok=True)
os.makedirs(test_result_path + "/results/", exist_ok=True)

tmp_exported_artifacts_path = "/tmp/artifacts/" + output_file_name
os.makedirs(tmp_exported_artifacts_path, exist_ok=True)



result["rc_status"] = run_command(["./start_script.sh", commit, test_cmd_path, test_cmd, git_repo], stdout_file_name)
result["duraiton"] = (str(datetime.now() - startTime)).split(".")[0]


tests_results_file_name =  test_result_path + "/results/" + output_file_name + ".json"

logging.info("writing results to: " + tests_results_file_name)
logging.info("writing results: " + str(result))
with open(tests_results_file_name, 'w') as json_file:
  json.dump(result, json_file, indent=4)
  

logging.info("writing tmp artifacts: ")

if (artifacts_paths):
    for each_path in artifacts_paths:
        export_dir(each_path, tmp_exported_artifacts_path)

logging.info("writing original artifacts: ")
exported_artifacts_path = test_result_path + "/artifacts/" + output_file_name
shutil.copytree(tmp_exported_artifacts_path, exported_artifacts_path, symlinks=True)

