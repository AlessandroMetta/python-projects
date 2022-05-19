d={
'Hendrix' : '1942', 'Allman' : '1946', 'King' : '1925', 'Clapton' : '1945', 'Johnson' : '1911', 'Berry' : '1926', 'Vaughan' : '1954', 'Cooder' : '1947', 'Page' : '1944', 'Richards' : '1943', 'Hammett' : '1962', 'Cobain' : '1967', 'Garcia' : '1942', 'Beck' : '1944', 'Santana' : '1947', 'Ramone' : '1948', 'White' : '1975', 'Frusciante': '1970', 'Thompson' : '1949', 'Burton' : '1939',
}

year = sorted(set(d.values()))

for element in year:
    for n in d.items():
        if n[1] == element:
            print(n[0]);

print();

for element in year:
    l = []
    for n in d.items():
        if n[1] == element:
            l.append(n[0])
    l.sort()
    for name in l:
        print(name);
