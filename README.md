# Bracket 101 
Welcome to the comprehensive documentation for Bracket, an elegantly designed, lightweight interpreted functional programming language crafted to empower developers with expressive and efficient code.

## Quick Start
To embark on your Bracket programming journey, initiate your code with the definition of a main function, exemplified below:

```bracket
fn main
~ print "Hello, World!"
end fn
```

# Documentation

## Functions
In Bracket, functions play a pivotal role in code organization. They are declared using the `fn` keyword, allowing for modular and reusable code, and the keyword `@` is used to invoke them. Here's an illustrative example of defining and invoking a function:

```bracket
fn functionName
~ [code]
end fn

fn main
~ @ functionName
end fn
```

## Includes
Enhance the functionality of your program by including external files using the `->include` keyword:

```bracket
->include std
fn main
~ [code goes here]
end fn
```

### Making a Module
Modules provide a structured way to encapsulate related code. A module example is presented below:

```bracket
fn imports
~ ;@Init
end fn
```

Conventionally, modules employ the `Imports` function instead of a primary `main` function.

## If & While Statements
Bracket offers robust control flow statements with the `if` and `while` constructs. Various operators, including `>=`, `<=`, `!=`, and `==`, facilitate intricate conditionals. An example of a while loop and an if statement is provided:

```bracket
->include std
fn mainLoop
~ @ cls
end fn

fn main
~ while 1 == 1 mainLoop
end fn
```

## Variables
Variables in Bracket are declared using the `var` keyword, promoting clarity and flexibility in your code. Dynamically including variables is seamlessly integrated:

```bracket
var VarName := [Value]

print #[VarName]
```

## Calculations
Bracket introduces a streamlined approach to calculations using the `py` command:

```bracket
py Calculation 1+1
print #[Calculation]
```

The variable specified after `py` serves as a container for the calculated result.

## System Commands
Effortlessly execute system commands within your Bracket program using the `sys` keyword:

```bracket
sys cls
```

Dive into the wealth of features offered by Bracket, empowering you to construct expressive, functional programs with precision and elegance. Happy coding!
