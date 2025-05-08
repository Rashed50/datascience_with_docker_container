import matplotlib.pyplot as plt

x =[1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y)
plt.xlabel('X-axis label')  # Corrected: plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')  # Corrected: plt.ylabel('Y-axis label')
plt.title('Sample Plot')  # Corrected: plt.title('Sample Plot')
#plt.show()  #show the plot, Corrected: plt.show()
plt.tight_layout()
plt.savefig('plot.png')