f = open('list.txt', 'r')
content = f.read()
f.close()
for block in content.split('\n\n'):
    print content
    
