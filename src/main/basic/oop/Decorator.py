def my_decorator(func):
    def wrapper(name:str, *args, **kwargs):
        print("Something is happening before the function is called.")
        func(name)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee(name:str):
    print(f"Whee! {name}")

# say_whee = my_decorator(say_whee)

say_whee("jas")