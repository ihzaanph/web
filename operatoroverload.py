class student:
    def __init__(self,mark1,mark2):
        self.mark1=mark1
        self.mark2=mark2
        print(self.mark1,self.mark2)
    def __eq__(self,other):
        s1=self.mark1+self.mark2
        s2=other.mark1+other.mark2
        return s1==s2

m1=int(input("enter mark1 of student1 "))
m2=int(input("enter mark2 of student1 "))
m3=int(input("enter mark1 of student2 "))
m4=int(input("enter mark2 of student2 "))
s1=student(m1,m2)
s2=student(m3,m4)
if s1==s2 :
    print("both s1 and s2 are equal");
else:
    print("s1 and s2 are different")
            
