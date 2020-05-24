salarios_jogadores = c(40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000)

#media de salarios
mean(salarios_jogadores)

#mediana
median(salarios_jogadores)

#quartis
quartis = quantile(salarios_jogadores)
quartis

# desvio padrão
sd(salarios_jogadores)

#summary traz um resumo da variável com alguns calculos prontos.
summary(salarios_jogadores)
