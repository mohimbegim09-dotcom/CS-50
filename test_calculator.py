from calculator import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print('test failed')
    if square(3) != 9:
        print('test failed')

if __name__ == '__main__':
    main()

    #or

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print('test failed')
    try:
        assert square(3) == 9
    except AssertionError:
        print('test failed')

 # OR to keep it short use pytest

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

    #and then enter to the terminal:
    # pytest test_calculator.py
    

   