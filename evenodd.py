def evenorodd(num):
    remainder = num%2  
    if (remainder == 0):
        return "even"                                                        
    else :
        return "odd"
    
if __name__ == "__main__":
    remainder = 27 
    print(evenorodd(remainder))