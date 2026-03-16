#-----------------------------SECTION 1------------------------------
print("Hello, Python")

print("\nThe itsy bitsy spider\nclimbed up the waterspout.")
print("\nDown came the rain\nand washed the spider out.")

print("\nThe itsy bitsy spider", "climbed up","the waterspout.")

print("My name is", "Python.")
print("Monty Python.")

print("My name is ", end="")
print("Monty Python.")

print("My", "name", "is", "Monty", "Python.", sep="-")

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

print("Programming","Essentials","in",end="...",sep="***")
print("Python")

print("    *    ","    *    ",sep=" --- ")
print("   * *   ","   * *   ",sep=" --- ")
print("  *   *  ","  *   *  ",sep=" --- ")
print(" *     * "," *     * ",sep=" --- ")
print("***   ***","***   ***",sep=" --- ")
print("  *   *  ","  *   *  ",sep=" --- ")
print("  *   *  ","  *   *  ",sep=" --- ")
print("  *****  ","  *****  ",sep=" --- ")


#-----------------------------SECTION 2------------------------------

print("2")
print(2)

print(0o123)
print(0x123)

print("I like \"Monty Python\"")
print('I like "Monty Python"')

print('I\'m Monty Python.')

print(True > False)
print(True < False)

print('"I\'m"',"\n\"\"learning\"\"","\n\"\"\"Python\"\"\"")


#-----------------------------SECTION 3------------------------------
print(2+2)

print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

#always float
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print(6 // 4)
print(6. // 4)

print(-6 // 4)
print(6. // -4)

print(14 % 4)

print(-4 - 4)
print(4. - 8)
print(-1.1)

print(9 % 6 % 2)

print(2 ** 2 ** 3)

#-----------------------------SECTION 4------------------------------
var = 1
print(var)


account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

var = var + 1
print(var)

var = 100
var = 200 + 300
print(var)

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

john = 3
mary = 5
adam = 6

print(john , mary,adam, sep=",")

total_apples = john + mary + adam
print("Total number of apples:",total_apples,sep="")

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print()
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

x = 0
x = float(x)
y = 3*x**3-2*x**2+3*x-1
print("y =", y)

x = 1
x = float(x)
y = 3*x**3-2*x**2+3*x-1
print("y =", y)

x = -1
x = float(x)
y = 3*x**3-2*x**2+3*x-1
print("y =", y)

#-----------------------------SECTION 5------------------------------

#this program computes the number of seconds in a given number of hours

a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours

#-----------------------------SECTION 6------------------------------

#print("Tell me anything...")
#anything = input()
#print("Hmm...", anything, "... Really?")

#anything = input("Tell me anything...")
#print("Hmm...", anything, "...Really?")

#anything = float(input("Enter a number: "))
#something = anything ** 2.0
#print(anything, "to the power of 2 is", something)

#leg_a = float(input("Input first leg length: "))
#leg_b = float(input("Input second leg length: "))
#print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)

#fnam = input("May I have your first name, please? ")
#lnam = input("May I have your last name, please? ")
#print("Thank you.")
#print("\nYour name is " + fnam + " " + lnam + ".")

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#leg_a = float(input("Input first leg length: "))
#leg_b = float(input("Input second leg length: "))
#print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

#valor1 =float(input("Insert value 1:"))
#valor2 =float(input("Insert value 2:"))

#print("a soma de ambos valores é igual a: " + str(valor1 + valor2))
#print("a soma de ambos valores é igual a: " + str(valor1 - valor2))
#print("a soma de ambos valores é igual a: " + str(valor1 * valor2))
#print("a soma de ambos valores é igual a: " + str(valor1 / valor2))

#print("\nThat's all, folks!")

#x = float(input("Enter value for x: "))
#y = 1./(x + 1./(x + 1./(x + 1./x)))
#print("y =", y)

horacomeco = int(input("Insira hora de começo: "))
mincomeco = int(input("Insira minutos de começo: "))
duracao = int(input("Insira quantos minutos irá demorar:"))

minutos = mincomeco + duracao
horas = horacomeco + minutos // 60
minutos = minutos % 60
horas = horas % 24
print(horas, ":", minutos, sep="")



