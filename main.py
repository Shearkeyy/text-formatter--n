with open("unformated.txt", "r") as f:
    unformatted = f.read()

# Replace newline characters with '\n'

def newlines_to_n():
    #formatted = unformatted.replace("\n", "\\n")
    #formatted = [s.replace("\n", "\\n") for s in unformatted]
    #output_string = "\n".join(unformatted)
    formatted_text = unformatted.replace('\n', '\\n')
    print("hello\nhi\nhow're")

# Print the formatted text
    print(formatted_text)

    # Replace all instances of "\n" with "\\n"
    #output_string = output_string.replace("\n", "\\n")

    with open("formatted.txt", "a+") as f:
        f.write(formatted_text)
        f.close()
newlines_to_n()