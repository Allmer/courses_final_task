import psycopg2


class DB:
    def __init__(self):

        #self.host = '127.0.0.1'
        #self.port = '5432'
        #self.user = 'postgres'
        #self.password = 'postgres'
        #self.dbname = 'postgres'
        self.conn = psycopg2.connect(
            dbname='postgres'
            host='127.0.0.1',
            port='5432',
            user='postgres',
            password='postgres',
            database='postgres'
        )
        self.cur = self.conn.cursor()

    # Insert new group query
    def do_insert_group(self, value):
        insert_query = "INSERT INTO auth_group (id, name) VALUES (%s, %s);"
        values = value
        self.cur.execute(insert_query, (99, values))
        self.conn.commit()

    # Delete added group query
    def do_delete_group(self, value):
        delete_query = "DELETE FROM auth_group WHERE name = %s;"
        self.cur.execute(delete_query, (value,))
        self.conn.commit()

    # Find added user in auth_users table
    def do_find_user(self, username: str, email: str):
        t_query = "SELECT username FROM auth_user WHERE username = %s AND email = %s"
        self.cur.execute(t_query, (username, email))

        result_list = []
        for table in self.cur.fetchone():
            result_list.append(table)
        result = ' '.join([str(elem) for elem in result_list])
        print(f"\nFound user: {result}")

        assert username == result

    def do_find_group_for_user(self, email: str, group_name: str):

        # Find user id in auth_user table
        find_user_id = "SELECT id FROM auth_user WHERE email = %s;"
        self.cur.execute(find_user_id, (email,))

        result_id_list = []
        for table in self.cur.fetchone():
            result_id_list.append(table)
        result_id = result_id_list[0]
        print(f"Your user id is {result_id}")

        # Find the group id in the auth_user_groups table to which our user belongs
        find_group_w_user_id = "SELECT group_id FROM auth_user_groups WHERE user_id = %s;"
        self.cur.execute(find_group_w_user_id, (result_id,))

        result_group_id_list = []
        for table in self.cur.fetchone():
            result_group_id_list.append(table)
        result_group_id = result_group_id_list[0]
        print(f"Group id is {result_group_id} to which our user belongs")

        # Find group name to which group_id belongs
        find_group_name = "SELECT name FROM auth_group WHERE id = %s;"
        self.cur.execute(find_group_name, (result_group_id,))

        result_group_name_list = []
        for table in self.cur.fetchone():
            result_group_name_list.append(table)
        result_group_name = result_group_name_list[0]
        print(f"Group name is {result_group_name}")

        assert result_group_name == group_name

    # Delete test user
    def do_delete_user(self, username: str, email: str):

        # Find user id in auth_user table
        find_user_id = "SELECT id FROM auth_user WHERE username = %s AND email = %s;"
        self.cur.execute(find_user_id, (username, email))

        result_list = []
        for table in self.cur.fetchone():
            result_list.append(table)
        result = result_list[0]
        print(f"User ID is {result}")

        # Delete user group in auth_user_groups table
        delete_user_group = "DELETE FROM auth_user_groups WHERE user_id = %s"
        self.cur.execute(delete_user_group, (result,))

        # Delete user record from auth_user table
        delete_user_query = "DELETE FROM auth_user WHERE username = %s AND email = %s;"
        self.cur.execute(delete_user_query, (username, email))
        print(f"User {username} was successfully deleted")

        self.conn.commit()

    def close_cursor(self):
        self.cur.close()
        self.conn.close()
