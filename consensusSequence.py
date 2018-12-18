
#get sequences and add to list of arrays
f = open("consensusInput.txt", "r");
s = "";
seqList = [];
seqCount = 0;
consensus = "";

for line in f:
    if line[0] != ">":
        s += line.strip();
    else:
        if s != "":
           
            seqList.append(s);
            s = "";
seqList.append(s);
f.close();
#initialize profile dictionary to store num of bases at each index
profile = {
    "A": [0 * i for i in range(len(seqList[0]))],
    "C": [0 * i for i in range(len(seqList[0]))],
    "G": [0 * i for i in range(len(seqList[0]))],
    "T": [0 * i for i in range(len(seqList[0]))]};
#add value each time base is present at index
for seq in seqList:
    for i, base in enumerate(seq):
       profile[base][i] += 1;

#set up lists to hold max counts and consensus bases
max = [0 * i for i in range(len(seqList[0]))];
cons = ["" * i for i in range(len(seqList[0]))];

#loop through profile to find max at each index

profileRes = "";
order = ["A", "C", "G", "T"];
for item in order:
    profileRes += item + ":";
    ind = 0;
    for val in profile[item]:
        profileRes += " " + str(val);
        if val > max[ind]:
            max[ind] = val;
            cons[ind] = item;
        ind += 1;
    profileRes += "\n";
#print seq to console        
res = "";
for base in cons:
    res += base;
print(res);

#print profile to console
print(profileRes);
    
