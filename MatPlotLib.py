import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(10,30,(20))
print(x)

n = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
plt.title("Ashish Gupta")
plt.xlabel("Python")
plt.ylabel("No.")


plt.hist(n,"auto",(0,300),color="grey", edgecolor="black", cumulative=-1, orientation="horizontal")
plt.legend("X")

plt.show()


#create pandas 2d dataframe