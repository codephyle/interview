'''
1094. Car Pooling

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).
You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that 
the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. 
The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

Examples
    Input: trips = [[2,1,5],[3,3,7]], capacity = 4
    Output: false

    Input: trips = [[2,1,5],[3,3,7]], capacity = 5
    Output: true
'''

def carPool(trips, cap):
    ts = []
    for trip in trips:
        print(trip)
        ts.append([trip[1], trip[0]])
        ts.append([trip[2], -trip[0]])
    
    print(ts)
    ts.sort()
    print(ts)

carPool([[2,1,5],[3,3,7]], 4)