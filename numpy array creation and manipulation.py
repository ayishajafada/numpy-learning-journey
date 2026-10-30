import numpy as np

### Part 1: Array Creation (Questions 1–10)
#1 . Create a NumPy array containing the numbers 10, 20, 30, 40, 50 and display it.

arr=np.array([10,20,30,40,50])
print(arr)

#2 . Create a one-dimensional NumPy array containing the first 10 natural numbers using np.arange().

arr1=np.arange(1,11,1)
print(arr1)

#3 .Create an array containing all even numbers between 2 and 50 using np.arange()
arr3=np.arange(2,51,2)
print(arr3)

# 4. Create an array containing all odd numbers between 1 and 49 using np.arange().

arr4=np.arange(1,50,2)
print(arr4)

# 5. Create a NumPy array containing five zeros using np.zeros().

arr5=np.zeros(5)
print(arr5)

# 6. Create a two-dimensional array of size 3 × 4 filled with zeros using np.zeros()

arr6=np.zeros((3,4))
print(arr6)

#7. Create a one-dimensional array containing six ones using np.ones().

arr7=np.ones(6)
print(arr7)

#8. Create a 3 × 3 array filled with ones using np.ones().

arr8=np.ones((3,3))
print(arr8)

# 9 .Create an array containing five evenly spaced values between 10 and 50 using np.linspace().

arr9=np.linspace(10,50,5)
print(arr9)

#10 .Create a 4 × 4 identity matrix using np.eye()

arr10=np.eye((4))
print(arr10)

### Part 2: Array Properties (Questions 11–15)

# 11 .Create an array containing 10 elements and display its number of dimensions using ndim.

arr11=np.array([10,20,30,40,50,60,70,80,90,100])
print("dimension",np.ndim(arr11))

# 12. Create a 3 × 4 array and display its shape using shape.

arr12=np.array([[1,2,3,4],[5,6,7,8],[3,6,4,9]])
print("shape",np.shape(arr12))

# 13 .Create a 4 × 5 array and display the total number of elements using size.

arr13=np.array([[1,2,3,4,5],[6,7,8,9,10],[2,4,6,8,10],[1,3,5,7,9]])

print("size",np.size(arr13))

#14 .Create an integer array and display its data type using dtype.

arr14=np.array([10,20,30,40,50])
print("data type ",(arr14.dtype))

# 15 . Create a 2D array containing three rows and five columns. Display its dimensions, shape, and total number of elements.

arr15=np.array([[1,2,3,4,5],[6,7,8,9,10],[2,4,6,8,10]])

print("dimenstion",np.ndim(arr15))
print("shape",np.shape(arr15))
print("total number of elements",np.size(arr15)) 

### Part 3: Indexing and Slicing (Questions 16–23)

# 16. Create an array containing [10, 20, 30, 40, 50, 60] and display its first element, third element, and last element.

arr16=np.array([10,20,30,40,50,60])
print("fisrt element",arr16[0])
print("third element",arr16[2])
print("last element",arr16[-1])

## 17. Create an array containing the numbers from 1 to 20. Display the first five elements using slicing.

arr17=np.arange(1,21,1)
print("first 5 elements",arr17[ :5])

#18 .Create an array containing the numbers from 10 to 100 in increments of 10. Extract the elements from index 2 to index 6.

arr18=np.arange(10,101,10)
result=arr18[2:7]

print("original array",arr18)
print("result array",result)

# 19 . Create an array containing the first 15 natural numbers. Display every second element using slicing.

arr19=np.arange(1,16,1)
print("second element",arr19[ : :2])

#20 Create an array containing [5, 10, 15, 20, 25, 30, 35, 40]. Display the last four elements.

arr20=np.array([5, 10, 15, 20, 25, 30, 35, 40])

print("last 4 elements:",arr20[-4:])

#21 Create an array containing the numbers from 1 to 10. Display the elements in reverse order using slicing.

arr21=np.arange(1,11,1)
print("reverse",arr21[ : :-1])

# 22 .Create a 3 × 3 array containing numbers from 1 to 9. Display the element in the second row and third column.

arr22=np.arange(1,10).reshape(3,3)
print(arr22)
print("element in second row and third column ",arr22[1,2])


# 23 . Create a 3 × 4 array containing numbers from 1 to 12. Extract the first two rows and the last two columns.

arr23=np.arange(1,13).reshape(3,4)
print("original array",arr23)
print(" first two rows and the last two columns",arr23[:2,-2:])

### Part 4: Reshaping and Flattening (Questions 24–29)

# 24 .Create a one-dimensional array containing the numbers from 1 to 12. Reshape it into a 3 × 4 array.

arr24=np.arange(1,13)
result=arr24.reshape(3,4)
print(result)

#25. Create an array containing 20 elements using np.arange(). Reshape it into a 4 × 5 array.

arr25=np.arange(1,21).reshape(4,5)
print(arr25)

#26 .Create an array containing the numbers from 1 to 9. Reshape it into a 3 × 3 matrix.

arr26=np.arange(1,10).reshape(3,3)
print(arr26)

#27 . Create a 2 × 3 array and convert it into a one-dimensional array using flatten()
arr27=np.array([[1,2,3],[4,5,6]])
result=arr27.flatten()
print(result)

#28 .Create an array containing 24 elements and reshape it into a 2 × 3 × 4 array.

arr28=np.arange(1,25).reshape(2,3,4)
print(arr28)

#29 . Create an array containing 15 elements. Attempt to reshape it into a 4 × 4 array and observe the error. Explain why the operation fails.

