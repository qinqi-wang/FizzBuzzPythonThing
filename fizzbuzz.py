def sayOne():
    return 1

def sayOneAndTwo():
    oneAndTwo = [1,2]
    return oneAndTwo

def sayOneTwoThree():
    oneTwoThree = [1,2,3]
    return oneTwoThree

def sayOneToFive():
    oneTwoThree = [1,2,3,4,5]
    return oneTwoThree

def sayOneToTen():
    numbers = []
    for number in range(1,11):
        numbers.append(number)
    return numbers

def sayOneToFifteen():
    numbers = []
    for number in range(1,16):
        numbers.append(number)
    return numbers

def teacher():
    teacherWords = []
    for number in range(1,101):
        teacherWords.append(number)
    return teacherWords

def studentReply(teacherWords):
    studentWords = []
    for word in teacherWords:
        studentWord = threesAndFivesFizzBuzz(word)
        studentWords.append(studentWord)
    return studentWords

def threesAreFizz(number):
    if number == 3:
        return "fizz"
    else:
        return number

def threesAndFivesFizzBuzz(number):
    if number == 3:
        return "fizz"
    elif number == 5:
        return "buzz"
    else:
        return number

def studentReplySmart(teacherWords):
    studentWords = []
    for word in teacherWords:
        if isAFizzNumber(word):
            studentWords.append("fizz")
        elif isABuzzNumber(word):
            studentWords.append("buzz")
        else:
            studentWords.append(word)
    return studentWords

def isAFizzNumber(number):
    if number % 3 == 0:
        return True
    else:
        return False

def isABuzzNumber(number):
    if number % 5 == 0:
        return True
    else:
        return False

def studentReplySmarter(teacherWords):
    studentWords = []
    for word in teacherWords:
        fizzAndOrBuzz = ""
        if isAFizzNumber(word):
            fizzAndOrBuzz += "fizz" 
        if isABuzzNumber(word):
            fizzAndOrBuzz += "buzz"
        if fizzAndOrBuzz:
            studentWords.append(fizzAndOrBuzz)
        else:
            studentWords.append(word)
    return studentWords
