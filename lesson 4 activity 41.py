def findWater(a, a_size):
    leftTallest = [0] * a_size
    rightTallest = [0] * a_size
    water = 0
    leftTallest[0] = a[0]
    for i in range(1, a_size):
        leftTallest[i] = max(leftTallest[i-1], a[i])
    for i in range(0, a_size):
        water += min(leftTallest[i], rightTallest[i]) - a[i]
    return water
a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
bars = len(a)
print("Water : ", findWater(a, bars))