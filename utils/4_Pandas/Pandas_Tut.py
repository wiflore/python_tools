import pandas
import OpenCV



df1 = pandas.DataFrame([[2, 3, 4], [10, 20, 30]])
print(df1)

df1 = pandas.DataFrame([[2, 3, 4], [10, 20, 30]], columns = ["Price", "Age", "Value"])
print(df1)

df1 = pandas.DataFrame([[2, 3, 4], [10, 20, 30]], columns = ["Price", "Age", "Value"], index = ["First", "Second"])
print(df1)

df2 = pandas.DataFrame([{"Name":"John"}, {"Name": "Jack"}])
print(df2)

df2 = pandas.DataFrame([{"Name":"John", "Surname":"Johns"}, {"Name": "Jack"}])
print(df2)

print(type(df1))
print(dir(df1))
print(df1)
print("\nmean\n")
print(df1.mean())
print("\nmean mean\n")
print(df1.mean().mean())
print("\nPrices\n")
print(df1.Price)
print("\nPrices mean\n")
print(df1.Price.mean())
print("\nPrices max\n")
print(df1.Price.max())