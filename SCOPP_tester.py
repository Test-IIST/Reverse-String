import StudentCode;
def test(*args, testIO , expectedIO) -> bool:
    result = (StudentCode.runner(testIO,*args)).isEquals(expectedIO)
    if testIO.is_outBuffer_empty():
        return False
    return result
