#c3m6g9
def final_comun_mayor(str1,str2):
	vector=list(str1)
	vector1=[]
	palabra2=list(str2)
	vector2=[]
	vector3=[]
	v=[]
	c=0
	for indice in range(len(str1)):
		vector1.append(vector[indice])

	for indice2 in range(len(str2)):
		vector2.append(palabra2[indice2])

	upa=len(str1)-1
	upb=len(str2)-1
	if(vector1[upa]==vector2[upb]):
		while(vector1[upa]==vector2[upb]):
			for i in range(c,-1,-1):
				vector3.append(vector1[upa])
	
			upa=upa-1
			upb=upb-1
			i=i+1
		p = vector3[::-1]
		cadena=''.join(p)
		print("'"+cadena+"'")
		return(str1,str2)
	else:
		print(" '  ' ")
str1=input("Primera cadena de caracteres: ")
str2=input("Segunda cadena de caracteres: ")
v=(str1,str2)
print("final_comun_mayor",v)
final_comun_mayor(str1,str2)
