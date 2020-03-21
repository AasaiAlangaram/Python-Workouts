# import the necessary packages
import argparse

# construct the argument parse and parse the arguments
'''
we add our only argument, --name .
We must specify both shorthand (-n) and longhand versions (--name)  where either flag could be used in the command line.
This is a required argument as is noted by required=True
'''
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
	help="name of the user")

'''
script instructs Python and the argparse  library to parse the command line arguments.
I also call vars  on the object to turn the parsed command line arguments into a Python dictionary where the key to the dictionary is the name of the command line argument and the value is value of the dictionary supplied for the command line argument. 
'''
args = vars(ap.parse_args())
print(ap.parse_args())
print(args)

# display a friendly message to the user
print("Hi there {}, it's nice to meet you!".format(args["name"]))


'''
E:\Python\Argparse>python simple_example.py --name AasaiAlangaram
Namespace(name='AasaiAlangaram')
{'name': 'AasaiAlangaram'}
Hi there AasaiAlangaram, it's nice to meet you!
'''
