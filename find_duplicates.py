import os


def find_sample_files():

    if not os.path.exists('Directory/'):
        os.mkdir('Directory')

    all_files = os.listdir('Directory/')

    start_file = all_files[1]
    path_to_start_file = 'Directory/' + all_files[1]
    for index in range(2, len(all_files)):
        path_to_look_file = 'Directory/' + all_files[index]
        look_file_size = os.stat(path_to_look_file).st_size
        start_file_size = os.stat(path_to_start_file).st_size

        if look_file_size == start_file_size:
            print("I found duplicates. '{0}' and '{1}' are duplicates".format(start_file, all_files[index]))

        elif look_file_size != start_file_size:
            start_file = all_files[index]
            look_file_size = start_file_size
            path_to_start_file = path_to_look_file


find_sample_files()
