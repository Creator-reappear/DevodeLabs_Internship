# To-Do list
def insert(L):
    List=input("Enter the quest u want me to hold on:\n")
    L.append(List)
    print("This is the quest u want to remember!")
    for i,quest in enumerate(L,start=1):
                     print(f"{i}.{quest}")        

def delete(L):
    a=len(L)
    b=int(input("Ener the index number u want to delete:"))
    if b>a :
          print("Invalid index")
          return 0
    else:
          L.pop(b-1)
          print("Your final Quest list!")
          for i,quest in enumerate(L,start=1):
               print(f"{i}.{quest}")

def list(L):
    while True:
        n=int(input("Enter '1', if u want to add another Quest:\n"))
        if(n==1):
            insert(L)
        else:
            print("I guess that the end of the for today :)")
            print("ohh,yay! Here is ur list of quest",)
            for i,quest in enumerate(L,start=1):
                  print(f"{i}.{quest}")
            a=int(input("Do u want to delete any,then enter 1:\n"))
            if a==1:
                  delete(L)
            break


def main():
    L=[]
    insert(L)
    list(L)

main()