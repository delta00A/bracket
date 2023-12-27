import os
import sys
import time

variables = {"null": "", "whitespace": " ", "newline": "\n", "tab": "\t"}
fns = {}


def randint(a, b):
    "Return random integer in range [a, b], including both end points."
    return a + randbelow(b - a + 1)


def randbelow(n):
    "Return a random int in the range [0,n).  Raises ValueError if n<=0."
    if n <= 0:
        raise ValueError
    k = n.bit_length()
    numbytes = (k + 7) // 8
    while True:
        r = int.from_bytes(random_bytes(numbytes), "big")
        r >>= numbytes * 8 - k
        if r < n:
            return r


def random_bytes(n):
    "Return n random bytes"
    with open("/dev/urandom", "rb") as file:
        return file.read(n)


def replacevar(line, vars):
    if "#{input}" in line:
        line = line.replace("#{input}", input())
    for ob in vars:
        line = line.replace("#[" + ob + "]", str(vars[ob]))
    return line


def join_by_first(sequences):
    out = {}
    for seq in sequences:
        try:
            out[seq[0]].extend(seq[1:])
        except KeyError:
            out[seq[0]] = list(seq)
    return [tuple(values) for values in out.values()]


class Base:
    # Foreground:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    # Formatting
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    # End colored text
    END = "\033[0m"
    NC = "\x1b[0m"  # No Color


c = 0


def merge_two_dicts(x, y):
    z = x.copy()  # start with keys and values of x
    z.update(y)  # modifies z with keys and values of y
    return z


def parse(text, caller):
    global c

    global variables
    text = text.replace("\\n", "\n").split("\n")
    infunc = False
    curfunc = []
    fnName = ""
    for lineUnformatted in text:
        c += 1

        line = replacevar(lineUnformatted, variables).split(" ")
        if line[0][0:1] == ";":
            pass
        elif line[0] == "var":
            if line[2] != ":=":
                print(
                    Base.FAIL
                    + f"[{c}] SyntaxError: Invalid syntax. Instead of "
                    + line[2]
                    + " use :="
                    + Base.END
                )
                sys.exit()

            l = replacevar(" ".join(line), variables).split(" ")
            # variables.append((l[1], " ".join(l[3:])))
            variables[l[1]] = " ".join(l[3:])

        elif line[0] == "print":
            content = replacevar(" ".join(line[1:]), variables)
            print(content)
        elif line[0] == "fn":
            fnName = line[1]
            curfunc = {"args": line[2:], "body": []}
            infunc = True
        elif line[0] == "~" and infunc:
            curfunc["body"].append(" ".join(line[1:]))
        elif line[0] == "end":
            if line[1] == "fn":
                infunc = False
                fns[fnName] = curfunc
        elif line[0] == "@":
            parse(
                replacevar(
                    "\n".join(fns[line[1]]["body"]),
                    merge_two_dicts(
                        variables, dict(zip(fns[line[1]]["args"], line[2:]))
                    ),
                ),
                line[1],
            )
        elif line[0] == "if":
            op = line[2]
            l = replacevar(" ".join(line), variables).split(" ")
            if op == "==":
                if l[1] == l[3]:
                    parse("\n".join(fns[line[4]]["body"]), line[4])
            elif op == "!=":
                if l[1] != l[3]:
                    parse("\n".join(fns[line[4]]["body"]), line[4])
            elif op == ">=":
                if int(l[1]) >= int(l[3]):
                    parse("\n".join(fns[line[4]]["body"]), line[4])
            elif op == "<=":
                if int(l[1]) <= int(l[3]):
                    parse("\n".join(fns[line[4]]["body"]), line[4])
        elif line[0] == "while":
            op = line[2]
            l = replacevar(" ".join(line), variables).split(" ")
            if op == "==":
                while l[1] == l[3]:
                    parse("\n".join(fns[line[4]]["body"]), line[4])
            elif op == "!=":
                while l[1] != l[3]:
                    parse("\n".join(fns[line[4]]["body"]), line[4])
            if op == ">=":
                while int(l[1]) >= int(l[3]):
                    parse("\n".join(fns[line[4]]["body"]), line[4])
            if op == "<=":
                while int(l[1]) <= int(l[3]):
                    parse("\n".join(fns[line[4]]["body"]), line[4])
        elif line[0] == "py":
            codeToExecute = replacevar(" ".join(line[2:]), variables)
            # print(variables[line[1]])
            variables[line[1]] = eval(codeToExecute)
        elif line[0] == "saveinput":
            variables[line[1]] = input(replacevar(" ".join(line[2:]), variables))
        elif line[0] == "->include":
            with open(line[1] + ".bracket", "r") as f:
                parse(
                    f.read()
                    + "\nvar runImports := true\nif #[runImports] == true imports",
                    0,
                )
        elif line[0] == "->f":
            with open(line[1] + ".bracket", "r") as f:
                parse(f.read())
        elif line[0] == "sys":
            os.system(" ".join(line[1:]))
        elif line[0] == "vars":
            print(variables)
        elif line[0] == "idx":
            variables[line[1]] = variables[line[2]][int(line[3])]
        elif line[0] == "sleep":
            time.sleep(int(line[1]) / 1000)

        else:
            if line[0] != "" and line[0] != "args":
                print(
                    Base.FAIL
                    + f'[{c}] KeywordError: {line[0]} is not a keyword.To call a function, use the keyword "@"'
                    + Base.END
                )

                sys.exit()


with open("main.bracket", "r") as f:
    parse(f.read() + "\nvar runMain := true\nif #[runMain] == true main", 0)
