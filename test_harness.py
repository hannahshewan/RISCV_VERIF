import subprocess #may be part of the python environment already
import filecmp
import os
import instructions
from hypothesis import example, given, strategies as st

#urgent + important: whitelisting for integers so they're reasonable + ensuring thy're the same length
#not urgent but important: better strategy for integer_list
#===> make a strategy, this makes everything easier

#cheats that are fine for now: opcode enumeration

#the instructions are labelled from 1 (should have a more sensible order though)

def same_length(x, y):
    max_length = min(len(x), len(y))
    x = x[0:max_length]
    y = y[0:max_length]
    return 



def build_assembly(blocks, opcode, integer_list): #2d array instead?, i added the block enumeration in here too
    assembly_file = open("assembly.s", "w")
    program = ['    .file    "assembly.s"', '    .option nopic', '    .attribute arch, "rv64i2p0_m2p0_a2p0_f2p0_d2p0_c2p0"', '    .attribute unaligned_access, 0', '    .attribute stack_align, 16', '    .text', '    .align	1', '    .globl  main', '    .type   main, @function', 'main:'] 
    
    instructions.blockhandler(opcode)
         
    for element in program:
       assembly_file.write(element + "\n")
    assembly_file.close()
    
    return 

@given(st.lists(st.integers(min_value = 1, max_value =2)), st.lists(st.integers(min_value = 0, max_value = 10)))
def test_cpu(opcode, int_for_instructions):
    print('test starting')
    same_length(opcode, int_for_instructions)
    build_assembly(opcode, int_for_instructions)
    subprocess.run(['cat', 'assembly.s'])    
    control, dut = run_flow("assembly.s")
    print('test complete')
    assert control == dut

def run_flow(file_name):
    #compile
    subprocess.run(['../riscv-toolchains/Linux64/bin/riscv64-unknown-elf-gcc', file_name, '-o', 'output']) 
    print('compiled')
    #run on control
    control_process = subprocess.run(['../riscv-toolchains/Linux64/bin/spike_control', '-l', '/home/hannah/project/riscv-toolchains/Linux64/riscv64-unknown-elf/bin/pk', 'output'], capture_output=True, text=True) 
    print('run on control complete')
    #run on DUT 
    dut_process = subprocess.run(['../riscv-toolchains/Linux64/bin/spike_dut', '-l', '/home/hannah/project/riscv-toolchains/Linux64/riscv64-unknown-elf/bin/pk', 'output'], capture_output=True, text=True) 
    print('run on dut complete')
    
    return control_process.stderr, dut_process.stderr


if __name__== "__main__":
	test_cpu()
