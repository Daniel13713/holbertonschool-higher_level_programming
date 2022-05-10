#!/usr/bin/python3
"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    if (len(argv) == 5):
        user = argv[1]
        password = argv[2]
        database = argv[3]
        state = argv[4]
        config = {
            'user': user,
            'passwd': password,
            'host': 'localhost',
            'db': database,
            'port': 3306,
        }
        db = MySQLdb.connect(**config)

        with db.cursor() as cursor:
            cursor.execute("""
                SELECT
                    *
                FROM
                    states
                WHERE
                    name = %(state)s
                ORDER BY
                    id
                """, {'state': state})

            data = cursor.fetchall()

        if not data:
            """print("Doesn't exist {0} state".format(state))"""
        else:
            [print(state) for state in data]
    else:
        """print("Usage: ./0-select_states.py
        username password database state")"""
