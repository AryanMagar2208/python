#main.py
import shapes
print("1.Circle")
print("2.Rectangle")
print("3.Triangle")
     
choice=int(input("Choose an option:  "))
 
     
if choice==1:
    r= float(input("Enter radius:"))
    area= shapes.circle_area(r)
    print("Area of the circle=",area)
     
                                                                             
elif choice ==2:
    L=float(input("Enter length:"))
    b=float(input ("Enter width:"))
    
    area =shapes.rectangle_area(L,b)
    print("Area of rectangle=",area)
    
    
elif choice==3:  
    b=float(input("Enter base:"))
    w=float(input("enter width:"))
    area =shapes.triangle_area(b,w)
    print("Area of the triangle=",area)
     
else:
    print("Invalid choice")
    
    

