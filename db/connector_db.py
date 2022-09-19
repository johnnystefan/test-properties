# MySQL
from mysql.connector import connect, Error

# Config
from config import settings

class Finder:
    """_summary_
    Finder is the one in charge of making the queries
    to the database.

    Features:
    connection : Create and get connection to MySQL
    """
    def __init__(self):
        self.connection = connect(
            host=settings.database_hostname,
            port=settings.database_port,
            user=settings.database_username,
            password=settings.database_password,
            db=settings.database_name
        )
        print(f"connection DB started")

    def __del__(self):
        """_summary_
        Once the app cycle is destroyed, this close
        the connection to the database.
        """
        if self.connection.is_connected():
            self.connection.close()
            print(f"connection DB finished")

    def get_properties(self):
        """_summary_
        Get the list of all properties
        available to the user.

        Returns:
            Type: json
            "ID": "The ID of the property",
            "Address": "Property address",
            "City": "City where the property is located",
            "Price": "The cost of ownership",
            "Description": "A brief description of the property",
            "Year": "Year the property was built",
            "Status": "The status or availability of the property"
        """
        try:
            with self.connection.cursor() as cursor:
                get_properties_query = '''
                                        SELECT
                                            PR.id as ID,
                                            PR.address as Address,
                                            PR.city as City,
                                            PR.price as Price,
                                            PR.description as Description,
                                            PR.year as Year,
                                            ST.name as Status
                                            FROM property PR
                                        INNER JOIN status_history SH ON PR.id = SH.property_id
                                        INNER JOIN  status ST ON SH.status_id = ST.id
                                        WHERE ST.name not in ('comprando','comprado')
                                        GROUP BY PR.id
                                        '''
                cursor.execute(get_properties_query)
                columns = [column[0] for column in cursor.description]
                results = []
                for row in cursor.fetchall():
                    results.append(dict(zip(columns, row)))
                return results
        except Error as ex:
            print(ex)

    def get_properties_filtered(self, year=2022, city='bogota', name='pre_venta'):
        """_summary_
        Filter properties by year, city and availability.

        Args:
            year (int): Year of construction of the property.
            city ​​(str): City where the property is located.
            status (str): Status or availability of the property.

        returns:
            "ID": "The ID of the property",
            "Address": "Property address",
            "City": "City where the property is located",
            "Price": "The cost of ownership",
            "Description": "A brief description of the property",
            "Year": "Year the property was built",
            "Status": "The status or availability of the property"
        """
        try:
            with self.connection.cursor() as cursor:
                if year == None:
                    year = ''
                if city == None:
                    city = 'Null'
                if name == None:
                    name = ''
                get_properties_filtered_query = f'''
                                        SELECT
                                            PR.id as ID,
                                            PR.address as Address,
                                            PR.city as City,
                                            PR.price as Price,
                                            PR.description as Description,
                                            PR.year as Year,
                                            ST.name as Status
                                            FROM property PR
                                        INNER JOIN status_history SH ON PR.id = SH.property_id
                                        INNER JOIN  status ST ON SH.status_id = ST.id
                                        WHERE ST.name not in ('comprando','comprado')
                                        and (PR.`year` IS NOT NULL
                                        and PR.description IS NOT NULL
                                        and (PR.`year` = {year} OR PR.city = '{city}' or ST.name = '{name}'))
                                        GROUP BY PR.id
                                        '''
                print(get_properties_filtered_query)
                cursor.execute(get_properties_filtered_query)
                columns = [column[0] for column in cursor.description]
                results = []
                for row in cursor.fetchall():
                    results.append(dict(zip(columns, row)))
                return results
        except Error as ex:
            print(f"Error en la base de datos: {ex}")
