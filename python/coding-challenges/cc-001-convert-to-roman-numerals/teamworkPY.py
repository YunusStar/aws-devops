print( " This program converts decimal numbers to Roman Numerals ###\
          \n To exit the program, please type 'exit'")

while True:
    number =input("\nPlease enter a number between 1 and 3999, inclusively: ")    
    if not number.isnumeric(): 
        if number.lower() == "exit":
            print("\nExiting the program... Good Bye")
            break
        elif type(number) == str :
            print("\nNot Valid Input")
    elif int(number) < 1 or int(number) > 3999:
        print("\nNot Valid Input")
    elif int(number) > 1 or int(number) < 3999:
        string_index = len(number)
        outputlist = []
        int_number = int(number[-1])
        if int_number < 4 :
            result = "I"* int_number
        elif int_number == 4 :
            result = (5-int_number)* "I" + "V"
        elif int_number == 5 :
            result = "V"
        elif int_number > 5 and int_number < 9 :
            result = "V" + (int_number-5)*"I"
        elif int_number == 9 :
            result = "IX"
        outputlist.append(result)
        if string_index > 1 :
            sec_number = int(number[-2])
            if sec_number < 4 :
                result_2 = sec_number * "X"
            elif sec_number == 4 :
                result_2 = "XL"
            elif sec_number == 5 :
                result_2 = "L"
            elif sec_number > 5 and sec_number < 9 :
                result_2 = "L" + (sec_number-5)*"X"
            elif sec_number == 9 :
                result_2 = "XC"
            outputlist.append(result_2)
        if string_index > 2 :
            third_number = int(number[-3])
            if third_number < 4 :
                result_3 = third_number * "C"
            elif third_number == 4 :
                result_3 = "CD"
            elif third_number == 5 :
                result_3 = "D"
            elif third_number >5 and third_number < 9 :
                result_3 = "D" + (third_number-5)*"C"
            elif third_number == 9 :
                result_3 = "CM"
            outputlist.append(result_3)
        if string_index > 3 :
            forth_number = int(number[-4])
            result_4 = "M" * forth_number
            outputlist.append(result_4)
        for i in reversed(outputlist):
            print(i,sep="", end="")
            outputlist = []
    else:
        print("\nNot Valid Input!!")
