def gt(a, b):
    return a > b
def lt(a, b):
    return a < b
def eq(a, b):
    return a == b
def ne(a, b):
    return a != b
def ng(a, b):
    return a <= b
def nl(a, b):
    return a >= b
ops = {
    ">" : gt,
    "<" : lt,
    "==" : eq,
    "<=" : ng,
    ">=" : nl
}