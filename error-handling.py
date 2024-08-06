file = open('youtube.txt','w')

try:
    file.write('first code in python')
finally:
    file.close()
    
with open('youtube.txt', 'w') as file:
    file.write('mr.beast video coming soon...')