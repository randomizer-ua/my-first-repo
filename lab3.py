# Лабораторна робота 3
# Я виконую варіант №18

first_comp = int(input("Enter the first component: "))
last_comp = int(input("Enter the last component: "))

def never_return_5(first_comp, last_comp):
    current_comp = first_comp
    count_var = 0

    while current_comp <= last_comp:
        if "5" not in str(current_comp):
            print("This number doesn't have a 5:", current_comp)
            count_var += 1

        current_comp += 1

    return count_var

count_var = never_return_5(first_comp, last_comp)
print(f"Amount of numbers that don't have a 5 in them: {count_var}")