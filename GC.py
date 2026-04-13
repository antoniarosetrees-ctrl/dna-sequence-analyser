dna = input("Enter DNA sequence: ")

a = dna.count("A")
t = dna.count("T")
g = dna.count("G")
c = dna.count("C")

total = len(dna)

if total == 0:
    print("Invalid input")
else:
    gc = ((g + c) / total) * 100

    print("A:", a)
    print("T:", t)
    print("G:", g)
    print("C:", c)
    print("GC Content:", gc)
