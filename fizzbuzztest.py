import unittest
from fizzbuzz import *

class FizzBuzzTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(sayOne(), 1)
    
    def testOneAndTwo(self):
        expectedResult = [1,2]
        self.assertEqual(sayOneAndTwo(), expectedResult)

    def testOneTwoThree(self):
        expectedResult = [1,2,"fizz"]
        teacherWords = sayOneTwoThree()
        spokenWords = studentReply(teacherWords)
        self.assertEqual(spokenWords, expectedResult)

    def testOneToFive(self):
        expectedResult = [1,2,"fizz",4,"buzz"]
        teacherWords = sayOneToFive()
        spokenWords = studentReply(teacherWords)
        self.assertEqual(spokenWords, expectedResult)

    def testOneToTen(self):
        expectedResult = [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz"]
        teacherWords = sayOneToTen()
        spokenWords = studentReplySmart(teacherWords)
        self.assertEqual(spokenWords, expectedResult)

    def testOneToFifteen(self):
        expectedResult = [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz", 11, "fizz", 13, 14, "fizzbuzz"]
        teacherWords = sayOneToFifteen()
        spokenWords = studentReplySmarter(teacherWords)
        self.assertEqual(spokenWords, expectedResult)

    def testAllTheWay(self):
        teacherWords = teacher()
        spokenWords = studentReplySmarter(teacherWords)
        print(spokenWords)

if __name__ == '__main__':
    unittest.main()