'''
This examples will show how to use the formmatting function
'''
varnumber = 10
vartext = "Itamar"
varboolean = True
myformatting = "This is a formatting {} {} {}"
print(myformatting.format(varnumber,
                          vartext,
                          varboolean))

phrase = "My name is {1} and I am {0} years old and living in {2}"
print(phrase.format(53, "Itamar Tafarello", "Brazil"))