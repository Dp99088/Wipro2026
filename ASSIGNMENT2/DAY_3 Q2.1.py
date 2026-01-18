#Question 1
def read_numbers_from_file(filename):
    try:
        file = open("files.txt", "r")
        content = file.read()
        file.close()

        print("File Content:")
        print(content)

    except FileNotFoundError:
        print("Error: File not found")

    except PermissionError:
        print("Error: Permission denied")
#
    except Exception as e:
        print("Unexpected error:", e)



filename = "files.txt"

a=read_numbers_from_file(filename)



def write_numbers_to_file(filename):
    try:
        file = open("files.txt","w")

        for i in range(1, 101):
            file.write(str(i) + "\n")

        file.close()
        print("Numbers written successfully")

    except FileNotFoundError:
        print("Error: File not found")

    except PermissionError:
        print("Error: Permission denied")

    except Exception as e:
        print("Unexpected error:", )
a=write_numbers_to_file("files.txt")