# Demonstrating basic file handling in Python

def handle_file():
    filename = "myfile.txt"

    # Step 1: Create and write initial content
    with open(filename, "w") as f:
        f.write("Hello! This is the first line.\n")
        f.write("Here's another line to start with.\n")
    print("Initial content written to the file.")

    # Step 2: Read and display the file's content
    with open(filename, "r") as f:
        content = f.read()
        print("\nReading the file content:")
        print(content)

    # Step 3: Add more lines to the file
    with open(filename, "a") as f:
        f.write("Adding one more line at the end.\n")
    print("\nNew content appended successfully.")

    # Step 4: Read the file again to see the changes
    with open(filename, "r") as f:
        updated_content = f.read()
        print("\nFile content after appending:")
        print(updated_content)

if __name__ == "__main__":
    handle_file()
    