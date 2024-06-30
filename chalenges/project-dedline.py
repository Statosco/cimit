import datetime



user = input("what is your dedline (dd/mm/yyyy)? ")
projectDedline = datetime.datetime.strptime(user, '%d/%m/%Y').date()

currentDate = datetime.date.today()
dedline = projectDedline - currentDate

numberofWeeks = dedline.days / 7
daays = currentDate.day % 7
print ("you have %d days" % daays, "and %d weeks" %numberofWeeks)