arr29=np.arange(1,16).reshape(4,4)
print(arr29) ## it will not workout , will generate an error because the no.of elements is not the product of no.of rows and columns


### Part 5: Joining and Splitting Arrays (Questions 30–34)

#30 .Create two one-dimensional arrays containing [10, 20, 30] and [40, 50, 60]. Join them using np.concatenate().

a=np.array([10,20,30])
b=np.array([40,50,60])

result=np.concatenate((a,b))
print(result)

# 31 . Create two 2 × 2 arrays. Join them vertically using np.concatenate() with axis=0.

c=np.array([[1,2],[3,4]])
d=np.array([[5,6],[7,8]])
result=np.concatenate((c,d),axis=0)
print(result)

#32 . Create two 2 × 2 arrays. Join them horizontally using np.concatenate() with axis=1.

e=np.array([[1,2],[3,4]])
f=np.array([[5,6],[7,8]])
result=np.concatenate((e,f),axis=1)
print(result)

# 33 . Create an array containing the numbers from 1 to 12. Split it into three equal sections using np.split().

arr33=np.arange(1,13)
result=np.split(arr33,3)
print(result)

# 34 . Create an array containing the numbers from 1 to 10. Divide it into three sections using np.array_split().

arr34=np.arange(1,11)
result=np.array_split(arr34,3)
print(result)

### Part 6: Inserting, Deleting, and Sorting (Questions 35–40)


#35 .Create an array containing [10, 20, 30, 40, 50]. Insert the number 25 at index 2 using np.insert().

arr35=np.array([10,20,30,40,50])
result=np.insert(arr35,2,25)
print(result)

#36 . Create an array containing [1, 2, 3, 4, 5, 6]. Insert the values [15, 25] at index 2.

arr36=np.array([1,2,3,4,5,6])
result=np.insert(arr36,2,([15,25]))
print(result)

#37 .Create an array containing [10, 20, 30, 40, 50]. Delete the element at index 2 using np.delete().

arr37=np.array([10,20,30,40,50])
result=np.delete(arr37,2)
print(result)

# 38 . Create an array containing [10, 20, 30, 40, 50, 60]. Delete the elements at indexes 1 and 4.

arr38=np.array([10,20,30,40,50,60])
result=np.delete(arr38,[1,4])
print(result)

# 39 .Create an unsorted array containing [45, 12, 89, 23, 56, 10]. Sort it in ascending order using np.sort().

unsorted=np.array([45,12,89,23,56,10])
sorted=np.sort(unsorted)
print(sorted)

#  40. Create an array containing [15, 40, 5, 30, 20, 10]. Display the elements in descending order using np.sort() and slicing.

arr39=np.array([15,40,5,30,20,10])
sorted39=np.sort(arr39)[::-1]
print(sorted39)


### Part 7: Arithmetic and Statistical Operations (Questions 41–45)

# 41 . Create an array containing [10, 20, 30, 40, 50]. Add 5 to every element and display the result.

arr41=np.array([10,20,30,40,50])
result=arr41+5
print(result)

# 42 . Create an array containing [2, 4, 6, 8, 10]. Multiply every element by

arr42=np.array([2,4,6,8,10])
result=arr42*3
print(result)

#43 . Create an array containing [10, 20, 30, 40, 50]. Display the sum, mean, maximum, and minimum using NumPy functions.

arr43=np.array([10,20,30,40,50])
print("sum", np.sum(arr43))
print("Max", np.max(arr43))
print("Mean",np.mean(arr43))
print("Min",np.min(arr43))

#44 . A student scores [75, 80, 65, 90, 85] in five subjects. Calculate the total marks and average marks using NumPy.

marks=np.array([75,80,65,90,85])
print("total",np.sum(marks))
print("average",np.mean(marks))

#45 .A shop records daily sales of [1200, 1500, 900, 1800, 2000, 1100, 1600]. Calculate the total sales, average sales, highest sales, and lowest sales.

sales=np.array([1200,1500,900,1800,2000,1100,1600])
print("Total sales",np.sum(sales))
print("Average sales",np.mean(sales))
print("Highest",np.max(sales))
print("Lowest",np.min(sales))

### Part 8: Filtering and Conditions (Questions 46–50)

#46 . Create an array containing [10, 25, 30, 45, 50, 65, 70]. Display all elements greater than 40 using Boolean indexing.

arr46=np.array([10,25,30,45,50,65,70])
print("result:",arr46[arr46>40])

#47 .Create an array containing the numbers from 1 to 30. Extract all even numbers using a condition.

arr47=np.arange(1,31)
print("result even:",arr47[arr47%2==0])

#48 . Create an array containing [15, 25, 35, 45, 55, 65]. Replace all elements below 40 with zero.

arr48=np.array([15,25,35,45,55,65])
arr48[arr48<40]=0
print(arr48)

# 49 . A teacher records marks as [25, 45, 67, 32, 89, 90, 38, 76]. Display the marks of students who passed, assuming 40 is the passing mark. Then display the marks of students who failed.

marks=np.array([25,45,67,32,89,90])
print("Passed:",marks[marks>40])
print("Failed:",marks[marks<40])

#50 .50. A company records employee salaries as [18000, 25000, 15000, 35000, 22000, 40000, 12000]. Display salaries above ₹20,000, calculate the average salary, and sort all salaries in ascending order.

salaries=np.array([18000,25000,15000,35000,22000,40000,12000])
print("Above 20000:",salaries[salaries>20000])
print("Average salary:",np.mean(salaries))
print("Sorted:",np.sort(salaries))