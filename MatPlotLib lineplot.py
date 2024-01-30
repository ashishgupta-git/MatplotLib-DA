import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [78,82,86,89,92]

#For Chart Figure Size:
plt.figure(figsize=(8,6))

#For Title of Chart:
plt.title('Ashish Report', fontsize=15)

#For X-Axis and Y-Axis Name:
plt.xlabel("Class", fontsize=12).set_color('green')
plt.ylabel("Marks", fontsize=12).set_color('green')
plt.style.use('')
plt.plot(x,y, color='red', marker='o', linestyle='dashdot')
plt.show()