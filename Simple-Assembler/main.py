import difflib

# Data and tables
opcodes = {
    'add':["10000","A"],
    'sub':["10001","A"],
	'mov':["10010","B"],
    'movi':["10010","B"],
    'movr':["10011","C"],
    'ld':["10100","D"],
    'st':["10101","D"],
    'mul':["10110","A"],
    'div':["10111","C"],
    'rs':["11000","B"],
    'ls':["11001","B"],
    'xor':["11010","A"],
    'or':["11011","A"],
    'and':["11100","A"],
    'not':["11101","C"],
    'cmp':["11110","C"],
    'jmp':["11111","E"],
    'jlt':["01100","E"],
    'jgt':["01101","E"],
    'je':["01111","E"],
    'hlt':["01010","F"],
}
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
registers = {
	'R0':'000',
	'R1':'001',
	'R2':'010',
	'R3':'011',
	'R4':'100',
	'R5':'101',
	'R6':'110',
}
lessthanflag=0
morethanflag=0
# Helper functions
def syntax(opcode):
	type = opcodeType[opcodes[opcode][0]]
	if type == 'A':
		return f'{opcode} reg1 reg2 reg3'
	if type == 'B':
		return f'{opcode} reg1 $Imm'
	if type == 'C':
		return f'{opcode} reg1 reg2'
	if type == 'D':
		return f'{opcode} reg1 mem_addr'
	if type == 'E':
		return f'{opcode} mem_addr'
	if type == 'F':
		return f'{opcode}'

def opcodeLength(opcode):
	s = syntax(opcode)
	return len(s.split())

def decToBin(a):
	sum = ''
	n = int(a)
	while (n):
		sum += str(n%2)
		n = n//2
	return (8-len(str(sum)))*'0'+str(sum)[::-1]

#Main code starts here
n = int(input())
arr = []
errors = []
bin = []
vars = {}
for i in range(0,n):
	arr.append(input())
data = [i.strip() for i in arr]
lines = [i.split() for i in data]
for inst in lines:
	if (len(inst) == 0):
		continue
	elif inst[0] == 'var':
		if len(inst) != 2:
			errors.append('[Error] Line '+str(lines.index(inst)+1)+f': Syntax for \'var\' is \'var name\'')
			continue
		vars[inst[1]] = 0
		continue
	elif inst[0] in opcodes and opcodeLength(inst[0]) != len(inst):
		s = syntax(inst[0])
		errors.append('[Error] Line '+str(lines.index(inst)+1)+f': Syntax for \'{inst[0]}\' is \'{s}\'')
		continue
	if inst[0] not in opcodes:
		suggest = difflib.get_close_matches(inst[0], opcodes.keys())
		if len(suggest) != 0:
			errors.append('[Error] Line '+str(lines.index(inst)+1)+": Invalid opcode '"+inst[0]+f"'. Did you mean '{suggest[0]}'?")
		else:
			errors.append('[Error] Line '+str(lines.index(inst)+1)+": Invalid opcode '"+inst[0]+f"'")
		continue
	type = opcodes[inst[0]][1]
	if type == 'A':
		if inst[1] not in registers or inst[2] not in registers or inst[3] not in registers:
			errors.append(f'[Error] Line {str(lines.index(inst)+1)}: Invalid register address')
			continue
		bin.append(opcodes.get(inst[0])[0]+'00'+registers.get(inst[1])+registers.get(inst[2])+registers.get(inst[3]))
	if type == 'B':
		if inst[1] not in registers:
			errors.append(f'[Error] Line {str(lines.index(inst)+1)}: Invalid register address')
			continue
		if inst[2][0] != '$':
			s = syntax(inst[0])
			errors.append('[Error] Line '+str(lines.index(inst)+1)+f': Syntax for \'{inst[0]}\' is \'{s}\'')
			continue
		if inst[2][1:].isnumeric() != True:
			errors.append(f'[Error] Line {str(lines.index(inst)+1)}: Invalid integer value {inst[2]}')
			continue
		if int(inst[2][1:]) > 255 or int(inst[2][1:]) < 0:
			errors.append(f'[Error] Line {str(lines.index(inst)+1)}: Integer {inst[2]} out of range, enter a numeric value between 0-255.')
			continue
		bin.append(opcodes.get(inst[0])[0]+ registers.get(inst[1])+ decToBin(inst[2][1:]))
	if type == 'C':
		if inst[1] not in registers or inst[2] not in registers:
			errors.append(f'[Error] Line {str(lines.index(inst)+1)}: Invalid register address')
			continue
		bin.append(opcodes.get(inst[0])[0]+'00000'+registers.get(inst[1])+registers.get(inst[2]))
	if type == 'D':
		if inst[1] not in registers:
			errors.append(f'[Error] Line {str(lines.index(inst)+1)}: Invalid register address')
			continue
	if type == 'E':
		if int(inst[1][1:]) > 255 or int(inst[1][1:]) < 0:
			errors.append(f'[Error] Line {str(lines.index(inst)+1)}: Integer {inst[1]} out of range, enter a numeric value between 0-255.')
			continue
		bin.append(opcodes.get(inst[0])[0]+'000' +dectoBin(inst[1][1:]))		
	if type == 'F':
		bin.append(opcodes.get(inst[0])[0]+11*'0')

if len(errors) == 0:
	for line in bin:
		print(line)
else:
	for line in errors:
		print(line)
