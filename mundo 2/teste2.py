lost = ['um','dois','tres','quatro']
lost.insert(1,'hello')
lost.remove('hello')
lost.append('santos')
lost.insert(3,'jatoba')
del lost[3]
lost.sort()
print(len(lost))
print(lost)
lost.sort(reverse=True)