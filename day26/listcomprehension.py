import pandas

#list comprehension

numbers = [1,2,3]
new_list = [n+100 for n in numbers]
print(new_list)

name = "Asher"
letter_list = [letter for letter in name]
print(letter_list)

range = range(1,5)
double_range_list = [n*2 for n in range if n == 1]
#print(double_range_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freedie']
up_names = [names.upper() for names in names if len(names)>5]
#print(up_names)

#New challenge
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_num = [n**2 for n in numbers]
#print(squared_num)

#new challenge
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in numbers if n%2==0]
#print(result)

#new challenge
file1 = pandas.read_csv("file1.txt")
file2 = pandas.read_csv("file2.txt")
file1_list = file1["x"].to_list()
file2_list = file2["y"].to_list()

result = [n for n in file1_list if n in file2_list]
print(result)
