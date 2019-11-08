l1=[]
def Eneque():
    global l1
    print("Enter the elements\n")
    x=int(input())
    l1.append(x)
def Deque():
    global l1
    l1=l1[1:]
    if len(l1)==0:
        print("List is empty")
def Retrival():
    global l1
    if len(l1)==0:
        print("List is empty")
    else:
        print(l1)
while 1:
    print("Menu\n 1.Enqeue \n 2.Deque \n 3.Retrival \n 4.exit")
    x=int(input())
    if x==1:
        Eneque()
    elif x==2:
        Deque()
    elif x==3:
        Retrival()
    elif x==4:
        break
    else:
        print("Invalid option")