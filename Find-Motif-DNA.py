#Determines location of Motif in Sequence

f = open("FindMotifDNAinput.txt", "r");
s = str(f.readline().strip()); #strip is essential to avoid breaking too soon 
t = str(f.readline().strip());
f.close();
res = "";
i = -1;
while True:
    i = s.find(t, i+1);
    if i == -1: break;
    res += str(i+1) +" "; #i+1 is to change from 0-based numbering to 1-based
    
print res;
