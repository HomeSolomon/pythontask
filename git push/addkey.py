import os;


class sshkey:

    def __init__(self,email,uname,passwd):
        self.email=email
        self.uname=uname
        self.passwd=passwd
        
        
    def addkey(self):
        os.chdir('/home/solomon/.ssh')
        print os.listdir(os.getcwd())
        
        #key generate   
        keyg="ssh-keygen -t rsa -f ~/.ssh/" + self.uname + " -C \"" + email + "\" -P \"\""
        os.system(keyg)
        
        #add ssh key on github
        filen='/home/solomon/.ssh/'+ self.uname +'.pub'
        f=open(filen,'r')
        rsakey=f.read()
        stradd="curl -u \"" + self.uname + ":" + self.passwd + "\" http://github.com/api/v2/json/user/key/add -F \"title=ExeCode\" -F \"key=" + rsakey + "\""
        print "\n" + stradd +"\n"
        os.system(stradd)

    def editconf(self):
        stri = "\nHost " + self.uname + "\nHostname github.com\nUser git\nIdentityFile ~/.ssh/" + self.uname 
        print stri

        


        fout = open("config", "a")
        fout.write(stri)
        fout.close()
        
         
    def createmaindir(self):
        chp="/home/solomon/"
        os.chdir(chp)
        folpath=" mkdir " + str(self.uname)
        os.system(folpath)
        chp="/home/solomon/" + self.uname
        os.chdir(chp)
        os.system("mkdir Private")

if __name__=="__main__":
    email=raw_input("\n Enter email id: ")
    uname=raw_input("\n Enter github username: ")
    passwd=raw_input("Enter password : ")
    usr=sshkey(email,uname,passwd)
    usr.addkey()
    usr.editconf()
    usr.createmaindir()
