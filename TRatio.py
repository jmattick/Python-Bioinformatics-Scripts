#Calculate the Transition to Transversion Ratio of two sequences in fasta format
f = open("C:\Users\jmatt\Desktop\Playground\Rosalind\Stronghold\TRatioinput.txt", "r");
#Separate sequences into variables
s1 = "";
s2 = "";
status = "";
for line in f:
    if line[0] == ">":
        if status == "":
            status = "first";
        elif status == "first":
            status = "second";
    if line[0] != ">":
        if status == "first":
            s1 += line.strip();
        elif status == "second":
            s2 += line.strip();
f.close();
#Caclulate number of transitions and transversions
transitions = 0;
transversions = float(0);
max = len(s1);
i = 0;
while i < max:
    if s1[i] == "A":
        if s2[i] == "G":
            transitions +=1;
        elif s2[i] == "C" or s2[i] == "T":
            transversions +=1;
        i=i+1;
    elif s1[i] == "G":
        if s2[i] == "A":
            transitions +=1;
        elif s2[i] == "C" or s2[i] == "T":
            transversions +=1;
        i+=1;
    elif s1[i] == "C":
        if s2[i] == "T":
            transitions +=1;
        elif s2[i] == "A" or s2[i] == "G":
            transversions +=1;
        i+=1;
    elif s1[i] == "T":
        if s2[i] == "C":
            transitions +=1;
        elif s2[i] == "A" or s2[i] == "G":
            transversions +=1;
        i+=1;
    else:
        i +=1;
#Calculate the ratio
ratio = transitions/transversions;
print ratio;
