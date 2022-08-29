"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [['1.cad', '1.bat', '1.aa']],
            "answer": ['1.aa', '1.bat', '1.cad'],
        },
        {
            "input": [['1.cad', '1.bat', '1.aa', '2.bat']],
            "answer": ['1.aa', '1.bat', '2.bat', '1.cad'],
        },
        {
            "input": [['1.cad', '1.bat', '1.aa', '.bat']],
            "answer": ['.bat', '1.aa', '1.bat', '1.cad'],
        },
        {
            "input": [['1.cad', '1.bat', '.aa', '.bat']],
            "answer": ['.aa', '.bat', '1.bat', '1.cad'],
        },
        {
            "input": [['1.cad', '1.', '1.aa']],
            "answer": ['1.', '1.aa', '1.cad'],
        },
        {
            "input": [['1.cad', '1.bat', '1.aa', '1.aa.doc']],
            "answer": ['1.aa', '1.bat', '1.cad', '1.aa.doc'],
        },
        {
            "input": [['1.cad', '1.bat', '1.aa', '.aa.doc']],
            "answer": ['1.aa', '1.bat', '1.cad', '.aa.doc'],
        },
    ],
    "Extra": [
        {
            "input": [['.config', 'my.doc', '1.exe', '345.bin', 'green.bat', 'format.c', 'no.name.', 'best.test.exe']],
            "answer": ['.config', 'no.name.', 'green.bat', '345.bin', 'format.c', 'my.doc', '1.exe', 'best.test.exe'],
        },
        {
            "input": [['1.cad', '2.bat', '1.aa', '1.bat']],
            "answer": ['1.aa', '1.bat', '2.bat', '1.cad'],
        },
    ]
}
