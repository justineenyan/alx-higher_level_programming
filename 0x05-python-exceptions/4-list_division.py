#!/usr/bin/python3
# A function that divides element by element 2 lists.
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (TypeError):
            print("Wrong type")
        except (IndexError):
            print("Out of range")
        finally:
            result.append(div)
    return result
