#Returns the sequence ID and GC% of the sequence with the highest gc-content from a fasta file with multiple sequences

f = open("ComputingGCContentinput.txt", "r");
d ={};
cont="";
id="";
#establishes dictionary with ids and gc-content based off of sequences from input file
for line in f:
    if line[0] == ">":
        id = line.strip();
        s=""; # starts a fresh sequence variable for next sequence
    else:
        s += line.strip(); #this handles the carriage returns if present
        slen = len(s);
        gc = 0;
        for nt in list(s):
            if nt == "C":
                gc = gc+1;
            if nt == "G":
                gc = gc +1;
        cont = float(gc) / slen *100; #float is required to get an answer with decimal points rather than an integer
    d[id] = cont;
f.close();
out = max(d, key=lambda key: d[key]);#determines the highest gc value in the dictionary
n = str(out).replace(">", "");
out = n + "\n"+str(d[out]);
print out;



