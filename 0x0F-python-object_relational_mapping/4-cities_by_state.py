#!/usr/bin/python3
"""
script that takes in an argument and displays
all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    if (len(argv) == 4):
        user = argv[1]
        password = argv[2]
        database = argv[3]

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
                        cities.id, cities.name, states.name
                    FROM
                        cities
                    INNER JOIN
                        states
                    ON
                        cities.state_id = states.id
                """)

                data = cursor.fetchall()  # obtain all data
        except Exception as err:
            """
            print(err)
            """

        """Print data"""
        if not data:
            """
            print("Doesn't exist {0} state".format(state))
            """
        else:
            [print(state) for state in data]
    else:
        """
        print("Usage: ./0-select_states.py username password database")
        """
