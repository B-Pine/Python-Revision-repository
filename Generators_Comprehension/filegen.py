import os

root = "music"
for path, directories, files in os.walk(root, topdown=True):
    if files:
        first_split = os.path.split(path)
        print(first_split)
        second_split = os.path.split(first_split[0])
        print(second_split)
        for file in files:
            # print(file)
            song_details = file[:-5].split(' - ')
            print(song_details)
        print("-" * 40)
