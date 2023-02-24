class MyCalc:
    ans = 0.0

    def add(a,b): 
        ans = a+b
        return ans
       
    def minus(a,b): 
        ans = a-b
        return ans
    
    def mul(a,b): 
        ans = a*b
        return ans
    
    def div(a,b): 
        if b == 0:
            raise ValueError("Cannot divide by zero. Please change the denominator")
        ans = a/b
        return ans
    
    do_math = {
        "+": add,
        "-": minus,
        "*": mul,
        "/": div 
    }

def main():
    print("Simple Calculator: Supports basic math operations between 2 numbers")
    
    Calc = MyCalc()

    while True:
        decide = input("Press 'Y' to do Math and 'Q' to quit: ") 
        if decide in ('Y', 'y'):
            one = (input("Enter first num (or ""ans"" to use the previous result): "))
            
            try:
                one = float(Calc.ans) if one.strip() == "ans" else float(one)
                two = float(input("Enter second num: "))
            except ValueError:
                print("Only Integers are allowed in the Calculator")
                return
            operator = input("operation to be performed (+,-,*,/): ")

            if operator not in Calc.do_math.keys():
                print("Invalid operation. Expected values : +,-,*,/")
                return

            Calc.ans = float(Calc.do_math[operator](one,two))
            print(f"Result = {Calc.ans}")      
        elif decide in ('Q', 'q'):
            print("Bye!")
            return
        else:
            print('Invalid Keyword. Expected values: Y,y,Q,q')
    
if __name__ == "__main__":
    main()
