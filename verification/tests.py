"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [["1.cad", "1.bat", "1.aa"]],
            "answer": ["1.aa", "1.bat", "1.cad"]
        },
        {
            "input": [["1.cad", "1.bat", "1.aa", "2.bat"]],
            "answer": ["1.aa", "1.bat", "2.bat", "1.cad"]
        },
        {
            "input": [["1.cad", "1.bat", "1.aa", ".bat"]],
            "answer": [".bat", "1.aa", "1.bat", "1.cad"]
        },
        {
            "input": [[ "1.cad", "1.bat", ".aa", ".bat"]],
            "answer": [".aa", ".bat", "1.bat", "1.cad"]
        },
        {
            "input": [[ "1.cad", "1.", "1.aa"]],
            "answer": ["1.", "1.aa", "1.cad"]
        },
        {
            "input": [["1.cad", "1.bat", "1.aa", "1.aa.doc"]],
            "answer": ["1.aa", "1.bat", "1.cad", "1.aa.doc"]
        },
        {
            "input": [["1.cad", "1.bat", "1.aa", ".aa.doc"]],
            "answer": ["1.aa", "1.bat", "1.cad", ".aa.doc"]
        }
    ],
    "Extra": [
        {
            "input": [[".config", "my.doc", "1.exe", "345.bin", "green.bat", "format.c", "no.name.", "best.test.exe"]],
            "answer": [".config", "no.name.", "green.bat", "345.bin", "format.c", "my.doc", "1.exe", "best.test.exe"]
        },
        {
            "input": [["1.cad", "2.bat", "1.aa", "1.bat"]],
            "answer": ["1.aa", "1.bat", "2.bat", "1.cad"]
        }
    ]
}