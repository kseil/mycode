ground = ['penny', 'penny', 'sock', 'penny', 'broccoli', 'cauliflower', 'trash', 'penny']

piggybank = int(0)

for i in ground:
    if i == 'penny':
        piggybank += int(1)

print(piggybank)
