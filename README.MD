# Documentation
After downloading the required libraries, to load the initialization code, say "code.txt", we run the command:
```
python main.py code.txt
```
If we add True to the end we get the values of every point and line.
```
python main.py code.txt True
```

The initialization code is separated into 4 parts divided by a line with just "~~~" in it. Of these 4 parts, none of them are strictly needed, but like you need them to actually do anything lol.
## Part I
In this part, you declare the variables. By default all the variables are real. If you want a variable to be positive, you can add "_p" after it. For example if you want to define 3 real variables a,b,c where c is positive, you can type:
```
a b c_p
```
Note that the variable c will not be saved as c_p but just as c.
## Part II
This is mostly where the magic happens. We currently have points and lines. Points are in the cartesian plane and defined as [x,y] where these are its x and y co-ordinates. Lines are in the form [a,b,c] describing the line ax+by+c=0. We have the following functions we can do:
### Point operations
```
Pt A def x y
```
A point A is defined with co-ordinates [x,y].
```
Pt A midpoint B C
```
B and C are points which have been defined before. Here, A will be their midpoint.
```
Pt A intersect L1 L2
```
L1 and L2 are lines which have been defined before. Here, A will be their intersection.
```
Pt A section B C m n
```
B and C are points which have been defined before. m and n are real numbers. Here, A is the point on BC such that AB:AC=m:n.
```
Pt A project L B
```
Here L is a pre-defined line and B is a pre-defined point. Here, A will be the projection of B onto L.
```
Pt A reflect L B
```
Here L is a pre-defined line and B is a pre-defined point. Here, A will be the reflection of B across L.

### Line operations

```
Line L def a b c
```
A line L will be defined as ax+by+c=0.
```
Line L 2poi A B
```
A line L will be defined passing through two pre-defined points A and B.
```
Line L perp L1 A
```
A line L perpendicular to L1 and passing through A will be defined
```
Line L angbis L2 L3
```
The line L will be one of the angle bisectors of two pre-defined lines L2 and L3.

## Part III
To understand Parts III and IV, we need to know how the lines and points are saved in the code. The lines are kept in a dictionary called "lines" and the points are kept in a dictionary called "points". We already know the format of a line and a point. So, this part will evaluate the values of each of the lines. For example, if we type:
```
-lines['L'][0]/lines['L'][1]
```
If L is the line ax+by+c=0, it will return -a/b, which is the slope of the line.
## Part IV
This is the same as the previous section but instead of evaluating the expression, it will find the values when the expression is 0. It will solve for every variable, in the order they were when defined in Part I. For example, in the given test file, the variables are (a,b,c), and after solving the expression we get [(-b/2, b, c)] meaning that there is only one solution, when a=-b/2, b=b and c=c.
