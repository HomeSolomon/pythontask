import os

def get(filename):
        Folders=[];
        Files=[]
        path=[]
        os.system("locate -b "+ filename + " > list.txt" );
        os.system("touch list.txt");
        fp=open("list.txt","r")
        lines=fp.readlines()
        line=""
        for l in lines:
            for dirname, dirnames, filenames in os.walk(l):
                for subdirname in dirnames:
                    Folders.append(os.path.join(dirname, subdirname))
                    print Folders
                for filename in filenames:
                    ext = os.path.splitext(filename)[-1][1:]
                    Files.append(os.path.join(dirname, filename))
                    print Files
                    
if __name__ == '__main__':

        print "Enter the folder name    "
        filename = raw_input();
        get(filename)
