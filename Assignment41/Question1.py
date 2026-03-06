# [A,B,C,D]
# X[1,2,3,6]
# Y[2,3,1,5]
# [R,R,B,B]

import math

def EucDistance(A1,A2):
    ans = math.sqrt((A1['X'] - A2['X'])**2 + (A1['Y'] - A2['Y'])**2)
    return ans

def UsedDefinfKNN():

    Border = "-" * 50
    print(Border)

    data = [
        {'point': 'A','X': 1, 'Y': 2, 'label': 'Red'},
        {'point': 'B','X': 2, 'Y': 3, 'label': 'Red'},
        {'point': 'C','X': 3, 'Y': 1, 'label': 'Blue'},
        {'point': 'D','X': 6, 'Y': 5, 'label': 'Blue'},
    ]


    for i in data:
        print(i)

    
    new_point = {'X': 2, 'Y': 2}

    for d in data:
        d['distance'] = EucDistance(d, new_point)
        print(f"Distance from {d['point']} to new point: {d['distance']}")

    
    sorted_data = sorted(data, key=lambda x: x['distance'])

    for i in sorted_data:
        print(i)

    K = 3

    nearest_neighbors = sorted_data[:K]

    for neighbor in nearest_neighbors:
        print(f"Neighbor: {neighbor['point']}, Label: {neighbor['label']}")

    
    votes = {}

    for neighbor in nearest_neighbors:
        label = neighbor['label']
        votes[label] = votes.get(label, 0) + 1
    
    for d in votes:
        print(f"Label: {d}, Votes: {votes[d]}")

    
    predicted_class = max(votes, key=votes.get)
    print(f"Predicted class for new point: {predicted_class}")

def main():

    UsedDefinfKNN()

if __name__ == "__main__":
    main()