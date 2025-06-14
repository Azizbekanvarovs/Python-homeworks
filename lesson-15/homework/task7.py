import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

plt.bar(products, sales, color=['red', 'green', 'blue', 'orange', 'purple'])
plt.title('Sales Data')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.show()