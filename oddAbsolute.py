def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = input("Enter a number: ")
    n = float(in_num)
    if n > 21:
        result = ((n-21)*2)
        print("Result:", int(result))
        return(int(result))
    elif n <= 21:
        result = (21-n)
        print("Result:", int(result))
        return(int(result))
    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
