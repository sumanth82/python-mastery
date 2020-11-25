with open('test.txt', 'r') as input_file:
    print(input_file.read())
    # .seek() - This takes the cursor to the next line to read and print
    input_file.seek(0)
    print(input_file.read())

# If you don't use with open() method, you close the file using
# file.close()

with open('output.txt', 'a') as output_file:
    text = output_file.write('I\'m writing a letter')
