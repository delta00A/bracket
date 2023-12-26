import os
import sys

variables = {}
fns = {}
def replacevar(line, vars):
  if "#{input}" in line:
    line = line.replace("#{input}", input())
  for ob in vars:
    line = line.replace("#["+ob+"]", str(variables[ob]))

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
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  # Formatting
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'    
  # End colored text
  END = '\033[0m'
  NC ='\x1b[0m' # No Color


c = 0
def parse(text):
  global c
  
  global variables
  text = text.replace("\\n","\n").split("\n")
  infunc = False
  curfunc = []
  fnName = ""
  for lineUnformatted in text:
    c +=1

    line = replacevar(lineUnformatted, variables).split(" ")
    if line[0][0:1] == ";":
      pass
    elif line[0] == "var":
      if line[2] != ":=":
        print(Base.FAIL+f"[{c}] SyntaxError: Invalid syntax. Instead of "+line[2]+" use :="+Base.END)
        sys.exit()
      
      l = replacevar(' '.join(line), variables).split(" ")
      #variables.append((l[1], " ".join(l[3:])))
      variables[l[1]] = " ".join(l[3:])
  
    elif line[0] == "print":
      content = replacevar(' '.join(line[1:]), variables)
      print(content)
    elif line[0] == "fn":
      fnName = line[1]
      for ob in line[2:]:
        #variables.append((fnName+"."+ob, ""))
        variables[fnName+"."+ob] = ""
      curfunc = []
      infunc = True
    elif line[0] == "~" and infunc:
      curfunc.append(replacevar(' '.join(line[1:]), variables))
    elif line[0] == "end":
      if line[1] == "fn":
       infunc = False
       fns[fnName] = curfunc
    elif line[0] == "@":
      parse('\n'.join(fns[line[1]]))
    elif line[0] == "if":
      op = line[2]
      l =  replacevar(' '.join(line), variables).split(" ")
      if op == "==":
        if l[1] == l[3]:
          parse('\n'.join(fns[line[4]]))
      elif op == "!=":
        if l[1] != l[3]:
          parse('\n'.join(fns[line[4]]))
      elif op == ">=":
        if int(l[1]) >= int(l[3]):
          parse('\n'.join(fns[line[4]]))
      elif op == "<=":
        if int(l[1]) <= int(l[3]):
          parse('\n'.join(fns[line[4]]))
    elif line[0] == "while":
      op = line[2]
      l =  replacevar(' '.join(line), variables).split(" ")
      if op == "==":
        while l[1] == l[3]:
          parse('\n'.join(fns[line[4]]))
      elif op == "!=":
        while l[1] != l[3]:
          parse('\n'.join(fns[line[4]]))
      if op == ">=":
          while int(l[1]) >= int(l[3]):
            parse('\n'.join(fns[line[4]]))
      if op == "<=":
          while int(l[1]) <= int(l[3]):
           parse('\n'.join(fns[line[4]]))
    elif line[0] == "py":
      codeToExecute = replacevar(' '.join(line[2:]), variables)
      #print(variables[line[1]])
      variables[line[1]] = eval(codeToExecute)
    elif line[0] == "saveinput":
      print(replacevar(' '.join(line[2:]), variables))
      variables[line[1]] = input()
    elif line[0] == "->include":
      with open(line[1]+".bracket", 'r') as f:
          parse(f.read()+"\nvar runImports := true\nif #[runImports] == true imports")
    elif line[0] == "sys":
        os.system(' '.join(line[1:]))
    else:
      if line[0] != "":
        print(Base.FAIL+f"[{c}] KeywordError: {line[0]} is not a keyword.To call a function, use the keyword \"@\""+Base.END)
        
        sys.exit()
with open("main.bracket", 'r') as f:
  parse(f.read()+"\nvar runMain := true\nif #[runMain] == true main")
