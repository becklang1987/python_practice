def outer_function():
    x = "outer"

    def inner_function_1():
        nonlocal x
        x = "inner 1"

    def inner_function_2():
            x = "inner 2"
            print(x)

    inner_function_2()
    print("Value of x in inner_function_1:", x)

    inner_function_1()
    print("Value of x in outer_function:", x)

outer_function()