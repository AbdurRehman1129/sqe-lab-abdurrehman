import matplotlib.pyplot as plt
import numpy as np

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

# Number of variables
N = len(categories)

# Compute angle for each category
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()

# Close the loop
app1_scores += app1_scores[:1]
app2_scores += app2_scores[:1]
angles += angles[:1]

# Create radar chart
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

# Plot data
ax.plot(angles, app1_scores, linewidth=2, label='Chrome')
ax.fill(angles, app1_scores, alpha=0.25)

ax.plot(angles, app2_scores, linewidth=2, label='Safari')
ax.fill(angles, app2_scores, alpha=0.25)

# Labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# Title and legend
plt.title("Quality Comparison (ISO 25010)", size=14)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))

plt.show()