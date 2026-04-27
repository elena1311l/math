import random
import numpy as np
'''
Math is 
1/10*1/10*1/10=1/1000=0.001 for Seven
0.001*100=0.1 Return to Player 0.1*100=10%

3/10*2/10*1/10=6/1000=0.006 for Cherry
0.006*10=0.6 Return to Player 0.6*10=6%

6/10*7/10*8/10=336/1000=0.336 for Lemon
0.336*100=33.6 Return to Player 33.6*3=100.8%

res=10+6+100.8=116.8%


'''

reel1 = ["Seven"] * 1 + ["Cherry"] * 3 + ["Lemon"] * 6
reel2 = ["Seven"] * 1 + ["Cherry"] * 2 + ["Lemon"] * 7
reel3 = ["Seven"] * 1 + ["Cherry"] * 1 + ["Lemon"] * 8

def simulate_slots(spins=100000):
    payouts = []
    
    for _ in range(spins):
        result1=random.choice(reel1)
        result2=random.choice(reel2)
        result3=random.choice(reel3)

        current_payout = 0

        if result1==result2==result3=="Seven":
            print('Plus 100')
            current_payout = 100
        elif result1==result2==result3=="Cherry":
            print('Plus 10')
            current_payout = 10
        elif result1==result2==result3=="Lemon":
            print('Plus 3')
            current_payout = 3
        payouts.append(current_payout)

    total_payout = np.array(payouts)
    mean_value = np.mean(total_payout)
    return mean_value, 

tmp = simulate_slots()
print(f'This is the average payout per spin: {tmp}')