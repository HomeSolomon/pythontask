import os

     
def git(op):
    #os.getcwd()
    #print s
#    print os.listdir(os.getcwd())

            #change directory
    folpath=""
    fold=raw_input("Enter repository name ");
    os.chdir("/home/solomon/SolomonPeter26/Private")
    folpath=" mkdir " + str(fold)
    os.system(folpath)
    chp="/home/solomon/SolomonPeter26/Private/" + fold
    os.chdir(chp)
    os.system(" touch README.md");
#    os.getcwd()
    
    print "\n\n"
    print os.listdir(os.getcwd())

            # only INITIALISE GIT IN FOLDER
    os.system(" git config --global user.name \"Solomon Peter\"")
    os.system(" git config --global user.email \"peterkingsley26@gmail.com\"")
    os.system(" git init")

    
            #add files for commit
    os.system(" git add .")
    stri=" git commit -m \" " + (raw_input("Enter message for commit:")) + "\""
    
            #view log of commits
    print "\t\tLocal ->"
    os.system(stri)
    os.system(" git log")
    
            #view status of repository
    print "\t\tStatus ->"
    os.system(" git status")
    
            #view files which have been commited
    print "\t\tCommited Files ->"
    os.system(" git ls-files")
    
    
    print "\t\tRemote ->"
    os.system(" git remote")
#    raw_input("Enter Login Name")
    
#    os.system("curl -F 'login=SolomonPeter26' -F 'token=a4d1fb125214f2a1ded31145ae77b068' https://github.com/api/v2/json/repos/create -F 'name=Test' -F 'description=This project is a test'")
#   os.system("git remote add origin git@github.com:nyeates/projectname.git")
#    git push origin master
    crn="curl -F 'login=SolomonPeter26' -F 'token=a4d1fb125214f2a1ded31145ae77b068' https://github.com/api/v2/json/repos/create -F 'name=" + fold + "' -F 'description=" + raw_input("Enter description for project: ") + "\'"
    print crn
    os.system(crn)
    strr=" git remote add origin git@github.com:SolomonPeter26/" + fold + ".git"
    print strr
    os.system(strr)
    os.system(" git push origin master")
    
#curl -F 'login=nyeates' -F 'token=XXX' https://github.com/api/v2/json/repos/create -F 'name=projectname' -F 'description=This project is a test'
#git remote add origin git@github.com:nyeates/projectname.git
#git push origin master

if __name__ == "__main__" :
    git(1)
