from difflib import get_close_matches
from datetime import date
import json
import os
import re
import mysql.connector

#txt_file = open("plant_list.txt", "r")

#content_list = txt_file.readlines()
#print(content_list)

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="aquapalustris"
)

mycursor = mydb.cursor()


mycursor.execute("SELECT * FROM plantas")

myresult = mycursor.fetchall()


myplants = []
for x in myresult:
  #print(x[1])
  myplants.append(x[1]);
  
  
n = 1
cutoff = 0.2

date = date.today()

outputfolder="orcamento/"

if not os.path.exists(outputfolder):
    os.mkdir(outputfolder)
    
#word = input("Enter plant: ")

#if os.path.isfile("output.txt") == False:
 #   foutput = open("output.txt", "x")
    
finput = open('input.txt', 'r', encoding="utf8", )
encomenda = finput.readlines()

TOTAL=0
portes=4
if os.path.isfile(outputfolder+"orcamento.txt") == True:
    os.remove(outputfolder+"orcamento.txt")

foutput = open(outputfolder + "orcamento.txt", "x")

# Strips the newline character
for line in encomenda:
    
    #print("Line{}: {}".format(count, line.strip()))
    close_matches = get_close_matches(line, 
                myplants, n, cutoff)
    #print(close_matches[0])
    if len(close_matches) > 0:
        mycursor.execute("SELECT preco FROM plantas WHERE name = '" + close_matches[0] + "'")
        myresult = mycursor.fetchall()
        preco = "unknown"
        for x in myresult:
            #print("this is: " + x[0])
            preco = x[0]            
            break;
        
        foutput = open(outputfolder+"orcamento.txt", "a")
        #write plant name
        foutput.write("\n" + close_matches[0])
        
        #detect number of plants
        parts = line.split(" ")
        numeric_string = "1"
        for piece in parts:
            if has_numbers(piece):
                #print(piece)
                #if "â‚¬" in piece:
                if "€" in piece or "euro" in piece:
                    #print("euro symbol found")
                    numeric_string = "1"
                elif "+" in piece:
                    operands = piece.split("+")
                    numeric_string =str(int(re.sub('\D', '',operands[0]))+int(re.sub('\D', '', operands[1])))
                    break
                else:
                    numeric_string = re.sub("[^0-9]", "", piece)                
                    break
            else:
                #clean variable
                numeric_string = "1"
        TOTAL = TOTAL+preco*int(numeric_string)
        foutput.write(" x" + numeric_string + " -" + str(preco*int(numeric_string))+"€")
    else:
        print("Error -"+ line +"- plant not found")

if TOTAL >= 40:
    foutput.write("\nportes gratuitos")
    foutput.write("\nTOTAL: " +str(TOTAL)+"€")
else:
    foutput.write("\nportes envio: " + str(portes) +"€")
    TOTAL = TOTAL+portes
    foutput.write("\nTOTAL: " +str(TOTAL)+"€")

foutput.close()
finput.close();