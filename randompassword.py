import random
characters=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(',')', '<','0', '1', '2', '3', '4', '5', '6', '7', '8',
            '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
 


password=""

for x in range(8):
    password=password+random.choice(characters)

print("Your new password is: ",password)
  
