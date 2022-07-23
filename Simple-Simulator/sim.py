opcodeType = {
    "10000":"A",
    "10001":"A",
    "10010":"B",
    "10010":"B",
    "10011":"C",
    "10100":"D",
    "10101":"D",
    "10110":"A",
    "10111":"C",
    "11000":"B",
    "11001":"B",
    "11010":"A",
    "11011":"A",
    "11100":"A",
    "11101":"C",
    "11110":"C",
    "11111":"E",
    "01100":"E",
    "01101":"E",
    "01111":"E",
    "01010":"F",
}

inp = []
instructions = []
pc = 0 #Program Counter
halted = False

while True:
	try:
		l = input()
		inp.append(l)
	except EOFError:
		break

for i in inp:
	if len(i.split()) == 0:
		continue
	else:
		instructions.append(i)

for inst in instructions:
    if inst[0:6] == '01010':
        halted = True
        break
    

