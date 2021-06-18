password = 'a123456'
fre = 3
fre = int(fre)

while fre > 0:
	fre = fre - 1
	uesr = input('請輸入密碼: ')
	if uesr == password :
		print('登入成功')
		break
	elif uesr != password : 
		print('密碼錯誤!')
		if fre > 0:
			print('還有', fre, '次機會!')
		
