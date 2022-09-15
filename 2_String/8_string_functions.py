story="once upon a time there was king who was loved by all"
len=len(story)
print("Length of the string is=",len)
print(story.endswith("hh"))
a=story.count("a")
print("story.count= ",a)
print("story.capitalize= ",story.capitalize())
print(story.find("a"))   #finds the first index in which "a" appears
print(story.find("time"))  #finds the index of "t"
story1=story.replace("o","pp")
print("Replaced string = ",story1)
