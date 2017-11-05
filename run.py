import os

SUBJECTS = 'subjects'
SUBJECT_LIST = {
    'LA': ['learning analytics', 'learning science']
}
SUBJECT_TYPES = ['conference', 'journal']

id_count = 1

def write_to_file(line, path):
    path = path + ".tsv"
    with open(path, 'a') as outfile:
        outfile.write(line+"\n")

def process_txt(folder_path, filename):
    global id_count
    path = os.path.join(folder_path, filename)

    with open(path, 'r') as ifile:
        lines = ifile.readlines()
        found_title = False
        str_title = ""
        final_title = ""

        for line in lines:
            line = line.strip()
            split_line = line.split()

            if(len(split_line) > 0):
                if(split_line[0] == 'TI'):
                    found_title = True
                    str_title += line[3:]
                elif(split_line[0] == 'SO'):
                    final_title = ''.join(str_title)
                    found_title = False
                    str_title = ""          
                elif(found_title):
                    str_title += " " +  line

                if(split_line[0] == 'AB'):
                    abstract = line[3:]
                    txt_line = str(id_count) + "\t"+ final_title + "\t" + abstract
                    out_path = path[:-6]
                    write_to_file(txt_line, out_path)
                    id_count += 1


for subject, query_list in SUBJECT_LIST.items():
    for query in query_list:
        for sub_type in SUBJECT_TYPES:
            id_count = 1
            folder_path = os.path.join(SUBJECTS, subject, query, sub_type)
            for filename in os.listdir(folder_path):
                if filename.endswith(".txt"):
                    print(filename)
                    process_txt(folder_path, filename)