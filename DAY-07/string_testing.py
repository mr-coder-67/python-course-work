"""Demonstrate common string methods with comments and example outputs.

Each example includes a `# cmnts:` line showing an expected result.
"""


def demo_strings():
    # basic creation and strip methods
    s = ' hello world '
    print('original:', repr(s))
    # cmnts: example -> original: ' hello world '

    print('strip():', s.strip())
    # cmnts: example -> strip(): 'hello world'

    print('lstrip():', s.lstrip())
    # cmnts: example -> lstrip(): 'hello world '

    print('rstrip():', s.rstrip())
    # cmnts: example -> rstrip(): ' hello world'

    # startswith / endswith: check prefixes and suffixes
    fname = 'sting.py'
    print("fname:", fname)
    # cmnts: example -> fname: 'sting.py'

    print("startswith 'str':", fname.startswith('str'))
    # cmnts: example -> startswith 'str': False

    print("endswith '.py':", fname.endswith('.py'))
    # cmnts: example -> endswith '.py': True

    # isalpha, isalnum: character-class checks
    print("'dfgh'.isalpha():", 'dfgh'.isalpha())
    # cmnts: example -> True

    print("'12345'.isalnum():", '12345'.isalnum())
    # cmnts: example -> True

    print("'123@345'.isalnum():", '123@345'.isalnum())
    # cmnts: example -> False

    # case checks
    print("'qwerty'.islower():", 'qwerty'.islower())
    # cmnts: example -> True

    print("'SDFGH'.isupper():", 'SDFGH'.isupper())
    # cmnts: example -> True

    # whitespace checks
    print("' '.isspace():", ' '.isspace())
    # cmnts: example -> True

    print("''.isspace():", ''.isspace())
    # cmnts: example -> False

    # title/identifier checks
    print("'Py Ty Lg'.istitle():", 'Py Ty Lg'.istitle())
    # cmnts: example -> True

    print("'py_python'.isidentifier():", 'py_python'.isidentifier())
    # cmnts: example -> True


def main():
    demo_strings()


if __name__ == '__main__':
    main()