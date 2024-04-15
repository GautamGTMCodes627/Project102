import os 
import shutil

from_dir = "/Users/gautammahesh/Downloads/P102_assets-main"
to_dir = "/Users/gautammahesh/Downloads/documents"
list_of_files = os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name, ext = os.path.splitext(file_name)
    #print(name)
   # print(ext)
    if ext==" ":
        continue
    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        pathone = from_dir+'/'+file_name
        pathtwo = to_dir+'/'+"document_files"
        paththree = to_dir+'/'+"document_files"+'/'+file_name
        #print("pathone", pathone)
        #print("paththree", paththree)
        if os.path.exists(pathtwo):
            print("moving "+file_name+" ...")
            shutil.move(pathone, paththree)
        else: 
            os.makedirs(pathtwo)
            print('moving '+file_name+" ...")
            shutil.move(pathone,paththree)