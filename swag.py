print('Hello to SWAG')

file = 'web/index.html'

f = open(file, 'r')
print('----------')
print('These are the contents of the original file:')
print('----------')
print(f.read())
f.close()

f = open(file, 'r')
lines = []
for x in f:
    if x == '<!-- MENU -->\n':
        text = 'Menu goes here\n'
        lines.append(text)
    else:
        lines.append(x)

f.close()

f = open(file, 'w')
for x in lines:
    f.write(x)
f.close()

print('----------')
print('Finished. These are the contents after modification:')
print('----------')
f = open(file, 'r')
print(f.read())
f.close()
