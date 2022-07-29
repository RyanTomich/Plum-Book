def str_to_lst(string):
    string = string.replace(" \n" or "\n ", " ")
    string = " ".join(string.split())
    lst = string.split(",")
    lst_final = []
    for i in lst:
        ela = i.strip()
        lst_final.append(ela)
    return lst_final
