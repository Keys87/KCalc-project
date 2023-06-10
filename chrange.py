# chrange.py
# a function to make a list of characters in latin alphabet
# takes starting and ending characters as arguments

def chrange(start, end):
    start = ord(start)
    end = ord(end)
    int_range = range(start, end)
    char_list = []
    no_go_strings = ["(", ")", "|", "[", "]", "{", "}", "<", ">"]
    for i in int_range:
        char = chr(i)
        char_list.append(char)
    char_list.append(f"{chr(end)}")
    for x in no_go_strings:
        char_list.append(x)
    return char_list
