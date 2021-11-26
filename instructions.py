class Instruction:
    def __init__(self):
        print("in the instruction constructor")
        pass
    def string(self):
        return 'instruction class'
        
class Load(Instruction): #load instructions: ld rd, offset(rs1)
    def __init__(self, rd, offset, rs1):
        self.rd = str(rd)
        self.offset = str(offset)
        self.rs1 = str(rs1)
        return  

    def string(self):
        return "ld x" + self.rd + ", " + self.offset + "(x" + self.rs1 + ")"

class Store(Instruction):
    def __init__(self, rs1, rs2, offset):
        self.rs1 = str(rs1)
        self.rs2 = str(rs2)
        self.offset = str(offset)
        return 

    def string(self):
        return "sd x" + self.rs1 + ", " + self.rs2 + "(x" + self.offset + ")"

class Block:
    def __init__(self):
        print('in block constructor')
        self.program = []
        return 
    def string(self):
        return self.program
    
    
class linear_block(Block):
    def __init__(self, opcode, integer_list):
        self.type = 1
        Block.__init__(self) #i should make this as separate method ie don't put it in the constructor
        for x in range(len(opcode)):
            if (opcode[x] == 1):     
                line = Load(integer_list[0], integer_list[1], integer_list[2]) 
            elif (opcode[x] == 2): 
                line = Store(integer_list[0], integer_list[1], integer_list[3])
            self.program.append('    ' + line.string())
        return 
    
class while_block(Block):
    def __init__(self, opcode, integer_list, function): #opcode for the while statement line + which function, function for what's inside the loop
        self.type = 2
        Block.__init__(self)
        self.program.append('Insert assembly for the beginning of a while loop') #this line will use the opcode variable
        inside_loop = linear_block(function, integer_list) #integer_list is wrong here, and i've assumed the function is linear but that'll change once i've made the function class
        self.program.append(inside_loop.string())
        #might be more assembly to add in here at the end of the loop
        return

   
class if_block(Block):
    def __init__(self, opcode, function_a, function_b, integer_list_a, integer_list_b):
        self.type = 3
        Block.__init__(self)
        self.program.append('insert assembly for if statement, using opcode variable')
        first_function = linear_block(function_a, integer_list_a)
        second_function = linear_block(function_b, integer_list_b)
        self.program.append(first_function.string())
        self.program.append(second_function.string())
        #might be more assembly to add in here
        return

#def block_handler(block_type, opcode) #block_type is an integer, #opcode as a list of strings
    
me = if_block([1,2], [1,2], [2,1], [1,2,3,4], [4,3,2,1])
print(me.string())
