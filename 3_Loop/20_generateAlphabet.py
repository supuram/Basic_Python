letters = ''
for i in range(ord('A'), ord('Z') + 1):
    letters = letters + chr(i) + chr(i + 32)
print(letters)