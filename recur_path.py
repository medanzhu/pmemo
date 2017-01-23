import os.path

topdir = '/home/danzhu/iwall'
arg = '*'
def visit(arg, dirname, names):
    for name in names:
        print(os.path.join(dirname,name))

os.path.walk(topdir, visit, arg)
