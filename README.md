# RISCV Verification Framework
Proof of concept for a property-based testing framework for RISCV CPUs

The program generates an assembly file, using object-oriented programming and property-based testing philosophies. This is then compiled, run through spike (the control) and the device under test. The logs are compared to identify any differences in execution and a relevant error/success message is outputed to the user. 

The hypothesis library in python allows testing of edge cases and provides shrinking so that the specific error can be found. For more information, see https://hypothesis.readthedocs.io/en/latest/ .

In this proof of concept, linear programs (instructions that are executed line by line without jumps) are generated and a subset of non-linear programs. More exhausive testing of depth can also be explored. 

For a full write up, see Property Based Testing with Hypothesis 1.10.2021 

For an alternative class structure, see Changes With Block Classes Defined file
 
# Tools for the testing environment:
1. Spike (an emulator) can be cloned and built following instructions on https://github.com/riscv-software-src/riscv-isa-sim
2. RISC-V toolchain: https://github.com/Imperas/riscv-toolchains
3. Pseudo-kernel: https://github.com/riscv-software-src/riscv-pk
