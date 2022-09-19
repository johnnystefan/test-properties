#TestProperties

_Backend with Python_

### Pre-requisites 📋

_Tools needed to build the project._

```
Python 3.8.10
```

## Built with 🛠️

* [Python](https://www.python.org/downloads/) - Language in which the test is written.
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
## How to Run the Project 📌

.-You must first install the libraries that you find in the requirements.txt (it is recommended that you do this in a virtual environment, such as venv).

.-Then run the following command:
```
uvicorn controllers.main:app --host 127.0.0.1 --port 8000 --reload
```

.-Ready you can start testing.

## Answers Regarding Test Instructions:

Based on the second requirement, the following arises:

+ In order to continue with the other micro we must also think about creating a table to relate the tables as "Like" by users as the properties, this includes the respective ForeignKeys of the users table and the property table.
+ In the "Like" Microservice, we would only build the logic to identify the property id and mark or unmark the "Like" of the property, for this we will need the information of the property that our first microservice is doing, this information can be obtained from microservice in parallel, consuming the same api that we already created or, two, using gRPC, gRPC being the best option in terms of performance and response speeds.
### Regarding the extra point:
++ Proposing a better structure is feasible. On my part, I also attached a file with the extension ".drawio" to the repo.

++ I would distribute the schema in this way: For the cities I would make a table with all the cities that we manage and reference them by a City_Code, the same as for the management of the Status table (since then there may be the possibility that there are more types of states for a dwelling) since as it is currently to be able to do the information flow I must do it by string, which seems to me to be a bad practice.

++ For the "Like" proposal, I propose a new table where the foreign keys of the Property and User tables are kept, allowing the historical data of each user and in addition to keeping the record of what properties they have been given "Like", I can also count and keep track of the most attractive properties for users in a general sample.


## Author ✒️

* **Johnny Stefan Ordoñez Mazurek** - *Backend Developer* -

---
⌨️ with ❤️ made in Colombia, September 19, 2022 by [Johnny Stefan](https://github.com/johnnystefan) 😊