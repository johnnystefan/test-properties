# FastAPI
from fastapi import Response
# App
from db.connector_db import Finder

finder = Finder()

class PropertiesManager:
    """_summary_
    This manager is in charge of being an intermediary
    between the finder and the controller
    """
    def __init__(self):
        pass

    def get_properties(self):
        """_summary_
        Receive the response that comes from the database
        with the json of the properties available to the user
        and serves them to the controller.

        Returns:
            josn
        """
        properties = finder.get_properties()
        return  properties

    def get_properties_filtered(self,year, city, status):
        """_summary_
        Receive the response that comes from the database
        with the json of the properties available to the user
        and serves them to the controller.

        Returns:
            josn
        """
        if status != 'comprado' or status != 'comprando':
            properties = finder.get_properties_filtered(year, city, status)
            return  properties
        else:
            return Response(status_code=status.HTTP_204_NO_CONTENT)