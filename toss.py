#BAN vs SL Toss

import random
head=0
tail=1
print "SL captain tossed the coin"
BAN_T=input("BAN captain says (head/tail): ")
if random.randint(0,1)==BAN_T:
    print "Bangladesh has won the toss:"
else:
    print "SL won the toss:"
