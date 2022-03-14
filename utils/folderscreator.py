import shutil, os

def create_folder(filepath,dir):
  if not os.path.exists(os.getcwd()+"/assets/"+dir+"_Files"):
    os.makedirs(os.getcwd()+"/assets/"+dir+"_Files")
    print("Created Directory : ", dir+"_Files" )
    shutil.copy(filepath, os.getcwd()+"/assets/"+dir+"_Files")
    print("File uploaded")
  else:
    print("Directory already existed :  ", dir+"_Files" )
    shutil.copy(filepath, os.getcwd()+"/assets/"+dir+"_Files")
    print("file uploaded")
  return dir

def filehandle(filepath,filename_in, ext):
        create_folder(filepath,ext)
