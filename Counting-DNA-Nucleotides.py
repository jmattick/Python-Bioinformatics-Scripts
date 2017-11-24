##Given a txt file containing a sequence, output 4 integers corresponding to the number of nucleotides A,C,G,T respectively separated by a space. 
f = open("countingDNAinput.txt", "r");
s = str(f.readlines());
d = {};
for nt in list(s):
    a = nt;
    if a in d:
        x = d[a];
        d[a] = x+1;
    else:
        d[a] = 1;
finalstring = str(d["A"])+" "+str(d["C"])+" "+str(d["G"])+" "+str(d["T"]);
print finalstring;
