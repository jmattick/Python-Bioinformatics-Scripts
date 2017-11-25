#Ouputs number of point mutations from text file with two sequences

f = open("CountingPointMutationsinput.txt", "r");
s = f.readline();
t = f.readline();
dH = 0;
i = 0;
while i<len(s):
    if (s[i] != t[i]):
        dH+=1;
    i = i+1;
print dH;
f.close();
