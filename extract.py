# 得到tbC2I.txt
with open("tbc2i.csv","r",encoding='utf-8')as f:
    lines=f.readlines()

with open("tbc2i.txt","w",encoding='utf-8')as f:
    for line in lines:
        line=line.split(',')
        new_line=line[1]+' '+line[2]+' '+line[4]+'\n'
        f.write(new_line)
