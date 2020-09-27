from pathlib import Path
import sys





if __name__ == '__main__':
    content=(Path(sys.path[0])/"javakeywordtable.txt").read_text().split("\n")
    keywordClass="class KeyWord:"
    for line in content:
        keytype,keywords=line.split(":")
        keywords=keywords.split(",")
        for keyword in keywords:
            keyword