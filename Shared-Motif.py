#Find a Shared Motif of Many Sequences

f = open("C:\Users\jmatt\Desktop\Playground\Rosalind\Stronghold\SharedMotifinput.txt", "r");

#oganize sequences into a list of strings
sequences = []
s = ""
count = 0;
current = 1;
for line in f:
    if line[0] == ">":
        count += 1;
    if line[0] != ">":
        if count == current:
            s += line.strip();
        else:
            sequences.append(s); #adds complete sequence
            s = line.strip(); #starts new sequence
            current +=1;
sequences.append(s);#this adds the last sequence
f.close();

#separate the shortest sequence to find the motif
sorted_seq = sorted(sequences, key=len);
shortest = sorted_seq[0];
remaining = sorted_seq[1:];
motif = "";
#loop through the shortest sequence until longest match is found
for i in range(len(shortest)):
    for j in range(i, len(shortest)):
        m = shortest[i:j+1];
        found = False;
        for seq in remaining:
            if m in seq:
                found = True;
            else:
                found = False;
                break; #if not found increase position in shortest seq
        if found and len(m) > len(motif):
            motif = m;
print motif;
               
