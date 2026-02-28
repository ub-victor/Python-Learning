course = 'Python for Beginners'

print("The length of course is ", end= "")
print(len(course))
print(course.upper())

# find() method help you to get the index of a character
print(course.find('y'))
print(course.find('Beginners'))
# Replace method
print(course.replace('Beginners', 'Absolute Beginners'))
# Check if a sentence have some words
print("Python" in course) # it will outpout a boolens operation