# define a list
stu_list = []


def menu():
    print("///////////////////////////////////")
    print(" Please select a number")
    print(" 1.Add student data")
    print(" 2.Del student data")
    print(" 3.Update student data")
    print(" 4.Search a student")
    print("///////////////////////////////////")


# add a student info
def add_student():
    # GLOBAL PARAM
    global stu_list
    # input value
    name = input("Please enter student's name: ")
    score = int(input("Please enter his/her grade: "))
    # for loop to verify the data
    for stu in stu_list:
        if stu["name"] == name:
            print("Already existed in the system！")
            return
    student = {
        "name": name,
        "score": score
    }
    stu_list.append(student)
    print("Success adding a student info!")


# del student info
def del_student():
    global stu_list
    # input a name
    name = input("please enter a name to delete: ")
    for stu in stu_list:
        if stu["name"] == name:
            # remove an info from dic
            stu_list.remove(stu)
            print("Deleted")
            return None
    print("Sorry, you provide a wrong name!")


# update info
def update_student():
    global stu_list
    name = input("Please enter a student name you want to update: ")
    for stu in stu_list:
        if stu["name"] == name:
            # modified
            stu["name"] = input("Please enter a new name: ")
            stu["score"] = input("Please enter a new grade: ")
            print("Success！")
    print("Sorry, the student does not exist in the system! ")


# Search info
def search_student():
    global stu_list
    name = input("Please enter a name to search: ")
    for stu in stu_list:
        if stu["name"] == name:
            print("name: %s\n grade: %d " % (stu["name"], stu["score"]))
            return None
    print("Sorry, the student does not exist in the system!")
    return None


# 定义流程主函数
def main():
    while True:
        menu()
        chose = int(input("Please enter a number to continue: "))
        if chose == 1:
            add_student()
            print(stu_list)
        elif chose == 2:
            del_student()
            print(stu_list)
        elif chose == 3:
            update_student()
            print(stu_list)
        elif chose == 4:
            search_student()
            print(stu_list)
        else:
            print("Error, please enter again!")
            continue
    return None


main()
