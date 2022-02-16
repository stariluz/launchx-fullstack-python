def main():
    try:
        configuration=open("config.txt")
    except FileNotFoundError:
        print("Coldn't find the config.txt file!")

if __name__=='__main__':
    main()