l = ["Rama","Sita","Ravana","Krishna","Radha"]
k = list(filter(lambda name:(name.startswith("R")),l))
m = list(map(lambda name:(name.upper()),l))
print(k)
print(m)
