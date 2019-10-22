import os
import sys

def problem_one(word):
    return word[::-1]

def problem_two(sentence):
    return sentence.split()

def problem_three(num, word_list):
    if num in word_list:
        return True
    else:
        return False

def problem_four(num):
    sum = 0
    for i in range(1, num + 1):
        sum = sum + i

    return sum

def problem_five(list1, list2):
    combine_list = list1 + list2
    return list(dict.fromkeys(combine_list))

def problem_six(radius):
    return (radius**2) * 3.1415

def problem_seven(io_word):
    f = open("name.txt", "w")
    f.write(io_word)
    f.close()
    send_word = None

    with open("name.txt", "r") as f:
        send_word = f.read(10)
    os.remove("name.txt")
    return send_word

def problem_eight(word_repeat, letter):
    sum = 0
    for i in range(0, len(word_repeat)):
        if word_repeat[i] == letter:
            sum += 1
    return sum

def problem_nine():
    return sys.version

def problem_ten(list_of_emails):
    domainList = []
    for i in range(0, len(list_of_emails)):
        tempname = (list_of_emails[i].split("@"))
        domainList.append(tempname[1])

    return domainList


if __name__ == '__main__':
    word = "hello"
    number = 9
    radius = 7
    sentence = "the quick brown fox jumps over the lazy dog"
    num_list = [1,2,3,4,5,6,7,8,9,0]
    list1 = ["a", "b", "c", "d"]
    list2 = ["c", "d", "e", "f", "g"]
    emaillist = ["dhunt@gmail.com", "chunt@yahoo.com", "hunt.dar@husky.neu.edu", "dhunt@brooksschool.org"]
    print(problem_one(word))
    print(problem_two(sentence))
    print(problem_three(1, num_list))
    print(problem_four(number))
    print(problem_five(list1, list2))
    print(problem_six(radius))
    print(problem_seven("Darin"))
    print(problem_eight("dbndfirbfirufirunfrnn", "n"))
    print(problem_nine())
    print(problem_ten(emaillist))

    """with open("jsondatanew.json", 'r') as f:
        ...: datastore = json.load(f)
    """

