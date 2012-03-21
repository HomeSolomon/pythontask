import os , glob
 
def dir(path):
    for infile in glob.glob( os.path.join(path) ):
        print "current file is: " + infile
        listing = os.listdir(path)
        for infile in listing:
            print "current file is: " + infile


path = dir(raw_input("Enter the path: "))
