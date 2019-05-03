import sys

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    doors_start,rounds,doors_round=[int(i) for i in sys.stdin.readline().split()]
    doors=doors_start
    prob_prize=100.0/doors_start
    for rnd in range(rounds):
        doors-=1
        prob_wrong_guess=doors*prob_prize
        doors-=doors_round
        prob_prize=prob_wrong_guess/doors
    print("{:.2f}%".format(prob_prize))
        
            
    
    
