restart = 0
while restart == 0:
    lift = input('Enter the chosen lift (S,B,D): ')
    if lift in ['s','S']:
        print ('Number of sets:')
        squatSets = int(input())
        if squatSets != 0:
            squatReps = [0]*squatSets
            squatWeights = [0]*squatSets
            for i in range(0, squatSets):
                print ('Reps for set', i+1,':')
                squatReps[i] = int(input())
                print ('Weight for set', i+1,':')
                squatWeights[i] = int(input())
            print()
            print ('Squat Session:',)
            for i in range(0,squatSets):
                print (squatReps[i],' reps at',squatWeights[i],'kg')
            break
        else:
           break 
    if lift in ['b','B']:
        print ('Number of sets:')
        benchSets = int(input())
        if benchSets != 0:
            benchReps = [0]*benchSets
            benchWeights = [0]*benchSets
            for i in range(0, benchSets):
                print ('Reps for set', i+1,':')
                benchReps[i] = int(input())
                print ('Weight for set', i+1,':')
                benchWeights[i] = int(input())
            print()
            print ('Bench Session:',)
            for i in range(0,benchSets):
                print (benchReps[i],' reps at',benchWeights[i],'kg')
            break
        else:
            break
        
    if lift in ['d','D']:
        print ('Number of sets:')
        deadliftSets = int(input())
        if deadliftSets != 0:
            deadliftReps = [0]*deadliftSets
            deadliftWeights = [0]*deadliftSets
            for i in range(0, deadliftSets):
                print ('Reps for set', i+1,':')
                deadliftReps[i] = int(input())
                print ('Weight for set', i+1,':')
                deadliftWeights[i] = int(input())
            print()
            print ('Deadlift Session:',)
            for i in range(0,deadliftSets):
                print (deadliftReps[i],' reps at',deadliftWeights[i],'kg')
            break
        else:
            break