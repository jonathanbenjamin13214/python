"""Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed."""
a=input("does the studant have a spacial health condition")
if(a=="yes"):
    print("can take the exam")
else:
    b=int(input("what is your atendence"))
    if(b<=75):
        print("can't tske the exam")
    else:
        print("can take the exam")