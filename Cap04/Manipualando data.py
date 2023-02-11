import datetime

#Obtendo a data e horas locais
tempoReal  = datetime.datetime.now()
print(f"As informações de tempo real são:")
print(tempoReal)
print(50*"--")

#É possível ainda criar uma data a partir de um parâmetro
t = datetime.time(23,32,45,16454)
print(f"Hora: {t.hour}")
print(f"Minunto: {t.minute}")
print(f"Segundo: {t.second}")
print(f"Milessegundo: {t.microsecond}")
print(50*"--")


#Obtendo da data de hoje
hoje  = datetime.date.today()
print(f"Hora: {hoje.ctime()}")
print(f"Minunto: {hoje.year}")
print(f"Segundo: {hoje.month}")
print(f"Milessegundo: {hoje.day}")
print(50*"--")


#Calculos entre datas
primeriaData = datetime.datetime(2015,4,28)
print("Primeira Data: ",primeriaData)

segundaData = primeriaData.replace(year=2016)
print("Segunda Data: ",segundaData)

diferencaDatas = segundaData - primeriaData
print(f"A diferença entre as datas é: {diferencaDatas.days}")

















































