import math


def demo_function_temp_var(x: int) -> None:
    f = abs
    print("absolute value f(x) = ", f(x))


def demo_function_parameter(f, x: int) -> int:
    return f(x)


def main()-> int:
    demo_function_temp_var(-4)
    y = demo_function_parameter(abs, -4)
    print("absolute value f(x) = ", y)
    z = demo_function_parameter(math.sqrt, 4)
    print("Square root of x = ", z)
    return 0


if __name__ == '__main__':
    main()
