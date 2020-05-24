#Amostra Sistemática
#instalar o pacote Teaching sampling
install.packages("TeachingSampling")
library(TeachingSampling)

#criar uma amostra sistemática aleatória do conjunto de dados iris trazendo um registro a cada 10.

amostra = S.SY(150,10)
amostrairis = iris[amostra,]

amostrairis