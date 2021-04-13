def standard_arg(arg):
    print(arg)

# Restricted to only positional parameters, coz there was an '/'
# after first argument
def pos_only_arg(arg, /):
    print(arg)

# Only allow keyword argumen,
# Indicated w/ '*' at first arg
def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(arg = 2)

print("")

pos_only_arg(3)

print("")

kwd_only_arg(arg = 4)

print("")

print("Combined Examples: ")

# combined_example(1, 2, 3)
combined_example(1, 2, kwd_only = 3)
combined_example(4, standard = 5, kwd_only = 6)

def foo(name, /, **kwds):
    return 'name' in kwds

foo(1, **{"3":5})
