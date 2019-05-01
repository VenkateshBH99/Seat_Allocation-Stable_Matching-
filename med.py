class info:
	def __init__(self,name1,m,j):
		self.name1=name1
		self.marks=m
		self.j=j

class intake:
	def __init__(self,name,no):
		self.name=name
		self.no=no
class med:
	def __init__(self,n):
		self.item=[[] for i in range(n)]
		self.it=[0 for i in range(n)]

	def addintake(self,i,name,no):
		self.it[i-1]=intake(name,no)

	def additem(self,i,m,name1,j):
		self.item[i-1].append(info(name1,m,j-1))

	def sort(self):
		for i in range(1,len(self.item)):
			for j in range(len(self.item[i])):
				r=self.item[i][j].marks
				keep=self.item[i][j]
				k=j-1
				while k>=0 and self.item[i][k].marks<r:
					self.item[i][k+1]=self.item[i][k]
					k-=1
				self.item[i][k+1]=keep

	def sort1(self):
		for k in range(len(self.item)):
			for i in range(len(self.item[k])-1):
				for j in range(i+1,len(self.item[k])):
					if self.item[k][i].marks<self.item[k][j].marks:
						self.item[k][i],self.item[k][j]=self.item[k][j],self.item[k][i]

class visit:
	def __init__(self,k,index,n):
		self.inst=k
		self.v="free"
		self.match=None
		self.d=0
		self.d1=0
		self.ind=[None for i in range(n)]
		for i in range(len(index)):
			self.ind[index[i].j]=i
class visit1:
	def __init__(self,k,index):
		self.inst=k
		self.v="free"
		self.match=None
		self.d=0
		self.d1=0
		
def allocate(collage,student,n,n1):
	C=[visit(k,collage.item[k],n1) for k in range(len(collage.item))]
	S=[visit(k,student.item[k],n) for k in range(len(student.item))]
	q=[]
	for i in C:
		q.append(i)
	while q:
		col=q.pop(0)
		#(col.inst+1)
		while col.d!=collage.it[col.inst].no and col.d<=len(collage.item[col.inst]):
			if S[collage.item[col.inst][col.d].j].v=="free":
				S[collage.item[col.inst][col.d].j].v="allocated"
				S[collage.item[col.inst][col.d].j].match=col.inst
				col.d+=1
			else:
				#print(S[collage.item[col.inst][col.d].j].match," ",S[collage.item[col.inst][col.d].j].)
				a=S[collage.item[col.inst][col.d].j].ind[col.inst]
				b=S[collage.item[col.inst][col.d].j].ind[S[collage.item[col.inst][col.d].j].match]
				if a<b:
					C[S[collage.item[col.inst][col.d].j].match].d-=1
					q.append(C[S[collage.item[col.inst][col.d].j].match])
					S[collage.item[col.inst][col.d].j].match=col.inst
					col.d+=1
				else:
					if collage.it[col.inst].no<len(collage.item[col.inst]):
						collage.it[col.inst].no+=1
					col.d+=1

	r=[]
	r.append(collage)
	r.append(C)
	r.append(student)
	r.append(S)
	return r



def main():
	n=int(input("Enter total number of collages to be entered:"))
	c=med(n)
	print("Enter collage names:")
	for i in range(n):
		print((i+1),":",end="")
		st=input()
		print("Enter total intake of this institute:",end="")
		no=int(input())
		c.addintake(i+1,st,no)

	n1=int(input("Enter total number of students applying:"))
	s=med(n1)
	print("Enter students names:")
	for i in range(n1):
		print((i+1),":",end="")
		st=input()
		print("Enter CGPA:",end="")
		per=int(input())
		s.addintake(i+1,st,per)


	print("List of collages are:")
	for i in range(n):
		print((i+1),":",c.it[i].name)

	print("Enter Perferences (in terms of collage code!!):")

	for i in range(n1):
		print("For ",(i+1),":",s.it[i].name,":",end="")
		n2=input()
		ar=list(map(int,n2.rstrip().split()))
		for j in ar:
			s.additem(i+1,s.it[i].no,c.it[j-1].name,j)
			c.additem(j,s.it[i].no,s.it[i].name,i+1)

	for i in range(len(c.item)):
		if c.it[i].no>=len(c.item[i]):
			print(c.it[i].no," ",len(c.item[i]))
			c.it[i].no=len(c.item[i])

	c.sort1()
	res=allocate(c,s,n,n1)
	print("--------------------------")
	print("FINAL ALLOCATION:")
	print("ROLL NO  NAME     CGPA    Allotted institute")
	for i in range(len(res[3])):
		if res[3][i].match!=None:
			print((i+1),"      |",res[2].it[i].name,"   | ",res[2].it[i].no,"  |   ",res[0].it[res[3][i].match].name)

if __name__ == '__main__':
	main()










				





