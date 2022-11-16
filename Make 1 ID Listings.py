for x in range(0,2698):
	pyautogui.moveTo(550,63, duration=0.3)
	pyautogui.click()
	time.sleep(0.1)
	pyautogui.typewrite("https://opensea.io/assets/ethereum/0xe55ef44be672ff4557931eb9ef91a42d8c9a0d6c/%d/sell" %numberarray[x])
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
	pyautogui.moveTo(709,516,duration=0.3)
	pyautogui.click() #click on date
	time.sleep(0.3)
	pyautogui.typewrite("11")
	pyautogui.typewrite("15")
	pyautogui.moveTo(727,975,duration=0.3)
	time.sleep(0.3)
	pyautogui.click() #click on time of offer
	pyautogui.typewrite("1159p")
	pyautogui.moveTo(196,674,duration=0.3)
	pyautogui.click() #click to remove calendar
	pyautogui.moveTo(340,781,duration=0.3)
	pyautogui.click() #click on complete listing
	time.sleep(11.5)
	pyautogui.moveTo(1525,577, duration=0.3)
	pyautogui.scroll(-200)
	time.sleep(0.3)
	pyautogui.scroll(-400)
	time.sleep(0.3)
	pyautogui.scroll(-300)
	time.sleep(0.3)
	pyautogui.scroll(-500)
	time.sleep(0.3)
	pyautogui.scroll(-400)
	pyautogui.moveTo(1565,755,duration=0.3)
	time.sleep(0.3)
	pyautogui.click()
	time.sleep(4.5) #wait for transaction to go through
	pyautogui.moveTo(856,792,duration=0.3)
	pyautogui.click() #click on "copy link"
	pyautogui.moveTo(1861,400,duration=0.3) #move to notepad++
	pyautogui.click() #click to put notepad in view
	time.sleep(0.1)
	pyautogui.hotkey('ctrl','end')
	time.sleep(0.3)
	pyautogui.typewrite(["enter"])
	pyautogui.hotkey('ctrl','v')
	
	