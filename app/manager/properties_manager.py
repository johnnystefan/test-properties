# FastAPI
from fastapi import Response
# App
from db.connector_db import Finder

finder = Finder()

class PropertiesManager:
    def __init__(self):
        pass

    def get_properties(self):
        properties = finder.get_properties()
        return  properties

    def get_properties_filtered(self,year, city, status):
        if status != 'comprado' or status != 'comprando':
            properties = finder.get_properties_filtered(year, city, status)
            return  properties
        else:
            return Response(status_code=status.HTTP_204_NO_CONTENT)