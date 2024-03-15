# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20221518
# Date: 14/12/2022

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

total_outcomes = 0

credit_list =[]
progress_list=[]

def input_marks(): #to get 3 inputs and validate
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

def check_marks(input1,input2,input3): #to append marks to list and get count for histogram
    global progress_count
    global trailer_count
    global exclude_count
    global retriever_count
    while input1 in marks and input2 in marks and input3 in marks:
        if input1 == 120:
            print("Progress")
            progress_list.append(f"Progress - {input1}, {input2}, {input3}")
            progress_count += 1
            loop=False
            break
        elif input1 == 100:
            print("Progress (module trailer)")
            progress_list.append(f"Progress (module trailer) - {input1}, {input2}, {input3}")
            trailer_count += 1
            loop = False
            break
        elif input3 >= 80:
            print("Exclude")
            progress_list.append(f"Exclude - {input1}, {input2}, {input3}")
            exclude_count += 1
            loop = False
            break
        else:
            print("Module retriever")
            progress_list.append(f"Module retriever - {input1}, {input2}, {input3}")
            retriever_count += 1
            loop = False
            break
    else:
        print("out of range")
        loop = False

def text_file(): #to create and write inside textfile
    file=open("progress.txt","a")
    for i in progress_list:
        file.write(i)
        file.write("\n")
    file.close()

def sum_values(input1,input2,input3): #to get total of the 3 marks
    total = input1 + input2 + input3
    return total

def histrograme(): #to print histrogram
    print("-" * 65)
    print(" Histogram")
    print(f"Progress {progress_count:<5} {':'} {'* ' * progress_count}")
    print(f"Trailer {trailer_count:<6} {':'} {'* ' * trailer_count}")
    print(f"Retriever {retriever_count:<4} {':'} {'* ' * retriever_count}")
    print(f"Excluded {exclude_count:<5} {':'} {'* ' * exclude_count}")
    print(f"\n{total_outcomes} outcomes in total")
    print("-" * 65)

def list_vals(mark1,mark2,mark3): #insert marks in to list and convert into string
    temp_list=[pass_mark,defer_mark,fail_mark]
    str_list=(str(temp_list))
    return str_list



while mainloop:
    print('\n'+"-Main menu-".center(55)+'\n'+str('~'*55))
    print(f"/\tInput '1'\t For Student version{' '*10}/\n\\\tInput '2'\t For Staff version{' '*12}\\\n/\tInput 'q or Q'\t To exit{' '*22}/\n{'~'*55}")
    main_option=input("Enter the version you want : ")
    main_option=main_option.lower()
    if main_option=='1':
        print(f"\n{'-'*20}Student version{'-'*20}")
        pass_mark,defer_mark,fail_mark = input_marks()
        list_value = list_vals(pass_mark,defer_mark,fail_mark)
        total=sum_values(pass_mark,defer_mark,fail_mark)
        if total !=120:
            print ("Total incorrect")
            continue
        else:
            check_marks(pass_mark,defer_mark,fail_mark)
            progress_list.clear()

    elif main_option=='2':
        viceloop=True
        while viceloop:
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
                    total_outcomes = progress_count + trailer_count + exclude_count +  retriever_count
                    histrograme()
                    for i in progress_list:
                        print(i)
                    text_file()
                    print(f"\nText file created\n<--Going back to main menu")
                    viceloop=False
                    break
                else:
                    print("Invalid Input")
                    continue
    elif main_option=='q':
        print("\nThe program exits !")
        mainloop=False
        break
    else:
        print("\nPlease check your input again")
        continue