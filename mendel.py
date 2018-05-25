#Mendel's First Law
def mend(dom,het,rec):
    k=dom;
    m=het;
    n=rec;
    pop = float(k + m + n); #this is necessary otherwise answer will be rounded to int
    #calculate probability of getting a dominant displaying offspring from a mixed population
    prob = (1 - (n/pop)*((n-1)/(pop-1)) - (n/pop)*(m/(pop-1)) - (m/pop)*((m-1)/(pop-1))*0.25);
    print prob;
mend(29,20,21);
