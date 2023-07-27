# Error-Middleware
***
A Django Middleware which will intercept each http response and if any error occurs it does the following:
● If Response "status_code" is in the given list (the list is
provided in settings file), then it should log the complete error stack and
insert it into the sqllite database in the given format.
    - { “status_code”: “xxx”,
    “error”: “Error Stack”
    }
● Responds the same request with the
    - { “status_code”:200,
    “error”: “Error”
    }

An independent django app which will allow CRUD operations and search operations for the above Error table.
***

Prerequisites: After getting the code into your remote system install packages from requirements.txt using "pip install -r requirements.txt" into your desired python virtual environment.

The API's Postman collection is in the root directory with name ErrorLog_Middleware_API's_Collection.postman_collection.json, simply import the collection and Happy API Testing.

***
Note: The Middleware file is in error_app but since it's added in settings.py middlewares it became global. And the error_app is there to add the CRUD functionality for the Error_Logs, and the API collection is provided for the same. 

***
P.S. please ignore the templates as they are just there in case you wanna have a little better FE part for this code. 
