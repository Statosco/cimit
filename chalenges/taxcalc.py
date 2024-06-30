country = input("what country are you in? ").upper()
taxPerProvince = 0
total = 0
pricePerItem = 0
if country == "CANADA":
    province = input("Which province? ").upper()
    if province == "ONTARIO" or province == "NEW BRUNSWICK" or province == "NOVA SCOTIA":
        taxPerProvince = 0.13
    elif province == "ALBERTA":
        taxPerProvince = 0.05
    else:
        taxPerProvince = 0.06

else:
    print("sorry, we dont sell products in your country")
    exit()



print("Laptop: A portable computer for various tasks and activities"\
    "\nSmartphone: A mobile device that offers communication, internet access, and various applications." \
    "\nHeadphones: Audio devices worn over the ears for listening to music or other audio content."\
    "\nFitness Tracker: A wearable device that monitors physical activities, heart rate, and sleep patterns."\
    "\nDigital Camera: An electronic device used for capturing and storing photographs."\
    "\nSmartwatch: A wrist-worn device that provides notifications, fitness tracking, and other smart features."\
    "\nHome Security System: A system that protects a home by monitoring and detecting intrusions."\
    "\nBluetooth Speaker: Portable speakers that connect wirelessly to devices via Bluetooth for audio playback."\
    "\nGaming Console: A dedicated device for playing video games on a television or monitor."\
    "\nE-book Reader: A device designed for reading electronic books, often featuring an e-ink display for a paper-like reading experience.")
order = input("what would you like to order? ").upper()

if order == "LAPTOP":
    pricePerItem = 2400
elif order == "SMARTPHONE":
    pricePerItem = 1000
elif order == "HEADPHONES":
    pricePerItem = 700
elif order == "FITNESS TRACKER":
    pricePerItem = 100
elif order == "DIGITAL CAMERA":
    pricePerItem = 2000
elif order == "SMARTWATCH":
    pricePerItem = 500
elif order == "HOME SECURITY SYSTEM":
    pricePerItem = 7000
elif order == "BLUETOOTH SPEAKER":
    pricePerItem = 200
elif order == "GAMING CONSOLE":
    pricePerItem = 1000
elif order == "E-BOOK READER":
    pricePerItem = 500
else:
    print("sorry we dont have those")
    exit()

totaltax = taxPerProvince / 100 * pricePerItem 
total = totaltax + pricePerItem
print (f"your total price plus tax of {totaltax} is {total}")