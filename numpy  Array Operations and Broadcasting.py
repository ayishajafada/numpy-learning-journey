
import numpy as np

# =========================
# SECTION A: Array Creation and Basic Operations
# =========================

# Q1
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])
print("Q1")
print(arr1)
print(arr2)

# Q2
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])
print("\nQ2")
print(arr1 + arr2)

# Q3
arr1 = np.array([100, 200, 300, 400])
arr2 = np.array([10, 20, 30, 40])
print("\nQ3")
print(arr1 - arr2)

# Q4
arr1 = np.array([2, 4, 6, 8])
arr2 = np.array([3, 5, 7, 9])
print("\nQ4")
print(arr1 * arr2)

# Q5
arr1 = np.array([100, 200, 300])
arr2 = np.array([10, 20, 30])
print("\nQ5")
print(arr1 / arr2)

# Q6
arr = np.array([11, 22, 33, 44, 55])
print("\nQ6")
print(arr % 2)

# Q7
arr = np.array([2, 3, 4, 5, 6])
print("\nQ7")
print(arr ** 2)

# Q8
arr = np.array([10, 20, 30, 40, 50])
print("\nQ8")
print(arr + 100)

# Q9
arr = np.array([100, 200, 300, 400, 500])
print("\nQ9")
print(arr - 50)

# Q10
arr = np.array([5, 10, 15, 20, 25])
print("\nQ10")
print(arr * 3)

# =========================
# SECTION B: Comparison and Mathematical Functions
# =========================

# Q11
marks = np.array([35, 45, 60, 75, 90])
print("\nQ11")
print(marks >= 60)

# Q12
arr = np.array([10, 25, 40, 55, 70])
print("\nQ12")
print(arr > 30)

# Q13
arr = np.array([12, 18, 25, 32, 45])
print("\nQ13")
print(arr <= 25)

# Q14
arr1 = np.array([10, 50, 30, 80])
arr2 = np.array([20, 40, 60, 70])
print("\nQ14")
print(np.maximum(arr1, arr2))

# Q15
arr = np.array([4, 9, 16, 25, 36])
print("\nQ15")
print(np.sqrt(arr))

# Q16
arr = np.array([1, 2, 3, 4, 5])
print("\nQ16")
print(np.exp(arr))

# Q17
arr1 = np.array([5, 10, 15, 20])
arr2 = np.array([2, 4, 6, 8])

print("\nQ17")
print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)

# Q18
arr = np.array([15, 25, 35, 45, 55])
print("\nQ18")
print(arr >= 35)

# Q19
arr1 = np.array([100, 250, 350, 450])
arr2 = np.array([150, 200, 400, 300])
print("\nQ19")
print(np.maximum(arr1, arr2))

# Q20
arr = np.array([9, 16, 25, 36, 49, 64])
print("\nQ20")
print(np.sqrt(arr))

# =========================
# SECTION C: Broadcasting with Scalars
# =========================

# Q21
arr = np.array([70, 80, 90])
print("\nQ21")
print(arr + 5)

# Q22
arr = np.array([100, 200, 300, 400])
print("\nQ22")
print(arr - 20)

# Q23
arr = np.array([10, 20, 30, 40, 50])
print("\nQ23")
print(arr * 5)

# Q24
arr = np.array([100, 200, 300, 400, 500])
print("\nQ24")
print(arr / 10)

# Q25
prices = np.array([150, 250, 350, 450])
final_prices = prices - 50

print("\nQ25")
print("Original Prices:", prices)
print("Final Prices:", final_prices)

# Q26
salaries = np.array([20000, 25000, 30000, 35000])
print("\nQ26")
print(salaries + 3000)

# Q27
arr = np.array([10, 20, 30, 40, 50])
print("\nQ27")
print((arr ** 2) + 10)

# Q28
arr = np.array([100, 200, 300, 400])
print("\nQ28")
print(arr * 0.18)

# Q29
arr = np.array([50, 100, 150, 200, 250])
print("\nQ29")
print((arr + 25) * 2)

# Q30
marks = np.array([80, 90, 70, 85, 95])
updated_marks = marks + 5

print("\nQ30")
print("Updated Marks:", updated_marks)
print(">=90 :", updated_marks >= 90)

# =========================
# SECTION D: Array Shapes and Dimensions
# =========================

# Q31
arr = np.array([10, 20, 30, 40])
print("\nQ31")
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)

# Q32
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\nQ32")
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)

# Q33
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nQ33")
print(arr + 10)

# Q34
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nQ34")
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)

# Q35
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("\nQ35")
print(arr + 100)

# =========================
# SECTION E: Broadcasting with 2D Arrays
# =========================

# Q36
arr1 = np.array([[10], [20], [30]])
arr2 = np.array([1, 2, 3, 4])

print("\nQ36")
print(arr1 + arr2)

# Q37
arr1 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

arr2 = np.array([1, 2, 3])

print("\nQ37")
print(arr1 + arr2)

# Q38
arr1 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

arr2 = np.array([
    [5],
    [10],
    [15]
])

print("\nQ38")
print(arr1 + arr2)

# Q39
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nQ39")
print(arr * 5)

# Q40
arr = np.array([
    [100, 200, 300],
    [400, 500, 600]
])

print("\nQ40")
print(arr - np.array([10, 20, 30]))

# =========================
# SECTION F: Broadcasting Rules and Applications
# =========================

# Q41
arr1 = np.ones((2, 3))
arr2 = np.array([1, 2, 3])

result = arr1 + arr2

print("\nQ41")
print(result)
print("Result Shape:", result.shape)

# Q42
arr1 = np.arange(12).reshape(3, 4)
arr2 = np.array([1, 2, 3, 4])

print("\nQ42")
print(arr1 + arr2)

# Q43
arr1 = np.arange(1, 10).reshape(3, 3)
arr2 = np.array([[10], [20], [30]])

print("\nQ43")
print(arr1 + arr2)

# Q44
arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2])

print("\nQ44")
try:
    print(arr1 + arr2)
except ValueError as e:
    print("Error:", e)

# Broadcasting fails because shapes (3,) and (2,) are incompatible.

# Q45
arr1 = np.ones((2, 3))
arr2 = np.array([10, 20])

print("\nQ45")
try:
    print(arr1 + arr2)
except ValueError as e:
    print("Error:", e)

# Broadcasting fails because (2,3) and (2,) do not match from the right side.

# Q46
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 78]
])

bonus = np.array([5, 3, 2])

print("\nQ46")
print(marks + bonus)

# Q47
salaries = np.array([20000, 25000, 30000, 35000])

increment = salaries * 0.10
final_salary = salaries + increment

print("\nQ47")
print("Original Salaries:", salaries)
print("Increment:", increment)
print("Final Salaries:", final_salary)

# Q48
prices = np.array([100, 200, 300, 400])

tax = prices * 0.18
final_prices = prices + tax

print("\nQ48")
print("Final Prices:", final_prices)

# Q49
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

column_means = np.mean(data, axis=0)
normalized = data - column_means

print("\nQ49")
print("Column Means:", column_means)
print("Normalized Data:")
print(normalized)

# Q50
marks = np.array([
    [65, 75, 85],
    [70, 80, 90],
    [55, 60, 75]
])

print("\nQ50")
print("Original Marks:")
print(marks)

means = np.mean(marks, axis=0)
bonus = np.array([5, 3, 2])

updated_marks = marks + bonus
final_result = updated_marks - means

print("Column Means:", means)

print("Updated Marks:")
print(updated_marks)

print("Final Result:")
print(final_result)