#Please follow the comment instructions.
#You'll only have to do this once for setup
#Make sure to enter the correct format for time and enter the exact Text for the other dropdown inputs
 # - mind the time format
 # - Make sure text matches the exact capitalizatioin and spaces used in the site
#Hope this Automation helps!
#Author: Reuben Bagtas
  # replace [browserPath] with your web browser path
  #if you dont know the path follow the following steps:
  #1) launch Terminal
  #2) type "whereis chromedriver"
  #3) the result is your web browser path
def browserPath(): 
  return '/home/rbagtas/Documents/python/seleniumExample/chromedriver'

def pw():
  return '[password]' #replace [password] with your password

def usr(): 
  return '[username]' #replace [username] with your username

def highlightMsg(): #replace [message] with highlight message
  return '[message]'

def nextStepMsg(): #replace [message] with next steps message
  return '[message]'

def startTime():
  return '09:00' #replace [time] with your start time(military time). 

def endTime():
  return '18:00' #replace [time] with your end time(military time). 

def lunch():
  return '1' #replace [time] with your lunch hours

def totalHours():
  return '8' #replace [hours] with your total hours 

def payrollType():
  return 'Hourly'

def businessPartner(): #replace [businesspartner] with your business partner
  return 'merQbiz'

def projectTeams(): #replace [projectTeams] with your project team
  return 'merQbiz'

def approvedProject(): #Most wont have to change this
  return 'QA Support'

def greenwork(): #change [greenframework] with your greenframework
  return '[greenframework]'