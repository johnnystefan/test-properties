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
    Home De la App

    Args:
        Empty

    Returns:
        str: Mensaje de Bienvenida
    """
    return {"Welcome": "Test Habi Backend"}


@app.get("/property/get-properties")
def get_properties():
    """_summary_
    Desde este path obtenemos las propiedasdes disponibles
    para los usuarios.

    Args:
        Empty

    Response:
        "ID": "El ID de la propiedad",
        "Address": "Direccion de la propiedad",
        "City": "Ciudad donde se ubica la propiedad",
        "Price": "El costo de la propieda",
        "Description": "Una breve descripcion de la propiedad",
        "Year": "Año en la que se construyo la propiedad",
        "Status": "El estado o disponibilida de la propiedad"
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
    Filtrar las propiedades por año, ciudad y disponibilidad.

    Args:
        year (int): Año de Construccion de la propiedad.
        city (str): Ciudad donde se ubica la propiedad.
        status (str): Estado o disponibilidad de la propiedad.

    Returns:
        "ID": "El ID de la propiedad",
        "Address": "Direccion de la propiedad",
        "City": "Ciudad donde se ubica la propiedad",
        "Price": "El costo de la propieda",
        "Description": "Una breve descripcion de la propiedad",
        "Year": "Año en la que se construyo la propiedad",
        "Status": "El estado o disponibilida de la propiedad"
    """
    properties = manager.get_properties_filtered(year, city, status)
    if properties == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"property list for that filter:'{year}','{city}' and '{status}' does not exist")
    return  properties
