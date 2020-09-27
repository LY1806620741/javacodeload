# -*- coding: utf-8 -*-
from pathlib import Path
import sys,re

if __name__ == '__main__':
    keywordtypeClass="class KeyWordType:\n"
    keywordClasss=""
    content=(Path(sys.path[0])/"javakeywordtable.txt").read_text("utf-8").split("\n")
    
    for line in content:
        keytype,keywords,notes=re.split(r":|#",line)
        keywordtypeClass+="    "+keytype+"="+keytype+"()\n"
        keywordClasss+="class "+keytype+":\n    \"\"\""+notes+"\"\"\"\n"
        keywords=keywords.split(",")
        for keyword in keywords:
            keywordClasss+="    "+("_"+keyword.capitalize() if keyword in ["true","false"] else keyword.capitalize())+"=\""+keyword+"\"\n"
        keywordClasss+=keytype+".members=["+",".join([keytype+"."+ ("_"+keyword.capitalize() if keyword in ["true","false"] else keyword.capitalize()) for keyword in keywords])+"]\n"
    Path("keyword.py").write_text(keywordClasss+keywordtypeClass,encoding="UTF-8")