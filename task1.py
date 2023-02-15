import subprocess
import psutil
from datetime import datetime
import time
import argparse
import sys


parser = argparse.ArgumentParser(description="Task 1 implementation.",
                                 epilog="As a result you will get a 'collected_data.csv' file with collected "
                                        "statistics. It will appear in the folder from which the script was launched.")

parser.add_argument("--path", dest="path", type=str, required=True, help="Enter path to the process.")
parser.add_argument("--time", dest="time", default=0, type=int, help="Enter time interval in seconds. DEFAULT=0")

#sys.exit()

def launch_and_count(path, time_interval):
    try:
        with subprocess.Popen(path, shell=True) as process:
            with open('collected_data.csv', 'a', encoding='utf-8') as f:
                f.write('CPU Usage, Resident Set Size, Virtual Memory Size, Number of File Descriptors')
                f.write('\n')
                proc = psutil.Process(process.pid)
                while proc:
                    f.write(str(proc.cpu_percent()) + ', ')
                    f.write(str(proc.memory_info().rss) + ', ')
                    f.write(str(proc.memory_info().vms) + ', ')
                    f.write(str(proc.num_fds()))
                    f.write('\n')
                    time.sleep(time_interval)
    except psutil.ZombieProcess:
        return False

#sys.exit()

if __name__ == '__main__':
    args = parser.parse_args()
    launch_and_count(args.path, args.time)