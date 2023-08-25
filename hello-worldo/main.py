# Do not modify these lines
__winc_id__ = 'e75b6cd4a7404e3ca76c308566dafb5d'
__human_name__ = 'hello-world'

# Add your code after this line
print ("Hello, world")

def initials(name):
    first = name[0].upper()
    last = name[name.find(' ')+1].upper()
    return f'{first}. {last}.'

print(initials('Ex Ample'))



