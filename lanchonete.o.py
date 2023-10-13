#leitura de comanda para lanchonete#

class Lanchonete:
    def __init__(self):
        self.cardapio = {"Hamburguer": 10.0, "Batata Frita": 5.0, "Refrigerante": 3.0, "Hot Dog": 7.0, "Pizza": 12.0}
        self.abreviacoes = {"H": "Hamburguer", "BF": "Batata Frita", "R": "Refrigerante", "HD": "Hot Dog", "P": "Pizza"}
        self.comanda = []

    def mostrar_cardapio(self):
        print("Cardápio:")
        for abreviacao, item in self.abreviacoes.items():
            preco = self.cardapio[item]
            print(f"{abreviacao}: {item} - R${preco:.2f}")

    def adicionar_item(self, pedido):
        if pedido in self.abreviacoes:
            item = self.abreviacoes[pedido]
            self.comanda.append((item, self.cardapio[item]))
            print(f"{item} adicionado à comanda.")

    def calcular_total(self):
        total = sum(item[1] for item in self.comanda)
        return total


# Exemplo de uso
lanchonete = Lanchonete()
lanchonete.mostrar_cardapio()

while True:
    pedido = input("Faça seu pedido (ou 'sair' para encerrar): ").upper()

    if pedido == 'SAIR':
        break

    lanchonete.adicionar_item(pedido)

total_comanda = lanchonete.calcular_total()
print(f"\nTotal da comanda: R${total_comanda:.2f}")
