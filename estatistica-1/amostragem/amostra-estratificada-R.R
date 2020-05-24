
# Amostra estratificada
# instalar o pacote sampling
install.packages("sampling")

#carregar o pacote
library(sampling)

#gerar o estrato onde cada especie tera 25 representantes escolhidos aleatóriamente sem reposição.
amostra = strata(iris, c("Species"), size=c(25,25,25), method="srswor")
summary(amostra)

#para gerar amostras com proporção dos estratos: calcular (n de elementos/população * tamanho da amostra)
#248 é o total da população
qt_1 = 12/248*100
qt_2 = 120/248*100
qt_3 = 116/248*100
amostra = strata(infert, c('education'), size = c(qt_1,qt_2,qt_3), method = 'srswor')
summary(amostra)