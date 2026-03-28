from todo import add_task, list_tasks,remove_last_task,count_tasks

add_task("Initial task by A")

tasks = list_tasks()
for t in tasks:
    print(t)
    
add_task("B: buy groceries")

add_task("A: clean room")

remove_last_task()
add_task("B: replaced last task")

print("Run by A")
print("Run by B")

print("Total tasks:", count_tasks())