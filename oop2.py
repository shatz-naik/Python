"""

Take N as input from user
create  a class Series
	create init
		create list of N numbers
		Insert numbers in the list
	
	create Function as PrintEven
		using loop travel the list from start to end
			check (no%2==0)
			if True	
				print no 
	
	create function as PrintOdd
		using loop travel the list from start to end	
			check (no%2 != 0)
			if True
				print no

inside main function
	create the object of the class
	call the function using object


"""

class Series:
	
	def __init__(self,n):
		self.size = n
		self.arr = []

	def AcceptInput(self):
		
		for i in range(self.size):
			print("Enter the element:",i+1)
			self.arr.append(int(input()))

	def DisplayList(self):
		print("Elements are:")

		for i in range(self.size):
			print(self.arr[i])


	def Summation(self):
		sum = 0
		for i in range(self.size):
			sum = sum + self.arr[i]

		return sum

	def PrintEven(self):
		print("Even elements are:")
		for i in range(self.size):
			if((self.arr[i] % 2) == 0):
				print(self.arr[i])

	def PrintPerfectNumber(self):
		print("Perfect numbers are:")
		for i in range(self.size):
			


	def PrintOdd():
		pass



def main():
	N = int(input("Enter the number of elements:"))

	obj1 = Series(N)

	obj1.AcceptInput()
	obj1.DisplayList()
	
	sum = obj1.Summation()
	print("Summation is:",sum)

	obj1.PrintEven()
if __name__ == "__main__":
	main()