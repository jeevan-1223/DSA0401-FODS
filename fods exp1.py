
import numpy as np

student_scores = np.array([
    [85, 90, 78, 88],
    [92, 85, 80, 75],
    [78, 95, 88, 82],
    [88, 80, 92, 90]
])

avg = np.mean(student_scores, axis=0)

subjects = ["Math", "Science", "English", "History"]

print("Average scores:", avg)

i = np.argmax(avg)
print("Highest average subject:", subjects[i])
print("Highest average:", avg[i])
