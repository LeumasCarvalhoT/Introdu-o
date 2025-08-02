nasc = int(input("Em que ano você nasceu?: "))
ano = int(input("Agora informe o ano atual: "))
idade = ano - nasc


if (idade >= 18):
    {
        
        print("A sua idade atual é", idade, "anos, já atingiu a maioridade.")
    }

else:
    {
     
        print("A sua idade atual é", idade, "anos, ainda não alcançou a maioridade.")
    }

    