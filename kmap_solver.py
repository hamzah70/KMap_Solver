# CSE 101 - IP HW2
# K-Map Minimization 
# Name : MOHAMMAD HAMZAH AKHTAR
# Roll Number : 2018051	
# Section : A
# Group : 3
# Date : 17/07/2018 		
test = []
def necessary_implicants(minterm_func,implicants):
	#This function finds the essential prime-implicants along with the prime-implicants necessary to write the boolean expression
	list = []
	dict = {}
	epi = [];pi = [];
	for i in minterm_func:
		dict[i]=0
	for i in implicants:
		p=[]
		minterm = []
		cnt = i.count('-')
		if (cnt==0):
			a=str(int(i,2))
			dict[a]=dict[a]+1
			p.append(i);p.append(a)
			list.append(p)
		elif (cnt==1):
			a=i.replace('-','1')
			b=i.replace('-','0')
			a=str(int(a,2))
			b=str(int(b,2))
			minterm.append(a);minterm.append(b);p.append(i)
			for z in minterm:
				if z in dict:
					dict[z]=dict[z]+1
					p.append(z)
			list.append(p)	
		elif (cnt==2):
			a=i.replace('-','1')
			b=i.replace('-','0')
			a=str(int(a,2))
			b=str(int(b,2))
			index1=i.find('-')
			index2=i.find('-',index1+1)
			c=i[:index1]+'1'+i[index1+1:index2]+'0'+i[index2+1:]
			d=i[:index1]+'0'+i[index1+1:index2]+'1'+i[index2+1:]
			c=str(int(c,2))
			d=str(int(d,2))
			minterm.append(a);minterm.append(b);minterm.append(c);minterm.append(d);p.append(i)
			for z in minterm:
				if z in dict:
					dict[z]=dict[z]+1
					p.append(z)
			list.append(p)
		elif cnt==3:
			epi.append(i)						
	for i in list:
		check=0
		for x in i:
			if x in dict:
				if (dict[x]==1) and (check==0):
					check=-1
					del dict[x]
					epi.append(i[0])
				if (x in dict) and (check==-1):
					del dict[x]	
		if (check==0):
			pi.append(i)			
	for i in pi:
		check = 0
		for x in i:
			if (x in dict) and (check==0):
				check=-1
				epi.append(i[0])
				del dict[x]
			if (x in dict) and (check==-1):
				del dict[x]				
	return epi
		
def simplification(num,list):
	#This function converts the quine mc-cluskey minterms into their normal lexicographic form	
	p=[]
	if (num==4):
		for i in list:
			z=''
			if(i[0]=='0'):
				z=z+"w'"
			elif(i[0]=='1'):
				z=z+"w"
			if(i[1]=='0'):
				z=z+"x'"
			elif(i[1]=='1'):
				z=z+"x"	
			if(i[2]=='0'):
				z=z+"y'"
			elif(i[2]=='1'):
				z=z+"y"
			if(i[3]=='0'):
				z=z+"z'"
			elif(i[3]=='1'):
				z=z+"z"	
			p.append(z)		
	elif (num==3):
		for i in list:
			z=''
			if(i[0]=='0'):
				z=z+"w'"
			elif(i[0]=='1'):
				z=z+"w"
			if(i[1]=='0'):
				z=z+"x'"
			elif(i[1]=='1'):
				z=z+"x"	
			if(i[2]=='0'):
				z=z+"y'"
			elif(i[2]=='1'):
				z=z+"y"
			p.append(z)					
	elif (num==2):
		for i in list:
			z=''
			if(i[0]=='0'):
				z=z+"w'"
			elif(i[0]=='1'):
				z=z+"w"
			if(i[1]=='0'):
				z=z+"x'"
			elif(i[1]=='1'):
				z=z+"x"	
			p.append(z)		
	return p							

