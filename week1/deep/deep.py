
x = input(("What is the Answer to the Great Question of Life, the Universe, and Everything?"))

if x.strip() == "42":
    print("Yes")
    
elif x.strip().lower() == "forty-two":
    print("Yes")

elif x.strip().lower() == "forty two":
    print("Yes")

else :
    print("No")