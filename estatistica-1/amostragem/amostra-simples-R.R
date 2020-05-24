#Amostra Simples

# usa o conjunto de dados iris existente no R
dim(iris)

#criar uma amostra contendo 0 e 1 entre 150 elementos com probabilidade de 50% para ambos.
amostra = sample(c(0,1), 150, replace=TRUE, prob=c(0.5,0.5))

#verificar a quantidade de amostras de cada tipo
length(amostra[amostra==1])
length(amostra[amostra==0])

# permitir que possa ser repetido o mesmo experimento
set.seed(2345)
sample(c(100), 1)