def groups(num,v,w,p,y,z):
	#This function makes all possible prime implicants
	list = []
	d = {}
	if (num == 4):
		for i in v:
			check =0
			index1=i.find('-')
			index2=i.find('-',index1+1)
			index3=i.find('-',index2+1)	
			for x in w:
				index4=x.find('-')
				index5=x.find('-',index4+1)
				index6=x.find('-',index5+1)	
				if(index1==index4) and (index2==index5) and (index3==index6):
					if(x[0] == '1'):
						q=x
						d[x]=1
						q = q.replace(x[0],'-')
						list.append(q)
						check=1
					elif(x[1] == '1'):
						q=x
						d[x]=1
						q = q.replace(x[1],'-')
						list.append(q)
						check=1	
					elif(x[2] == '1'):
						q=x
						d[x]=1
						q = q.replace(x[2],'-')
						list.append(q)
						check=1	
					elif(x[3] == '1'):
						q=x
						d[x]=1
						q = q.replace(x[3],'-')
						list.append(q)	
						check=1	
			if (check==0):
				list.append(i)	
									
		for i in w:
			check=0
			index1=i.find('-')
			index2=i.find('-',index1+1)
			index3=i.find('-',index2+1)	
			for x in p:
				index4 =x.find('-')
				index5=x.find('-',index4+1)
				index6=x.find('-',index5+1)
				if(index1==index4) and (index2==index5) and (index3==index6):
					if(i[0]==x[0]) and (i[1]==x[1]) and (i[2]==x[2]) and (i[3]!=x[3]):
						q = x[0:3]+'-'
						d[x]=1
						list.append(q)
						check=1	
					elif(i[0]==x[0]) and (i[1]==x[1]) and (i[2]!=x[2]) and (i[3]==x[3]):
						q = x[0:2]+'-'+x[3]
						d[x]=1
						list.append(q)
						check=1	
					elif(i[0]==x[0]) and (i[1]!=x[1]) and (i[2]==x[2]) and (i[3]==x[3]):
						q = x[0]+'-'+x[2:]
						d[x]=1
						list.append(q)	
						check=1
					elif(i[0]!=x[0]) and (i[1]==x[1]) and (i[2]==x[2]) and (i[3]==x[3]):
						q = '-'+x[1:]
						d[x]=1
						list.append(q)
						check=1
			if i not in d:	
				if(check==0):
					list.append(i)								
		for i in p:
			check=0
			index1=i.find('-')
			index2=i.find('-',index1+1)
			index3=i.find('-',index2+1)	
			for x in y:
				index4 =x.find('-')
				index5=x.find('-',index4+1)
				index6=x.find('-',index5+1)
				if(index1==index4) and (index2==index5) and (index3==index6):
					if(i[0]==x[0]) and (i[1]==x[1]) and (i[2]==x[2]) and (i[3]!=x[3]):
						q = x[0:3]+'-'
						d[x]=1
						list.append(q)
						check=1
					elif(i[0]==x[0]) and (i[1]==x[1]) and (i[2]!=x[2]) and (i[3]==x[3]):
						q = x[0:2]+'-'+x[3]
						d[x]=1
						list.append(q)
						check=1	
					elif(i[0]==x[0]) and (i[1]!=x[1]) and (i[2]==x[2]) and (i[3]==x[3]):
						q = x[0]+'-'+x[2:]
						d[x]=1
						list.append(q)
						check=1
					elif(i[0]!=x[0]) and (i[1]==x[1]) and (i[2]==x[2]) and (i[3]==x[3]):
						q = '-'+x[1:]
						d[x]=1
						list.append(q)	
						check=1
			if i not in d:	
				if(check==0):
					list.append(i)			
		length = len(y)
		length2= len(z)
		if(length==0) and (length2!=0):
			list.append(z[0])
		else:	
			for i in y:
				check=0
				index1=i.find('-')
				index2=i.find('-',index1+1)
				index3=i.find('-',index2+1)	
				for x in z:
					index4 =x.find('-')
					index5=x.find('-',index4+1)
					index6=x.find('-',index5+1)
					if(index1==index4) and (index2==index5) and (index3==index6):
						if(i[0]==x[0]) and (i[1]==x[1]) and (i[2]==x[2]) and (i[3]!=x[3]):
							q = x[0:3]+'-'
							list.append(q)	
							check=1
						if(i[0]==x[0]) and (i[1]==x[1]) and (i[2]!=x[2]) and (i[3]==x[3]):
							q = x[0:2]+'-'+x[3]
							list.append(q)
							check=1	
						if(i[0]==x[0]) and (i[1]!=x[1]) and (i[2]==x[2]) and (i[3]==x[3]):
							q = x[0]+'-'+x[2:]
							list.append(q)
							check=1	
						if(i[0]!=x[0]) and (i[1]==x[1]) and (i[2]==x[2]) and (i[3]==x[3]):
							q = '-'+x[1:]
							list.append(q)
							check=1
				if i not in d:	
					if(check==0):
						list.append(i)			
	if (num == 3):
		for i in v:
			check=0
			index1 =i.find('-')
			index2=i.find('-',index1+1)
			for x in w:
				index3 =x.find('-')
				index4=x.find('-',index3+1)
				if(index1==index3) and (index2==index4):
					if(i[0]==x[0]) and(i[1]==x[1]) and (i[2]!=x[2]):
						q=x
						d[x]=1
						q = q.replace(x[2],'-')
						list.append(q)
						check=1
					elif(i[0]==x[0]) and(i[1]!=x[1]) and (i[2]==x[2]):
						q=x
						d[x]=1
						q = q.replace(x[1],'-')
						list.append(q)
						check=1
					elif(i[0]!=x[0]) and(i[1]==x[1]) and (i[2]==x[2]):
						q=x
						d[x]=1
						q = q.replace(x[1],'-')
						list.append(q)	
						check=1
			if(check==0):
				list.append(i)			
		for i in w:
			check=0
			index1 =i.find('-')
			index2=i.find('-',index1+1)
			for x in p:
				index3 =x.find('-')
				index4=x.find('-',index3+1)
				if(index1==index3) and (index2==index4):
					if(i[0]==x[0]) and(i[1]==x[1]) and (i[2]!=x[2])	:
						q=x[0:2]+'-'
						d[x]=1
						list.append(q)
						check=1
					elif(i[0]==x[0]) and(i[1]!=x[1]) and (i[2]==x[2])	:
						q=x[0]+'-'+x[2]
						d[x]=1
						list.append(q)
						check=1
					elif(i[0]!=x[0]) and(i[1]==x[1]) and (i[2]==x[2])	:
						q='-'+x[1:]
						d[x]=1
						list.append(q)	
						check=1
			if i not in d:	
				if(check==0):
					list.append(i)
		length = len(p)
		if(length==0):
			list = list + y
		else:				
			for i in p:
				check=0
				index1 =i.find('-')
				index2=i.find('-',index1+1)
				for x in y:
					index3 =x.find('-')
					index4=x.find('-',index3+1)
					if(index1==index3) and (index2==index4):
						if(i[0]==x[0]) and(i[1]==x[1]) and (i[2]!=x[2]):
							q=x[0:2]+'-'
							list.append(q)
							check=1
						elif(i[0]==x[0]) and(i[1]!=x[1]) and (i[2]==x[2]):
							q=x[0]+'-'+x[2]
							list.append(q)
							check=1
						elif(i[0]!=x[0]) and(i[1]==x[1]) and (i[2]==x[2]):
							q='-'+x[1:]
							list.append(q)	
							check=1
				if i not in d:	
					if(check==0):
						list.append(i)						
	if (num == 2):
		for i in v:
			check=0
			index1=i.find('-')
			for x in w:
				index2 =x.find('-')
				if(index1==index2):
					if(i[0]==x[0]) and (i[1]!=x[1]):
						q = x.replace(x[1],'-')
						list.append(q)
						check=1		
					if(i[0]!=x[0]) and (i[1]==x[1]):
						q = x.replace(x[0],'-')
						list.append(q)	
						check=1
			if(check==0):
				list.append(i)	
		length = len(w)
		if(length==0):
			list.append(p[0])
		else:
			for i in w:			
				index1=i.find('-')
				for x in p:				
					index2 =x.find('-')
					if(index1==index2):
						if(i[0]==x[0]) and (i[1]!=x[1]):
							q = x[0]+'-'					
							list.append(q)
							check=1		
						if(i[0]!=x[0]) and (i[1]==x[1]):
							q = '-'+x[1]
							list.append(q)	
							check=1				
	return list							

