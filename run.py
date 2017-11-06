## TODO: Need to optimize this! 4 for-loops are really bad :-)
import os

SUBJECTS = 'subjects'
SUBJECT_LIST = {
    'LA': [
        'learning analytics',
        'learning science',
        'computer supported collaborative learning',
        'natural language processing',
        'learning at scale', 
        'educational data mining', 
        'massive open online course', 
        'virtual learning environment', 
        'education technology'
    ],
    'DL': [
        'deep learning', 
        'convolutional neural network', 
        'recurrent neural network', 
        'generative adversarial network'
    ]
}

SUBJECT_TYPES = ['conference', 'journal']

id_count = 1

def write_to_file(line, path):
    path = path + ".tsv"
    with open(path, 'a') as outfile:
        outfile.write(line+"\n")

def process_txt(folder_path, filename, sub_type, doc_type):
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
                    txt_line = sub_type+"_"+doc_type+"_"+str(id_count) + "\t"+ final_title + "\t" + abstract
                    out_path = os.path.join(folder_path, filename[:6])
                    # print(out_path)
                    write_to_file(txt_line, out_path)
                    id_count += 1


for subject, query_list in SUBJECT_LIST.items():
    for query in query_list:
        for sub_type in SUBJECT_TYPES:
            id_count = 1
            folder_path = os.path.join(SUBJECTS, subject, query, sub_type)
            for filename in os.listdir(folder_path):
                if filename.endswith(".txt"):
                    print(filename, sub_type)
                    process_txt(folder_path, filename, subject, (sub_type[0]).upper())