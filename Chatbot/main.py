print("👋 Olá! Bem-vindo(a) ao nosso Chatbot de Atendimento! \n Estamos aqui para ajudar.\n Como posso tornar o seu dia mais fácil hoje? 😊")
print("")
print("Sobre qual assunto deseja falar? \n [1] Acesso às informações acadêmicas \n [2] Solicitação de documentos \n [3] Atualização de informações \n [4] Envio de feedback")

resposta = int(input("Digite o número que deseja obter inforações: "))

if resposta == 1:
	print("Resposta 1")
elif resposta == 2:
	print("Resposta 2")	
elif resposta == 3:
	print("Resposta 3")	
elif resposta == 4:
	print("Resposta 4")	
else:
	print("Número inválido!")