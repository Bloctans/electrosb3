from electrosb3.block_engine.block_support import API

api_instance = API(None)

"""
    0: The first arg
    1: The second arg
    2: The result
"""
tests = {
    "(0 = \"\")": ["0", "", 0],
    "(0 = \" \")": ["0", " ", 0]
}

def run():
    for i in tests:
        test = tests[i]

        result = api_instance.compare(test[0], test[1]) == test[2]

        print(f"Test {i} {result and "Passed" or "Failed"}")