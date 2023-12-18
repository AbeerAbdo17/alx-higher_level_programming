#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    resu_lis = []

    for i in range(list_length):
        try:
            resu_lis.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            resu_lis.append(0)
            print("division by 0")
            continue
        except IndexError:
            resu_lis.append(0)
            print("out of range")
            continue
        except TypeError:
            resu_lis.append(0)
            print("wrong type")
            continue
        finally:
            pass
    return resu_lis
