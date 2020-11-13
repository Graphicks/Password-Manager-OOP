import time
from cryptography.fernet import Fernet


start = time.time()
key = Fernet.generate_key()
f = Fernet(key)
time.sleep(1)

class passwordmanager:
  def __init__(self, username, password):
    self.username = username.encode()
    self.password = password.encode()

  def encryption(self):
    global user_encrypt
    global pass_encrypt

    user_encrypt = f.encrypt(self.username)
    pass_encrypt = f.encrypt(self.password)

    print(user_encrypt,"\n",pass_encrypt)
  
  def decryption(self):
    global decrypt_user 
    global decrypt_pass

    decrypt_user = f.decrypt(user_encrypt).decode()
    decrypt_pass = f.decrypt(pass_encrypt).decode()
    print(decrypt_user,"\n",decrypt_pass)

  def filesave(self):
    file = open("database.txt", 'w')
    file.write(str(user_encrypt) + "\n" + str(pass_encrypt) + "\n" + str(decrypt_user) + "\n" + str(decrypt_pass))

end = time.time()
print(f'Compile time {end - start}')

p1 = passwordmanager(input("Username: "), input("Password: "))
p1.encryption()
p1.decryption()
p1.filesave()



#class myClass:

  #def __init__(self, name, age):
   # self.name = name
   # self.age = age

  #def speak(self):
   # print(f"Hello {self.name}. You're {self.age} years young!")

#a1 = myClass(input("Name "), input("Age "))
#a1.speak()