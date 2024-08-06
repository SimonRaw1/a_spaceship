print ('Hello World')
squatSets = int(input('Number of sets:'))
squatWeights = [0]*squatSets
for i in range(1, squatSets+1):
    print ('Weight for set', i,':')
    squatWeights[i-1] = int(input())
for i in range(0,squatSets):
    print (squatWeights[i])
