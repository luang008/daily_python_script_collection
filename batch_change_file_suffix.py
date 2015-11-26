import sys
import os
import glob
import shutil
def batch_copy_file_change_suffix(in_dir,out_dir):
    '''
        I write this code to copy all the java source file to python files in another place
    '''
    OLD_SUFFIX = "txt"
    NEW_SUFFIX = "csv"
    in_dir = os.path.abspath(in_dir)
    base_dir = os.path.abspath(out_dir)
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    for dirName, subdirList, filenames in os.walk(in_dir):
        out_dir = base_dir + dirName[len(in_dir):]
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        for filename in filenames:
            if filename.endswith(OLD_SUFFIX):
                filename = filename[:-len(OLD_SUFFIX)] + NEW_SUFFIX
            open(os.path.join(out_dir,filename),'w+').close()

if __name__ == '__main__':
	in_dir = sys.argv[1]
	out_dir = sys.argv[2]
	batch_copy_file_change_suffix(in_dir,out_dir)
