Limit=1000     # Search under 1 million for now
factors=[0]*Limit # number of prime factors.
count=0
for i in xrange(2,Limit):
    if factors[i]==0:
        # i is prime
        count =0
        val =i
        while val < Limit:
            factors[val] += 1
            val+=i
    elif factors[i] == 3:
        count +=1
        if count == 3:
            print i-2 # First number
            break
    else:
        count = 0

print factors
