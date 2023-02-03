import telebot

CHAVE_API = '5856611792:AAHx1KEt6adrjk8RhgvGV1FgqFU_Uks3aJ8'

bot = telebot.TeleBot(CHAVE_API)


#-------Recebimento de pedido----------#
@bot.message_handler(commands=['entrega'])
def salgado(mensagem):
    texto_pizza = """ Seu pedido chegará no seu endereço em breve... Obrigado e seja bem vindo!

Clique ou digite /start para voltar ao menu inicial!
    """
    bot.send_message(mensagem.chat.id, texto_pizza)
    
@bot.message_handler(commands=['retirada'])
def salgado(mensagem):
    texto_pizza = """ Seu pedido estará pronto em breve, venha pegá-lo em nosso restaurante... Obrigado e volte sempre!

Clique ou digite /start para voltar ao menu inicial! 
    """
    bot.send_message(mensagem.chat.id, texto_pizza)



#-------Sabores de pizza----------#
@bot.message_handler(commands=['mussarela'])
def salgado(mensagem):
    texto_pizza = """ Olá este sabor fica R$ 15,00... Como vai receber seu pedido? (Escolha uma opção):
    
/entrega Entrega
/retirada Retirada

Clique ou digite /pizza para voltar ao menu de sabores! 
"""
    bot.send_message(mensagem.chat.id, texto_pizza)
    
@bot.message_handler(commands=['calabresa'])
def salgado(mensagem):
    texto_pizza = """ Olá este sabor fica R$ 20,00... Como vai receber seu pedido? (Escolha uma opção):
    
/entrega Entrega
/retirada Retirada 

Clique ou digite /pizza para voltar ao menu de sabores! 
"""
    bot.send_message(mensagem.chat.id, texto_pizza)



#-------Sabores do salgado--------#

@bot.message_handler(commands=['misto'])
def salgado(mensagem):
    texto_salgado = """ Olá este sabor fica R$ 4,50... Como vai receber seu pedido? (Escolha uma opção):
    
/entrega Entrega
/retirada Retirada
    
Clique ou digite /salgado para voltar ao menu de sabores! """
    bot.send_message(mensagem.chat.id, texto_salgado)


@bot.message_handler(commands=['carne'])
def salgado(mensagem):
    texto_salgado = """ Olá este sabor fica R$ 4,50... Como vai receber seu pedido? (Escolha uma opção):
    
/entrega Entrega
/retirada Retirada

Clique ou digite /salgado para voltar ao menu de sabores! """
    bot.send_message(mensagem.chat.id, texto_salgado)


@bot.message_handler(commands=['queijo'])
def salgado(mensagem):
    texto_salgado = """ Olá este sabor fica R$ 4,50... Como vai receber seu pedido? (Escolha uma opção):

/entrega Entrega
/retirada Retirada

Clique ou digite /salgado para voltar ao menu de sabores! """
    bot.send_message(mensagem.chat.id, texto_salgado)


@bot.message_handler(commands=['frango'])
def salgado(mensagem):
    texto_salgado = """ Olá este sabor fica R$ 4,50... Como vai receber seu pedido? (Escolha uma opção):

/entrega Entrega
/retirada Retirada

Clique ou digite /salgado para voltar ao menu de sabores! """
    bot.send_message(mensagem.chat.id, texto_salgado)



#--------Menu de pedidos opcao1------#

@bot.message_handler(commands=['salgado'])
def salgado(mensagem):
    texto_salgado = """ Qual sabor você deseja? (Escolha uma opção):

Sabores:
/misto Misto
/carne Carne
/queijo Queijo
/frango Frango

Clique ou digite /cardapio para voltar ao cardápio! """
    bot.send_message(mensagem.chat.id, texto_salgado)
    

@bot.message_handler(commands=['pizza'])
def pizza(mensagem):
    texto_pizza = """ Qual sabor você deseja? (Escolha uma opção):

Sabores:
/mussarela Mussarela
/calabresa Calabresa

Clique ou digite /cardapio para voltar ao cardápio! """
    bot.send_message(mensagem.chat.id, texto_pizza)





#-------BOTÕES DA MENSAGEM INICIAL---------#

@bot.message_handler(commands=['cardapio'])
def opcao1(mensagem):
    texto = """ Cardápio (Escolha uma opção):

/salgado Salgados
/pizza Pizzas

Clique ou digite /start para voltar ao menu inicial! """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['reclamar'])
def opcao2(mensagem): 
    bot.send_message(mensagem.chat.id, 'Para fazer uma reclamação, mande um email para reclamar@gmail.com')

@bot.message_handler(commands=['feedback'])
def opcao3(mensagem):
    #print(mensagem) #--> MOSTRA MAIS INFORMAÇÕES DA MENSAGEM NO TERMINAL
    bot.reply_to(mensagem, 'Obrigado! Volte sempre...')  #--> send_message(mensagem.chat.id, '...') RESPONDE A MENSAGEM SEM MARCAR 
    #bot.reply_to(mensagem, 'Obrigado! Bem vindo sempre...')   # bot.reply_to(mensagem, '...') RESPONDE MARCANDO A ULTIMA MENSAGEM




#----FUNÇÕES INICIAIS E ONDE O USUARIO VAI ESTAR CASO NÃO ESCOLHA NADA, SEMPRE DEIXAR POR ULTIMO----# 

def verificar(mensagem):   #RECEBE A MENSAGEM E RETORNA O TEXTO
    #if mensagem.text == "Opa":
        return True
    #else:
        #return False

@bot.message_handler(func=verificar)    #O BOT SÓ RESPONDE APENAS QUANDO DIGITAR A MENSAGEM QUE ESTA DENTRO DO COMANDO /'mensagem' --> #@bot.message_handler(commands=['ola'])
def responder(mensagem):      #RESPONDE A MENSAGEM DO USUARIO
    texto = """ Olá! Seja bem vindo ao restaurante... O que você deseja?
(Clique no Item):

Quero fazer fazer um pedido --> /cardapio
Quero reclamar um pedido --> /reclamar
Quero fazer um feedback --> /feedback

Responder qualquer outra coisa não irá funcionar, por favor clique em uma das opções acima!"""
    bot.reply_to(mensagem, texto)


bot.polling()  #BOT.POLLING PEGA AS INFORMAÇÕES DAS CONVERSAS E RODA O BOT


#foi instalado a biblioteca pip install pytelegrambotapi