"""
Created on 1/28/2020
@author:Marvin  Senjaliya
"""

"""
problem statement:Commercial data processing - StockAccount.java implements a data type that might be used by a financial institution to keep track of customer information. The StockAccount class implements following methods

The StockAccount class also maintains a list of CompanyShares object which has Stock Symbol and Number of Shares as well as DateTime of the transaction. When buy or sell is initiated StockAccount checks if CompanyShares are available and accordingly update or create an Object.
"""
import json
class StockAccount:
	
	def __init__(self):
		file=open('stock.json')
		self.person_dict=json.load(file)


	def BuyStock(self,StockDetails,price,name,Symbol,NoOfShare):
		self.person_dict[StockDetails].append({'SharePrice':price,'StockName':name,'StockSymbol':Symbol,'NoOfShare':NoOfShare})

	def SellStock(self,StockDetails,price,name,Symbol,NoOfShare):
		self.person_dict[StockDetails].remove({'SharePrice':price,'StockName':name,'StockSymbol':Symbol,'NoOfShare':NoOfShare})   

                
			
	def BuyShare(self):
		for index in range(int(input("Please,Enter the no of stock you want to add:"))):
			name=input("please,enter the name of stock")
			price=input("stockprice:")
			Symbol=input("symbol:")
			NoOfShare=input("NoOfShare")
			self.BuyStock('StockDetails',price,name,Symbol,NoOfShare)
	
	def ShellShare(self):
		 
		   for _ in range(int(input("please,Enter the no of stock you want to delete:"))):
			   name=input("please,enter the name of stock")
			   price=input("stockprice:")
			   Symbol=input("symbol:")
			   NoOfShare=input('NoOfShare')
			   self.ShellStock('StockDetails',price,name,Symbol,NoOfShare)


	def Accountvalue(self):
		for stock in self.person_dict:
			for share in range(0,len(stock)):
				total_value = int(self.person_dict[stock][share]['SharePrice']) * int(self.person_dict[stock][share]['NoOfShare'])
				print(total_value)
				return total_value

	def PrintReport(self):
		print(self.person_dict)

	def SaveAccount(self):
		file = open('stock.json', 'w')
		file = json.dump(self.person_dict)
		file.close()

          


if __name__=="__main__":
	obj=StockAccount()
	num=int(input("please Enter your Choice:\n1: Buy Stock\n2: Shell Stock\n3: print report\n4: Account value\n5: Save Account"))

	if num == 1:
		obj.BuyShare()
		obj.PrintReport()
	if num == 2:
		obj.ShellShare()
		obj.PrintReport()
	if num == 3:
		obj.PrintReport()
	if num == 4:
		obj.Accountvalue()
	if num== 5:
		obj.SaveAccount()
		

