def squart(x):    
    if (x == 0 or x == 1): 
        return x
    elif x<0 :
        return None
   
    start = 1
    end = x    
    while start <= end: 
        mid = (start + end) // 2          
         
        if (mid*mid == x) : return mid              
        elif (mid * mid < x) :
            start = mid + 1
            ans = mid 
              
        else :
            end = mid-1
              
    return ans 

print ("Pass" if  (3 == squart(9)) else "Fail")
print ("Pass" if  (0 == squart(0)) else "Fail")
print ("Pass" if  (4 == squart(16)) else "Fail")
print ("Pass" if  (1 == squart(1)) else "Fail")
print ("Pass" if  (5 == squart(27)) else "Fail")
print ("Pass" if  (None == squart(-1)) else "Fail")
print ("Pass" if  ( 625== squart(390625)) else "Fail")
print ("Pass" if  (11111 == squart(123456789)) else "Fail")
print ("Pass" if  (1 == squart(1.2)) else "Fail")
print ("Pass" if  (351 == squart(123456.123456)) else "Fail")
