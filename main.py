
def auth():
    print("Authenticating...")
    return True

def main():
    if auth():
        print("Welcome to the main function!")
    else:
        print("Authentication failed!")
    return

if __name__ == "__main__":
    main()