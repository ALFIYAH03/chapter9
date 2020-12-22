#chapter9
#no05

nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	{'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
        {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
        {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	{'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]
print("=" *40)
print("NIM".ljust(10), "NAMA".ljust(10), "N.MID".ljust(10), "N.UAS".ljust(10))
print("-"*40)

for data in nilai:
    a = str(data['mid'])
    b = str(data['uas'])
    print (data['nim'].ljust(10), end='')
    print (data['nama'].ljust(10),end='')
    print (a.rjust(6),b.rjust(9))
print("-" * 40)














                                                    
