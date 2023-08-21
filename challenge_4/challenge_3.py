def f(x,y,z,a=1,b=2):
    """ Returns the result of two optional params
    multiplied by the addition of 3 required params.
    :param x: int.
    :param y: int.
    :param z: int.
    :param a: int.
    :param b: int.
    :return: int.
    """
    return x+y+z+a+b

result = f(1,2,3,0,0)
print(result)
