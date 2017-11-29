#returns the protein sequence given a fasta file containing a full DNA sequence and several introns

f = open("RNASplicinginput.txt", "r");
#make dictionary of sequences
d={};
fullID = "";
switch = "off";
for line in f:
    if switch == "off":#this identifies the first item in the file as the main sequence
        fullID = line.strip()
        id = line.strip();
        s = "";
        switch = "on";
    if line[0] == ">": #separates the IDs from the sequences
        id = line.strip();
        s = "";
    else:
        s += str(line.strip());
    d[id] = s;
f. close();
fullseq = d[fullID];

#create dictionary of only introns
inD = {i:d[i] for i in d if i!= fullID};
#remove introns from full sequence
for key in inD:
    fullseq = fullseq.replace(inD[key], "");
    
#translates to RNA:
i = 0;
RNA = "";
while i < len(fullseq):
    if fullseq[i] == "T":
        RNA += "U";
    else:
        RNA+=str(fullseq[i]);
    i +=1;

#transcribes RNA to protein
codons = {
"UUU" : "F",
"CUU" : "L",
"AUU" : "I",
"GUU" : "V",
"UUC" : "F",
"CUC" : "L",
"AUC" : "I",
"GUC" : "V",
"UUA" : "L",
"CUA" : "L",
"AUA" : "I",     
"GUA" : "V",
"UUG" : "L",
"CUG" : "L",
"AUG" : "M",
"GUG" : "V",
"UCU" : "S",
"CCU" : "P",
"ACU" : "T",
"GCU" : "A",
"UCC" : "S",
"CCC" : "P",
"ACC" : "T",
"GCC" : "A",
"UCA" : "S",
"CCA" : "P",
"ACA" : "T",
"GCA" : "A",
"UCG" : "S",
"CCG" : "P",
"ACG" : "T",
"GCG" : "A",
"UAU" : "Y",
"CAU" : "H",
"AAU" : "N",
"GAU" : "D",
"UAC" : "Y",
"CAC" : "H",
"AAC" : "N",
"GAC" : "D",
"UAA" : "Stop",
"CAA" : "Q",
"AAA" : "K",
"GAA" : "E",
"UAG" : "Stop",
"CAG" : "Q",
"AAG" : "K",
"GAG" : "E",
"UGU" : "C",
"CGU" : "R",
"AGU" : "S",
"GGU" : "G",
"UGC" : "C",
"CGC" : "R",
"AGC" : "S",
"GGC" : "G",
"UGA" : "Stop",
"CGA" : "R",
"AGA" : "R",
"GGA" : "G",
"UGG" : "W",
"CGG" : "R",
"AGG" : "R",
"GGG" : "G"
};
i = 0;
p="";
while i < (len(RNA)-3):
    cod = RNA[i:i+3];
    p += codons[cod];
    i +=3;
print p;
