#vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles
num1 = int(input('Digite o primeiro número: ')) #vamos pedir o primeiro número  
num2 = int(input('Digite o segundo número: ')) #vamos pedir o segundo número
#vamos realizar a operação de soma entre os dois números
operacao = input('Digite a operação desejada: ') #vamos pedir a operação desejada
#vamos realizar a operação desejada entre os dois números
if operacao == '+':
    resultado = num1 + num2 #vamos realizar a operação de soma entre os dois números        
elif operacao == '-':
    resultado = abs(num1 - num2)  # Usando abs() para retornar o valor absoluto
elif operacao == '*':
    resultado = num1 * num2
#vamos realizar a operação de multiplicação entre os dois números
elif operacao == '/':
    resultado = num1 / num2
#vamos realizar a operação de divisão entre os dois números 
else:
    resultado = 'Operação inválida'
#vamos mostrar o resultado da operação para o usuário   
print('O resultado da operação é: ', resultado) 
#vamos mostrar o resultado da operação para o usuário




