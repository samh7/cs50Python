def main():
    user_in = str(input("what's up? "))
    print(twttr(user_in))
def twttr(user_in):
    in_len = len(user_in)
    tmp_in = ""
    for i in range(in_len):
        if (user_in[i] == 'a') or (user_in[i] == 'e') or (user_in[i] == 'i') or (user_in[i] == 'o') or (user_in[i] == 'u'):
            continue
        tmp_in += user_in[i]

    return tmp_in

main()