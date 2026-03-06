import math

def EucDistance(A1, A2):
    ans = math.sqrt((A1['X'] - A2['X'])**2 + (A1['Y'] - A2['Y'])**2)
    return ans


def UsedDefinfKNN(K):

    Border = "-" * 50
    print(Border)

    data = [
        {'point': 'A','X': 1, 'Y': 2, 'label': 'Red'},
        {'point': 'B','X': 2, 'Y': 3, 'label': 'Red'},
        {'point': 'C','X': 3, 'Y': 1, 'label': 'Blue'},
        {'point': 'D','X': 6, 'Y': 5, 'label': 'Blue'},
    ]

    new_point = {'X': 2, 'Y': 2}

    for d in data:
        d['distance'] = EucDistance(d, new_point)

    print("\nDistances:")
    for d in data:
        print(f"Distance from {d['point']} to new point: {d['distance']:.2f}")

    sorted_data = sorted(data, key=lambda x: x['distance'])

    print("\nSorted Data:")
    for i in sorted_data:
        print(i)

    # Using if-elif for K values
    if K == 1:
        nearest_neighbors = sorted_data[:1]

    elif K == 3:
        nearest_neighbors = sorted_data[:3]

    elif K == 5:
        nearest_neighbors = sorted_data[:5]

    else:
        print("Invalid K value")
        return

    print(f"\nNearest Neighbors for K = {K}")
    for neighbor in nearest_neighbors:
        print(f"Neighbor: {neighbor['point']} Label: {neighbor['label']}")

    votes = {}

    for neighbor in nearest_neighbors:
        label = neighbor['label']
        votes[label] = votes.get(label, 0) + 1

    print("\nVotes:")
    for label in votes:
        print(label, ":", votes[label])

    predicted_class = max(votes, key=votes.get)

    print(f"\nPrediction Result for K = {K} -> {predicted_class}")


def main():

    UsedDefinfKNN(1)
    UsedDefinfKNN(3)
    UsedDefinfKNN(5)

    # As K inceases, more neighbors are considered for classification. This can chnage the majority class among the neighbors, leading to a different predicted class. For example, with K=1, the nearest neighbor might be 'Red', but with K=3, the majority of neighbors might be 'Blue', resulting in a different prediction.

if __name__ == "__main__":
    main()