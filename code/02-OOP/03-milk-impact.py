class s_class:
    def __init__(self, number, ages, heights, weights):
        self.number = number
        self.ages = ages
        self.heights = heights
        self.weights = weights

    def get_average_age(self):
        return sum(self.ages)/ len(self.ages)

    def get_average_height(self):
        return sum(self.heights)/ len(self.heights)

    def get_average_weight(self):
        return sum(self.weights)/ len(self.weights)

# code driver
num = int(input())
ages = list(map(int, input().split()))
heights = list(map(int, input().split()))
weights = list(map(int, input().split()))

A = s_class(num, ages, heights, weights)

num = int(input())
ages = list(map(int, input().split()))
heights = list(map(int, input().split()))
weights = list(map(int, input().split()))

B = s_class(num, ages, heights, weights)

print(A.get_average_age())
print(A.get_average_height())
print(A.get_average_weight())

print(B.get_average_age())
print(B.get_average_height())
print(B.get_average_weight())

if A.get_average_height() > B.get_average_height():
    print("A")
elif A.get_average_height() < B.get_average_height():
    print("B")
elif A.get_average_weight() > B.get_average_weight():
    print("B")
elif A.get_average_weight() < B.get_average_weight():
    print("A")
else:
    print("Same")