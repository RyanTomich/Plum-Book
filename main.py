
def grade_to_honor():
    def add_list():
        if list_num == 1:
            gold_list.append(i)
        if list_num == 2:
            silver_list.append(i)
        if list_num == 3:
            bronze_list.append(i)
        if list_num == 4:
            bug_list.append(i)

    school_string = input("comma seperated 3rd grade")
    print(school_string)
    school_list = school_string.split(",")
    gold_list = []
    silver_list = []
    bronze_list = []
    bug_list = []
    list_num = 0

    for i in school_list:
        add_list()
        if i == " Gold":
            list_num = 1
        if i == " Silver":
            list_num = 2
        if i == " Bronze":
            list_num = 3
        if i == " BUG":
            list_num = 4

    print("honors list")
    print("Gold")
    print(gold_list)
    print("Silver")
    print(silver_list)
    print("Bronze")
    print(bronze_list)
    print("BUG")
    print(bug_list)


grade_to_honor()

print("This is a tes of github!!")


