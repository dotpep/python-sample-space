SAMPLE_VAR: str = "constant variable in sample.py"

def sample_function() -> str:
    FUNC_VAR: str = "variable in sample function"
    return FUNC_VAR


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
