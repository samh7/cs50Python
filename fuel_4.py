while True:
    in_pt = input("what is the value: ")
    in_len = len(in_pt)
    f_left = ""
    f_right = ""
    for i in range(in_len):
        if in_pt[i] == "/":
            break
        f_left += in_pt[i]
    for j in range(in_len):
        if in_pt[j] == "/":                       
            for k in range(j+1,in_len,1):
                f_right+= in_pt[k]                    
    f_right = int(f_right)
    f_left = int(f_left)
    
    try:   
        amt = f_left/f_right
        
    except ZeroDivisionError:
        pass