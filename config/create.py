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
  ('Thalia Dealbata', 15, 'casa'),
  ('Estrelicia de Agua', 15, 'casa'),
  ('Pontederia Cordata', 5, 'casa'),
  ('Orelha de Veado', 5, 'casa'),
  ('Ludwigia Palustris', 1, 'casa'),
  ('Beldroega dos Pantanos', 1, 'casa'),
  ('Nenufar Branco', 15, 'eira'),
  ('Nymphaea Alba', 15, 'eira'),
  ('Lirio Amarelo', 5, 'horta'),
  ('Iris Pseudacorus', 5, 'horta'),
  ('Trevo Aquatico', 5, 'eira'),
  ('Marsilea Mutica', 5, 'eira'),
  ('Jarro', 3, 'casa'),
  ('Zantedeschia Aetopica', 3, 'casa'),
  ('Nenufar Anao', 5, 'casa'),
  ('Golfao Pequeno', 5, 'casa'),
  ('Papiro', 5, 'casa'),
  ('Cyperus Alternifolius', 5, 'casa'),
  ('Cana Japonesa', 5, 'entrada'),
  ('Erva Japonesa', 5, 'entrada'),
  ('Equisetum Hyemale', 5, 'entrada'),
  ('Cabeca de Ra', 3, 'eira'),
  ('Hydrocharis Morsus Ranae', 3, 'eira'),
  ('Lentilha', 10, 'stoantonio'),
  ('Lemna Minor', 10, 'stoantonio'),
  ('Cauda de Raposa', 1, 'stoantonio'),
  ('Sedum dos Pântanos', 5, 'eira'),
  ('Crassula Helmsii', 5, 'eira'),
  ('Rotala Indica', 5, 'eira'),
  ('Amania Bonsai', 5, 'eira'),
  ('Vallisneria Gigantea', 5, 'stoantonio'),
  ('Sagittaria Subulata', 3, 'eira'),
  ('Sagittaria Graminea', 3, 'eira'),
  ('Lirio do Rio', 5, 'casa'),
  ('Hesperantha Coccinea', 5, 'casa'),
  ('Lírio do Vento', 5, 'eira'),
  ('Zephyranthes Candida', 5, 'eira'),
  ('Violeta de Água', 2, 'casa'),
  ('Hottonia Palustris', 2, 'casa'),
  ('Salvinia Natans', 5, 'povoa'),
  ('Salvinia', 5, 'povoa'),
  ('Espinheiro de Agua', 5, 'povoa'),
  ('Aponogeton Distanchyos', 5, 'povoa'),
  ('Nenufar Selvagem', 5, 'povoa'),
  ('Lysimachia Nummularia', 3, 'eira'),
  ('Estrela Rastejante', 3, 'eira'),
  ('Erva Estrelada', 3, 'eira'),
  ('Heteranthera Zosterifolia', 3, 'eira'),
  ('Fibra Optica', 4, 'entrada'),
  ('Scirpus Cernuus', 4, 'entrada'),
  ('Junco', 4, 'casa'),
  ('Juncus Effusus', 4, 'casa'),
  ('Erva Camaleao', 3, 'entrada'),
  ('Houttunya Cordata Plena', 3, 'entrada')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
