def den():
    for p, i in students.items():
        print("-"*30)
        print(f"{p} решил: ")
        for tasks in i:
            print(f"\t-{tasks}")
students ={ 
    'Kirill':['task1', 'task2', 'task3', 'task4', 'task5', 'task6', 'task7', 'task8' ,'task9'],
    'Renat':['task1', 'task2', 'task3', 'task4'],
    'Vania': ['task1'],
    'Yaroslav':['task1', 'task2', 'task3', 'task4', 'task5']
    }
den()
