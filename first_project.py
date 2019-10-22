import os
import sys


def problem_one(word_full):
    """
    Uses a simple method to reverse a string
    :param word_full: string input
    :return: 'word_full' in reverse
    """
    return word_full[::-1]


def problem_two(sentence_full):
    """
    Splits a sentence with the space as delimiter and adds each element to a list
    :param sentence_full: sentence to be split
    :return: a list of words in the sentence represented
    as individual elements of a list
    """
    return sentence_full.split()


def problem_three(num, word_list):
    """
    :param num: number to be checkec
    :param word_list: list of numbers
    :return: boolean, true if num is in word_list
    """
    if num in word_list:
        return True
    else:
        return False


def problem_four(num):
    """
    For loop that iterates from 1 to the number (have to do + 1 in range) and adds i every time
    :param num: number to be iterated over
    :return: the sum of 0 to num
    """
    sum = 0
    for i in range(1, num + 1):
        sum = sum + i

    return sum


def problem_five(list_1, list_2):
    """
    Combines the two lists, then turns them into a dictionary which only allows one key, hence removing duplicates
    then turns it back into a list
    :param list_1: list of numbers
    :param list_2: list of numbers
    :return: a combined list with duplicates removed
    """
    combine_list = list_1 + list_2
    return list(dict.fromkeys(combine_list))


def problem_six(radius_input):
    """
    Squares the radius and multiplies it by pi
    :param radius_input: radius of a circle
    :return: area of a circle with radius = radius_input
    """
    return (radius_input**2) * 3.1415


def problem_seven(io_word):
    """
    Makes a file called 'name.txt', writes the word to it, closes, then opens it again and reads the word,
    then uses the os to remove the file
    :param io_word: word to be put in the 'name.txt' file
    :return: the word read from the file
    """
    f = open("name.txt", "w")
    f.write(io_word)
    f.close()

    with open("name.txt", "r") as f:
        send_word = f.read(10)
    os.remove("name.txt")
    return send_word


def problem_eight(word_repeat, letter):
    """
    Same logic as problem three but now if there is an instance of the chosen number it adds to counter
    :param word_repeat: string with letters
    :param letter: letter
    :return: how many times letter exists in the string
    """
    summation = 0
    for i in range(0, len(word_repeat)):
        if word_repeat[i] == letter:
            summation += 1
    return summation


def problem_nine():
    """
    Uses sys library to get the version of python
    :return: version of python
    """
    return sys.version


def problem_ten(list_of_emails):
    """
    Takes in a list of emails and splits by using the '@' as the delimiter and takes the second half of the split
    which will be the domain
    :param list_of_emails: a list of email addresses
    :return: the domains to all the email addresses
    """
    domain_list = []
    for i in range(0, len(list_of_emails)):
        temp_name = (list_of_emails[i].split("@"))
        if temp_name[1] not in domain_list:
            domain_list.append(temp_name[1])

    return domain_list


if __name__ == '__main__':
    word = "hello"
    number = 10
    radius = 7
    sentence = "the quick brown fox jumps over the lazy dog"
    num_list = [1,2,3,4,5,6,7,8,9,0]
    list1 = ["a", "b", "c", "d"]
    list2 = ["c", "d", "e", "f", "g"]
    email_list = ["dhunt@gmail.com", "chunt@yahoo.com",
                  "hunt.dar@husky.neu.edu", "dhunt@brooksschool.org", "darin@gmail.com"]
    print(problem_one(word))
    print(problem_two(sentence))
    print(problem_three(1, num_list))
    print(problem_four(number))
    print(problem_five(list1, list2))
    print(problem_six(radius))
    print(problem_seven("Darin"))
    print(problem_eight("darin hunt", "n"))
    print(problem_nine())
    print(problem_ten(email_list))
