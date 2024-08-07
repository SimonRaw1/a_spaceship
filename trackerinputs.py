restart = 0
from datetime import date
dateToday = str(date.today())
'2021-01-26'
while restart == 0:
    lift = input('Enter the chosen lift (S,B,D): ')
    if lift in ['s','S']:
        print ('Number of sets:')
        squatSets = int(input())
        if squatSets != 0:
            squatReps = [0]*squatSets
            squatWeights = [0]*squatSets
            for i in range(0, squatSets):
                print (f"Reps for set {i+1}:")
                squatReps[i] = int(input())
            for i in range(0, squatSets):    
                print (f"Weight for set {i+1}:")
                squatWeights[i] = int(input())
            with open("Training Sessions.txt", "w") as text_file:
                print(f"Squat Session ({dateToday}):", file=text_file)
                for i in range(0,squatSets):
                    print(f"{squatReps[i]} reps at {squatWeights[i]}kg", file=text_file)
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
                print (f"Reps for set {i+1}:")
                benchReps[i] = int(input())
            for i in range(0, benchSets):    
                print (f"Weight for set {i+1}:")
                benchWeights[i] = int(input())
            with open("Training sessions.txt", "w") as text_file:
                print(f"Bench Session ({dateToday}):", file=text_file)
                for i in range(0,benchSets):
                    print(f"{benchReps[i]} reps at {benchWeights[i]}kg", file=text_file)
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
                print (f"Reps for set {i+1}:")
                deadliftReps[i] = int(input())
            for i in range(0, deadliftSets):    
                print (f"Weight for set {i+1}:")
                deadliftWeights[i] = int(input())
            with open("Training sessions.txt", "w") as text_file:
                print(f"Deadlift Session ({dateToday}):", file=text_file)
                for i in range(0,deadliftSets):
                    print(f"{deadliftReps[i]} reps at {deadliftWeights[i]}kg", file=text_file)
            break
        else:
            break