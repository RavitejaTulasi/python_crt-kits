lang={'java', 'python', 'c', 'c++', 'SQL', 'c'}
print(lang)
lang.add('Ruby')
print(lang)
ui={'HTML', 'Express js', 'angular'}
lang.update(ui)
print(lang)

print('\n')

la = {'Java', 'Python', 'C', 'C++', 'SQL', 'C'}
la.remove('C')
print(la)
la.discard('C++')
print(la)

print('\n')

set1 = {'Tom & jerry', 'oggy & cockroach', 'Doraemon', 'Shinchan', 'motu patlu'}
set2 = {'oggy & cockroach','little Krishna', 'Shinchan', 'heidi'}
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.issubset(set2))
print(set2.issubset(set1))
print(set1.issuperset(set2))
print(set2.issuperset(set1))

print('\n')


