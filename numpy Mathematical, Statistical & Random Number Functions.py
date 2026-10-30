
import numpy as np

# =========================
# Section A: Mathematical Functions
# =========================

# 1
arr1 = np.array([10, 20, 30, 40, 50])
print("1.", np.add(arr1, 5))

# 2
arr2a = np.array([10, 20, 30, 40])
arr2b = np.array([5, 10, 15, 20])
print("2.", np.add(arr2a, arr2b))

# 3
arr3a = np.array([50, 60, 70, 80])
arr3b = np.array([10, 20, 30, 40])
print("3.", np.subtract(arr3a, arr3b))

# 4
arr4 = np.array([2, 4, 6, 8, 10])
print("4.", np.multiply(arr4, 3))

# 5
arr5 = np.array([100, 200, 300, 400, 500])
print("5.", np.divide(arr5, 10))

# 6
arr6 = np.array([17, 23, 35, 47, 59])
print("6.", np.mod(arr6, 5))

# 7
arr7 = np.array([2, 3, 4, 5, 6])
print("7.", np.square(arr7))

# 8
arr8 = np.array([25, 36, 49, 64, 81])
print("8.", np.sqrt(arr8))

# 9
arr9 = np.array([2, 3, 4, 5])
print("9.", np.power(arr9, 3))

# 10
arr10 = np.array([-10, -25, 30, -45, 50])
print("10.", np.abs(arr10))

# 11
arr11 = np.array([2.345, 4.567, 6.789, 8.123])
print("11.", np.round(arr11, 2))

# 12
arr12 = np.array([2.3, 4.7, 6.1, 8.9, 9.2])
print("12.", np.ceil(arr12))

# 13
arr13 = np.array([2.3, 4.7, 6.1, 8.9, 9.2])
print("13.", np.floor(arr13))

# 14
arr14 = np.array([1, 2, 3, 4, 5])
print("14.", np.exp(arr14))

# 15
arr15 = np.array([1, 10, 100, 1000])
print("15.", np.log10(arr15))

# 16
arr16 = np.array([0, 30, 45, 60, 90])
radians = np.deg2rad(arr16)
print("16.", np.sin(radians))

# 17
arr17a = np.array([10, 20, 30])
arr17b = np.array([2, 4, 5])
print("17.", np.divide(arr17a, arr17b))

# 18
arr18 = np.array([15, 25, 35, 45, 55])
print("18. Square Root:", np.sqrt(arr18))
print("18. Square:", np.square(arr18))
print("18. Cube:", np.power(arr18, 3))

# 19
arr19 = np.array([12, 25, 37, 48, 59])
print("19.", np.floor_divide(arr19, 4))

# 20
arr20 = np.array([2, 3, 4, 5, 6])
squares20 = np.square(arr20)
print("20. Squares:", squares20)
print("20. Sum of Squares:", np.sum(squares20))

# =========================
# Section B: Statistical Functions
# =========================

# 21
arr21 = np.array([10, 20, 30, 40, 50])
print("21.", np.mean(arr21))

# 22
arr22 = np.array([45, 60, 75, 80, 90, 95])
print("22.", np.median(arr22))

# 23
arr23 = np.array([10, 20, 30, 40, 50, 60])
print("23.", np.std(arr23))

# 24
arr24 = np.array([5, 10, 15, 20, 25])
print("24.", np.var(arr24))

# 25
arr25 = np.array([45, 67, 89, 23, 56, 78])
print("25.", np.min(arr25))

# 26
arr26 = np.array([45, 67, 89, 23, 56, 78])
print("26.", np.max(arr26))

# 27
arr27 = np.array([12, 24, 36, 48, 60])
print("27.", np.sum(arr27))

# 28
arr28 = np.array([2, 3, 4, 5])
print("28.", np.prod(arr28))

# 29
arr29 = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print("29.", np.percentile(arr29, 25))

# 30
arr30 = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print("30.", np.percentile(arr30, 75))

# 31
arr31 = np.array([45, 20, 75, 10, 90, 35])
print("31.", np.argmin(arr31))

# 32
arr32 = np.array([45, 20, 75, 10, 90, 35])
print("32.", np.argmax(arr32))

# 33
arr33 = np.array([10, 20, 30, 40, 50])
print("33.", np.ptp(arr33))

# 34
arr34 = np.array([1, 2, 3, 4, 5])
print("34.", np.cumsum(arr34))

# 35
arr35 = np.array([1, 2, 3, 4, 5])
print("35.", np.cumprod(arr35))

# =========================
# Section C: Random Number Generation
# =========================

rng = np.random.default_rng()

# 36
print("36.", rng.random())

# 37
print("37.", rng.random(10))

# 38
print("38.", rng.integers(1, 101))

# 39
print("39.", rng.integers(10, 51, 20))

# 40
print("40.", rng.integers(1, 101, 15))

# 41
print("41.", rng.uniform(10, 50, 5))

# 42
students = np.array([
    "Asha", "Rahul", "Priya", "Kiran", "Anjali",
    "Rohit", "Sneha", "Vijay", "Neha", "Arjun"
])
print("42.", rng.choice(students))

# 43
arr43 = np.arange(1, 21)
print("43.", rng.choice(arr43, size=5, replace=False))

# 44
arr44 = np.array([10, 20, 30, 40, 50, 60, 70, 80])
rng.shuffle(arr44)
print("44.", arr44)

# 45
arr45 = np.arange(1, 11)
print("45.", rng.permutation(arr45))

# 46
print("46.", rng.normal(50, 10, 10))

# 47
print("47.", rng.integers(1, 7, 20))

# 48
arr48 = rng.random(100)
print("48. Mean:", np.mean(arr48))

# 49
arr49 = rng.normal(100, 15, 1000)
print("49. Mean:", np.mean(arr49))
print("49. Std:", np.std(arr49))

# 50
arr50 = rng.integers(1, 101, 100)
print("50. Mean:", np.mean(arr50))
print("50. Median:", np.median(arr50))
print("50. Min:", np.min(arr50))
print("50. Max:", np.max(arr50))
print("50. Std:", np.std(arr50))