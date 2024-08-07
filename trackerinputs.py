restart = 0
from datetime import date
dateToday = str(date.today())
while restart == 0:
    lift = input('Enter the chosen lift (S,B,D): ')
    if lift in ['s','S']:
        print ('Number of sets:')
        squatSets = int(input())
        print()
        if squatSets != 0:
            try:
                open('Squat Sessions.txt')
            except:
                with open ('Squat Sessions.txt', 'w') as text_file:
                    print(f"Record of all Squat Sessions", file=text_file)
            squatReps = [0]*squatSets
            squatWeights = [0]*squatSets
            for i in range(0, squatSets):
                print (f"Reps for set {i+1}:")
                squatReps[i] = int(input())
            print()  
            for i in range(0, squatSets):    
                print (f"Weight for set {i+1}:")
                squatWeights[i] = int(input())
            with open("Squat Sessions.txt", "a") as text_file:
                print(f"\nSquat Session ({dateToday}):", file=text_file)
                for i in range(0,squatSets):
                    print(f"{squatReps[i]} reps at {squatWeights[i]}kg", file=text_file)
            end = input('Would you like to enter another session? (Y/N) ')
            if end in ['y','Y']:
                print('\n')
            if end in ['n','N']:
                break
        else:
            end = input('Would you like to enter another session? (Y/N) ')
            if end in ['y','Y']:
                print('\n')
            if end in ['n','N']:
                break
    if lift in ['b','B']:
        print ('Number of sets:')
        benchSets = int(input())
        print()
        if benchSets != 0:
            try:
                open('Bench Sessions.txt')
            except:
                with open ('Bench Sessions.txt', 'w') as text_file:
                    print(f"Record of all Bench Sessions", file=text_file)
            benchReps = [0]*benchSets
            benchWeights = [0]*benchSets
            for i in range(0, benchSets):
                print (f"Reps for set {i+1}:")
                benchReps[i] = int(input())
            print()  
            for i in range(0, benchSets):    
                print (f"Weight for set {i+1}:")
                benchWeights[i] = int(input())
            with open("Bench Sessions.txt", "a") as text_file:
                print(f"\nBench Session ({dateToday}):", file=text_file)
                for i in range(0,benchSets):
                    print(f"{benchReps[i]} reps at {benchWeights[i]}kg", file=text_file)
            end = input('Would you like to enter another session? (Y/N) ')
            if end in ['y','Y']:
                print('\n')
            if end in ['n','N']:
                break
        else:
            end = input('Would you like to enter another session? (Y/N) ')
            if end in ['y','Y']:
                print('\n')
            if end in ['n','N']:
                break
        
    if lift in ['d','D']:
        print ('Number of sets:')
        deadliftSets = int(input())
        print()
        if deadliftSets != 0:
            try:
                open('Deadlift Sessions.txt')
            except:
                with open ('Deadlift Sessions.txt', 'w') as text_file:
                    print(f"Record of all Deadlift Sessions", file=text_file)
            deadliftReps = [0]*deadliftSets
            deadliftWeights = [0]*deadliftSets
            for i in range(0, deadliftSets):
                print (f"Reps for set {i+1}:")
                deadliftReps[i] = int(input())
            print()   
            for i in range(0, deadliftSets):    
                print (f"Weight for set {i+1}:")
                deadliftWeights[i] = int(input())
            with open("Deadlift Sessions.txt", "a") as text_file:
                print(f"\nDeadlift Session ({dateToday}):", file=text_file)
                for i in range(0,deadliftSets):
                    print(f"{deadliftReps[i]} reps at {deadliftWeights[i]}kg", file=text_file)
            end = input('Would you like to enter another session? (Y/N) ')
            if end in ['y','Y']:
                print('\n')
            if end in ['n','N']:
                break
        else:
            end = input('Would you like to enter another session? (Y/N) ')
            if end in ['y','Y']:
                print('\n')
            if end in ['n','N']:
                break