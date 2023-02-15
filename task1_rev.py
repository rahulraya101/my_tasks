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
        process = subprocess.Popen(path)
        with open('collected_data.csv', 'a') as f:
            f.write('CPU Usage, Resident Set Size, Virtual Memory Size, Number of File Descriptors')
            f.write('\n')
            proc = psutil.Process(process.pid)
            
            while psutil.pid_exists(process.pid) and proc.status() != psutil.STATUS_ZOMBIE:
            #while process.poll() is None:
                print(process.pid, psutil.pid_exists(process.pid))
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