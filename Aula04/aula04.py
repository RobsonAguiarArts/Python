#Tipos de Dados

#Tipos simples
x=1 #int
x = "CFB Cursos" #string
x = 15.6 #float
x = False #bool

#Tipos complexos
n1=5;n2=2;x=complex(n1,n2) #complex

#Coleções
x=["Carro","Aviao", "Navio",1,18.3,True] #List / Array
x=("Carro","Aviao", "Navio",1,18.3,True) #Tupla
x=range(0,100,1) #List
x={  #Dictionary
  "canal":"CFB Cursos",
  "curso":"Curso de Python",
  "nome":"Bruno"
}
# print(x.real)
# print(x.imag)
x={5,4,5,4,87,4,6} #set não repete valores
x=frozenset({5,4,5,4,87,4,6}) #set bloqueado
print("Valor:  " +str(x))
print("Tipo: " +str(type(x)))