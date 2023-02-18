from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    
    task = TASK_TEMPLATE.copy() # don't delete this
    task['name'] = name.strip()# set the name, description, and due date (all must be provided)
    task['description'] = description.strip()

    try:
        task['due'] = str_to_datetime(due.strip()) # due date must match one of the formats mentioned in str_to_datetime()
    except ValueError:
        print("Invalid Date format. The date should be in the format mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss")
        
    task['lastActivity'] = datetime.now() # update lastActivity with the current datetime value

    tasks.append(task)# add the new task to the tasks list
    print("New task added to the tasklist sucessfully") # output a message confirming the new task was added or if the addition was rejected due to missing data    
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution

    # UCID: sk3374
    # Date: Feb 16, 7:32 PM
    # Solution: 
    # inserted the appropriates values into the dictionary using the relavent key
    # also removed the whitespaces leading and trailing whitespaces
    # and called str_to_datetime funtion to convert the string to date and then insert to lastActivity
    save()

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # get the task by index
    try: 
        task = tasks[index]
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    except IndexError:
        print("Invalid index. Please enter a valid index.")
    
    # show the existing value of each property where the TODOs are marked in the text of the inputs (replace the TODO related text)
    print(f"Updating task '{task['name']}'")
    print(f"Current description: '{task['description']}'")
    print(f"Current due date: '{task['due']}'")

    # UCID: sk3374
    # Date: Feb 16, 8:10 PM
    # The function first tries to get the task by the given index and checks for any index out of bounds scenarios.
    # If the index is not valid, it prints a message and returns.
    # If the index is valid, it shows the existing value of each property where the TODOs are marked in the text of the inputs. 
    # Then it prompts the user for the updated values of the name, description, and due date of the task. 
    # Finally, it passes the updated task properties to the update_task function. 

    name = input(f"What's the name of this task? (TODO name) \n").strip()
    desc = input(f"What's a brief descriptions of this task? (TODO description) \n").strip()
    due = input(f"When is this task due (format: m/d/y H:M:S) (TODO due) \n").strip()
    update_task(index, name=name, description=desc, due=due)

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    
    # Find the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    try:
        task = tasks[index]
    except IndexError:
        print("Invalid index. Please enter a valid index.")
        return
    
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    if name:
        task['name'] = name
    if description:
        task['description'] = description
    if due:
        task['due'] = datetime.strptime(due, "%m/%d/%y %H:%M:%S")
    
    # update lastActivity with the current datetime value
    task['lastActivity'] = datetime.now()

    # output that the task was updated if any items were changed, otherwise mention task was not updated
    if name or description or due:
        print(f"Task with index {index} was updated.")
    else:
        print(f"Task with index {index} was not updated.")

    # make sure save() is still called last in this function

    # UCID: sk3374
    # Date: Feb 16, 8:23 PM 
    # We first try to find the task with the given index. If it doesn't exist, we print an appropriate error message and return.
    # We then update the task data with the incoming data if it was provided. We check if each property was provided, and if it was, we update the corresponding property of the task. If it wasn't provided, we use the original task property value.
    # We update the lastActivity property of the task with the current datetime value.
    # We output a message indicating if the task was updated or not, depending on whether any items were changed.
    save()

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    try:
        task=tasks[index]
    except IndexError:
        print(f"Task with index {index} does not exist.")
        return

    # if it's not done, record the current datetime as the value
    if not task['done']:
        task['done'] = True
    # if it is done, print a message saying it's already completed
    else:        
        print(f"Task with index {index} had been marked done already.")        
    
    # UCID: sk3374
    # Date: Feb 16, 8:35 PM
    # Solution: 
    # We first try to find the task with the given index. If it doesn't exist, we print an appropriate error message and return.
    # If the task exists and it has been already marked done, we send a message to the user saying its already marked done.
    # Else, we mark it done
    save()

def view_task(index):
    """ View more info about a specific task fetch by index """
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    try:
        task=tasks[index]
    except IndexError:
        print(f"Task with index {index} does not exist.")
        return

    # utilize the given print statement when a task is found

    # UCID: sk3374
    # Date: Feb 17, 7:30 pm 
    # added code to handle an invalid index by catching the IndexError and printing an error message
    # If the index is valid, I use the given print statement to print the task number
    # then we print the task information using f-strings and the given format
    # later we use a replace() call to remove any double spaces that may appear in the output
    print(f"""
        [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
        Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))

def delete_task(index):
    """ deletes a task from the tasks list by index """
    
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    try:
        task=tasks[index]
    except IndexError:
        print(f"Task with index {index} does not exist.")
        return

    try: 
    # delete/remove task from list by index
        task = tasks.pop(index)
    # Print a success message
        print(f"Task '{task}' at index {index} successfully deleted.")
    except:
    # message should show if it was successful or not
        print(f"Task '{task}' at index {index} could not be deleted.")
    save()
    
    # make sure save() is still called last in this function
    
    # UCID: sk3374
    # Date: Feb 17, 7:47 pm 
    # First we get the task by index. IF index invalid, let user know
    # We delete the give task using pop. Also added error handling for this delete

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    _tasks = [task for task in tasks if not task["done"]]
    list_tasks(_tasks)
    # Include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # UCID: sk3374
    # Date: Feb 17, 7:55 pm
    # got all the incomplete tasks whose done is not marked to true
    # then displayed all those fetched tasks using list_tasks function

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than now and that are not complete
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    _tasks = [task for task in tasks if not task["done"] and str_to_datetime(str(task["due"])) < datetime.now()]
    list_tasks(_tasks)    
    # Include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # UCID: sk3374
    # Date: Date: Feb 17, 8:13 pm 
    # We fetch the tasks where stats done is not marked and the due value is less than current timestamp
    # then displayed all those fetched tasks using list_tasks function

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    try:
        task = tasks[index]    
    except: 
        print("Invalid index. Please enter a valid index.")
        return
    # get the days, hours, minutes, seconds between the due date and now
    #due = datetime.strptime(task["due"], '%Y-%m-%d')
    due = str_to_datetime(str(task["due"]))
    time_remaining = due - datetime.now()
    
    # display the remaining time via print in a clear format showing days, hours, minutes, seconds
    if time_remaining.total_seconds() <= 0:
        # If the due date is in the past, print out how many days, hours, minutes, seconds the task is overdue
        overdue_time = datetime.now() - due
        print(f"Task '{task['name']}' is {overdue_time.days} days, {overdue_time.seconds//3600} hours, {(overdue_time.seconds//60)%60} minutes, and {overdue_time.seconds%60} seconds overdue.")
    else:
        # Otherwise, print out the time remaining until the task is due
        print(f"Task '{task['name']}' is due in {time_remaining.days} days, {time_remaining.seconds//3600} hours, {(time_remaining.seconds//60)%60} minutes, and {time_remaining.seconds%60} seconds.")
    # UCID: sk3374
    # Date: Date: Feb 17, 8:13 pm 
    # We fetch the tasks where stats done is not marked and the due value is less than current timestamp
    # then displayed all those fetched tasks using list_tasks function

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()