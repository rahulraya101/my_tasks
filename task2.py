import shutil
import time
import argparse
from sync_folders.main import get_files

parser = argparse.ArgumentParser(description="Task 2 implementation.",
                                 epilog="As a result you will get replica folder and log file with collected data.")

parser.add_argument("--source", dest="source", type=str, required=True, help="Enter path to the source folder.")
parser.add_argument("--replica", dest="replica", type=str, required=True, help="Enter path to the replica folder.")
parser.add_argument("--interval", dest="interval", default=0, type=int, help="Enter time interval in seconds. "
                                                                             "DEFAULT=0")
parser.add_argument("--log", dest="log", type=str, required=True, help="Enter path to the log file.")


def sync_folders(path_to_source, path_to_replica, path_to_log):

    if not path_to_source or not path_to_replica:
        raise NameError('Required path to both dirs')

    logs = ''
    files_in_a = get_files(path_to_source)
    files_in_b = get_files(path_to_replica)
    same_files = []

    for file_a in files_in_a:
        for file_b in files_in_b:
            if file_b['name'] == file_a['name']:
                if file_b['date'] < file_a['date']:
                    shutil.copy2(path_to_source + '/' + file_a['name'], path_to_replica)
                    logs += f"Change {file_a['name']} in {path_to_replica}" + '\n'
            same_files.append(file_b['name'])

    for file_a in files_in_a:
        if not file_a['name'] in same_files:
            shutil.copy2(path_to_source + '/' + file_a['name'], path_to_replica)
            logs += f"Create {file_a['name']} in {path_to_replica}" + '\n'

    with open(path_to_log, 'a', encoding='utf-8') as f:
        f.write(logs)
        f.write('-------------------------------------------------------------------------------------')
        f.write('\n')
    print(logs)


if __name__ == '__main__':
    args = parser.parse_args()
    while True:
        sync_folders(args.source, args.replica, args.log)
        time.sleep(args.interval)