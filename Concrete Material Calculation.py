#amount of materials
cem_amt = int(input("Enter Cement Amount = "))
san_amt = int(input("Enter Sand Amount = "))
aggre_amt = int(input("Enter Aggregate Amount = "))
#Ratio calculation
cq = float(input("Concrete Qty = "))
mratio =input("M-num = ")
cem = float(input("Cement ratio = "))
san = float(input("Sand ratio = "))
aggre = float(input("Aggregate ratio = "))
print("Concrete ratio = ",mratio,"=",cem,":",san,":",aggre)

con_ratio =float(input("Constant Ratio = "))
total = cem+san+aggre

#qty calculation
x = (cem/total)*con_ratio*1440*cq
y = (san/total)*con_ratio*cq
z = (aggre/total)*con_ratio*cq
print("Cement = ",x,"kg")
print("Sand = ",y,"𝑚^3")
print("Aggregate = ",z,"𝑚^3")

#bags and units calculation
cem_bag = x/50
san_unit = y/2.831
aggre_unit = z/2.831
print(cem_bag," bags")
print(san_unit," unit")
print(aggre_unit," unit")

#Amount calculation
cement = cem_amt*x
sand = san_amt*y
aggregate = aggre_amt*z

#Amount printing
print("Cement = Rs:",cement)
print("Sand = Rs:",sand)
print("Aggregate = Rs:",aggregate)