# This is a simple api service

# Prerequisites
 * Windows OS
 * Python 3.8.x installed

# How to run locally #

* In the Python terminal navigate to the root of this repository
* create a virtual environment based on Python 3.8.6, `python -m venv .venv`
* `.\.venv\Scripts\activate`
* `pip install -r requirements.txt`
* `set FLASK_APP=api_service`
* `flask run` 
* This will run the flask application and returns the localhost url

# Usage

 * Use postman for API testing
 * API for different CRUD operations
    * GET - http://localhost:5000/items (All the items in DB)
    * GET - http://localhost:5000/items/1 (get the item with id 1)
    * POST - http://localhost:5000/items (Creates a new item)
    * PUT - http://localhost:5000/items/1 (updates the item with id 1)
    * DELETE - http://localhost:5000/items/1 (deletes the item with id 1)


* For POST & PUT the input paarameter should be a json object like below
```bash
    {
        "file_name": "XXX",
        "media_type": "YYY"
        }
```