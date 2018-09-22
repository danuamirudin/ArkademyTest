import json


nama = input("Nama = ")
address = input("Alamat = ")
hobbies = input("Sebutkan Hobi = ")
married = input("Status Pernikahan ketikkan salah satu ! (press ENTER)")
status  = input(["Lajang", "Menikah", "Duda", "Cerai", "Ditikung Teman"])
school  = input("Nama Sekolah / Kampus = ")
skill   = input("Sebutkan Skill yang telah anda kuasai = ")

	

def retjson():
	pythontojson1 = json.dumps(nama )
	pythontojson2 = json.dumps(address)
	pythontojson3 = json.dumps(hobbies)
	pythontojson4 = json.dumps(status)
	pythontojson5 = json.dumps(school)
	pythontojson6 = json.dumps(skill)
	
	print ("Nama =  %s"  %pythontojson1)
	print ("Alamat = %s"  %pythontojson2)
	print ("Hobi = %a"  %pythontojson3)
	
	def marrie():
		
		if status == "Menikah" :
			print ("Status = Sudah %s" %pythontojson4)
			
		else :
			print("Masih ada kesempatan %s" %pythontojson4)
			
	
	marrie()
	
	print ("Skill yang dikuasai = %a"  %pythontojson6 )
	


retjson()
