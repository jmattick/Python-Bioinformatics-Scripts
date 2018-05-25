#get sequence
f = open("C:\Users\jmatt\Desktop\Playground\Rosalind\Stronghold\ORFinput.txt", "r");
s = "";
for line in f:
    if line[0] != ">":
        s += line.strip();
f.close();
print s;

#store rc into a variable
rc = "";
for nt in list(s):
    if nt == "A":
        rc += "T";
    if nt == "C":
        rc += "G";
    if nt == "G":
        rc += "C";
    if nt == "T":
        rc += "A";
rc = rc[::-1];

#Translate to RNA
i = 0;
rfwd = "";
while i < len(s):
    if s[i] == "T":
        rfwd += "U";
    else:
        rfwd+=str(s[i]);
    i +=1;

i = 0;
rrc = "";
while i < len(rc):
    if rc[i] == "T":
        rrc += "U";
    else:
        rrc+=str(rc[i]);
    i +=1;

#calculate the three posibilities for foward
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
#transcribe function given sequence (a) and reading frame (i)
def transcribe(a,i):
    c="";
    while i < (len(a)-3):
        cod = a[i:i+3];
        c += codons[cod];
        i +=3;
    return c;

#trim the ends
#
#
#
#
#
#
#
#
#
#trimmer doesn't account for an m - stop after the first stop
#
#
#
#


def trimmer(b):
    switch = "off"
    i = 0;
    tp = "";
    while i< len(b):
        if b[i] == "M" and switch == "off": #to prevent transcription before start codon

            switch = "on";
        if i == len(b)-1 and switch == "off": #prevents error if no start codon
            break;

        if b[i] == "S" and b[i+1] == "t" and b[i+2] == "o" and switch == "on": #this loop is iterating over characters not words
            break;
        if switch == "on":
            tp += b[i];
            
        i += 1;
    return tp;

#Calls the trimmmer and transcribe functions for each reading frame and outputs to an array
trimmed = [];
trimmed.append(trimmer(transcribe(rfwd,0)));
trimmed.append(trimmer(transcribe(rfwd,1)));
trimmed.append(trimmer(transcribe(rfwd,2)));
trimmed.append(trimmer(transcribe(rrc,0)));
trimmed.append(trimmer(transcribe(rrc,1)));
trimmed.append(trimmer(transcribe(rrc,2)));

print trimmed;


#Remove repeated
un = list(set(trimmed));
#Removes empty 
un = filter(None, un);
#identifies if another sequence is within our sequence      
final = [];
for x in list(un):        
    if x.count("M") == 1:
        final.append(x);
    else:
        i = 0;
        while i <len(x):
            if x[i] == "M":
                final.append(x[i:]);
            i += 1;

#Remove repeated
final = list(set(final));

i = 0;
while i< len(final):
    print final[i];
    i += 1;
            
    
