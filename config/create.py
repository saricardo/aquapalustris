import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)

mycursor = mydb.cursor()

sql = "SHOW DATABASES LIKE 'aquapalustris'"
mycursor.execute(sql)
myresult = mycursor.fetchall()

if len(myresult) == 0:
    print (len(myresult))
    mycursor.execute("CREATE DATABASE aquapalustris")

mycursor.execute("SHOW DATABASES")

#uncomment to list databases
#for x in mycursor:
  #print(x) 
  
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="aquapalustris"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS plantas (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), preco SMALLINT(255), lago VARCHAR(255))")

sql = "INSERT INTO plantas(name, preco, lago) VALUES (%s, %s, %s)"
val = [
  ('Acorus Gramineus Variegatus', 4, 'entrada'),
  ('Erva Japonesa', 4, 'entrada'),
  
  ('Aponogeton Distachyos', 5, 'povoa'),
  ('Espinheiro de Agua', 5, 'povoa'),
  ('Lotus de Inverno', 5, 'povoa'),
  ('Nenufar Selvagem', 5, 'povoa'),
  
  ('Ceratophyllum Demersum', 2, 'stoantonio'),
  ('Cauda de Raposa', 2, 'stoantonio'),
  ('Foxtail', 2, 'stoantonio'),
  
  ('Clorofitum Comosum', 4, 'povoa'),
  ('Clorofito', 4, 'povoa'),
  
  ('Crassula Helmsii', 3, 'eira'),
  ('Crassula Aquatica', 3, 'eira'),
  ('Sedum dos Pântanos', 3, 'eira'),
  ('Sedum Aquatico', 3, 'eira')
  
  ('Cyperus Alternifolius', 5, 'casa'),
  ('Papiro Guarda Chuva', 5, 'casa'),
  ('Sombrinha Chinesa', 5, 'casa'),
  ('Papiro', 5, 'casa'),
  
  ('Eichhornia Azurea', 6, 'casa'),
  ('Jacinto Ancorado', 6, 'casa'),
  
  ('Equisetum Hyemale', 5, 'entrada'),
  ('Cana Japonesa', 5, 'entrada'),
  
  ('Equisetum Scirpoides', 3, 'entrada'),
  ('Cana Japonesa Ana', 3, 'entrada'),
  
  ('Hesperantha Coccinea', 8, 'casa'),
  ('Lirio do Rio', 8, 'casa'),
  
  ('Heteranthera Zosterifolia', 5, 'eira'),
  ('Erva Estrelada', 5, 'eira'),
  
  ('Hottonia Palustris', 2, 'casa'),
  ('Violeta de Água', 2, 'casa'),
  
  ('Houttunya Cordata Plena', 3, 'entrada'),
  ('Erva Camaleao', 3, 'entrada'),
  
  ('Hydrocharis Morsus Ranae', 2, 'eira'),
  ('Cabeca de Ra', 2, 'eira'),
  
  ('Iris Pseudacorus', 5, 'horta'),
  ('Lirio Amarelo', 5, 'horta'),
  
  ('Juncus Effusus', 4, 'casa'),
  ('Junco', 4, 'casa'),

  ('Lemna Minor', 10, 'stoantonio'),
  ('Lentilha', 10, 'stoantonio'),

  ('Ludwigia Palustris', 5, 'casa'),
  ('Ludwigia', 5, 'casa'),
  
  ('Lysimachia Nummularia', 2, 'eira'),
  ('Estrela Rastejante', 2, 'eira'),
  
  ('Marsilea Mutica', 4, 'eira'),
  ('Trevo Aquatico', 4, 'eira'),
  
  ('Nymphaea', 15, 'eira'),
  ('Nenufar', 15, 'eira'),
  
  ('Nymphoides Peltata', 5, 'casa'),
  ('Golfao Pequeno', 5, 'casa'),
  ('Nenufar Anao', 5, 'casa'),
  
  ('Pontederia Cordata', 5, 'casa'),
  ('Orelha de Veado', 5, 'casa'),
  ('Lucio Pequeno', 5, 'casa'),
  
  ('Rotala Indica', 5, 'eira'),
  ('Dente de Dragao', 5, 'eira'),
  
  ('Sagittaria Subulata', 2, 'eira'),
  ('Flecha Prateada', 2, 'eira'),
  
  ('Salvinia', 5, 'casa'),
  ('Salvinia Natans', 5, 'casa'),
  
  ('Scirpus Cernuus', 4, 'entrada'),
  ('Fibra Optica', 4, 'entrada'),
  
  ('Thalia Dealbata', 15, 'casa'),
  ('Estrelicia de Agua', 15, 'casa'),

  ('Valisneria', 4, 'stoantonio'),
  ('Vallisneria Gigantea', 4, 'stoantonio'),

  ('Zantedeschia Aetopica', 3, 'casa'),
  ('Jarro', 3, 'casa'),
  
  ('Zephyranthes Candida', 4, 'eira'),
  ('Lírio do Vento', 4, 'eira'),

]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
