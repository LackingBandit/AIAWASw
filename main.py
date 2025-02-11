
# # v=input("What's your name? ")
# # '''
# # print(v)
# # print(len(v))
# # print(len(v.strip()))
# # '''
# # # .strip removes the spaces from the ends of the strings
# # x=v.strip("d")
# # print(x)
# # # .split splits the before and after the string and removing the letter and returns an array
# # print(x.split("s")) 
# # print(x.split()[0])
# # print(x.split()[3:4])
# # y=x.split()[0]
# # print(y.upper())
# # print(y.lower())
# # #all occurances are replaced if there is nothing specified 
# # print(y.replace("a","z"))
# # z=y.lower()


# # # If there is number after the replaced letters then it changes the first occurances in order
# # print(z.replace("a","",2))
# # s=y.replace("a", "z")
# # print('r' in s)
# # s="store"
# # print(s[0:2])

# # user_input=input("Write some words ")
# # user_input= user_input.split()
# # print(len(user_input))
# # print(str(user_input))
# # print("You have "+str(len(user_input))+" words")
# # # user_input=input("Hi, what's your name? ")
# # # user_age=input("How old are you? ")
# # # user_age=int(user_age)
# # # user_age=user_age+8
# # # user_input=user_input.strip()
# # # print("Hey "+user_input+" you have "+str(len(user_input))+" letters in your name and you will be "+ str(user_age) + " years old")
# # user_input='b'.join(user_input)
# # print(user_input)

# #Write a program to create a new string made of an input string’s first, middle, and last character
# # input=input("What is your name?-->")
# # last_letter=(len(input))
# # last_num=input[(len(input))-1]
# # middle_letter=(len(input))//2
# # first_letter=input[0]
# # print(first_letter+input[middle_letter]+last_num)

# x="block"
# print(x[0:5:2])

s1 = input("Enter a string: ")
s2 = input("Enter a string: ")
split=len(s1)//2
print(s1[:split]+s2+s1[split:])


# middle_letter=(len(x))//2
# print(x[middle_letter-1]+x[middle_letter]+x[middle_letter+1])
# print(x[middle_letter-1:middle_letter+2])



