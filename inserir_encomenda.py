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

if os.path.isfile("counter.txt") == False:
    counterfile = open("counter.txt", "x")
    counterfile = open("counter.txt", "w")
    counterfile.write("0")
counterfile = open("counter.txt", "r")
counter = counterfile.readlines()

newcounter = 0
for count in counter:
    newcounter = int(count)+1;
    break

counterfile = open("counter.txt", "w")
counterfile.write(str(newcounter))

ordercode= str(date.year) + str(date.month) + str(date.day) + "-" + str(newcounter)
outputfolder="encomendas/"

if not os.path.exists(outputfolder):
    os.mkdir(outputfolder)
    
#word = input("Enter plant: ")

#if os.path.isfile("output.txt") == False:
 #   foutput = open("output.txt", "x")
    
finput = open('input.txt', 'r', encoding="utf8", )
encomenda = finput.readlines()

# Strips the newline character
for line in encomenda:
    
    #print("Line{}: {}".format(count, line.strip()))
    close_matches = get_close_matches(line, 
                myplants, n, cutoff)
    #print(close_matches[0])
    if len(close_matches) > 0:
        mycursor.execute("SELECT lago FROM plantas WHERE name = '" + close_matches[0] + "'")
        myresult = mycursor.fetchall()
        lago = "unknown"
        for x in myresult:
            #print("this is: " + x[0])
            lago = x[0]
            break;
        if os.path.isfile(outputfolder + lago+".txt") == False:
            foutput = open(outputfolder + lago+".txt", "x")
        foutput = open(outputfolder + lago+".txt", "a")
        #write plant name
        foutput.write("\n" + close_matches[0])
        
        #detect number of plants
        parts = line.split(" ")
        numeric_string = "1"
        for piece in parts:
            if has_numbers(piece):
                #print(piece)
                #if "â‚¬" in piece:
                if "€" in piece:
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
        foutput.write(" #" + numeric_string + " -" + ordercode)
    else:
        print("Error -"+ line +"- plant not found")

print("Nova encomenda processada: " + ordercode)

if os.path.isfile("encomendas.txt") == False:
    orderfile = open("encomendas.txt", "x")
orderfile = open("encomendas.txt", "a")
orderfile.write(ordercode+"\n")

foutput.close()
finput.close();