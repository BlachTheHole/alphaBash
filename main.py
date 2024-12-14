import sympy
import sys
from sympy.solvers import solve
from sympy.parsing.sympy_parser import parse_expr


f = open(sys.argv[1], "r")
code = []
for line in f:
    if line[0] != '#':
        code.append(line[0:-1].strip())
mode = 0
names = ""
vars = {}
points = {}
lines = {}
circles = {}
for line in code:
    if line == "~~~":
        if mode == 0:
            names.strip()
            for i in names.split():
                if i[-2:] == "_p":
                    vars[i[:-2]] = sympy.Symbol(i[:-2], real=True, positive=True)
                else:
                    vars[i] = sympy.Symbol(i, real=True)
        mode += 1
    else:
        if mode == 0:
            names += line + " "
        if mode == 1:
            instr = line.split()
            if instr[0] == "Pt":
                if instr[2] == "def":
                    points[instr[1]] = [sympy.simplify(parse_expr(instr[3])), sympy.simplify(parse_expr(instr[4]))]
                elif instr[2] == "midpoint":
                    points[instr[1]] = [sympy.simplify((points[instr[3]][0]+points[instr[4]][0])/2), sympy.simplify((points[instr[3]][1]+points[instr[4]][1])/2)]
                elif instr[2] == "intersect":
                    points[instr[1]] = [sympy.simplify((lines[instr[3]][2]*lines[instr[4]][1]-lines[instr[3]][1]*lines[instr[4]][2])/(lines[instr[3]][1]*lines[instr[4]][0]-lines[instr[3]][0]*lines[instr[4]][1])), sympy.simplify((lines[instr[3]][2]*lines[instr[4]][0]-lines[instr[3]][0]*lines[instr[4]][2])/(-lines[instr[3]][1]*lines[instr[4]][0]+lines[instr[3]][0]*lines[instr[4]][1]))]
                elif instr[2] == "section":
                    points[instr[1]] = [sympy.simplify((points[instr[3]][0]*parse_expr(instr[6])+points[instr[4]][0]*parse_expr(instr[5]))/(parse_expr(instr[6])+parse_expr(instr[5]))),sympy.simplify((points[instr[3]][1]*parse_expr(instr[6])+points[instr[4]][1]*parse_expr(instr[5]))/(parse_expr(instr[6])+parse_expr(instr[5])))]
                elif instr[2] == "project":
                    interm = sympy.simplify((lines[instr[3]][0]*points[instr[4]][0]+lines[instr[3]][1]*points[instr[4]][1]+lines[instr[3]][2])/((lines[instr[3]][0]**2)+(lines[instr[3]][1]**2)))
                    points[instr[1]] = [sympy.simplify(points[instr[4]][0]-interm*lines[instr[3]][0]), sympy.simplify(points[instr[4]][1]-interm*lines[instr[3]][1])]
                elif instr[2] == "reflect":
                    interm = 2*sympy.simplify((lines[instr[3]][0]*points[instr[4]][0]+lines[instr[3]][1]*points[instr[4]][1]+lines[instr[3]][2])/((lines[instr[3]][0]**2)+(lines[instr[3]][1]**2)))
                    points[instr[1]] = [sympy.simplify(points[instr[4]][0]-interm*lines[instr[3]][0]), sympy.simplify(points[instr[4]][1]-interm*lines[instr[3]][1])]
            if instr[0] == "Line":
                if instr[2] == "def":
                    lines[instr[1]] = [sympy.simplify(parse_expr(instr[3])), sympy.simplify(parse_expr(instr[4])), sympy.simplify(parse_expr(instr[5]))]
                elif instr[2] == "2poi":
                    lines[instr[1]] = [sympy.simplify(points[instr[4]][1]-points[instr[3]][1]), sympy.simplify(points[instr[3]][0]-points[instr[4]][0]), sympy.simplify(points[instr[3]][1]*points[instr[4]][0]-points[instr[3]][0]*points[instr[4]][1])]
                elif instr[2] == "perp":
                    lines[instr[1]] = [-sympy.simplify(lines[instr[3]][1]), sympy.simplify(lines[instr[3]][0]), sympy.simplify(lines[instr[3]][1]*points[instr[4]][0]-points[instr[4]][1]*lines[instr[3]][0])]
                elif instr[2] == "angbis":
                    a_1, a_2, a_3 = lines[instr[3]]
                    b_1, b_2, b_3 = lines[instr[4]]
                    sqrt_L1 = sympy.sqrt(a_1**2 + a_2**2)
                    sqrt_L2 = sympy.sqrt(b_1**2 + b_2**2)
                    lines[instr[1]] = [sympy.simplify((a_1/sqrt_L1)-(b_1/sqrt_L2)), sympy.simplify((a_2/sqrt_L1)-(b_2/sqrt_L2)), sympy.simplify((a_3/sqrt_L1)-(a_4/sqrt_L2))]
        if mode == 2:
            print(line)
            expr = (sympy.simplify(sympy.cancel(eval(line))))
            print(sympy.simplify(expr))
        if mode == 3:
            print(line)
            expr = (sympy.simplify(sympy.cancel(eval(line))))
            print(solve(sympy.factor(sympy.simplify(sympy.cancel(eval(line)))), vars))
            
if (len(sys.argv) > 2) and (sys.argv[2]):
    for point in points.keys():
        print(f"{point}: ({points[point][0]},{points[point][1]})")
    for line in lines.keys():
        print(f"{line}: {lines[line][0]}x + {lines[line][1]}y + {lines[line][2]} = 0")
f.close()
