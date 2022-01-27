num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

# isnumeric isdigit isdecimal

# Números e positivos (ex: 1,2,3,4,5,6,7,8,...)
print(num1.isnumeric()) # Estas variáveis podem ser convertidas para número inteiro (int)
print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print ("A soma dos números é: ", num1 + num2)

else:
    print("Não possível realizar a operação. Verifique se foi digitado números inteiros e positivos.")

try:
    num1 = float(num1)
    num2 = float(num2)

    print("A subtraçã dos números é: ", num1 - num2)

except:
    print("ERROR")
