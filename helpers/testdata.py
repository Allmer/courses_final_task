import random
import string


# random email generator
def random_char():
    return ''.join(random.choice(string.ascii_letters) for i in range(10))


# test_create_bd_group
class CreateBDGroup:
    group_name_tcbg = "Third"


# Admin user credentials
class AdminCreds:
    admin_login = "yaroslav"
    admin_password = "123456Aa!"


# test_create_user_and_add_group
class CreateUserAndAddGroup:
    user_name = "Oleg"
    user_email = random_char() + "@mac-24.com"
    user_password = "123123Aa!"
    group_name_tcuaag = "First"
