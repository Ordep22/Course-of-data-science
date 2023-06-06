#Importin OS library
import os

#Text with we will put on file
text  = "Cientistas de dados é a profissão que mais tem cido em todo mundo . " \
        "Esses profissionais precisam se especializar em progração, estatistica " \
        "e Machine Learning!"

#Criate a file
##Whe there isn't a file on the directory the built in function OPEN will create this
txtFile  = open(os.path.join("/Cap06 - Processing files, modules, packages and built-in functions/Cientista.txt"), 'w')

#Save data in file
for words in text.split():
        if words == ".":

                txtFile.write(words + "\n")

        else:

                txtFile.write(words + " ")

#Close file
txtFile.close()

#Read file

readFile = open("/Cap06 - Processing files, modules, packages and built-in functions/Cientista.txt")
content  = readFile.read()
readFile.close()
print(content)
