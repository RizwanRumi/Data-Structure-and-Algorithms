# problem string reverse
print('--------string reverse----------')

def string_reverser(our_string):
    new_string = ""

    for i in range(len(our_string)):
        # Grab the charecter from the back of the string and add them to the new string
        new_string += our_string[(len(our_string)-1)-i]

    # Return our solution
    return new_string


# Test Cases

print("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
print("Pass" if ('3432 :si edoc each ehT' == string_reverser('The house code is: 2343')) else "Fail")


# problem anagram
print('-------------Anagram-----------')

def anagram_checker(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Compare the length of both strings
    if len(str1) == len(str2):
        # Sort each string and compare
        if sorted(str1) == sorted(str2):
            return True

    return False


print("Pass" if not (anagram_checker('water', 'waiter')) else "Fail")
print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")
print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")
print("Pass" if anagram_checker('Time and tide wait for no man', 'Notified madman into water') else "Fail")
print("Pass" if (anagram_checker('rat', 'art')) else "Fail")


# problem word flipper
print('----------------Word Flipper----------------')

def word_flipper(our_string):

    word_list = our_string.split(" ")

    for idx in range(len(word_list)):
        # print('before: ', format(word_list[idx]))
        word_list[idx] = word_list[idx][::-1]
        # print('after: ', format(word_list[idx]))

    return " ".join(word_list)

# word_flipper('sihT si na elpmaxe')

print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")


# problem Hamming distance : The Hamming distance between two strings of equal length is the number of positions at
# which the corresponding symbols are different.

def hamming_distance(str1, str2):

    if len(str1) == len(str2):
        count = 0

        for char in range(len(str1)):
            if str1[char] != str2[char]:
                count += 1

        return count

    return None


print("Pass" if (10 == hamming_distance('ACTTGACCGGG','GATCCGGTACA')) else "Fail")
print("Pass" if  (1 == hamming_distance('shove','stove')) else "Fail")
print("Pass" if  (None == hamming_distance('Slot machines', 'Cash lost in me')) else "Fail")
print("Pass" if  (9 == hamming_distance('A gentleman','Elegant men')) else "Fail")
print("Pass" if  (2 == hamming_distance('0101010100011101','0101010100010001')) else "Fail")


