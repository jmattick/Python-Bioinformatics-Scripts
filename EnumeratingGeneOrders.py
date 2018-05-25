#Enumerating Gene Orders (Print Permutations)
def perm(n):
    #create original list in numerical order
    original = [];
    i = 1;
    while i <= n:
        original.append(i);
        i+=1;
    #use itertools to find all combinations of list 
    import itertools;
    res = list(itertools.permutations(original));
    #format answer 
    print len(res);
    j = 0;
    k = 1;
    perm = ""
    while j < len(res):
        if j == k:
            print perm;
            k+=1;
            perm = "";
        for item in res[j]:
             perm = perm + str(item)+ " ";
        
        j+=1;
    print perm;
perm(3);
    
