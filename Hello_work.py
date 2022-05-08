import argparse
par = argparse.ArgumentParser()
par.add_argument("a",type = int, help = "Num 1")
par.add_argument("b",type = int, help = "Num 2")
par.add_argument("-v", "--numer", action="count", default= 0)
x = par.parse_args()
ans = x.a+x.b
print('Hi')
print(ans)
print('New Line')
