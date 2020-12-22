#chapter9
#no06

nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	{'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
        {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
        {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
        {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]
print("=" * 65)
print("NIM" .ljust(10), "NAMA".ljust(10), "N.MID".ljust(10), "N.UAS".ljust(10),"N.AKHIR".ljust(10), "STATUS".ljust(10))
print("-"*65)

for data in nilai:
	a = str(data['mid'])
	b = str(data['uas'])
	c = int((data['mid']+2*(data['uas']))/3)
	d = str(c)
        if (c >= 60):
                status = 'LULUS'
        else:
                status = 'TIDAK LULUS'
	print(data['nim'].ljust(11), end='')
	print((data['nama'].upper()).ljust(11), end='')
	print(a.rjust(6), b.rjust(9), d.rjust(12), status.rjust(10))
    
print("-" * 65)
