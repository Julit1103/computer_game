name=input("enter your name: ")
print("welcome", name, "to this adventure!")

answer=input("You are on a dirt road.You can either go left or right.which way would you like to go? ").lower()

if answer=="left":
    answer=input("you have come to a river. you can walk around it or swim across.which one would you choose(walk/swim)? ").lower()
    if answer=="swim":
        print("you swam.you got eaten by alligator. ")
    elif answer=="walk":
        print("you walked for many miles,ran out of water and died. ")
    else:
        print("not a valid option. you lose")

elif answer=="right":
    answer=input("you come to a bridge.it looks wobly.do you wanna cross it or head back(cross/back)? ").lower()
    if answer=="cross":
        print("the bridge collapsed.you loose ")
    elif answer=="back":
        print("you walked and reached a safe house. YOU WON! ")
    else:
        print("not a valid option. you lose")

else:
    print("not a valid option. you lose")

print("Thank you for trying", name)