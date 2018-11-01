# Kroon Studio PDT

Kroon Studio Backend API project

## About project

This is Django Rest Framework project built with Python 3.6

### Requirements

All requirements are in requirements/requirements.txt file


### Installing

pip install requirements/requirements.txt

```
  Inside project, there is virtual environment (.ent_kroon) with all requirements already installed.
```

## Running

  All API endpoints are in this location: http://127.0.0.1:8000/api/
     
## Running celery task for sending email reports
```  
  celery -A KroonStudioPDT beat -l info
  
  celery -A KroonStudioPDT worker -l info
```  
 
## Documentation

  API documentation is made with Swagger: http://127.0.0.1:8000/api-doc/

## Authors

* **Milos Damjanovic** - (https://github.com/mdamjanovic2012)
