
def decToBin(a):
	sum = ''
	n = int(a)
	while (n):
		sum += str(n%2)
		n = n//2
	return (8-len(str(sum)))*'0'+str(sum)[::-1]
def xor(a,b):
    s=""
    for i in range(len(a)):
        s+='0' if int(a[i])!=int(b[i]) else '1' 
    return s
def aand(a,b):
    s=""
    for i in range(len(a)):
        s+='1' if int(a[i])==int(b[i])==1 else '0'
    return s
def oor(a,b):
    s=""
    for i in range(len(a)):
        s+='0' if int(a[i])==int(b[i])==0 else '1'
    return s

def binToDec(binary):
    binary1 = int(binary)
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = int(binary) % 10
        decimal = decimal + dec * pow(2, i)
        binary= int(binary)//10
        i+= 1
    return decimal
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
	'000':'R0',
	'001':'R1',
	'010':'R2',
	'011':'R3',
	'100':'R4',
	'101':'R5',
	'110':'R6',
	'111':'FLAGS'
}
regvals={
    'R0':6,
    'R1':3,
    'R2':2,
    'R3':0,
    'R4':0,
    'R5':0,
    'R6':0,
    "FLAGS.V":0,
    "FLAGS.L":0,
    "FLAGS.G":0,
    "FLAGS.E":0,
}



inp = []
instructions = []
pc = 0 #Program Counter
halted = False
def prinr(a):
    for i in a:
        print(i,":",a[i])
    
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
while(pc<len(instructions)):
    print(pc,"ddea")
    inst=instructions[pc]
    if inst[0:5] == '01010':
        halted = True
        break
    elif inst[0:5] == '10000':
        print("adding")
        rs2=inst[10:13]
        rd=inst[13:16]
        rs1=inst[7:10]
        rs1r=regvals[registers[rs1]]
        rs2r=regvals[registers[rs2]]
        rdv=rs1r+rs2r
        regvals[registers[rd]]=rdv
        prinr(regvals)
        pc=pc+1
    elif inst[0:5] == '10001':
        print("subtracting")
        rs2=inst[10:13]
        rd=inst[13:16]
        rs1=inst[7:10]
        rs1r=regvals[registers[rs1]]
        rs2r=regvals[registers[rs2]]
        rdv=rs1r-rs2r
        regvals[registers[rd]]=rdv
        prinr(regvals)
        pc=pc+1
    elif inst[0:5] == '10110':
        print("multiplying")
        rs2=inst[10:13]
        rd=inst[13:16]
        rs1=inst[7:10]
        rs1r=regvals[registers[rs1]]
        rs2r=regvals[registers[rs2]]
        rdv=rs1r*rs2r
        regvals[registers[rd]]=rdv
        prinr(regvals)
        pc=pc+1
    elif inst[0:5] == '11010':
        print("xoring")
        rs2=inst[10:13]
        rd=inst[13:16]
        rs1=inst[7:10]
        rs1r=regvals[registers[rs1]]
        rs2r=regvals[registers[rs2]]
        x1=decToBin(rs1r)
        x2=decToBin(rs2r)
        s=xor(x1,x2)        
        rdv=binToDec(s)
        regvals[registers[rd]]=rdv
        prinr(regvals)
        pc=pc+1
    elif inst[0:5] == '11011':
        print("oring")
        rs2=inst[10:13]
        rd=inst[13:16]
        rs1=inst[7:10]
        rs1r=regvals[registers[rs1]]
        rs2r=regvals[registers[rs2]]
        x1=decToBin(rs1r)
        x2=decToBin(rs2r)
        s=oor(x1,x2)        
        rdv=binToDec(s)
        regvals[registers[rd]]=rdv
        prinr(regvals)
        pc=pc+1
    elif inst[0:5] == '11100':
        print("anding")
        rs2=inst[10:13]
        rd=inst[13:16]
        rs1=inst[7:10]
        rs1r=regvals[registers[rs1]]
        rs2r=regvals[registers[rs2]]
        x1=decToBin(rs1r)
        x2=decToBin(rs2r)
        s=aand  (x1,x2)        
        rdv=binToDec(s)
        regvals[registers[rd]]=rdv
        prinr(regvals)
        pc=pc+1
