def triangle(sides):
    a, b, c = sides
    
    # Check if the sides form a valid triangle
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b < c or b + c < a or a + c < b:
        return False
    
    # If all checks pass, it is a triangle
    return True
 

def equilateral(sides):
       if (triangle(sides)):
           return (sides[0] == sides[1] == sides[2])
       else:
           return False
         

def isosceles(sides):
    if (triangle(sides)):
        if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
            return True
        else:
            return False
    else:
        return False

def scalene(sides):
    if (triangle(sides)):
        if (sides[0] != sides[1] and sides[0] != sides[2]) and sides[1] != sides[2]:
            return True
        else:
            return False
    else:
        return False



print (isosceles([10,30,30]))