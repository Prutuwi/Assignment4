import numpy as np
import matplotlib.pyplot as plt

n=[500, 1000, 2000, 5000, 10000, 15000, 20000, 50000, 100000]

for i in n:
    die1 = np.random.randint(1,7,size=i)
    die2 = np.random.randint(1,7,size=i)
    sum = die1 + die2
    print("Sum ", sum)
    h, h2 = np.histogram(sum, bins=np.arange(2, 14))
    plt.bar(h2[:-1], h / i)
    plt.title(f"Histogram of sums of two dice (n = {n})")
    plt.xlabel("Sum of dice")
    plt.ylabel("Relative frequency")
    plt.show()



