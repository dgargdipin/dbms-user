Repo for User portal of CS207 project Course management system.
#  Flask course management system with jinja2 as rendering engine
## Usage Instructions

- Create an empty folder and cd into it

- Git Clone the dbms-user repo.

- Git Clone the dbms-professor repo.

- To run user portal:

  

```bash
cd dbms-user
python3 -m venv venv
source venv/bin/activate # if you're on windows run the following command instead
venv\Scripts\activate.bat
pip install -r requirements.txt
cd ..
mkdir temp
mkdir static_material
cd dbms-user
python3 app.py
```



The user portal can be opened up at localhost:5001
