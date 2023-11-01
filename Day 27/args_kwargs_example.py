# args is a way of passing many positional arguments
# the type of the args will be tuple
# printing the args

def args_example(*args):
    print(type(args))
    print(args)


args_example(1, 2, 3, 4)

# iterate through args and indexing


def iterate_args(*args):
    print(args[0])
    print(args[1])
    print(args[2])

    for element in args:
        print(element)


iterate_args(1, 2, 3, 4)


# kwargs is a way of passing many keyword arguments
# the type of the kwargs will be dictionary
# printing the kwargs

def kwargs_example(**kwargs):
    print(type(kwargs))
    print(kwargs)


kwargs_example(first_name="Ajay", last_name="Dev")

# iterating through the kwargs and accessing the value


def iterate_kwargs(**kwargs):
    print(kwargs["first_name"])
    print(kwargs["last_name"])

    for key, value in kwargs.items():
        print(key, value)


iterate_kwargs(first_name="Ajay", last_name="Dev")


