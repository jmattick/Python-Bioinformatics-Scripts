#Outputs the reverse compliment sequence
f = open("ReverseComplimentinput.txt", "r");
z = open("ReverseComplimentoutput.txt", "w");
o = f.readline();
r = o[::-1];
lr = len(r);
rc="";
i = 0;
while i<lr:
    if r[i] == "A":
        rc += "T";
    if r[i] == "C":
        rc += "G";
    if r[i] == "G":
        rc += "C";
    if r[i] == "T":
        rc += "A";   
    i = i+1;
z.write(rc);
f.close();
z.close();
