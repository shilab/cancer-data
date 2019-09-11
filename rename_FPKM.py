import os

def rename_func():
    dir_name = os.getcwd()
    for root, dirs, files in os.walk(dir_name, topdown = False):
        for file in files:
            file_name =  os.path.splitext(file)[0][-5:]
            first_name = os.path.splitext(file)[0]
            extension1 = os.path.splitext(file)[1]
            dir_name =  os.path.basename(root)
            if extension1.endswith('.py'):
                continue
            if first_name.startswith("barcodes"):
                continue
            if extension1.endswith(".sh"):
                continue
            if first_name.startswith("gdc"):
                continue
            else:
                os.rename(root+"/"+file,root+"/"+dir_name+file_name+extension1)
	
if __name__ == '__main__':
    rename_func()
