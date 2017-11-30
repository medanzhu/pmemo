import os
def VisitDir(path):
    for root,dirs,files in os.walk(path):
        for name in files:
            print(os.path.join(root,name))



path="D:\\portables\\burpsuite"
VisitDir(path)