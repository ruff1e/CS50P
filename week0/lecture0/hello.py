name = input("Hi, what's your name: ")
age = input("How old are you?: ")

#remove the whitespace from the name then capilatize it 
#(since it is .title() it will cap the 2nd word too)
name = name.strip().title()



print(f"{name} you are dumb and {age} years old")
