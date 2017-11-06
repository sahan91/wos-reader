import os

arr = os.listdir('raw data')

for folder in arr:
    dir_path = os.path.join('raw data', folder)
    files = os.listdir(dir_path)
    count = 1
    for file in files:
        if file.endswith(".txt"):
            file_path_orig = os.path.join(dir_path, file)
            file_path_dest = os.path.join(dir_path, folder+"_"+str(count)+".txt")
            count += 1
            os.rename(file_path_orig, file_path_dest)
        