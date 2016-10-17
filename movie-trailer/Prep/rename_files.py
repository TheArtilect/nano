import os


def rename_files():

    original_path = os.getcwd()

    file_list = os.listdir('/home/onyx/projects/nano/movie-trailer/prank')

    os.chdir("/home/onyx/projects/nano/movie-trailer/prank")
    for file_name in file_list:

        new_name = file_name.translate(None, "0123456789")
        print "old name: " + file_name + ", new name: " + new_name
        os.rename(file_name, new_name)

    os.chdir(original_path)



rename_files()
