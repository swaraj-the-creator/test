grabook1 = {"name":"Swaraj","marks":"70"}
grabook2 = {"name":"Harshwardan","marks2":"59"}
grabook3 = {"name":"Samaksh","marks3":"68"}
grabook4 = {"name":"Aayush","marks4":"75"}
grabook5 = {"name":"Rudra","marks5":"72"}
mark = grabook1["marks"] + grabook2["marks2"] + grabook3["marks3"] + grabook4["marks4"] + grabook5["marks5"]
int(mark)
avg =int(mark / 5)
print(f"Average of class is {avg}")
#top = max()
print("Enter the grade book's name you want to access ")
boo = input()
if boo == "grabook1":
    acc = input("Enter students name you want to access: ")