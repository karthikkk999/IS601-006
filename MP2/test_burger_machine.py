import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
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

# Test 4 - Can add up to 3 patties of any combination
def test_add_up_to_three_patties(machine):
    machine.reset()
    machine.handle_bun("no bun")
    for _ in range(3):
        machine.handle_patty("Beef")

    with pytest.raises(ExceededRemainingChoicesException):
        machine.pick_patty("beef")

# Test 5 - Can add up to 3 toppings of any combination
def test_add_up_to_three_toppings(machine):
    machine.reset()
    machine.handle_bun("no bun")
    machine.handle_patty("next")
    for _ in range(3):
        machine.handle_toppings("lettuce")

    with pytest.raises(ExceededRemainingChoicesException):
        machine.pick_toppings("lettuce")

# test 6 - cost must be calculated properly based on the choices
def test_calculate_cost(machine):
    machine.reset()
    machine.handle_bun("white burger bun") #1.0 
    machine.handle_patty("beef") #1
    machine.handle_patty("next") #1
    machine.handle_toppings("lettuce") #.25
    machine.handle_toppings("tomato") #.25
    machine.handle_toppings("cheese") #.25
    
    assert machine.calculate_cost() == 2.75

    machine.reset()
    machine.handle_bun("wheat burger bun") #1.25
    machine.handle_patty("veggie") #1
    machine.handle_patty("next") #1
    machine.handle_toppings("ketchup") #.25
    machine.handle_toppings("mayo") #.25
    
    assert machine.calculate_cost() == 2.75

    machine.reset()
    machine.handle_bun("lettuce wrap")
    machine.handle_patty("turkey")
    machine.handle_patty("beef")
    machine.handle_patty("next") #1
    machine.handle_toppings("mustard")

    assert machine.calculate_cost() == 3.75

# Test 7 - Total Sales (sum of costs) must be calculated properly
def test_total_sales(machine):
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("Beef")
    machine.handle_patty("next")
    machine.handle_toppings("Lettuce")
    machine.handle_toppings("Tomato")
    machine.handle_toppings("Cheese")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), str(machine.calculate_cost()))
    assert machine.total_sales == 2.75

    machine.reset()
    machine.handle_bun("wheat burger bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("ketchup")
    machine.handle_toppings("mayo")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), str(machine.calculate_cost()))
    assert machine.total_sales == 5.5

    machine.reset()
    machine.handle_bun("Lettuce Wrap") 
    machine.handle_patty("Turkey") 
    machine.handle_patty("Beef")
    machine.handle_patty("next")
    machine.handle_toppings("Mustard") #.25
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), str(machine.calculate_cost()))
    assert machine.total_sales == 9.25

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
    machine.handle_pay(machine.calculate_cost(), str(machine.calculate_cost()))
    assert machine.total_burgers == 1

    machine.reset()
    machine.handle_bun("Wheat Burger Bun")
    machine.handle_patty("Veggie")
    machine.handle_patty("next")
    machine.handle_toppings("Ketchup")
    machine.handle_toppings("Mayo")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), str(machine.calculate_cost()))
    assert machine.total_burgers == 2

    machine.reset()
    machine.handle_bun("Lettuce Wrap")
    machine.handle_patty("Turkey")
    machine.handle_patty("Beef")
    machine.handle_patty("next")
    machine.handle_toppings("Mustard")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), str(machine.calculate_cost()))
    assert machine.total_burgers == 3