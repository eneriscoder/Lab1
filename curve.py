import matplotlib.pyplot as plt
import math as math
import numpy as np

def binom_coef(n,k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def curve(points, amount, dimension):

    # visual test
    # curve_pt.append(start)
    # curve_pt.append(mid)
    # curve_pt.append(end)
    # curve_pt.append(start)
    t = np.linspace(0, 1, amount)
    n=  len(points) - 1
    curve_pt = np.zeros((amount, dimension))

    for i in range(len(points)):

        bernstein =  binom_coef(n, i) * (t**i) * ((1 - t)**(n - i))
        curve_pt += np.outer(bernstein, points[i])
    #print(curve_pt)
    return curve_pt

actual_points = np.array([[0,10], [4, -20],[7, 50] , [11, -20], [13,10]])
cords = curve( actual_points, 1000, 2)

plt.figure(figsize=(8, 6))
plt.plot(actual_points[:, 0], actual_points[:, 1], 'r--')
plt.plot(cords[:, 0], cords[:, 1], 'b-')
plt.show()
