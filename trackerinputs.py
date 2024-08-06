print ('Hello World')
squatSets = int(input('Number of sets:'))
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
   print (squatReps[i],'at',squatWeights[i],'kg')
