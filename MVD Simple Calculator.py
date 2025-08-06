print("Calculating Mass, Volume, or Density")
print("Please Answer YES or NO only in questions below (CAPTIAL LETTERS ONLY)")
a=input("Are you calculating for Mass?: ")
b=input("Are you calculating for Volume?: ")
c=input("Are you calculating for Density?: ")
if a=="YES":
    print("\n")
    print("Mass Calculator")
    print("The formula for Mass is m=v*d")
    v1=int(input("Insert your Volume here: "))
    d1=int(input("Insert your Density here: "))
    print("Calculating Mass")
    m=v1*d1
    print("\n")
    print("The total of Density is: "+str(m))
    
if b=="YES":
    print("\n")
    print("Volume Calculator")
    print("The formula for Volume is v=m/d")
    m1=int(input("Insert your Mass here: "))
    d2=int(input("Insert your Density here: "))
    print("Calculating Volume")
    v=m1/d2
    print("\n")
    print("The total of Volume is: "+str(v))
    
if c=="YES":
    print("\n")
    print("Density Calculator")
    print("The formula for Density is d=m/v")
    m2=int(input("Insert your Mass here: "))
    v2=int(input("Insert yout Volume here: "))
    print("Calculating Density")
    d=m2/v2
    print("\n")
    print("The total of Density is: "+str(d))
else:
    print("Thank you for using this program")
exit()
