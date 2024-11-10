def open_file(file_name, file_mode):
    try:
        with open(file_name, file_mode) as file:
            if file_mode == "r":
                lines_count = sum(1 for _ in file)
                return f"The number of lines in the file: {lines_count}"
            elif file_mode == "rb":
                return "The file is opened in the binary mode"
    except FileNotFoundError:
        return "The file was not found"
    except IOError:
        return "The file could not be opened"


def main():
    while True:
        file_name = input("Enter file name: ")
        mode = input("Enter file reader mode('t' for text, 'b' for binary): ").strip().lower()

        if mode == "t":
            file_mode = "r"
        elif mode == "b":
            file_mode = "rb"
        else:
            print("Invalid mode. Please enter either 't' or 'b'")
            continue

        result = open_file(file_name, file_mode)
        print(result)
        break


if __name__ == '__main__':
    main()
