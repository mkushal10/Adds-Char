# Add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'kiss'
# Expected Result : 'kissing'
# Sample String : 'parking'
# Expected Result : 'parkingly'

def getStringWithIng(input_str):
    # checks the string len greater than three
    if len(input_str) >= 3:
        # checks the string string ends with ing or not
        if 'ing' == input_str[-3:]:
            return input_str + 'ly'
        else:
            return input_str + 'ing'
    return input_str

if __name__ == "__main__":
    in_string = input('Enter the string : ')
    print(getStringWithIng(in_string))
