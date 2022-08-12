n= float(input("introdusca los grados brix: "))

ri=1.3330
x=1.3330
while(n>x):
	x = 0.0087 + 699.82353*( ri - 1.3330) - 1801.9215*(( ri - 1.3330) **2)+ 4696.422*(( ri - 1.3330)**3)- 6427.26*(( ri - 1.3330) **4)
	
	ri=ri+0.0001
print(ri)