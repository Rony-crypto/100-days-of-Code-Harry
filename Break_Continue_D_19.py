#BREAK

for i in range(12):
    if(i==10):
        break      #break skips the loop
    print("5 X", i, "=", 5 * i)
print ("Exit the loop")

#CONTINUE

for i in range(12):
    if(i==10):
        print("skip the iteration")  #continue skips only iteration
        continue
    print("5 X", i, "=", 5 * i)


#EMULATING DO WHILE LOOP IN PYTHON

i = 0

while True:
    print(i)
    i+=1
    if(i%100 == 0):
        break



