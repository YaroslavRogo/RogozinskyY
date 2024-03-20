threshold = float(input())

with open('freqs.txt', 'r') as file:
    lines = file.readlines()

filt_freqs = []
for line in lines:
    freqs = line.strip().split(';')
    filt_freqs.extend([freq for freq in freqs
                       if float(freq) <= threshold])

output = ' '.join(filt_freqs)
print(output)