#Breach Bot Starter Code
breachYear = 2017

#Greets user
print("\033[1;31;40mHello! I'm CyHelp.")
print ("What is your name?\033[0m")
userName = input("Your name: ")

print ("Nice to meet you " + userName + "!\n")

#Recounts year of breach
todaysYear = input("\033[1;31;40mWhat year is it?\033[0m\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the National Health Services data breach!\n")

#Introduces breach
print("\033[1;31;40mWould you like to learn about the National Health Services data breach of 2017?\033[0m\n")
giveInfo = input("Type \033[1;31;40m'yes'\033[0m or \033[1;31;40m'no'\033[0m\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("\n\033[1;31;40mWhat would you like to learn more about? Enter the lowercase letter of the following options:\033[0m \n(a) \033[1;32;40mbreach details\033[0m, (b) \033[1;36;40morganization's response\033[0m, (c) \033[1;35;40mI would like to hear your reflections\033[0m")
  topic = input()
  
  if topic.lower() == "a":
    print("\033[1;32;40mOn Friday, May 12th, 2017, the ransomware program WannaCry shutdown work at 16 hospitals across the United Kingdom and 45,000 computers across 74 countries. The attack makes use of an exploit called EternalBlue. Microsoft issued an update to protect against the vulnerability before hackers made it public, but the update didn’t make it to every Windows machine. The attack began at roughly 12:30PM local time. When employees tried to access the computers, they were presented with a demand for $300 in bitcoin, a classic ransomware tactic.\033[0m")
  
  elif topic.lower() == "b":
    print("\033[1;36;40mThe result was a wave of canceled appointments and general disarray, as many hospitals were left unable to access basic medical records. At least one hospital canceled all non-urgent operations as a result.FBI agents have informally recommended that ransomware targets pay to decrypt their files, although the practice remains controversial.\033[0m")
  
  elif topic.lower() == "c": 
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")


#Introduces take
print("\n\033[1;31;40mI'm excited to share my perspective with you. Are you ready to hear my take?\033[0m\n")
giveInfo = input("Type \033[1;31;40m'yes'\033[0m or \033[1;31;40m'no'\033[0m\n")

#Shares take
while giveInfo.lower() == "yes":
  print("\n\033[1;31;40mWhat would you like to learn more about? Enter the lowercase letter of the following options:\033[0m \n(a)\033[1;32;40m relation to the CIA Triad\033[0m, (b)\033[1;33;40m my reaction\033[0m,(c)\033[1;36;40mmy advice\033[0m or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("\033[1;32;40mHackers gained access to the unauthorized data of medical records. The data breach also compromised thousands of operating systems worldwide.\033[0m")
  
  elif topic.lower() == "b":
    print("\033[1;33;40mI disagree with the organization's response. I think its very insensitive because The NSA created the EternalBlue exploit in the first place. I think they should have taken more responsibility for the damages done.\033[0m")
  
  elif topic.lower() == "c": 
    print("\033[1;36;40mHackers have the ability to deeply impact your life in a negative way. With a name and a date of birth, a cyberattacker has the potential to steal your identity.My advice would be to issue credit freezes and file an identity theft report immediately.\033[0m")

  elif topic.lower() == "d":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")


  
#Chatbot ends conversation
print("\nThanks for chatting with me, and I hope you learned something new!")