def prime_implicants(num,function):
	#This function separates the minterms based on the number of 1's in them	
	func = []
	a = []
	b = []
	c = []
	d = []
	e = []
	for elements in function:
		cnt = elements.count('1')
		if (num == 4):
			if(cnt == 0):
				a.append(elements)
			elif(cnt == 1):
				b.append(elements)
			elif(cnt == 2):
				c.append(elements)	
			elif(cnt == 3):
				d.append(elements)
			elif(cnt == 4):
				e.append(elements)	
		elif (num == 3):
			if(cnt == 0):
				a.append(elements)	
			elif(cnt == 1):
				b.append(elements)	
			elif(cnt == 2):
				c.append(elements)	
			elif(cnt == 3):
				d.append(elements)	
		elif (num == 2):	
			if (cnt == 0):
				a.append(elements)
			elif(cnt == 1):
				b.append(elements)	
			elif(cnt == 2):
				c.append(elements)
	return (a,b,c,d,e)

def prime_implicants_call(num,func):
	#This function calls other functions based on the number of variables in kmap	
	if (num == 4):
		(v,w,x,y,z) = prime_implicants(num,func)
		group = groups(num,v,w,x,y,z)
		(v,w,x,y,z) = prime_implicants(num,group)
		group = groups(num,v,w,x,y,z)
		(v,w,x,y,z) = prime_implicants(num,group)
		group = groups(num,v,w,x,y,z)
		list = []
		for i in group:
 			if i not in list:
 				list.append(i)
	elif (num == 3):
		(v,w,x,y,z) = prime_implicants(num,func)
		group = groups(num,v,w,x,y,z)
		(v,w,x,y,z) = prime_implicants(num,group)
		group = groups(num,v,w,x,y,z)
		list = []
		for i in group:
 			if i not in list:
 				list.append(i)
	elif (num == 2):
		(v,w,x,y,z) = prime_implicants(num,func)
		group = groups(num,v,w,x,y,z)
		list = []
		for i in group:
 			if i not in list:
 				list.append(i)
	return list		
					
