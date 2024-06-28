BD=[    {"Album":"Taylor Swift",
            "Caracteristicas": {"country": 10, "pop": 2, "alternativo": 0, "love": 7, "melancolica": 0} },
        {"Album":"Fearless",
            "Caracteristicas": {"country": 5, "pop": 7, "alternativo": 0, "love": 9, "melancolica": 0} },
        {"Album":"Speak Now",
            "Caracteristicas": {"country": 2, "pop": 7, "alternativo": 0, "love": 6, "melancolica": 0} },
        {"Album":"Red",
            "Caracteristicas": {"country": 3, "pop": 9, "alternativo": 0, "love": 8, "melancolica": 3} },
        {"Album":"1989",
            "Caracteristicas": {"country": 0, "pop": 10, "alternativo": 2, "love": 8, "melancolica": 0} },
        {"Album":"Reputation",
            "Caracteristicas": {"country": 0, "pop": 6, "alternativo": 8, "love": 7, "melancolica": 4} },
        {"Album":"Lover",
            "Caracteristicas": {"country": 0, "pop": 9, "alternativo": 0, "love": 10, "melancolica": 0} },
        {"Album":"Folklore",
            "Caracteristicas": {"country": 4, "pop": 6, "alternativo": 9, "love": 7, "melancolica": 8} },
        {"Album":"Evermore",
            "Caracteristicas": {"country": 6, "pop": 3, "alternativo": 9, "love": 6, "melancolica": 9} },
        {"Album":"Midnights",
            "Caracteristicas": {"country": 0, "pop": 7, "alternativo": 2, "love": 6, "melancolica": 4} }]

caracteristicas = {1: "country", 2: "pop", 3: "alternativo", 4: "love", 5: "melancolica"}

#Função para pegar so numeros naturas no intervalo de 1 a 6, que serão usados depois
def numeroNatural(pergunta):
    while True:
        try:   
            resposta=int(input(pergunta)) 
        except:
            print("Só numeros por favor!")
            print("Tente novamente!")
        else:
            if resposta >= 1 and resposta <= 6: return resposta
            print("O numero precisa ser um valor entre 1 e 6!")
            print("Tente navamente!")

#Função que pega os numeros naturais cria uma lista com eles, que representa cada caracteristica
def selecionarCaracterisitcas(pergunta):
    caracteristicasSelecionadas = []
    while True:
        caracteristica = numeroNatural(pergunta)
        if caracteristica == 6 or len(caracteristicasSelecionadas) == 5:
            break
        if caracteristica not in caracteristicasSelecionadas:
            caracteristicasSelecionadas.append(caracteristica)
        else:
            print("Caracteristica já selecionada!")
    return caracteristicasSelecionadas

#Função que calcula a porcentagem de cada album de acordo com as caracteristicas selecionadas
def calcularPesos(selecionado):
    for album in BD:
        album["peso"] = 0
        for caracteristica in selecionado:
            album["peso"] += album["Caracteristicas"][caracteristicas[caracteristica]]
        #divide by album total
        album["peso"] = album["peso"] / sum(album["Caracteristicas"].values())

#Função que verifica se a pessoas respondeu a pergunta so com "s" ou "n"
def perguntaSimouNao(pergunta):
    while True:
        resposta=input(pergunta).upper()
        if resposta == "S" or resposta == "N": return resposta
        print("A resposta tem que ser S ou N! Tente novamente!")

#Função que printa album e possibilidade
def printAlbums():
    for album in BD:
        percentage = album["peso"] * 100 
        percentage = round(percentage, 2)
        print(album["Album"] + ":", percentage,"%")

fimdoPrograma= False
while not fimdoPrograma:
    print("Esse programa irá te recomendar um album da Taylor Swift dependendo das caracteristicas que você escolher!")
    print("As caracteristicas são: ")
    print("1) Country")
    print("2) Pop")
    print("3) Alternativo")
    print("4) Love")
    print("5) Melancólica")
    print("6) Não quero mais escolher caracteristicas")
    selecionado = selecionarCaracterisitcas("Escolha uma das caracteristicas acima: ")
    calcularPesos(selecionado)
    print("\nA porcentagem de compatibilidade dos albuns e as caracteristicas que você escolheu é: ")
    BD.sort(key=lambda x:x["peso"], reverse=True)
    printAlbums()
    print("Entao o album mais recomendado é: ", max(BD, key=lambda x:x["peso"])["Album"])
    resp = ""
    resp=perguntaSimouNao("Você gostaria de olhar mais uma recomendação de um album da Taylor Swift? ")    
    if resp == "N":
        fimdoPrograma = True
print("Fim do programa!")