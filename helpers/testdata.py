import random
import string


# random email generator
def random_char():
    return ''.join(random.choice(string.ascii_letters) for i in range(10))


# random user id generator
def random_id_generator():
    return ''.join(random.choice(string.digits) for i in range(10))


# random username generator
def random_username_generator():
    return ''.join(random.choice(string.ascii_letters) for i in range(10))


user_id = random_id_generator()
user_name = random_username_generator()


# test_create_bd_group
class CreateBDGroup:
    group_name_tcbg = "Third"


# Admin user credentials
class AdminCreds:
    admin_login = "yaroslav"
    admin_password = "123456Aa!"


# test_create_user_and_add_group
class CreateUserAndAddGroup:
    user_name = random_username_generator()
    user_email = random_char() + "@mac-24.com"
    user_password = "123123Aa!"
    group_name_tcuaag = "First"
