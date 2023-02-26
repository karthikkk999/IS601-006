class MyCalc:
    ans = 0.0

    def add(a,b): 
        ans = a+b
        return ans
    #UCID: sk3374
    #Date: 2/23/23 9:00 PM
    #function add() takes in 2 parameters a and b, adds them and stores the result in ans
    #In the end returns ans

    def sub(a,b): 
        ans = a-b
        return ans
    #UCID: sk3374
    #Date: 2/23/23 9:02 PM
    #function sub() takes in 2 parameters a and b, does a minus b and stores the result in ans
    #In the end returns ans

    def mul(a,b): 
        ans = a*b
        return ans
    #UCID: sk3374
    #Date: 2/23/23 9:05 PM
    #function mul() takes in 2 parameters a and b, does a times b and stores the result in ans
    #In the end returns ans
    
    def div(a,b): 
        if b == 0:
            print("Cannot divide by zero. Please change the denominator")
            return
        ans = a/b
        return ans
    #UCID: sk3374
    #Date: 2/23/23 9:07 PM
    #function div() takes in 2 parameters a and b, does a divided by b and stores the result in ans
    #In the end returns ans
        
    do_math = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div 
    }
    #UCID: sk3374
    #Date: 2/23/23 8:43 PM
    #Used a dictionary and stored the operators as key and the reference to their functions as values

    def calculate(self, num1, num2, op):
        if num1  == "ans":
            return self.calculate(self.ans, num2, op)
        else:
            try:
                num1 = float(num1)
                num2 = float(num2) 
            except:
                print("Please use valid numbers in the equation")
                return
            self.ans = MyCalc.do_math[op](num1, num2)
        return self.ans        
    #UCID: sk3374
    #Date: 2/25/23 8:23 PM
    #function calculate() takes in 4 arguments (including self) 
    #checks if the num1 is equal to ans, if yes, takes the previous result ans as num1 
    #else, we convert both the nums to float and if it fails we send a prompt to use and return
    #if the conversion is successfull, we call the appropriate function using do_math dict   
    

def main():
    print("Simple Calculator: Supports basic math operations between 2 numbers (like 4/5)")
    
    calc = MyCalc()

    while True:
        decide = input("Press 'M' to do math or 'Q' to quit: ") 
        if decide in ('M', 'm'):
            eq  = input("Enter the equation: ")
            for op in calc.do_math.keys():
                if op in eq:
                    nums = eq.split(op)
                    r = calc.calculate(nums[0].strip(), nums[1].strip(), op)
                    print("Result: " + str(r))
        if decide in ('Q','q'):
            print("GoodBye")
            return
        
if __name__ == "__main__":
    main()
    #UCID: sk3374
    #Date: 2/25/23 8:13 PM
    #the main function asks user to press 'M' to do the math or 'Q' to quit 
    #if user presses 'M' we check for the operation involved in the equation using a for op in keys()  
    #when there is a match we split the equation that is stored in the string and store them in nums
    #we then send these values after removing whitespaces to the calculate() function using an object calc of MyCalc class.   
 