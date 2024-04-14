# Gradebook
# You are a student and you are trying to organize your 
# subjects and grades using Python.   Use lists to organize your 
# subjects and scores.

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#print(gradebook)

gradebook.append(["computer scuence", 100])
gradebook.append(["visual arts", 93])
#print(gradebook)

gradebook[-1][-1] = 98
print(gradebook)

gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook )

print(last_semester_gradebook)

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)