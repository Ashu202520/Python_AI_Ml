import math

def EucDistance(A1, A2):
    ans = math.sqrt((A1['Hours'] - A2['Hours'])**2 + (A1['Attendance'] - A2['Attendance'])**2)
    return ans


def UsedDefinfKNN(K):

    Border = "-" * 50
    print(Border)

    data = [
        {'student': 'A', 'Hours': 2, 'Attendance': 60, 'label': 'Fail'},
        {'student': 'B', 'Hours': 5, 'Attendance': 80, 'label': 'Pass'},
        {'student': 'C', 'Hours': 6, 'Attendance': 85, 'label': 'Pass'},
        {'student': 'D', 'Hours': 1, 'Attendance': 50, 'label': 'Fail'}
    ]

    for i in data:
        print(i)

    hours = int(input("Enter Study Hours: "))
    attendance = int(input("Enter Attendance: "))

    new_point = {'Hours': hours, 'Attendance': attendance}

    print("\nDistances:")

    for d in data:
        d['distance'] = EucDistance(d, new_point)
        print(f"Distance from {d['student']} to new student: {d['distance']:.2f}")

    sorted_data = sorted(data, key=lambda x: x['distance'])

    print("\nSorted Data:")
    for i in sorted_data:
        print(i)

    nearest_neighbors = sorted_data[:K]

    print(f"\nNearest Neighbors for K = {K}")
    for neighbor in nearest_neighbors:
        print(f"Student: {neighbor['student']} Label: {neighbor['label']}")

    votes = {}

    for neighbor in nearest_neighbors:
        label = neighbor['label']
        votes[label] = votes.get(label, 0) + 1

    print("\nVotes:")
    for v in votes:
        print(v, ":", votes[v])

    predicted_class = max(votes, key=votes.get)

    print("\nPredicted Result:", predicted_class)


def main():

    K = 3
    UsedDefinfKNN(K)


if __name__ == "__main__":
    main()