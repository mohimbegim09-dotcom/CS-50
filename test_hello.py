from hello import hello

def test_hello():
    assert hello('David') == 'hello, David'# to check this code
    # enter 'pytest test_hello.py' to the terminal


#OR

def test_default():
    assert hello() == 'hello, world'# in case if the user will not enter anything

def test_argument():
    assert hello('David') == 'hello, David'


# Or if the user enters multiple names

def test_argument():
    for name in ['Hermione', 'Harry', 'Ron']:
        assert hello(name) == f'hello,{name}' 