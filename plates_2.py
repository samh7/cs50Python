def main():
    user_in = input("what up?")
    validate(user_in)
def validate(user_in):
    in_len = len(user_in)
    if in_len < 2 or in_len > 6:
        print("invalid plate number")
        return
    for i in range(2):
        if not user_in[i].isalpha():
            print("invalid plate number")
            return
    if not user_in.isalnum():
        print("invalid plate number")
        return
    for i in range(2,in_len):
        if i+1 == in_len:
            break
        if user_in[i].isdigit() and user_in[i+1].isalpha():
            print("invalid  plate number")
            return    
    print("valid")
    

main()