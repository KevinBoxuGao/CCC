num_pairs = input()

def patterns(length, ones):
    print("The bit patterns are")
    
for i in range(0, num_pairs):
    pair = input()
    patterns(pair.split()[0], pair.split()[1])