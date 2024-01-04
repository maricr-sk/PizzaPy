def add_toppings():
    yes = True
    p = 0
    num_l = [""] * 3
    check = [0] * 3
    while yes:
        question = input("Add a topping: pepperoni, mushrooms, spinach, or enter 'done'.\n")
        if question.lower() == "pepperoni".lower():
            if check[0] != 1:
                num_l[p] = question.lower()
                p = p + 1
                check[0] = 1
        elif question.lower() == "mushrooms".lower():
            if check[1] != 2:
                num_l[p] = question.lower()
                p = p + 1
                check[1] = 2
        elif question.lower() == "spinach".lower():
            if check[2] != 3:
                num_l[p] = question.lower()
                p = p + 1
                check[2] = 3
        elif question.lower() == "done".lower():
            yes = False
        else:
            print("Error")
            exit(0)

    value = ""
    i = 0
    if p != 0:
        while i < p:
            if i != 0 and p == 3 and i <= p - 1:
                value = value + ", "
            if i != 0 and p > 1 and p != 3:
                value = value + " "
            if p != 1 and i == (p - 1):
                value = value + "and "
            value = value + num_l[i]
            i = i + 1

    if p == 0:
        return value
    else:
        return " with " + value


def choose_pizza():
    answer = input("Small, Medium, or Large?\n")
    return "a " + answer + " pizza" + add_toppings()


def choose_salad():
    answer = input("Garden or Greek salad? \n")
    return "a " + answer + " salad" + choose_dressing()


def choose_dressing():
    answer = input("Choose a dressing: vinaigrette, ranch, blue cheese, or lemon.\n")
    return " with " + answer + " dressing"


def choose_meal():
    question = input("Would you like a pizza or salad?\n")
    b = ""
    check = True
    while check:
        if question.lower() == "pizza".lower():
            b = choose_pizza()
            check = False
        elif question.lower() == "salad".lower():
            b = choose_salad()
            check = False
        else:
            print("Error")
            exit(0)
    return b


def main():
    check = True
    value = ""
    print("Thank you for choosing our restaurant!")
    while check:
        if value == "":
            value = value + choose_meal()
        else:
            value = value + " and " + choose_meal()
        print("Your order contains " + value + ".")
        question = input("Would you like to continue ordering? (yes/no)\n")
        if question.lower() == "yes".lower():
            pass
        elif question.lower() == "no".lower():
            value = value + "."
            check = False
        else:
            print("Error")
            exit(0)
    print("Your order has been placed. Thank you come again!")
    exit(1)


if __name__ == "__main__":
    main()
