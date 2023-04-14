with open("unformated.txt", "r") as f:
    unformatted = f.read()

def newlines_to_n():
    formatted_text = unformatted.replace('\n', '\\n')

    with open("formatted.txt", "a+") as f:
        f.write(formatted_text)
        f.close()
newlines_to_n()
