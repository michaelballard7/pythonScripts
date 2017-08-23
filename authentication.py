user_loggedin = False
users = {"Julius":"abc123", "Mark":"qwerty", "Tiffany":"godslove"}

while user_loggedin == False:
  print("Are you an existing client?")
  existing_user = input()

  if existing_user == "yes":
    print('Username?')
    username = input()
    if username in users:
      print("Hello " + username + " what's your password")
      password = input()
    if users[username] == password:
      print("Access granted")
      user_loggedin = True
    else:
      print("Login Failed")

  if existing_user != "yes":
    print("Sorry, We Cant Find your account, would you like to sign up?")
    sign_up = input()
    if sign_up == "yes":
      print("Hello new user what will your username be? ")
      new_username = input()
      print("Thank you, what will your password be")
      new_password = input()
      users.__setitem__(new_username, new_password)
      print ("Thanks for signing up " + new_username)
      user_loggedin = True
    elif sign_up != "yes":
      print("Access Denied Unauthorized User")
      break
print (users)
