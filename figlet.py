from pyfiglet import figlet_format
import sys

def main():
    if len(sys.argv) == 2:
        print("Invalid argument(s)")
        sys.exit()
    elif len(sys.argv)  == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            sys_in = sys.argv[2]
            try:
                user_in = input("Input: ")
                print(figlet_format(f"{user_in}", font=sys_in))   
                sys.exit()
            except:
                print("Font Not Found!")
                sys.exit()
        else:
            print("Invalid argument(s)")
            sys.exit
    user_in = input("Input: ")
    print(figlet_format(f"{user_in}"))
            
main()