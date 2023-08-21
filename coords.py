import pyperclip

badChars = ['°', "'", '"', ","]

while True:
    inputCoords = input("Enter coords: ")
    inputCoords = inputCoords.replace(" ", "")

    for i in range(len(badChars)):
        inputCoords = inputCoords.replace(badChars[i],"|")

    inputCoords = "{{coords|" + inputCoords + "|display=title}}"
    print(inputCoords)
    pyperclip.copy(inputCoords)
    print("Output copied to clipboard.\n")
