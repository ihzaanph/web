class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length*self.breadth)
    def __eq__(self,other):
        return self.length*self.breadth == other.length*other.breadth
    
m1=int(input("enter the length of rectangle 1"))
m2=int(input("enter the breadth of rectangle 1"))
m3=int(input("enter the length of rectangle 2"))
m4=int(input("enter the breadth of rectangle 2"))
r1=rectangle(m1,m2)
r2=rectangle(m3,m4)

print("rectangle 1\n")
print("area of rectangle",r1.area())
print("perimeter of rectangle",r1.perimeter())

print("rectangle 2\n")
print("area of rectangle",r2.area())
print("perimeter of rectangle",r2.perimeter())

if r1==r2:
    print("\narea of rectangles are equal")
else:
    print("\narea of rectangles are not equal")
