import sys,os
from pathlib import Path
import logging

"""https://github.com/openjdk/jdk/"""

class JavaReader:
    def __init__(self,content):
        self.content=content
        self.offset=0
    def findKey(self):
        pass


# class JavaClass:
#     """java类信息"""
#     def __init__(self,path,classLoader=None):
#         self.classLoader=classLoader
#         self.filepath=path
#         self.Imports=[]
#         self.Fileds=[]
#         self.Methods=[]
#         self.Annotations=[]
#         self.innerClass=[]
#         self.read()
#     def read(self):
#         """读取代码"""
#         content=self.path.read_text("utf-8")
#     def _import(self,line):
#         self.importlist.append(line)
#     def print(self):
#         pass

if __name__ == '__main__':
    if len(sys.argv)!=2:
        print("""Usage: python -m javacodeloader [file]
        """)
        sys.exit(1)
    JavaClass(Path(sys.argv[1])).print()