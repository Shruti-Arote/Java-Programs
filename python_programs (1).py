# -*- coding: utf-8 -*-
"""Python_Programs.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qLsjHixfP3w72iP55uB2VoCB_QkBff-m

## String Methods
"""

str="This is me"
str1='1234'
print("The occurance of letter i is -" ,str.count("i") , "times")
print("Total number of letters in the given string is" , len(str))
print("find the word is in the sentence-", str.find("is"))
print(str.lower())
print(str.upper())
print(str.capitalize())
print(str.title())
print(str.swapcase())
print(str.split())
list=str.split()
print(list[1])
print(str.ljust(13 ,'@'))
print(str.rjust(14 ,'#'))
print(str.center(18,'-'))
print(str.replace('me','pycharm'))
#print(str.join())
print(str.endswith('arm'))
print(str.isdigit())
print(str1.isdigit())
print(str.istitle())

"""# List"""

list=['I','am','robo']
list1=[2,56,98,34]
print(list1[2])
print(list[:3])
print(list[:])
print(list[2:])
print(list1[1:3:1])
list[2]='abc'
print(list)
#print(delattr(list[2]))
print(list+list1)
print(list*2)
if 'an' in list:
    print("yes")
else:
    print('no')
print(max(list1))
print(sorted(list1))

"""# Dictionary"""

# creating a dictionary
country_capitals = {
  "Germany": "Berlin",
  "Canada": "Ottawa",
  "England": "London"
}

# printing the dictionary
print(country_capitals)

country_capitals = {
  "Germany": "Berlin",
  "Canada": "Ottawa",
  "England": "London"
}

# access the value of keys
print(country_capitals["Germany"])
print(country_capitals["England"])

country_capitals = {
  "Germany": "Berlin",
  "Canada": "Ottawa",
}

# delete item having "Germany" key
del country_capitals["Germany"]

print(country_capitals)

