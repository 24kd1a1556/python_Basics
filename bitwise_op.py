#bitwise operators
# & , | , ~ , ^ , << , >>


# & means 1&1 only 1 in every condition it will become 0
a = 5 #0101
b = 7 #0111
print(a & b)  #0101 it prints 5

# | means except 0|0 only "0" all conditions r "1"
a = 8    #1000
b = 4    #0100
print( a | b)   #1100 (12)

# ~ means  if 1^1 and 0^0 then o/p is 0
a = 5  #0101
b = 6  #0110   
print( a^b)  #0011 (3)

# ~ 0 will replace with 1 and 1 with 0
a = 6 #0110
print(~a) #1001  find 2's complement then 
# 1's complement +1
#simply we can flw that no.+1
#eg:a = 6 ~a = -7

#in left shift we will gain bits
#in right shift we will loss bits
a = 5 #0101
b = 4 #0100
print(a<<2)  #0100 left side 2 bits will move a*2(power n)
print(a>>2) #0001  a/2pown++