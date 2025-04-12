# (My) Proposed stucture for your progra ms is:

def solver(a,b,c):
    ...
    print(soluion)

# Main
while(reading_cases):
    a, b, c = read_input()
    solver(a, b, c)

#-----------------------------------------------------------------
#  Another structure:
def read_input():
    while True:
        a = input().strip()
        if len(a) == 0: # Or a == "0" or others
            return
        bs = []
        for _ in range(int(a)):
            bs.append(int(input()))
            yield bs
# Main
for case in read_cases():
    solver(*case)



# Problems: 
# - Steps
import sys 
n = int(sys.stdin.readline())

for _ in range(n):
    line = sys.stdin.readline()
    i, j = [int(x) for x in line.split(' ')]
    step = 1
    steps = 0 
    while j-i-2*step > 0:
        i+=step
        j-=step
        step +=1
        steps+=2
    if j-i>step:
        i+=step
        step+=1
    if j-i>0:
        steps+=1
    print(steps)

# - Maximum Sum

        