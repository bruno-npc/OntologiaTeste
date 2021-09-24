from owlready2 import *

#Necessario colocar a localização do arquivo owl
onto = get_ontology("c:/Users/Bruno/Documents/OntoTeste/pizzaBr.owl")
onto.load()

# Crie novas classes na ontologia, misturando construções OWL e métodos Python:
print("\n### Nova classe ###")
with onto:
    class escolha (Thing):
        pass
       
    class Pizza(Thing):
        def comer(self): print("Preferencia pizza ")

    class tipoPizza(Pizza >> escolha):
      python_name = "escolhaPizza"

    class PizzaNaoVegetariana(Pizza):
       equivalent_to = [
         Pizza & tipoPizza.exactly(2, escolha)]
       def comer(self): print("Eu não sou vegetariano!")

    class PizzaVegetariana(Pizza):
       equivalent_to = [
         Pizza &  tipoPizza.exactly(2, escolha)]
       def comer(self): print("Eu sou ovolactovegetariano!")


Tomate = escolha("pizzaTomate")
Queijo = escolha("pizzaQueijo")
Carne = escolha("pizzaCarne")

AllDifferent([Tomate, Queijo, Carne])

pedido1 = Pizza(escolhaPizza = [Queijo, Tomate])
pedido2 = Pizza(escolhaPizza = [Carne])

close_world(Pizza)

print("\n### Teste reação ###")
sync_reasoner_hermit()

pedido1.comer()
pedido2.comer()
