import os
import sys
from multiprocessing import Pool

if __name__ == "__main__":
    command = ""
    for code in sys.argv[1:-1]:
        command = command + f"python3 {code}.py & "
    command = command + f"python3 {sys.argv[-1]}.py"

    print("EXECUTING COMMAND:",command)
    os.system(command=command)