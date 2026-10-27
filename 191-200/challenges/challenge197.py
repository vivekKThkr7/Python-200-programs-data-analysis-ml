# Visualizing data ; Create a readable monthly sales chart.
# Create a line chart with months on the X-axis, sales on the y-axis, a clear title, axis labels, makers and a grid. Save the chart to monthly_sales.png

# Hint: use  plt.plot(), plt.xlabel(), plt.ylabel, plt.title(), plt.grid() and plt.savefig().

import matplotlib.pyplot as plt
 
months = ["January", "February", "March", "April", "May", "June"]
sales = [1200, 1500, 1350, 1800, 2100, 1950]
 
plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker="o")        # marker="o" = dot on each point
plt.title("Monthly Sales (January - June)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("monthly_sales.png", dpi=150, bbox_inches="tight")  # save BEFORE show
print("Chart saved to monthly_sales.png")
plt.show()
 