import re
txt = '''ORIGIN      
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//
'''

#extract preproinsulin string
insulin = re.sub('[^a-z]', "", txt)
print(insulin)
print(len(insulin))

print(len(insulin))

print(insulin[0:24])
print(len(insulin[0:24]))



print(insulin[24:54])
print(len(insulin[24:54]))

print(insulin[54:89])
print(len(insulin[54:89]))


print(insulin[89:])
print(len(insulin[89:]))
