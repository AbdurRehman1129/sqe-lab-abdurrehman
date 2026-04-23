import matplotlib.pyplot as plt

categories = [
    "Functional Suitability",
    "Performance Efficiency",
    "Compatibility",
    "Usability",
    "Reliability",
    "Security",
    "Maintainability",
    "Portability"
]


app1_scores = [4.5,4,5,4.5,4.5,4,4,5]  
app2_scores = [5,5,3.5,4,5,5,3,4]  

# Bar positions
x = range(len(categories))

plt.figure(figsize=(10, 6))

plt.plot(categories, app1_scores, marker='o', label='Chrome')
plt.plot(categories, app2_scores, marker='s', label='Safari')

plt.xlabel("Quality Attributes")
plt.ylabel("Scores")
plt.title("Quality Comparison (ISO 25010)")

plt.xticks(rotation=30)
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()