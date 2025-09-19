from exercicio3_ import Trip

trip0 = Trip("Itabirito")
trip1 = Trip("Belo Horizonte")
trip2 = Trip("Ouro Preto")
trip3 = Trip("Nova lima")
trip4 = Trip("Rio Acima")

print("Olá, temos algumas dicas de turismo para você.")
traveler = input("Me diga seu nome para comerçamos\n")
print(f"{traveler}, temos 5 destinos que combinam com você"
    '''
      [0] - Itabirito
      [1] - Belo Horizonte
      [3] - Ouro Preto
      [4] - Nova Lima
      [5] - Rio Acima
    
    '''
)

choice = int(input("Selecione o que mais te agrada.\n"))
list_trip = [trip0, trip1, trip2, trip3, trip4]

for option in list_trip:
    if choice >= 5:
        print("Opção inválida")
        break
    else:
        print(f"{traveler} sua viagem para {list_trip[choice].destiny} está marcada.")
        print("Boa viagem!!")
        break