from utils import folderscreator as fc, func
import sys
 
def main():
    print("Enter Input_File_name :" )
    file_path,file_name_in,ext= func.browseFiles() 
    fc.filehandle(file_path,file_name_in,ext)

main()
