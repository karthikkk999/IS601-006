import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidPaymentException, InvalidStageException, OutOfStockException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

# Test1 - bun must be the first selection (can't add patties/toppings without a bun choice)
def test_bun_first(machine):
    machine.reset()
    with pytest.raises(InvalidStageException):
        machine.pick_patty("turkey")

    with pytest.raises(InvalidStageException):
        machine.pick_toppings("lettuce")
    # UCID: sk3374@njit.edu
    # Date: 3/16/23 8.00 PM
    # we reset the state of the machine object. and use it for all the test cases
    # used context manager - pytest.raises to check if an InvalidStageException is raised when we selected a patty without a bun choice
    # again used context manager to check if an Exception is raised when we selected a toppings without a bun choice and a patty first

# Test 2 - can only add patties if they're in stock
def test_add_instock_patties(machine):
    machine.reset()
    machine.handle_bun("no bun")

    for p in machine.patties:
        p.quantity = 0

    with pytest.raises(OutOfStockException):
        machine.pick_patty("turkey")
    
    for p in machine.patties:
        p.quantity = 10
    # UCID: sk3374@njit.edu
    # Date: 3/16/23 8.10 PM
    # we reset the machine using machine.reset()
    # first made made the quantity value of all patties to 0 using a for ...in and iterating over the patties in the object
    # then we see if we get an OutOfStockException when we try to pick a patty when the quantity of all patties is 0.
    # we use context manager - pytest.raises() to check if an expected Exception has raised
    # then we restock all the patties (i.e. change back the quantity value of all the patties)


# Test 3 - can only add toppings if they're in stock
def test_add_instock_toppings(machine):
    machine.reset()
    machine.handle_bun("no bun")
    machine.handle_patty("next")

    for t in machine.toppings:
        t.quantity = 0

    with pytest.raises(OutOfStockException):
        machine.pick_toppings("lettuce")

    for t in machine.toppings:
        t.quantity = 10
    # UCID: sk3374@njit.edu
    # Date: 3/16/23 8.28 PM
    # we reset the machine using machine.reset()
    # first made made the quantity value of all toppings to 0 using a for ...in and iterating over the toppings in the object
    # then we see if we get an OutOfStockException when we try to pick a topping when the quantity of all toppings is 0.
    # we use context manager - pytest.raises() to check if an expected Exception has raised
    # then we restock all the toppings (i.e. change back the quantity value of all the toppings)

# Test 4 - Can add up to 3 patties of any combination
def test_add_up_to_three_patties(machine):
    machine.reset()
    machine.handle_bun("no bun")
    for _ in range(3):
        machine.handle_patty("Beef")

    with pytest.raises(ExceededRemainingChoicesException):
        machine.pick_patty("beef")
    # UCID: sk3374@njit.edu
    # Date: 3/16/23 8.35 PM
    # we reset the machine using machine.reset()
    # first we select a bun using handle_bun function and passing the "no bun" option
    # and then we select Beef as patty 3 times using for - in range(3). This means we already used 3 patties.
    # and then when we select the 4th patty, we check if the system is throwing an ExceededRemainingChoicesException using the context manager pytest.raises.

# Test 5 - Can add up to 3 toppings of any combination
def test_add_up_to_three_toppings(machine):
    machine.reset()
    machine.handle_bun("no bun")
    machine.handle_patty("next")
    for _ in range(3):
        machine.handle_toppings("lettuce")

    with pytest.raises(ExceededRemainingChoicesException):
        machine.pick_toppings("lettuce")
    # UCID: sk3374@njit.edu
    # Date: 3/16/23 8.40 PM
    # we reset the machine using machine.reset()
    # first we select a bun using handle_bun function and passing the "no bun" option
    # and then we select lettuce as topping 3 times using for - in range(3). This means we already used 3 toppings.
    # and then when we select the 4th topping, we check if the system is throwing an ExceededRemainingChoicesException using the context manager pytest.raises.

