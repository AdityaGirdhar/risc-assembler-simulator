# Custom Assembler and Simulator
Here's an assembler and simulator based on a hypothetical instruction set architecture implemented in Python3.

This is a project for CSE112 - Computer Organisation, IIIT Delhi.

## Adding code
* Add the assembler code in `Simple-Assembler` directory
* Add the simulator code in the `Simple-Simulator` directory
* Make sure that both the assembler and the simulator read from `input.txt`
* Make sure that both the assembler and the simulator write to `output.txt`


## Known bugs
* ~~No movr, mov acts as movi~~
* var assigning needs to be tested
* No support for labels (yet).
* Labels can't be repeated
* print the max value in case of overflow(i.e - 255)
* calculate the number of lines except for var and empty and then start allocating the value one by one from the last count
* halt condition
* variables would be there in the start so while counting just check where the last var is declared
