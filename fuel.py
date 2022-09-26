def main():
    fuel_amt("fraction: ") 
                  
def fuel_amt(prompt):
    while True:
        in_pt = input(prompt)
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
        try:   
            f_right = int(f_right)
            f_left = int(f_left)
            amt = (f_left/f_right) * 100
            break
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
    
    if amt >= 99:
        print("F")
    elif amt <= 1:
        print("E")
    else:
        print(f"{amt:.0f}%")


main()