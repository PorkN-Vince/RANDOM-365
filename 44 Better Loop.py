#Old Style Loop
tasks = ["eat", "code", "sleep"]

counter = 0
for task in tasks:
    print(counter, task)
    counter += 1

#Better Loop

for counter, task in enumerate(tasks):
    print(counter, task)