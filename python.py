#String : it is a sequencce of charecter containe in a string.
#str = "1234_string"
#print(type(str)) 
# we have used the type() function for understanding the data type   output : <class 'str'>
# length (len()) : it is use to count the charecters
# var = "1234_string"
# print(len(var))    # 11

# upper() : it is use to make the string into upper case charecter
# var = "string"
# print(var.upper())    # STRING

# lower() : it is use to make the string into lower case.
# str = "STRING"
# print(str.lower())   # string

# title() : it is use to make the first  charecter into capital.
# str = "python"
# print(str.title())   # Python

# concatination : it is use to concatinate the two string ( it is use to add the two string or it is use to join the string as it)
# str = "python"
# str_1 = " programing"
# print(str + str_1)  # python programing


# Replace : it is a operation in python which is used to replace a base charecter into the new charecters.
# str = "cython"
# print(str.replace("c","p"))  # python

#Index : it is used to find the position of the charecters.
# str = "python is a programmig language !"
# print(str.index("is"))  # 7

# Slicing : it is a way to extract a substring from a string using indexing or its ranges.
# syntax :variable[start:end:step]
# start : it is starting of the indexing
# end : it is ending charecter of the string
# step : it is interval given into the string.
# var = "python is a programing language"
# print(var[0:34:2])   # pto sapormn agae
                     
# Negative indexing : it is use to access elements from the end of the charecters / string
# note : every NI will be refere to -1 of the last element.
# var = "python is s programing language"
#print(var[::-1])
#print(var[-1:34])



# strip() method: it is use to remove leading and trailing white 
#                 spaces from the string.
# syntax : var.strip([charecter])
# var = "  string   "
# var_1 = var.strip()
# print(var_1)    # string

# var = "____name____"
# var_1 = var.strip("_")
# print(var_1)
# output : name
# type of strip() : 1) lstrip()  2) rstrip()
# i want to remove left side special symbol :
#var = "     string    "
#print(var.lstrip())
# output : string
#print(var.rstrip())
# output :      string 

# split() method or operation :  it is use to divide a string into list of substring based onb the specified seperator ( delimetor)
# syntax : variable.split(seperator = None, maxsplit=-1)
# var = input("enter the string : ")
# print(type(var.split()))
# enter the string : I am learning python
#['I', 'am', 'learning', 'python']    <class 'list'>

#var = input("enter the string : ")
#print(var.split())
#output : ['I', 'am', 'learning', 'python']
#var_2 = ['I', 'am', 'learning', 'python']
#print(type(var_2))

#name = "   hi python   "
#print(name.split())
# output : ['hi', 'python']

#name = "a-b-c-d"
#print(name.split("-",1))
#output :['a', 'b', 'c-d']
#print(name.split("-",-1))
# output : ['a', 'b', 'c', 'd']
#print(name.split("-",-2))


#print(var.split())
# output : ['I', 'am', 'learning', 'python', 'and', 'java']

# input() : whenever you want an input from the user then you have to use input()
# note : whenever you will provide any kind data to the input function it will be consider as string