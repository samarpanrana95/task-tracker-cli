from models.taskModel import Task
from task_manager import addTask, readJson, get_ID, updateTask, deleteTask, mark_in_progress, mark_done, list
import sys

all_arguments = sys.argv
if (len(all_arguments) > 4):
    print("Too many arguments")
    sys.exit()
elif (len(all_arguments) <= 1):
    print("Provide more arguments.")
    sys.exit()
else:
    action = all_arguments[1]
    if ((action != 'add') and (action != 'update') and (action != 'delete') and (action != 'list') and (action != 'mark-in-progress') and (action != 'mark-done')):
        print("Use a valid command, add or update or delete or list or mark-done or mark-in-progress")
        sys.exit()

match action:
    case 'add':
        if (len(all_arguments) != 3):
            print("Provide one task for adding at a time.") 
            sys.exit()
        task_description = all_arguments[2]
        if (task_description == ''):
            print("Provide a meaningful task.") 
            sys.exit()
        id_number = get_ID()
        addTask(id_number, task_description)
    case 'update':
        if (len(all_arguments) != 4):
            print("Provide one task for updating at a time.") 
            sys.exit()
        task_id = all_arguments[2]
        task_description = all_arguments[3]
        if (task_description == ''):
            print("Provide a meaningful task.") 
            sys.exit()
        updateTask(task_id, task_description)
    case 'delete':
        if (len(all_arguments) != 3):
            print("Provide one task for deleting at a time.") 
            sys.exit()
        task_id = all_arguments[2]
        try:
            int(task_id) > 0
        except:
            print("Provide a correct id.") 
            sys.exit()
        deleteTask(task_id)
    case 'mark-in-progress':
        if (len(all_arguments) != 3):
                print("Provide one task for marking at a time.") 
                sys.exit()
        task_id = all_arguments[2]
        try:
                int(task_id) > 0
        except:
                print("Provide a correct id.") 
                sys.exit()
        mark_in_progress(task_id)
    case 'mark-done':
        if (len(all_arguments) != 3):
                print("Provide one task for marking at a time.") 
                sys.exit()
        task_id = all_arguments[2]
        try:
                int(task_id) > 0
        except:
                print("Provide a correct id.") 
                sys.exit()
        mark_done(task_id)
    case 'list':
        listing_type = ''
        if (len(all_arguments) == 2):
            listing_type = 'normal'
        elif (len(all_arguments) == 3 and (all_arguments[2] == 'done') or (all_arguments[2] == 'todo') or (all_arguments[2] == 'in-progress')):
            listing_type = all_arguments[2]
        else:
            print('For all listings, use only list. For listing done or todo or in-progress, use list done, list todo, list in-progress respectively.')
            sys.exit()
        list(listing_type)