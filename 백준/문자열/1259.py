
while True:
    num = input()
    if num == "0":
        break;
    
    rev_num = num[::-1]
    if num == rev_num:
        print("yes")
    else:
        print("no")