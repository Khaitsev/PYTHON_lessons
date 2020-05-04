import re

m_file = open('text_6.txt', 'r', encoding='utf-8')
readfile = m_file.readlines()
my_dict = {}
for n in readfile:
    a = n.split(':')
    b = re.findall(r'\d+', str(n))
    c = sum(list(map(int, b)))
    my_dict[a[0]] = c
print(my_dict)
m_file.close()