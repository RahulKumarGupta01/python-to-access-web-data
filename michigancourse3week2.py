import re
f=open("regex_sum_1233091.txt")
s=0
lst=[]
for line in f:
    line=line.rstrip()
    lst=list(map(int,re.findall("[0-9]+",line)))
    s=s+sum(lst)
f.close()
print(s)