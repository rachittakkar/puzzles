#custom_password_gen

import string as s
from random import *


characters = s.ascii_letters + s.digits + s.punctuation

custom_password = "".join(choice(characters) for x in range(randint(8,16)))

print(custom_password)
    