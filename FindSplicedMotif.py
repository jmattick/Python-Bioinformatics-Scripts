#Finding a Spliced Motif
f = open("C:\Users\jmatt\Desktop\Playground\Rosalind\Stronghold\SplicedMotifinput.txt", "r");
#Separate sequences into variables
s = "";
t = "";
status = "";
for line in f:
    if line[0] == ">":
        if status == "":
            status = "first";
        elif status == "first":
            status = "second";
    if line[0] != ">":
        if status == "first":
            s += line.strip();
        elif status == "second":
            t += line.strip();
f.close();

#Find index where motif (t) is present
si = 0;
ti = 0;
smax = len(s);
tmax = len(t);
index_collection = "";

while si < smax and ti < tmax:
    if s[si] == t[ti]:
        index_collection += (str(si+1)+" "); #add 1 to index to match biological index
        ti += 1;
        si += 1;
    else:
        si +=1;
print index_collection;
        
