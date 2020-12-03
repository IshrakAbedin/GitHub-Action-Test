import subprocess

def log(msg : str):
    print("[Python Tester]:", msg)

log("Beginning Test")
try:
    subprocess.check_call(["./bin/test.exe", "Hello", "GitHub", "Action", ", Yey!"])
    log(f"Process Completed Successfull with Return Code <0>")
except subprocess.CalledProcessError as error:
    log(f"Execution Failed with Returned Code <{error.returncode}>")