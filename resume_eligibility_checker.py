def resumeEligibility():
    name = input("Enter your name: ")
    experience = int(input("Enter years of experience: "))
    if experience >= 5:
        print(name,"is eligible for Senior developer role")
    else:
        print(name,"is eligible for Junior Developer role")
 resumeEligibility()       
