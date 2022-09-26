def main():
    user_in = input("enter a vanity plate number: ")
    validate(user_in)
def validate(user_in):
    in_len = len(user_in)
    if in_len < 2 or in_len > 6:
        print("invalid")
        return -1
    else:
        if not user_in.isalnum():
            print("invalid")
            return -1
        else:
            for i in range(2):
                if not user_in[i].isalpha():
                    print("invalid")
                    return -1
            for j in range(in_len):
                if not user_in[j].isalpha():
                    continue
                for k in range(j,in_len):
                    if user_in[k].isalpha():
                        print("invalid")
                        return -1
    print("valid")
    return 0
    
main()