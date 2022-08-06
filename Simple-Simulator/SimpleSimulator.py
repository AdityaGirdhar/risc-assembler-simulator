def decToBin(a):
	sum = ''
	n = int(a)
	while (n):
		sum += str(n%2)
		n = n//2
	return (8-len(str(sum)))*'0'+str(sum)[::-1]
def decToBin16(a):
	sum = ''
	n = int(a)
	while (n):
		sum += str(n%2)
		n = n//2
	return (16-len(str(sum)))*'0'+str(sum)[::-1]
def binToDec(binary):
    binary1 = int(binary)
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = int(binary) % 10
        decimal = decimal + dec * pow(2, i)
        binary= int(binary)//10
        i+= 1
    return decimal

def reverse_IEEE754(n):
        binary= binToDec(n[8:16])
        exponent= binToDec(n[5:8])
        return exponent*binary
def formattedOutput(pc, regvals):
    print(f"{decToBin(pc)} {decToBin16(regvals['R0'])} {decToBin16(regvals['R1'])} {decToBin16(regvals['R2'])} {decToBin16(regvals['R3'])} {decToBin16(regvals['R4'])} {decToBin16(regvals['R5'])} {decToBin16(regvals['R6'])} 000000000000{regvals['FLAGS.V']}{regvals['FLAGS.L']}{regvals['FLAGS.G']}{regvals['FLAGS.E']}")
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
def inv(a):
    s=""
    for i in range(len(a)):
        s+='0' if int(a[i])==1 else '1'
    return s
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
    'R0':0,
    'R1':0,
    'R2':0,
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

memory_add = inp.copy()
ls_inputs_length = len(inp)

for i in range(256 - ls_inputs_length):
    memory_add.append('0'*16)    
	
CYCLE_COUNTER = 0
PROGRAM_COUNTER = 0

PROGRAM_COUNTER_LOCATION = []
CYCLE_COUNTER_VALUES = []
loop=0

