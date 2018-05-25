#Rabbits and Recurrence Relations
def fibRab(nmax,k): #nmax is months, k is number of offspring per adult pair
        n = 1;
        #function that calculates number of rabbits for every month
        def numRabbits(months, k):
                if (months == 1):
                        return 1;
                if (months == 2):
                        return 1;
                
                if (months == 3):
                        return 1+k;
                oneprev = numRabbits(months-1, k); #saves calculation of previous month
                twoprev = numRabbits (months-2, k);#saves calculation of two months prior

                if(months >= 4):
                        return oneprev + (twoprev*k);# only two months prior are mature enough to breed
        sequence = [];
        while n <= nmax:
                
                sequence.append(numRabbits(n, k));
                n +=1;

        print sequence[-1];

fibRab(33,4);
