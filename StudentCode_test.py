import SCOPP_tester;
from IOWrapper import IOWrapper
testIO = IOWrapper()
expectedIO = IOWrapper()


def test_hello():
    expectedList = ["!dlroW ,olleH", "nuf si nohtyP", "54321"]
    testList = ["Hello, World!", "Python is fun", "12345"]
    i=0
    for expected in expectedList:
        testArg = testList[i]                                                                  # use these lOCs while using list object
        print("Testing: Test case",testArg,"Expected",expected)
        #print("Testing: Test case","Expected",expected)
        expectedIO.print(expected)
        assert SCOPP_tester.test(testArg ,testIO = testIO,expectedIO = expectedIO)
        #assert SCOPP_tester.test(testIO = testIO,expectedIO = expectedIO)
        i+=1
        print("Test case Passed")
    print("Code is correct.All Test cases passed")