# test 6 - cost must be calculated properly based on the choices
def test_calculate_cost(machine):
    #Burger 1
    machine.reset()
    machine.handle_bun("white burger bun") #1.0 
    machine.handle_patty("beef") #1.0
    machine.handle_patty("next") 
    machine.handle_toppings("lettuce") #.25
    machine.handle_toppings("tomato") #.25
    machine.handle_toppings("cheese") #.25    
    machine.handle_toppings("done")

    assert machine.calculate_cost() == 2.75 # to check calculated amount

    machine.handle_pay(machine.calculate_cost(), '$2.75') # to check the currency formatting 

    #Burger 2
    machine.reset()
    machine.handle_bun("wheat burger bun") #1.25
    machine.handle_patty("veggie") #1
    machine.handle_patty("next") 
    machine.handle_toppings("ketchup") #.25
    machine.handle_toppings("mayo") #.25
    machine.handle_toppings("done")
    
    assert machine.calculate_cost() == 2.75

    machine.handle_pay(machine.calculate_cost(), '2.75') #should work even when '$' is not passed

    #Burger 3
    machine.reset()
    machine.handle_bun("lettuce wrap") #1.5
    machine.handle_patty("turkey") #1
    machine.handle_patty("beef") #1
    machine.handle_patty("next")
    machine.handle_toppings("mustard") #0.25
    machine.handle_toppings("done")    
    
    assert machine.calculate_cost() == 3.75
    
    with pytest.raises(InvalidPaymentException):
        machine.handle_pay(machine.calculate_cost(), '4') # should be 3.75 and hence and InvalidPaymentException should be thrown

    # UCID: sk3374@njit.edu
    # Date: 3/16/23 8.50 PM
    # we reset the machine using machine.reset()
    # then we add the bun, patties and toppings using the appropriate handle_bun(), handle_patty() and handle_toppings() functions 
    # after the burger has been made, we use handle_toppings("done") to mark the burger as done
    # Then assert the calculate_cost with the expected amount to see if it is calculating the cost accurately
    # Then we cal handle_pay by passing the calculated amount and the amount the user gives manually 
    # The above step is to check the currency formatting  
    # we repeat this process 3 times. 
    # In the 2nd burger while while in handle_pay we give an amount without the '$' sign and it should work
    # In the 3rd burger while while in handle_pay we involuntarily pass an incorrect amount and so an InvalidPaymentException is raised

# Test 7 - Total Sales (sum of costs) must be calculated properly
def test_total_sales(machine):
    #Burger 1
    machine.reset()
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("Beef")
    machine.handle_patty("next")
    machine.handle_toppings("Lettuce")
    machine.handle_toppings("Tomato")
    machine.handle_toppings("Cheese")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), '2.75')
    assert machine.total_sales == 2.75

    #Burger 2
    machine.reset()
    machine.handle_bun("wheat burger bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("ketchup")
    machine.handle_toppings("mayo")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), '2.75')
    assert machine.total_sales == 5.5

    #Burger 3
    machine.reset()
    machine.handle_bun("Lettuce Wrap") 
    machine.handle_patty("Turkey") 
    machine.handle_patty("Beef")
    machine.handle_patty("next")
    machine.handle_toppings("Mustard") #.25
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), '3.75')
    assert machine.total_sales == 9.25
    # UCID: sk3374@njit.edu
    # Date: 3/16/23 9.00 PM
    # we reset the machine using machine.reset()
    # then we add the bun, patties and toppings using the appropriate handle_bun(), handle_patty() and handle_toppings() functions 
    # after the burger has been made, we use handle_toppings("done") to mark the burger as done
    # The calculate the cost of the burger and send it to the handle_pay function
    # later we assert the value of the the total_sales.
    # we repeat this process 3 times. 
    # 2nd time the total_sales should include the cost of the first burger and the second burger.
    # And in the 3rd time the assert of total_sales would include the total cost of the 3 burgers.

# Test 8 - Total number of burgers that were made should be stored accurately
def test_total_burgers_increment(machine):
    machine.reset()
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("Beef")
    machine.handle_patty("next")
    machine.handle_toppings("Lettuce")
    machine.handle_toppings("Tomato")
    machine.handle_toppings("Cheese")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), '2.75')
    assert machine.total_burgers == 1

    machine.reset()
    machine.handle_bun("Wheat Burger Bun")
    machine.handle_patty("Veggie")
    machine.handle_patty("next")
    machine.handle_toppings("Ketchup")
    machine.handle_toppings("Mayo")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), '2.75')
    assert machine.total_burgers == 2

    machine.reset()
    machine.handle_bun("Lettuce Wrap")
    machine.handle_patty("Turkey")
    machine.handle_patty("Beef")
    machine.handle_patty("next")
    machine.handle_toppings("Mustard")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), '3.75')
    assert machine.total_burgers == 3
    # UCID: sk3374@njit.edu
    # Date: 3/16/23 9.20 PM
    # first we reset the machine.
    # Then we choose the bun, patty and topping using the handle_bun(), handle_patty() and handle_toppings functions.
    # After the burger is made, we mark it as done using the handle_toppings() function
    # Later we calculate the cost of the burger and send it to the handle_pay() function
    # In handle_pay() function we increment the value of the total_burgers by 1 everytime it is called
    # then we assert the value of total_burger witht he expected value.
    # we repeat this process 3 times.
    # each time a new burger is made the value of total_burgers should be incremented by 1.  