# Classes--->
##Trabalhando com orientação a objetos em python utilizamos as classes para facilitar nosso codigo


class Clientes:
    pass


class Produtos:
    pass


## criei 2 classes para utilizar futuramente no meu codigo, ao invez de criar varios clientes
## E varios produtos... So preciso criar uma vez e utilizar posteriomente fazendo a interação de ambos.
## Todos meus clientes vão estar armazenado na class cliente e meus produtos na class produtos.

# Objetos--->
## Quando falamos de objetos, estamos criando um conjuto de dados(variaveis de classe e de isntancia)
## Logo a baixo vamos ver atributos do objeto


# Atributos--->
## São caracteristicas do objeto... Qual a cor dele? Qual seu tamanho?
## Quando formos criar as classes(nesse caso os atributos) colocamos a função init.. Int significa inicializar
## Então ela vai inicar aquela classe, e dentro dos parenteses os atributos
## O selfie. vai definir a caracteristica da classe criada (nesse caso os atributos do celular)
## Em baixo colocarei um print para mostrar a funcionalidade
class Celular_atb:
    def __init__(self, cor, tamanho, armazenamento):
        self.cor = cor
        self.tamanho = tamanho
        self.armazenamento = armazenamento
        pass


celular_print = Celular_atb("vermelho", "10cm", "128gb")
print(celular_print.cor)


# Metodos---->
## Oque nossa classe consegue fazer
class Celular_mtd:
    def __init__(self, ligar, atender, Mensagems):
        self.ligar = ligar
        self.Atender = atender
        self.Mensagens = Mensagems
        pass


celular_print2 = Celular_mtd("lIGAR PARA PAI", "TIM ESTÁ LIGAndo", "oi amor")
print(celular_print2.Mensagens)


# Tipo de objetos ---->
## São as operações que o objeto surpota... Ex: o objeto é um float ou um str

# Variaveis Privadas ----->
## De inicio python não tem variavel privada... Mas conseguimos deixar um metodo ou variavel privado

# Herança ---->
## Uma classe pode herdar seus metodos e propiedades de outra classe...
## Se eu quero usar uma mesma propiedade ja criada em outra classe
## Ao inves de copiar o codigo novamente eu consigo herdar facilitando meu trabalho
## Isso tambem pode gerar uma hierarquia de classes
## Em baixo colocarei um print para mostrar a funcionalidade
class novo_celular(Celular_mtd):
    def __init__(self, ligar, atender, Mensagems):
        super().__init__(ligar, atender, Mensagems)

    novo_celular_print = Celular_mtd("ligar para escola", "atender sozinho", "ler mensagens pelo viva voz")
    print(novo_celular_print.ligar)


# Metodos herdados ---->
## São os metodos e propiedades herdados pelas classes
## Podemos adicionar novos metodos na classe herdade... Não ficamos limitados a herança
## Em baixo colocarei um print para mostrar a funcionalidade
## Herdei a classe
class cachorro():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class gato(cachorro):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.cor = cor


miau = gato("faruken", "10 anos", "preto")
print(miau.cor)


# Herança mutipla ---->
## Vai herdar duas classes diferentes ou mais para uma unica classe
## podemos usar qualquer elemento das 2
class sport ():
    def __init__(self,cor,torcedores):
        self.cor = cor
        self.torcedores = 900

        def socios(object):
            self.socios = 1500

        def publico(object):
            self.publico = 40000


class nautico (sport):
    def __init__(self,cor,torcedores,camisas):
        super().__init__(cor,torcedores)
        self.camisas = camisas

class santa_cruz(nautico):
    def __init__(self,cor,torcedores,camisas,funcionarios,):
        super().__init__(cor,torcedores,camisas)
        self.funcionarios = 300


total = santa_cruz("cor","torcedores","30","funcionarios")
print(total.torcedores)

#Sobrescrita de métodos ---->
## Modifica os metodos herdados 

class salgueiro ():
    def __init__(self,cor,torcedores):
        self.cor = cor
        self.torcedores = 900

        def socios(object):
            self.socios = 1500

        def publico(object):
            self.publico = 40000

        def total_torcida (self):
            return self.total_torcida

## Repare no total torcida eu rescrevi ele logo em baixo...
class central (salgueiro):
    def __init__(self,cor,torcedores,camisas):
        super().__init__(cor,torcedores)
        self.camisas = camisas

    def total_torcida (self):
            return super().publico() + self.socios


#Sobrecarga de metodos ---->
## Quando temos metodos iguais.. Com mesmo nome e mesma classe
## Em python esses metodos tem que ser diferentes 

#Interface
## São implementadas por classes
## Definem metodos
## Existes interfaces formais e informais 
## A formal vamos criar classes com seus metodos 