def binary_value(num,function):	
	#This function assigns binary values to all the respective minterms	
	gray_code = []
	for item in function:
			if (num == 4):
				if (item == '0'):
					x = '0000'
					gray_code.append(x)
				elif (item == '1'):
					x = '0001'
					gray_code.append(x)
				elif (item == '2'):
					x = '0010'
					gray_code.append(x)
				elif (item == '3'):
					x = '0011'
					gray_code.append(x)
				elif (item == '4'):
					x = '0100'
					gray_code.append(x)
				elif (item == '5'):
					x = '0101'
					gray_code.append(x)
				elif (item == '6'):
					x = '0110'
					gray_code.append(x)
				elif (item == '7'):
					x = '0111'
					gray_code.append(x)
				elif (item == '8'):
					x = '1000'
					gray_code.append(x)
				elif (item == '9'):
					x = '1001'
					gray_code.append(x)
				elif (item == '10'):
					x = '1010'
					gray_code.append(x)
				elif (item == '11'):
					x = '1011'
					gray_code.append(x)
				elif (item == '12'):
					x = '1100'
					gray_code.append(x)	
				elif (item == '13'):
					x = '1101'
					gray_code.append(x)	
				elif (item == '14'):
					x = '1110'
					gray_code.append(x)
				elif (item == '15'):
					x = '1111'
					gray_code.append(x)												
			elif (num == 3):
				if (item == '0'):
					x = '000'
					gray_code.append(x)
				elif (item == '1'):
					x = '001'
					gray_code.append(x)	
				elif (item == '2'):
					x = '010'
					gray_code.append(x)	
				elif (item == '3'):
					x = '011'
					gray_code.append(x)					
				elif (item == '4'):
					x = '100'
					gray_code.append(x)	
				elif (item == '5'):
					x = '101'
					gray_code.append(x)			
				elif (item == '6'):
					x = '110'
					gray_code.append(x)	
				elif (item == '7'):
					x = '111'
					gray_code.append(x)	
			elif (num == 2):
				if (item == '0'):
					x = '00'
					gray_code.append(x)
				elif (item == '1'):
					x = '01'
					gray_code.append(x)
				elif (item == '2'):
					x = '10'
					gray_code.append(x)
				elif (item == '3'):
					x = '11'
					gray_code.append(x)
	return gray_code							

def minFunc(numVar, stringIn):
	"""
        This python function takes function of maximum of 4 variables
        as input and gives the corresponding minimized function(s)
        as the output (minimized using the K-Map methodology),
        considering the case of Don’t Care conditions.

	Input is a string of the format (a0,a1,a2, ...,an) d (d0,d1, ...,dm)
	Output is a string representing the simplified Boolean Expression in
	SOP form.

        No need for checking of invalid inputs.
        
	Do not include any print statements in the function.
	"""
	stringIn = stringIn.split(' ')
	string_function = stringIn[0]
	string_dontcare = stringIn[2]
	stringOut = ''
	graycode = []
	if (string_dontcare == '-'):
		string_function = string_function.split('(')
		string_function = string_function[1].split(')')
		string_function = string_function[0].split(',')
		graycode = binary_value(numVar,string_function)		
		groups_of_implicants=prime_implicants_call(numVar,graycode)		
		global test
		test = test + string_function	
		final_implicants = necessary_implicants(string_function,groups_of_implicants)
		expression=simplification(numVar,final_implicants)
		stringOut = '+'.join(expression)	
	else:
		string_function = string_function.split('(')
		string_function = string_function[1].split(')')
		string_function = string_function[0].split(',')
		string_dontcare = string_dontcare.split('(')
		string_dontcare = string_dontcare[1].split(')')
		string_dontcare = string_dontcare[0].split(',')
		function = string_function
		string_function = string_function + string_dontcare
		graycode_function = binary_value(numVar,string_function)
		groups_of_implicants1 = prime_implicants_call(numVar,graycode_function)	
		graycode_dontcare = binary_value(numVar,string_dontcare)
		groups_of_implicants2 = prime_implicants_call(numVar,graycode_dontcare)
		groups_of_implicants = list(set(groups_of_implicants1).difference(groups_of_implicants2))
		final_implicants = necessary_implicants(function,groups_of_implicants1)
		expression = simplification(numVar,final_implicants)
		stringOut = '+'.join(expression)
	return stringOut

if __name__=='__main__':
	number = int(input('Enter the no. of variable : '))
	function = input('Enter the function : ')
	simplified_function = minFunc(number, function)
	print(simplified_function)
	

	
