# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20221518
# Date: 14/12/2022

progress_dict={}
stu_id=''
marks = [120, 100, 80, 60, 40, 20, 0]

mainloop = True
viceloop=True
loop=True

pass_mark = 0
defer_mark = 0
fail_mark = 0

progress_count = 0
trailer_count = 0
exclude_count = 0
retriever_count = 0

credit_pass = 0
credit_defer = 0
credit_fail = 0

credit_list =[]
progress_list=[]


def input_marks():  #to get 3 inputs and validate
    credit_pass = 0
    credit_defer = 0
    credit_fail = 0
    while loop:

        try:
            credit_pass = int(input("\nPlease enter your credit pass: "))
            assert(credit_pass in marks)
            if credit_pass>120:
                print("Out of range")
                continue
            credit_defer = int(input("Please enter your credit defer: "))
            assert (credit_defer in marks)
            if credit_defer>120:
                print("Out of range")
                continue
            credit_fail = int(input("Please enter your credit fail: "))
            assert (credit_fail in marks)
            if credit_fail>120:
                print("Out of range")
                continue
        except ValueError:
            print("Integer Required")
            continue
        except AssertionError:
            print("Out of range")
            continue
        break
    return credit_pass,credit_defer,credit_fail

def check_marks(input1,input2,input3): #to append marks to dictionary
    global progress_count
    global trailer_count
    global exclude_count
    global retriever_count
    while input1 in marks and input2 in marks and input3 in marks:
        if input1 == 120:
            print("Progress")
            progress_dict[stu_id] = (f"Progress - {input1}, {input2}, {input3}")
            loop=False
            break
        elif input1 == 100:
            print("Progress (module trailer)")
            progress_dict[stu_id] =(f"Progress (module trailer) - {input1}, {input2}, {input3}")
            loop = False
            break
        elif input3 >= 80:
            print("Exclude")
            progress_dict[stu_id] =(f"Exclude - {input1}, {input2}, {input3}")
            loop = False
            break
        else:
            print("Module retriever")
            progress_dict[stu_id] =(f"Module retriever - {input1}, {input2}, {input3}")
            loop = False
            break
    else:
        print("out of range")
        loop = False

def userid_check(): #to check the student id is in correct format
    loop=True
    while loop:
        stu_id=input(f"\nEnter the Student ID : ")

        if len(stu_id)!=8:
            print("\nTotal must be 8 charachters")
            continue

        elif stu_id[0]!='w':
            print("\nFirst charactor must be Simple'w'")
            continue
        

        elif stu_id in progress_dict.keys():
            print("\nThe Student ID you entered already exists")
            continue

        try:
            for x in stu_id[1:8]:
                int(x)
        except ValueError:
            print("\nThe last 7 characters should be numbers only")
            continue
        
        return stu_id

def sum_values(input1,input2,input3):#to get total of the 3 marks
    total = input1 + input2 + input3
    return total
    
def list_vals(mark1,mark2,mark3):#insert marks in to list and convert into string
    temp_list=[pass_mark,defer_mark,fail_mark]
    str_list=(str(temp_list))
    return str_list

while viceloop:
    stu_id=userid_check()
    pass_mark,defer_mark,fail_mark = input_marks()
    list_value = list_vals(pass_mark,defer_mark,fail_mark)
    total=sum_values(pass_mark,defer_mark,fail_mark)
    if total !=120:
        print ("Total incorrect")
        continue
    else:

        check_marks(pass_mark,defer_mark,fail_mark)  
        option =input("\nwould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results : ")
        option=option.lower()
        if option == "y":
            continue
        elif option == "q":
            print(f"{'~'*49}")
            for key, val in progress_dict.items():
                print(f"{key} : {val}")
            print(f"{'~'*49}")
            viceloop=False
            break
        else:
            print("Invalid Input")
            continue
