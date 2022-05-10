#!/usr/bin/python3
"""
script that takes in an argument and displays
all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    if (len(argv) == 5):
        user = argv[1]
        password = argv[2]
        database = argv[3]
        state = argv[4]

        """Configuration to database connection"""
        config = {
            'user': user,
            'passwd': password,
            'host': 'localhost',
            'db': database,
            'port': 3306,
        }

        try:
            db = MySQLdb.connect(**config)
            with db.cursor() as cursor:
                """Database Contect Manager"""
                cursor.execute("""
                    SELECT
                        cities.name
                    FROM
                        cities
                    INNER JOIN
                        states
                    ON
                        cities.state_id = states.id
                    WHERE
                        states.name
                    LIKE
                        %(state)s
                    ORDER BY
                        cities.id ASC
                """, {'state': state})

                data = cursor.fetchall()  # obtain all data
                """Print data"""
                if not data:
                    """
                    print("Doesn't exist {0} state".format(state))
                    """
                else:
                    states = [state[0] for state in data]
                    print(*states, sep=', ', end="\n")
            db.close()

        except Exception as err:
            """
            print(err)
            """

    else:
        """
        print("Usage: ./0-select_states.py username password database state")
        """
