import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pantaufungi"
)

cursor = db.cursor()
sql = "select count(*) from set_poin"
cursor.execute(sql)

result = cursor.fetchone()


jml = result[0]
w = 1

#PILIH TANAMAN
print("=====pilih_tanaman======") 
while w < jml+1 :
        z = str(w)
        sql = cursor.execute("select nama_tanaman from set_poin where id_tanaman ='"+z+"'")
        tanaman = cursor.fetchone()
        t = str(tanaman[0])
        print(w,t)
        w+=1
nm_tanaman =  str(input("masukkan nama tanaman : "))

#PILIH SENSOR
print("=======pilih sensor======")
print("1.Suhu")
print("2.Kelembapan")

sensor = int(input("masukkan nomor sensor :"))
    
waktu_cek =  input("masukkan waktu (menit) : ")
total_cek =  input("masukkan total cek : ")

a = cursor.execute("select * from set_poin where nama_tanaman like '%"+nm_tanaman+"%'")
b = cursor.fetchone()
id_tanaman = str(b[0])


#SENSOR SUHU        
if sensor == 5:    
    pilih_sensor = 'water_temperature'
    nilai = 0
    ttc = int(total_cek)
    wtc =  int(waktu_cek)
    nilai_max = ttc
    while nilai < nilai_max :
        #x = 0    
        #y = 1
        ph = str(random.randint(10,37))
        #while x < y :
        t_end = time.time() + 60 * wtc
        v=0
        tbl_ph =[]
            
        while time.time() < t_end:
        # do whatever you d
            print("-----")
            v+=1  
           
        waktu = str(datetime.now())
        inp_ph= id_tanaman,waktu,ph
        tbl_ph.append(inp_ph)
        sq = "insert into "+pilih_sensor+" (id_tanaman,Waktu,Temperature) values (%s,%s,%s)"
        inpt = cursor.executemany(sq,tbl_ph)
        print("BERHASIL",tbl_ph)
            
        nilai+=1
        
#SENSOR KELEMBAPAN        
if sensor == 3:
    pilih_sensor = 'room_humidity'
    nilai = 0
    ttc = int(total_cek)
    wtc =  int(waktu_cek)
    nilai_max = ttc
    while nilai < nilai_max :
        #x = 0    
        #y = 1
        ph = str(random.randint(20,60))
        #while x < y :
        t_end = time.time() + 60 * wtc
        v=0
        tbl_ph =[]
            
        while time.time() < t_end:
        # do whatever you d
            print("-----")
            v+=1  
           
        waktu = str(datetime.now())
        inp_ph= id_tanaman,waktu,ph
        tbl_ph.append(inp_ph)
        sq = "insert into "+pilih_sensor+" (id_tanaman,Waktu,Humidity) values (%s,%s,%s)"
        inpt = cursor.executemany(sq,tbl_ph)
        print("BERHASIL",tbl_ph)
                        
        nilai+=1 
        
        
db.commit()
db.close()

