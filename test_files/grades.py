students = {"ali": 85, "sara": 92, "ahmed": 78}
total = 0
for name, grade in students.iteritems():
    total = total + grade
    print name, ":", grade
print "Average:", total / len(students)
