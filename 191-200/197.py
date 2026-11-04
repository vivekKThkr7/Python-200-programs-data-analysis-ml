# Visualizing Data with Matplotlib

# Matplotlib is a pyhton visualization library used to create line charts, bar charts, scatter plots, and other graphics.The usual structure is to create a figure and axes, draw the data, label the charts and display or save it. 
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "product": ["Keyboard", "Mouse", "Chair", "Monitor"],
    "revenue": [250, 150, 400, 900]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots()

ax.bar(df["product"], df["revenue"])

ax.set_title("Revenue by Product")
ax.set_xlabel("Product")
ax.set_ylabel("Revenue")

fig.tight_layout()

fig.savefig("outputs/charts/sales_chart.png", dpi=150)

print("Chart saved as outputs/charts/sales_chart.png")

plt.show()