def f():
    while True:
        arm = str(input("Введите число для проверки\n"))
        k = 0
        for i in range(len(arm)):
            k+=int(arm[i])**len(arm)
        if k == int(arm):
            print("Число является числом Армстронга")
        else: print("Число не является числом Армтстронга")
        print("\n")
f()
