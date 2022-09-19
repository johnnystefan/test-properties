# Test Properties

_Backend with Python_

### Pre-requisites 📋

_Tools needed to build the project._

```
Python 3.8.10
```

## Built with 🛠️

* [Python](https://www.python.org/downloads/) - Language in which the test is written.
* [venv](https://docs.python.org/3/library/venv.html) - Virtual environments.
* [FastAPI](https://fastapi.tiangolo.com/) - micro framework to build rest api.
* [Uvicorn](https://www.uvicorn.org/) - Server.
* [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/) - connector to MySQL DB.
* [VS Code](https://code.visualstudio.com/) - Code Editor.


### Installation 🔧

_In order to run the python script you will need to have Python installed on your system._

_It is recommended to download its 3.x versions, example:_

```
Python 3.8.10
```

_Otherwise if you use versions like:_

```
Python 2.x
```

_you should modify the code since many of the statements and syntax of the language have been updated in its 3.x versions of Python_
### How to Run the Project 📌

.-You must first install the libraries that you find in the requirements.txt (it is recommended that you do this in a virtual environment, such as venv).

.- But first let's clone the project as follows:
    on your command line create a folder (assuming you are using a unix or linux command line, bash type):

```bash
mkdir folder_test
# and
cd folder_test
```
the next thing is to clone our Repo. (ac I leave you a link to the tutorial to know how to install git)
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) - Installation link.

```bash
# with https
git clone https://github.com/johnnystefan/test-properties.git
# Or with SSH
git clone git@github.com:johnnystefan/test-properties.git
```
As we have already installed Python3, the next thing is to install a tool that helps us to have a virtual environment (like a laboratory) so that we do not affect our global development environment and we are as isolated as possible to be able to develop calmly, we do it with the commands:

```bash
# update our package system
sudo apt-get update
# dependencies and installation of virtualenv
sudo apt-get install libpython3-dev
sudo apt-get install python3-venv
```
The next thing is to run our environment, we do it in two steps, one that we will only do once:
```bash
# this allows us to install the environment in our folder
python3 -m venv venv
```
the above should create a directory with the name "venv"
then the one we will use the most is:
```bash
source venv/bin/activate
```
that activates our development environment. To deactivate it we can just write `deactivate`

what follows is to install our dependencies which we find in the `requirements.txt` file like this:

```bash
pip install -r requirements.txt
```
Then we can verify the installation:
```bash
pip list

## should show you the following list
PackageVersion
---------------------- -------
year 3.6.1
autopep8 1.7.0
click 8.1.3
fastapi 0.85.0
h11 0.13.0
idna 3.4
mysql-connector-python 8.0.30
pip 20.0.2
pkg-resources 0.0.0
protobuf 3.20.1
pycodestyle 2.9.1
pydantic 1.10.2
setuptools 44.0.0
sniffio 1.3.0
starlette 0.20.4
toml 0.10.2
typing-extensions 4.3.0
uvicorn 0.18.3
```
we can now run the following command
```bash
uvicorn controllers.main:app --host 127.0.0.1 --port 8000 --reload

### should show something like this
INFO:     Will watch for changes in these directories: ['/home/johnny/development/test_habi']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [5915] using StatReload
connection DB started
INFO:     Started server process [5917]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

#### Ready you can start testing. 🚀

## Answers Regarding Test Instructions:

Based on the second requirement, the following arises:

+ In order to continue with the other micro we must also think about creating a table to relate the tables as "Like" by users as the properties, this includes the respective ForeignKeys of the users table and the property table.
+ In the "Like" Microservice, we would only build the logic to identify the property id and mark or unmark the "Like" of the property, for this we will need the information of the property that our first microservice is doing, this information can be obtained from microservice in parallel, consuming the same api that we already created or, two, using gRPC and configuring protobuffers on both micros, gRPC being the best option in terms of performance and response speeds.
### Regarding the extra point:
++ Proposing a better structure is feasible. On my part, I also attached a file with the extension [".drawio"](https://github.com/johnnystefan/test-properties/blob/main/Drawio/model.drawio) to the repo.

* [Drawio](https://drawio-app.com/) - Viewer .drawio

<p align="center">
  <img src="https://github.com/johnnystefan/test-properties/blob/main/MER_Properties.png" alt="MER image"/>
</p>

++ I would distribute the schema in this way: For the cities I would make a table with all the cities that we manage and reference them by a City_Code, the same as for the management of the Status table (since then there may be the possibility that there are more types of states for a dwelling) since as it is currently to be able to do the information flow I must do it by string, which seems to me to be a bad practice.

++ For the "Like" proposal, I propose a new table where the foreign keys of the Property and User tables are kept, allowing the historical data of each user and in addition to keeping the record of what properties they have been given "Like", I can also count and keep track of the most attractive properties for users in a general sample.

##### NOTE: on the other hand, I see that creating a microservice for something so simple is wasting time, effort, money and more resources. An event handler in a lambda function in a Cloud service, that saves me much more resources. Since it is something that in a few lines of code I can solve.

## Author ✒️

* **Johnny Stefan Ordoñez Mazurek** - *Backend Developer* -

---
⌨️ with ❤️ made in Colombia, September 19, 2022 by [Johnny Stefan](https://github.com/johnnystefan) 😊