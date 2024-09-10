#Creat a dictionary of dangerous sharks

dangerous_sharks={ 
    "Great White Shark": "Very dangerous to humans",
    "Tiger Shark": "Known to attack humans",
    "Bull Shark":"Aggressive and dangerous",
    "Oceanic Whitetip Shark":"Involved in attacks on humans",
    "Shortfin Mako Shark":"Fast and can be dangerous"
}
#Print all the values (descriptions) of the sharks
for description in dangerous_sharks.values():
    print(description)

#Print the description of the Bull Shark
print(dangerous_sharks["Bull Shark"])

#Adding new sharks to the dictionary
dangerous_sharks["Hammerhead Shark"]="Can be dangerous, though attacks on humans are rare"

dangerous_sharks["Blacktip Shark"]="Occasionally bites humans but not ususally dangerous"

#Print the updated dictionary
print (dangerous_sharks)

#Check if "Bull Shark" is in the dictionary
if "Bull Shark" in dangerous_sharks:
    print ("Bull Shark is in the dictionary.")
    