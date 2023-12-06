"""
William Beeker
Fall 2023

Tests for various aspects of password_checker.
"""
from password_checker import counter_score, check_uppercase, check_lowercase, check_digits, \
    check_symbols, check_length, check_common, score_total


def test_counter_score():
    # Test1
    failed = 0
    expected = 2
    actual = counter_score(5)
    if expected != actual:
        failed += 1
        print("test_counter_score failed")
        print("expected: ", expected)
        print("actual: ", actual)
    # Test2
    expected = 0
    actual = counter_score(-1)
    if expected != actual:
        failed += 1
        print("test_counter_score failed")
        print("expected: ", expected)
        print("actual: ", actual)
    return failed


def test_check_uppercase():
    # Test1
    failed = 0
    expected = 2
    actual = check_uppercase("HELLOWoRld23!")
    if expected != actual:
        failed += 1
        print("test_check_uppercase failed")
        print("expected: ", expected)
        print("actual: ", actual)
    # Test2
    expected = 0
    actual = check_uppercase("helloworld23!")
    if expected != actual:
        failed += 1
        print("test_check_uppercase failed")
        print("expected: ", expected)
        print("actual: ", actual)
    return failed


def test_check_lowercase():
    # Test1
    failed = 0
    expected = 1
    actual = check_lowercase("helloworld23!")
    if expected != actual:
        failed += 1
        print("test_check_lowercase failed")
        print("expected: ", expected)
        print("actual: ", actual)
    # Test2
    expected = 0
    actual = check_lowercase("!HELLOWORLD23!")
    if expected != actual:
        failed += 1
        print("test_check_lowercase failed")
        print("expected: ", expected)
        print("actual: ", actual)
    return failed


def test_check_digits():
    # Test1
    failed = 0
    expected = 2
    actual = check_digits("123456789")
    if expected != actual:
        failed += 1
        print("test_check_digits failed")
        print("expected: ", expected)
        print("actual: ", actual)
    # Test2
    expected = 0
    actual = check_digits("threetwoone!!!??@")
    if expected != actual:
        failed += 1
        print("test_check_digits failed")
        print("expected: ", expected)
        print("actual: ", actual)
    return failed


def test_check_symbols():
    # Test1
    failed = 0
    expected = 2
    actual = check_symbols("`~{}]\?/*&^()#@")
    if expected != actual:
        failed += 1
        print("test_check_symbols failed")
        print("expected: ", expected)
        print("actual: ", actual)
    # Test2
    expected = 0
    actual = check_symbols("symbols")
    if expected != actual:
        failed += 1
        print("test_check_symbols failed")
        print("expected: ", expected)
        print("actual: ", actual)
    # Test3
    expected = 1
    actual = check_symbols("234456  ! ")
    if expected != actual:
        failed += 1
        print("test_check_symbols failed")
        print("expected: ", expected)
        print("actual: ", actual)
    return failed


def test_check_length():
    # Test1
    failed = 0
    expected = 0
    actual = check_length("hello")
    if expected != actual:
        failed += 1
        print("test_check_length failed")
        print("expected: ", expected)
        print("actual: ", actual)
    # Test2
    expected = 1
    actual = check_length("1234567891")
    if expected != actual:
        failed += 1
        print("test_check_length failed")
        print("expected: ", expected)
        print("actual: ", actual)
    # Test3
    expected = 2
    actual = check_length("123456789112345")
    if expected != actual:
        failed += 1
        print("test_check_length failed")
        print("expected: ", expected)
        print("actual: ", actual)
    # Test4
    expected = 3
    actual = check_length("12345678911234567892")
    if expected != actual:
        failed += 1
        print("test_check_length failed")
        print("expected: ", expected)
        print("actual: ", actual)
    return failed


def test_check_common():
    # Test1
    failed = 0
    expected = True
    actual = check_common("helloworld")
    if expected != actual:
        failed += 1
        print("test_check_common failed")
        print("expected: ", expected)
        print("actual: ", actual)
    # Test2
    expected = None
    actual = check_common("HeLlowoRlD23!!")
    if expected != actual:
        failed += 1
        print("test_check_common failed")
        print("expected: ", expected)
        print("actual: ", actual)
    # Test3
    expected = True
    actual = check_common("password12")
    if expected != actual:
        failed += 1
        print("test_check_common failed")
        print("expected: ", expected)
        print("actual: ", actual)
    return failed


def test_score_total():
    # Test1
    failed = 0
    expected = 9
    actual = score_total("HeLloWorLd23!?@")
    if expected != actual:
        failed += 1
        print("test_score_total failed")
        print("expected: ", expected)
        print("actual: ", actual)
    # Test2
    expected = 5
    actual = score_total("Helloworld2!")
    if expected != actual:
        failed += 1
        print("test_score_total failed")
        print("expected: ", expected)
        print("actual: ", actual)
    # Test3
    expected = 10
    actual = score_total("HElloworld23@$567892")
    if expected != actual:
        failed += 1
        print("test_score_total failed")
        print("expected: ", expected)
        print("actual: ", actual)
    return failed


def main():
    failed = 0
    failed += test_counter_score()
    failed += test_check_uppercase()
    failed += test_check_lowercase()
    failed += test_check_digits()
    failed += test_check_symbols()
    failed += test_check_length()
    failed += test_check_common()
    failed += test_score_total()
    if failed == 0:
        print("All tests passed!")
    else:
        print("Number of tests failed:", failed)


if __name__ == "__main__":
    main()
