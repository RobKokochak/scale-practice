import random

roots = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
scales = ['major', 'minor', 'melodic minor', 'harmonic minor']
intervals = ['3rds', '4ths', '5ths', '6ths']
directions = ['ascending', 'descending']
modifiers = ['', ', inverted', ', up one/down other', ', down one/up other']

root = random.choice(roots)
scale = random.choice(scales)
interval = random.choice(intervals)
direction = random.choice(directions)
modifier = random.choice(modifiers)

print(f"{root} {scale} in {interval}, {direction}{modifier}")
