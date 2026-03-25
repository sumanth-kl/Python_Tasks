# 1. Create a dictionary with 3 student names and their marks.

std_details={'a':[70,60,80],'b':{65,75,85},'c':[61,71,81]}

for name, scores in std_details.items():
    print(f"{name}: {scores}")
