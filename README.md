# Bracket: A Nimble and Expressive Functional Programming Language

Bracket distinguishes itself as a lightweight and interpreted functional programming language, placing a premium on simplicity and expressiveness in its intricately designed syntax and structure.

## Getting Started: Initiating Your Journey with Bracket File Creation

Embark on your programming journey with Bracket by laying the foundation of your code. Commence with the establishment of a main function, which serves as an introductory glimpse into the language's fundamental syntax:

```bracket
fn main
~ print Hello, World!
end fn
```

# Comprehensive Documentation

## Functions: Crucial Building Blocks of Code

Functions, the bedrock of Bracket's programming paradigm, play a pivotal role in code construction. Use the `fn` keyword to meticulously define a function and employ the `@` symbol for its seamless execution:

```bracket
fn [functionName]
~ [code]
end fn

fn main
~ @ [fnName]
end fn
```

## Includes: Seamless Integration of External Files

Immerse yourself in the streamlined integration of external files into your program through the utilization of the `->include` keyword:

```bracket
->include std
fn main
~ [code goes here]
end fn
```

### Module Creation: Elevating Code Modularity

Take code modularity to new heights with the creation of modular components through the `imports` function:

```bracket
fn imports
~ ;@Init
end fn
```

Modules, diverging from a conventional main function, embrace an "Imports" function, adding a layer of sophistication to code organization.

## Conditional Statements: Mastering Logic and Flow Control

Embark on a journey of logical prowess with a comprehensive exploration of conditional statements. Uncover an array of operators governing both `if` and `while` statements. Dive into the syntax intricacies and learn the art of executing functions within these statement constructs:

```bracket
>= (Greater than)
<= (Less than)
!= (Not Equal)
== (Equal)

->include std
fn mainLoop
~ @ cls
end fn

fn main
~ while 1 == 1 mainLoop
end fn
```

## Variables: Dynamic Data Storage Unveiled

Delve into the dynamic nature of data storage within Bracket by acquainting yourself with the meticulous process of variable definition and its pervasive incorporation throughout your code:

```bracket
var [VarName] := [Value]
print #[VarName]
```

## Calculations: Harnessing the Power of Computational Operations

Unleash the full potential of computational operations with the `py` command, steering your code toward sophisticated calculations:

```bracket
py Calculation 1+1
print #[Calculation]
```

The variable specified after the `py` command serves as the designated storage location for the calculated result.

## System Commands: Seamlessly Interacting with the Environment

Effortlessly execute system commands with the `sys` keyword, facilitating seamless interaction with the programming environment:

```bracket
sys cls
```
