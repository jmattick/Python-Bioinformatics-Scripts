##Transcribes DNA text file into an RNA text file
f = open("DNAtoRNAinput.txt", "r");
z = open("DNAtoRNAoutput.txt", "w");
t = str(f.readline());
u = "";
lt = len(t);
i = 0;
while i<lt:
    if t[i] == "T":
        u+="U"
    else:
        u+=str(t[i])
    i+=1;

print u;
z.write(u);
f.close();
z.close();