while(PROGRAM_COUNTER<len(instructions)):
    #print(PROGRAM_COUNTER,"ddea")
    inst=instructions[PROGRAM_COUNTER]
    if inst[0:5] == '01010':
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
        halted = True
        break
    elif inst[0:5] == '10000':
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
        #print("adding")
        rs2=inst[10:13]
        rd=inst[13:16]
        rs1=inst[7:10]
        rs1r=regvals[registers[rs1]]
        rs2r=regvals[registers[rs2]]
        rdv=rs1r+rs2r
        if rdv <= 255:
            regvals[registers[rd]]=rdv
        else:
            regvals[registers[rd]]=rdv%256
            regvals["FLAGS.V"] = 1
        #prinr(regvals)
        
    elif inst[0:5] == '10001':
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
        rs2=inst[10:13]
        rd=inst[13:16]
        rs1=inst[7:10]
        rs1r=regvals[registers[rs1]]
        rs2r=regvals[registers[rs2]]
        rdv=rs1r-rs2r
        if rdv >= 0:
            regvals[registers[rd]]=rdv
        else:
            regvals[registers[rd]]=0
            regvals["FLAGS.V"] = 1
        #prinr(regvals)
       
    elif inst[0:5] == '10110':
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
        #print("multiplying")
        rs2=inst[10:13]
        rd=inst[13:16]
        rs1=inst[7:10]
        rs1r=regvals[registers[rs1]]
        rs2r=regvals[registers[rs2]]
        rdv=rs1r*rs2r
        if rdv <= 255:
            regvals[registers[rd]]=rdv
        else:
            regvals[registers[rd]]=rdv%256
            regvals["FLAGS.V"] = 1
        #prinr(regvals)
       
    elif inst[0:5] == '11010':
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
        #print("xoring")
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
        #prinr(regvals)
        
    elif inst[0:5] == '11011':
        #print("oring")
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
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
        #prinr(regvals)
        
    elif inst[0:5] == '11100':
        #print(CYCLE_COUNTER)
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
        #print("anding")
        rs2=inst[10:13]
        rd=inst[13:16]
        rs1=inst[7:10]
        rs1r=regvals[registers[rs1]]
        rs2r=regvals[registers[rs2]]
        x1=decToBin(rs1r)
        x2=decToBin(rs2r)
        s=aand(x1,x2)        
        rdv=binToDec(s)
        regvals[registers[rd]]=rdv
        #prinr(regvals)
        
    elif inst[0:5] == '10010':
        #print("move immediate")
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
        rd=inst[5:8]
        a=binToDec(inst[8:16])
        regvals[registers[rd]]=a
        #prinr(regvals)
        
    elif inst[0:5] == '11001':
        #print("left shift")
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
        rd=inst[5:8]
        a=binToDec(inst[8:16])
        b=2**a
        regvals[registers[rd]]=regvals[registers[rd]]*b
        #prinr(regvals)

    elif inst[0:5] == '11000':
        #print("right shift")
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
        rd=inst[5:8]
        a=binToDec(inst[8:16])
        b=regvals[registers[rd]]>>a
        regvals[registers[rd]]=b
        #prinr(regvals)
       
    elif inst[0:5] == '10011':
        #print("move register")
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
        rs1=inst[10:13]
        rs2=inst[13:16]
        if( registers[rs1]== 'FLAGS'):
            rs2r=regvals["FLAGS.V"]+ regvals["FLAGS.L"]+regvals["FLAGS.G"]+regvals["FLAGS.E"]
            regvals["FLAGS.V"]=0
            regvals["FLAGS.E"]=0
            regvals["FLAGS.L"]=0
            regvals["FLAGS.G"]=0
            regvals[registers[rs2]]=rs2r
        else:   
            rs2r= regvals[registers[rs1]]
            regvals[registers[rs2]]=rs2r

    elif inst[0:5] == '10111':
        #print("dividing")
        rs1=inst[10:13]
        rs2=inst[13:16]
        rs2r=regvals[registers[rs2]]
        rs1r=regvals[registers[rs1]]
        a=rs1r//rs2r
        b=rs1r%rs2r
        regvals["R0"]=a
        regvals["R1"]=b
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
    elif inst[0:5] == '11101':
        #print("inverting")
        rs1=inst[10:13]
        rs2=inst[13:16]
        rs1r=regvals[registers[rs1]]
        x1=decToBin(rs1r)
        s=inv(x1)        
        rdv=binToDec(s)
        regvals[registers[rs2]]=rdv
        #prinr(regvals)
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
    elif inst[0:5] == '11110':
        #print("Comparing")
        rs1=inst[10:13]
        rs2=inst[13:16]
        rs1r=regvals[registers[rs1]]
        rs2r=regvals[registers[rs2]]
        if rs1r==rs2r:
            regvals["FLAGS.E"]=1
        elif rs1r>rs2r:
            regvals["FLAGS.G"]=1
        else:
            regvals["FLAGS.L"]=1                
        #prinr(regvals)
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
        
    elif inst[0:5] == '10100':
        #print("loading")
        rd=inst[5:8]
        mem_addf=binToDec(inst[8:16])
        regvals[registers[rd]]=binToDec(memory_add[mem_addf])
        PROGRAM_COUNTER_LOCATION.append(mem_addf)
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        #prinr(regvals)

    elif inst[0:5] == '10101':
        #print("storing")
        rd=inst[5:8]
        mem_addf=binToDec(inst[8:16])
        memory_add[mem_addf] = decToBin16(regvals[registers[rd]])
        PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        #prinr(regvals)

    elif inst[0:5]== '11111':
        #print("unconditional jump")
        mem_addf=binToDec(inst[8:16])
        #print("printing program counters",end="\n")
        #prinr(regvals)
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
        formattedOutput(PROGRAM_COUNTER, regvals)
        PROGRAM_COUNTER = mem_addf
        CYCLE_COUNTER+=1
        continue
    elif inst[0:5]== "01111":
        if(regvals["FLAGS.E"]==1):
            regvals["FLAGS.G"]=0
            regvals["FLAGS.L"]=0
            regvals["FLAGS.E"]=0
            regvals["FLAGS.V"]=0
            mem_addf=binToDec(inst[8:16])
            CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
            PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
            formattedOutput(PROGRAM_COUNTER, regvals)
            #print("printing program counters",end="\n")
            PROGRAM_COUNTER = mem_addf
            CYCLE_COUNTER+=1
            #prinr(regvals)
            continue
        else:
            regvals["FLAGS.G"]=0
            regvals["FLAGS.L"]=0
            regvals["FLAGS.E"]=0
            regvals["FLAGS.V"]=0
            CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
            PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
            pass
            #print(" flag.L value isn't 1 ")
            #prinr(regvals)
        
    elif inst[0:5] == "01100":
        if(regvals["FLAGS.L"]==1):
            regvals["FLAGS.G"]=0
            regvals["FLAGS.L"]=0
            regvals["FLAGS.E"]=0
            regvals["FLAGS.V"]=0
            CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
            PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
            mem_addf=binToDec(inst[8:16])
            formattedOutput(PROGRAM_COUNTER, regvals)
            PROGRAM_COUNTER = mem_addf
            CYCLE_COUNTER+=1
            continue
        else:
            regvals["FLAGS.G"]=0
            regvals["FLAGS.L"]=0
            regvals["FLAGS.E"]=0
            regvals["FLAGS.V"]=0
            CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
            PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
            pass
            
    elif inst[0:5] == "01101":
       
        mem_addf=binToDec(inst[8:16])
        if(regvals["FLAGS.G"]==1):
            regvals["FLAGS.G"]=0
            regvals["FLAGS.L"]=0
            regvals["FLAGS.E"]=0
            regvals["FLAGS.V"]=0
            
            CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
            PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
            formattedOutput(PROGRAM_COUNTER, regvals)
            PROGRAM_COUNTER = mem_addf
            
            CYCLE_COUNTER+=1

            continue
        else:
            regvals["FLAGS.G"]=0
            regvals["FLAGS.L"]=0
            regvals["FLAGS.E"]=0
            regvals["FLAGS.V"]=0
            CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
            PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
            pass
            
    elif inst[0:5] == "00010":
            regvals[registers[inst[5:8]]]= reverse_IEEE754(inst[8:16])
            CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
            PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
            continue
    
                        
    elif inst[0:5]== "00001":
        x1= regvals[registers[inst[10:13]]]
        x2= regvals[registers[inst[13:16]]]
        if (x1-x2 <1 ):
                regvals[registers[inst[5:8]]]= 1
                regvals["FLAGS.V"]=1
        elif (x1 -x2>252):
                regvals[registers[inst[5:8]]]= 252
                regvals["FLAGS.V"]=1
        else :
                regvals[registers[inst[5:8]]]= x1 -x2    
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
        continue

    elif inst[0:5]== "00000":
        x1= regvals[registers[inst[10:13]]]
        x2= regvals[registers[inst[13:16]]]
        if (x1+x2 <1 ):
                regvals[registers[inst[5:8]]]= 1
        elif (x1 +x2>252):
                regvals[registers[inst[5:8]]]= 252
                regvals["FLAGS.V"]=1
                
        else :
                regvals[registers[inst[5:8]]]= x1+x2
                regvals["FLAGS.V"]=1
                        
        CYCLE_COUNTER_VALUES.append(CYCLE_COUNTER)
        PROGRAM_COUNTER_LOCATION.append(PROGRAM_COUNTER)
        continue
        
    formattedOutput(PROGRAM_COUNTER, regvals)
    PROGRAM_COUNTER+=1 
    CYCLE_COUNTER+=1

formattedOutput(PROGRAM_COUNTER, regvals)

# print(memory_add)
for i in memory_add:
    if len(i.split()) == 0:
        memory_add[memory_add.index(i)] = '0000000000000000'

ln = len(memory_add) if len(memory_add) <= 256 else 256

for i in range(ln):
    print(memory_add[i])
