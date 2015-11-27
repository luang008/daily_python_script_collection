import sys,os
def tree_copy(src,dst):
    """
        Copy the tree structure of src to dst, all metadata ignored
        Usage: python tree_copy.py src dst
    """
    if not os.path.exists(dst):
        os.makedirs(dst)
    current_src = os.path.abspath(src)
    current_dst = os.path.abspath(dst)
    names = os.listdir(src)
    names = [name for name in names if not name.startswith(".")] # Ignore metadata
    for name in names:
        if os.path.isfile(os.path.join(current_src,name)):
            with open(os.path.join(current_src,name),'r') as fin, open(os.path.join(current_dst,name),'w') as fout:
                for line in fin:
                    fout.write(line)
        elif os.path.isdir(os.path.join(current_src,name)):
            tree_copy(os.path.join(current_src,name), os.path.join(current_dst,name))
        else:
            pass
    
if __name__ == '__main__':
    src = sys.argv[1]
    dst = sys.argv[2]
    tree_copy(src,dst)