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

format_string = "{artist} sang {song} in {year}"
print(format_string.format(artist="Caetano", year=2019, song="Leaozinho"))

'''
format an string with 25 characters {:25}
'''
format_string = "| {:25}|"
print(format_string.format("Itamar"))

'''
format an string with 25 characters and aligning the string
>right
<left
^center
'''
format_left = "| {:<25}|"
format_right = "| {:>25}|"
format_center = "| {:^25}|"
print(format_left.format("Itamar"))
print(format_center.format("Itamar"))
print(format_right.format("Itamar"))


