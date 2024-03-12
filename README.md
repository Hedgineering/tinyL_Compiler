# TinyL Compiler for Principles of Programming Languages

## Overview

This project implements a compiler for the TinyL language, a simple expression language allowing assignments and basic I/O operations. Developed as part of the coursework for Principles of Programming Languages (01:198:314:01), this compiler translates TinyL code into RISC machine instructions.

## Author

- **Name:** Rahul Hegde
- **NetID:** rah248

## Course Details

- **Course:** Principles of Programming Languages
- **Course Code:** 01:198:314:01
- **Institution:** Rutgers University

## Project Structure

The compiler is implemented in Python and resides within the `tinyL_Compiler/tinyL_Compiler` subdirectory. The Python script `Compiler.py` serves as the entry point for compiling TinyL source code into RISC machine code.

## TinyL Language

TinyL supports the following operations:

- Assignments (`=`)
- Basic I/O operations (`?` for read and `%` for print)
- Arithmetic operations (`+`, `-`, `*`)
- Bitwise operations (`&`, `|`)

Variables are single characters (`a` to `f`), and digits range from `0` to `9`.

## Target Architecture

The target architecture for this compiler is a simplified RISC machine with an unlimited number of virtual registers. Supported instructions include load, store, add, subtract, multiply, bitwise AND/OR, and I/O operations.

## Getting Started

To use the compiler, navigate to the `tinyL_Compiler/tinyL_Compiler` directory and execute the following command:

```bash
python3 Compiler.py compile <source_file.tinyL>
```
*Note*: On Mac you would use `python3` and on windows you would use `python` for this command.

This will generate RISC machine code for the provided TinyL source file.

## Testing

The project includes a set of test cases for validating the compiler's functionality. These tests cover various aspects of the TinyL language and the expected RISC machine code output. The tests are written using `unittest`, a built-in Python3 library, and can be found in the same `tinyL_Compiler/tinyL_Compiler` subdirectory in this repository.

## Contributions

This project is part of an academic assignment, and collaboration is limited to discussing concepts and ideas. Direct code sharing is not permitted.

## Acknowledgements

- Principles of Programming Languages course staff and instructor for providing the project guidelines and support.

## License

This project is for educational purposes only and not licensed for reuse or distribution.