import os
import fnmatch
import id3reader_p3 as id3


def file_finder(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, f"*.{extension}*"):
            relative_path = os.path.join(path, file)
            yield os.path.abspath(relative_path)


found = file_finder('C:\\Users\\USER\\Downloads', 'mp4')

error_list = []
for song in found:
    try:
        id3r = id3.Reader(song)
        print(f"Artist: {id3r.get_value('performer')}, "
              f"Album: {id3r.get_value('album')},"
              f"Track: {id3r.get_value('track')},"
              f"Song: {id3r.get_value('title')}")
    except:
        error_list.append(song)

print(error_list)
