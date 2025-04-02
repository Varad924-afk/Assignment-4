file_name = "output.txt"
try:
    with open(file_name, "w") as file:
        user_input = input("Enter trxt to write to file:\n")
        file.write(user_input + "\n")
        print("Data successfully written to output.txt.")
    with open(file_name, "a") as file:
        additional_input = input("Enter additional text to append: ")
        file.write(additional_input + "\n")
        print("Data successfully appended.")
    with open(file_name, "r") as file:
        print("\nFinal content of output.txt:\n ")
        print(file.read())
except Exception as e:
    print(f"An error occured: {e}")