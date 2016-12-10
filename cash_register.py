'''
datchedda - A program for managing the money of a small enterpoorise.

What does a cash register do?
	-Type in sold items & compare.
	-Keep track of money and stock.
	-Saving!
	-Plot time vs. sold amount.
'''

#Try to: Define a function that returns a dictionary, which has the following format:
#{'value' : <input value>, 'stock' : <input stock>}

#I should be able to call the function like this: <function name>(<input value>, <input stock>)


def val(price, stock) :
	return {"price" : price, "stock" : stock}


items = {	'Wodka'			: val(40, 42),
			'cykacola'		: val(4, 5) ,
			'chicken hearts': val(0.93, 8)
}
bank = 0

while True :
	userInput = input('rameinnoodle-^- ')
	print(userInput)
	if userInput in items :	
		bank += items[userInput]["price"]
		print('value:', items[userInput])
	else :
		print('We dont have this go to costco')
		
		
#This is a cool change that I'm committing!


#Create a cash register that: Lets me sell items, compare items sold, keep track of money and stock, and save!
