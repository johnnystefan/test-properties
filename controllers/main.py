# FastAPI
from fastapi import FastAPI, status, HTTPException
from fastapi import Body

# App
from app.manager.properties_manager import PropertiesManager

app = FastAPI()
manager = PropertiesManager()


@app.get("/")
def home():
    """_summary_
    App Home

    Args:
        Empty

    returns:
        str: Welcome Message
    """
    return {"Welcome": "Test Habi Backend"}


@app.get("/property/get-properties")
def get_properties():
    """_summary_
    From this path we obtain the available properties
    For the users.

    Args:
        Empty

    Response:
        "ID": "The ID of the property",
        "Address": "Property address",
        "City": "City where the property is located",
        "Price": "The cost of ownership",
        "Description": "A brief description of the property",
        "Year": "Year the property was built",
        "Status": "The status or availability of the property"
    """
    properties = manager.get_properties()
    if properties == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"list properties does not exist")
    return  properties


@app.post("/property/get-properties-filtered")
def get_properties_filtered(
    year: int = Body(
        title="Year",
        default=2022,
        description="This is the year.",
        ge=0,
        lt=2023
        ),
    city: str = Body(
        title="City",
        default='bogota',
        description="This is the city Property. It's between 1 and 50 characters",
        min_length=1,
        max_length=50
        ),
    status: str = Body(
        title="Status",
        default="pre_venta",
        description="This is the Status Property.",
        max_length=50,
        )
):
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
    properties = manager.get_properties_filtered(year, city, status)
    if properties == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"property list for that filter:'{year}','{city}' and '{status}' does not exist")
    return  properties
