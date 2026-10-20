import matplotlib.pyplot as plt

# 1. Customer Migration Data
stages = ["Awareness", "Consideration", "Purchase", "Retention", "Advocacy"]
customers = [1000, 600, 350, 280, 150]

# 2. Create 3 charts
plt.figure(figsize=(8,4))
plt.plot(stages, customers, marker='o')
plt.title("Customer Migration Journey - Spaza to L'Oreal")
plt.ylabel("Customers")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("chart_1_journey.png")
print("✅ chart_1 created")

plt.figure(figsize=(8,4))
plt.bar(stages, customers)
plt.title("Customers per Stage")
plt.tight_layout()
plt.savefig("chart_2_bars.png")
print("✅ chart_2 created")

plt.figure(figsize=(6,6))
plt.pie(customers, labels=stages, autopct='%1.1f%%')
plt.title("Customer Distribution")
plt.tight_layout()
plt.savefig("chart_3_pie.png")
print("✅ ALL 3 CHARTS CREATED! Check your my_project folder!")