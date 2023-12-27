## Bracket 101

### Welcome
Welcome to Bracket, an elegant, lightweight, interpreted functional programming language designed to empower developers with expressive and efficient code.

### Quick Start
Initiate your Bracket programming journey by defining a main function. Here's an example:

```bracket
fn main
~ print "Hello, World!"
end fn
```

### Documentation

#### Functions
Functions are central to Bracket's code organization. Declare them using `fn` and invoke with `@`. Example:

```bracket
fn functionName
~ [code]
end fn

fn main
~ @ functionName
end fn
```

#### Includes
Enhance functionality by including external files with `->include`:

```bracket
->include std
fn main
~ [code]
end fn
```

##### Making a Module
Structurally encapsulate related code in modules:

```bracket
fn imports
~ ;@Init
end fn
```

Conventionally, modules use the `Imports` function instead of a primary `main`.

#### If & While Statements
Control flow with `if` and `while`. Operators include `>=`, `<=`, `!=`, and `==`. Example:

```bracket
->include std
fn mainLoop
~ @ cls
~ sleep 1000
end fn

fn main
~ while 1 == 1 mainLoop
end fn
```

#### Variables
Declare variables with `var` for clarity and flexibility:

```bracket
var VarName := [Value]

print #[VarName]
```

#### Calculations
Streamlined calculations with `py`:

```bracket
py Calculation 1+1
print #[Calculation]
```

#### System Commands
Execute system commands with `sys`:

```bracket
sys cls
```

#### Sleep
Introduce a sleep function to pause execution:

```bracket
sleep milliseconds
```

#### Save Input
Capture user input with `saveinput`:

```bracket
saveinput variableName "Enter your input: "
```

Dive into Bracket's features to construct expressive, functional programs with precision and elegance. Happy coding!
