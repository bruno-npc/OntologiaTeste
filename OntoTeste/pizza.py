from owlready2 import *

#Necessario colocar a localização do arquivo owl
onto = get_ontology("c:/Users/Bruno/Documents/OntoTeste/pizzaBr.owl")
onto.load()

# Crie novas classes na ontologia, misturando construções OWL e métodos Python:
print("\n######################### Classes #########################")
with onto:
    class Pizza(Thing):
        def comer(self): print("Preferencia pizza ")

    class Cobertura (Thing):
        pass

    class tem_cobertura(Pizza >> Cobertura):
      python_name = "escolhaPizza"

    class PizzaNaoVegetariana(Pizza):
       equivalent_to = [Pizza & tem_cobertura.min(4, Cobertura)]
       def comer(self): print("Eu não sou vegetariano!")

    class PizzaVegetariana(Pizza):
       equivalent_to = [Pizza & tem_cobertura.exactly(2, Cobertura)]
       def comer(self): print("Eu sou ovolactovegetariano!")


print("\n############################################################################")
Tomate = Cobertura(onto.CoberturaTomate)
Queijo = Cobertura(onto.CoberturaQueijo)
Carne = Cobertura(onto.CoberturaCarne)
Peixe = Cobertura(onto.CoberturaPeixe)

AllDifferent([Queijo, Tomate, Carne, Peixe])

print("\n############################################################################")
# Pedidos com 2 ingredientes são "vegetarianos"
pedido1 = Pizza(escolhaPizza = [Tomate, Queijo])

# Pedidos com no minimo 4 ingredientes não são "vegetarianos"
pedido2 = Pizza(escolhaPizza = [Carne, Peixe, Queijo, Tomate])

close_world(Pizza)

print("\n############################ Teste hermit ############################")
sync_reasoner_hermit()

pedido1.comer()
pedido2.comer()