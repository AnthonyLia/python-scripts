for x in range(0,936):
	multiple = math.ceil(numberarray[x]/30)
	if (multiple == 1):
		pyautogui.moveTo(550,68, duration=0.3)
		pyautogui.click()
		time.sleep(0.15)
		pyautogui.typewrite("https://opensea.io/assets/ethereum/0xe55ef44be672ff4557931eb9ef91a42d8c9a0d6c/%d/sell" %bundleitemsarray[x][0])
		pyautogui.typewrite(["enter"])
		time.sleep(7.2)
		pyautogui.typewrite("0.000001")  #enter price
		pyautogui.moveTo(700,700, duration = 0.3) # move to scroll
		pyautogui.scroll(-500)   # scroll to see
		pyautogui.moveTo(350,630, duration = 0.3)
		time.sleep(0.1)  
		pyautogui.click()    # click on more options
		time.sleep(0.2)
		pyautogui.scroll(-200)   
		pyautogui.moveTo(813,495,duration=0.25)
		pyautogui.click()  # click on reserve
		pyautogui.moveTo(800,570,duration=0.25)
		time.sleep(0.3)
		pyautogui.click() # click on address
		pyautogui.typewrite(addressarray[x])
		pyautogui.moveTo(556,350,duration=0.35)
		pyautogui.click() # click on calendar
		time.sleep(0.3)
		pyautogui.typewrite(["tab"])
		pyautogui.moveTo(709,506,duration=0.3)
		pyautogui.click() #click on date
		time.sleep(0.3)
		pyautogui.typewrite("11")
		pyautogui.typewrite("15")
		pyautogui.moveTo(727,965,duration=0.3)
		time.sleep(0.3)
		pyautogui.click() #click on time of offer
		pyautogui.typewrite("1159p")
		pyautogui.moveTo(196,674,duration=0.3)
		pyautogui.click() #click to remove calendar
		time.sleep(0.1)
		pyautogui.scroll(100)
		pyautogui.moveTo(807,390,duration=0.25)
		pyautogui.click() #click on bundle
		time.sleep(0.2)
		pyautogui.moveTo(750,460,duration=0.25) #move to bundle name
		pyautogui.click()
		time.sleep(0.2)
		pyautogui.typewrite(addressarray[x]+" Bundle") #type who the bundle is to
		time.sleep(0.25)
		time.sleep(0.25)
		pyautogui.moveTo(1177,381,duration=0.4) #move to add items
		time.sleep(0.15)
		pyautogui.click()
		time.sleep(0.35)
		pyautogui.typewrite(str(bundleitemsarray[x][1]))
		time.sleep(0.9)
		pyautogui.moveTo(1177,465,duration=0.5)
		time.sleep(0.6)
		pyautogui.click()
		time.sleep(0.9)
		pyautogui.scroll(-320)
		time.sleep(0.9)
		for y in range(2,numberarray[x]):
			pyautogui.click()
			time.sleep(0.2)
			pyautogui.hotkey('ctrl','backspace')
			time.sleep(1.2)
			pyautogui.typewrite(str(bundleitemsarray[x][y]))
			time.sleep(1.2)
			pyautogui.moveTo(1177,538,duration=0.4)
			time.sleep(0.4)
			pyautogui.click()
			time.sleep(0.9)
			pyautogui.moveTo(1177,458,duration=0.3)
			time.sleep(0.15)
		
		pyautogui.moveTo(405,740,duration=0.3)
		pyautogui.click() #click on complete listing
		time.sleep(14)
		pyautogui.moveTo(1525,577, duration=0.3)
		pyautogui.scroll(-200)
		time.sleep(0.3)
		pyautogui.scroll(-400)
		time.sleep(0.3)
		pyautogui.click()
		time.sleep(0.2)
		pyautogui.typewrite(["end"])
		time.sleep(0.2)
		pyautogui.moveTo(1565,755,duration=0.3)
		time.sleep(1.5)
		pyautogui.click()
		time.sleep(8.5) #wait for transaction to go through
		pyautogui.moveTo(856,792,duration=0.3)
		pyautogui.click() #click on "copy link"
		pyautogui.moveTo(1861,400,duration=0.3) #move to notepad++
		pyautogui.click() #click to put notepad in view
		time.sleep(0.1)
		pyautogui.hotkey('ctrl','end')
		time.sleep(0.3)
		pyautogui.typewrite(["enter"])
		time.sleep(0.1)
		pyautogui.typewrite("%s" % addressarray[x] + ",1,")
		time.sleep(0.1)
		pyautogui.hotkey('ctrl','v')
		

	else:
		for counter in range(1,multiple+1): 
			pyautogui.moveTo(550,68, duration=0.3)
			pyautogui.click()
			time.sleep(0.15)
			pyautogui.typewrite("https://opensea.io/assets/ethereum/0xe55ef44be672ff4557931eb9ef91a42d8c9a0d6c/%d/sell" %bundleitemsarray[x][(counter-1)*30])
			pyautogui.typewrite(["enter"])
			time.sleep(7.2)
			pyautogui.typewrite("0.000001")  #enter price
			pyautogui.moveTo(700,700, duration = 0.3) # move to scroll
			pyautogui.scroll(-500)   # scroll to see
			pyautogui.moveTo(350,630, duration = 0.3)
			time.sleep(0.1)  
			pyautogui.click()    # click on more options
			time.sleep(0.2)
			pyautogui.scroll(-200)   
			pyautogui.moveTo(813,495,duration=0.25)
			pyautogui.click()  # click on reserve
			pyautogui.moveTo(800,570,duration=0.25)
			time.sleep(0.3)
			pyautogui.click() # click on address
			pyautogui.typewrite(addressarray[x])
			pyautogui.moveTo(556,350,duration=0.35)
			pyautogui.click() # click on calendar
			time.sleep(0.3)
			pyautogui.typewrite(["tab"])
			pyautogui.moveTo(709,506,duration=0.3)
			pyautogui.click() #click on date
			time.sleep(0.3)
			pyautogui.typewrite("11")
			pyautogui.typewrite("15")
			pyautogui.moveTo(727,965,duration=0.3)
			time.sleep(0.3)
			pyautogui.click() #click on time of offer
			pyautogui.typewrite("1159p")
			pyautogui.moveTo(196,674,duration=0.3)
			pyautogui.click() #click to remove calendar
			time.sleep(0.1)
			pyautogui.scroll(100)
			pyautogui.moveTo(807,390,duration=0.25)
			pyautogui.click() #click on bundle
			time.sleep(0.2)
			pyautogui.moveTo(750,460,duration=0.25) #move to bundle name
			pyautogui.click()
			time.sleep(0.2)
			pyautogui.typewrite(addressarray[x]+" Bundle %d" %counter)
			time.sleep(0.25)
			time.sleep(0.25)
			pyautogui.moveTo(1177,381,duration=0.3) #move to add items
			time.sleep(0.15)
			pyautogui.click()
			time.sleep(0.5)
			pyautogui.typewrite(str(bundleitemsarray[x][(counter-1)*30+1]))
			time.sleep(0.9)
			pyautogui.moveTo(1177,465,duration=0.5)
			time.sleep(0.6)
			pyautogui.click()
			time.sleep(0.9)
			pyautogui.scroll(-320)
			time.sleep(0.9)
			if (counter == multiple):
				for y in range((counter-1)*30+2,numberarray[x]):
					pyautogui.click()
					time.sleep(0.2)
					pyautogui.hotkey('ctrl','backspace')
					time.sleep(1.2)
					pyautogui.typewrite(str(bundleitemsarray[x][y]))
					time.sleep(1.2)
					pyautogui.moveTo(1177,538,duration=0.4)
					time.sleep(0.4)
					pyautogui.click()
					time.sleep(0.9)
					pyautogui.moveTo(1177,458,duration=0.3)
					time.sleep(0.15)
			else:
				for y in range ((counter-1)*30+2,(counter-1)*30+30):
					pyautogui.click()
					time.sleep(0.2)
					pyautogui.hotkey('ctrl','backspace')
					time.sleep(1.2)
					pyautogui.typewrite(str(bundleitemsarray[x][y]))
					time.sleep(1.2)
					pyautogui.moveTo(1177,538,duration=0.4)
					time.sleep(0.4)
					pyautogui.click()
					time.sleep(0.9)
					pyautogui.moveTo(1177,458,duration=0.3)
					time.sleep(0.15)
	
	
			pyautogui.moveTo(405,740,duration=0.3)
			pyautogui.click() #click on complete listing
			time.sleep(14)
			pyautogui.moveTo(1525,577, duration=0.3)
			pyautogui.scroll(-200)
			time.sleep(0.3)
			pyautogui.scroll(-400)
			time.sleep(0.3)
			pyautogui.click()
			time.sleep(0.4)
			pyautogui.typewrite(["end"])
			time.sleep(0.2)
			pyautogui.moveTo(1565,755,duration=0.3)
			time.sleep(1.5)
			pyautogui.click()
			time.sleep(8.5) #wait for transaction to go through
			pyautogui.moveTo(856,792,duration=0.3)
			pyautogui.click() #click on "copy link"
			pyautogui.moveTo(1861,400,duration=0.3) #move to notepad++
			pyautogui.click() #click to put notepad in view
			time.sleep(0.1)
			pyautogui.hotkey('ctrl','end')
			time.sleep(0.3)
			pyautogui.typewrite(["enter"])
			time.sleep(0.1)
			pyautogui.typewrite("%s" % addressarray[x] + ",%d," % multiple)
			time.sleep(0.1)
			pyautogui.hotkey('ctrl','v')
	
	
	
	
	#	numberarray[x] is number of punks owned by xth wallet
	#	addressarray is an array of wallet addresses
	#	bundleitemsarray is a 936x423 matrix where the rows are each arrays of the punk IDs owned by the wallet for that row.
	#						maximum IDs in a wallet is 423, and lesser wallets had yth indexes filled with burned token in case script
	#						were to accidentally miss clicking a punk and trying to list more than that wallet should be listed