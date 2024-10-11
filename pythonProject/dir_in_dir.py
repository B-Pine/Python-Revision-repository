import os


def list_dir(p):

    def dir_walk(path):
        nonlocal tab_size
        files = os.listdir(path)
        for f in files:
            current_file = os.path.join(path, f)
            if os.path.isdir(current_file):
                print(f"{'\t'*tab_size}Directory: {f}")
                tab_size += 1
                dir_walk(current_file)
                tab_size -= 1
            else:
                print(f"{'\t'*tab_size}{f}")
    tab_size = 0
    if os.path.exists(p):
        print('Directories for ' + p)
        dir_walk(p)
    else:
        print("Path doesn't exist")


list_dir('.')

# ########################################################
# walk method of os module seems to work fine though
# listing = os.walk('.')
# for root, directory, files in listing:
#     print(root)
#     for objr in directory:
#         print("\t"+objr)
#     for file in files:
#         print("\t\t"+file)
