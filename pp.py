print("Enter the numbers of the list one by onw\n")
size = int(input("Enter size of list\n"))
mylist = []
for i in range(size):
    mylist.append(int(input("Enter list Element")))

print(f"Your list is {mylist}")

reverse1 = mylist[:]
reverse1.reverse()
print(f"My first reversed list is {reverse1}")

reverse2 = mylist[:]
print(f"My second reversed list is {reverse2[::-1]}")

reverse3 = mylist[:]
for i in range(len(mylist)//2):
    reverse3[i],reverse3[len(mylist)-i-1] = reverse3[len(mylist)-i-1],reverse3[i]

print(f"My third reverse list is {reverse3} ")

if reverse3 == reverse1 == reverse2:
    print("All the three methods return the same result")