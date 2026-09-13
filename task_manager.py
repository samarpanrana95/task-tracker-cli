import json
from models.taskModel import Task

def readJson():
    try :
        with open('data.json', 'r') as file:
            content = file.read()
            if (content == ''):
                return []
            # Apparently the cursor moves to the end when file.read() is used and seek fixes it
            file.seek(0)
            existing_data = json.load(file)
            return existing_data
    except:
        return []

def addTask(id_number, description):
    newTask = Task (id_number, description)
    existing_data = readJson()
    existing_data.append(newTask.to_dict())
    with open('data.json', 'w') as file:
        file.write(json.dumps(existing_data, indent=4))
    print(f'Task added successfully (ID: {id_number})')

def updateTask(id_number, description):
    existing_data = readJson()
    task_found = False
    for task in existing_data:
        if (task['id'] == int(id_number)):
            task['description'] = description
            task_found = True
    with open('data.json', 'w') as file:
        file.write(json.dumps(existing_data, indent=4))
    if task_found == True:
        print(f'Task updated successfully (ID: {id_number})')
    else:
        print(f'Failed to find task (ID: {id_number})')

def get_ID():
    existing_data = readJson()
    id_number = 1
    for task in existing_data:
        if task['id'] == id_number:
            id_number = id_number + 1
        else:
            break
    return id_number
