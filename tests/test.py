import subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    ITALICIZED = '\033[3m'
    UNDERLINED = '\033[4m'
    INVERTED = '\033[7m'

def log(msg : str):
    print(f"[{bcolors.OKBLUE}Python Tester{bcolors.ENDC}]:", msg)

def main():
    log("Beginning Tests")
    try:
        subprocess.check_call(["./bin/out", "Hello", "GitHub", "Action", ", Yey!"])
        log(f"Process Completed Successfull with Return Code <0>")
    except subprocess.CalledProcessError as error:
        log(f"Execution Failed with Returned Code <{error.returncode}>")

main()