#Calculates the molecular weight given a file containing the protein sequence

d = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333,
}

f = open("CalculateProteinMassinput.txt","r");
s = f.readline().strip(); #use readline instead of readlines
f.close();
i = 0;
sl = len(s);
w = 0;
while i < sl:
    aa = s[i];
    w += d[aa];
    i += 1;
print w;
