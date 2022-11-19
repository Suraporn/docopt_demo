# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: demo.py <arg1> [<arg-new>] --arg2=<arg2> [--arg3=<arg3>]

Options:
<arg1>            Takes any value (this is a required positional argument)
<arg-new>         Takes any value (this is a optional positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
""" 

from docopt import docopt

# define main function
def main():
    # code for "guts" of script goes here
    opt = docopt(__doc__)
    print(opt)
    print(type(opt))

# code for other functions & tests goes here

# call main function
if __name__ == "__main__":
    main()