# paathshaala-user
Repo for Professor portal of CS258 project
#  Flask course management system with jinja2 as rendering engine
## Usage Instructions

- Create an empty folder and cd into it

- Git Clone the paathshaala-user repo.

- Git Clone the paathshaala-professor repo.

- To run user portal:

  

```bash
cd paathshaala-user
python3 -m venv venv
source venv/bin/activate # if you're on windows run the following command instead
venv\Scripts\activate.bat
pip install -r requirements.txt
cd ..
mkdir temp(if temp does not exist)
mkdir static_material(if static_material folder does not exist already)
cd paathshaala-user
python3 app.py
```



The user portal can be opened up at localhost:5001
## Testing

To run tests on the app, run the following commands(in the root folder of app)

```
source venv/bin/activate 
venv\Scripts\activate.bat# if you're on windows run the following command instead of above
pip install -e .
export testing=true
```

then just a simple `pytest -v` will run all the functional and unit tests.

**After you are done testing make sure to run** `export testing=false`

