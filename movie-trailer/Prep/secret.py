import os

def rename():
    original_path = os.getcwd()

    directory = "/home/onyx/projects/nano/movie-trailer/secret"

    file_list = os.listdir(directory)

    os.chdir(directory)

    for file_name in file_list:

        new_name = file_name.translate(None, "0123456789")

        print "old name: " + file_name + ", new name: " + new_name

        os.rename(file_name, new_name)

    os.chdir(original_path)


rename()
