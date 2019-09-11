import os
def make_list():
    with open("filename_list.txt", 'w') as outfile:
        for f in os.listdir():
            if os.path.isfile(f):
                files_no_ext = '.'.join(f.split('.')[:-2])
                outfile.write(files_no_ext + '\n')

if __name__ == '__main__':
    make_list()    
