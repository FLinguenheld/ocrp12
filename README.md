![badge](https://img.shields.io/static/v1?label=Project&nbsp;OC&message=12&color=blueviolet&style=for-the-badge)
![badge](https://img.shields.io/static/v1?label=Status&message=InProgress&color=blue&style=for-the-badge)

# ocrp12

Develop a Secure Back-End Architecture Using Django ORM

![Logo epicevents](https://raw.githubusercontent.com/FLinguenheld/ocrp12/main/logos/epicevents.png "Logo")


****
### Documentation

All endpoints are explained in the Postman documentation :  

[![Logo PostMan](https://raw.githubusercontent.com/FLinguenheld/ocrp12/main/logos/postman.png "Postman")](https://documenter.getpostman.com/view/19051270/2s8YzXwLV1)

To easily add several users, you can use the file *postman_init.py*.  
💡 You need user credentials who's authorised to create new users (admin or manager).  

Launch the server in a terminal. Then open a new one, move into the root folder and use the command :  

    python postman_init.py --email <admin@epiccrm.com> --password <admin01234>

Five users will be created :

    manager@postman.com
    salesperson@postman.com
    salesperson_2@postman.com
    technical_support@postman.com
    test@test.com

    test01234

****
### Database

This application uses [postgresql](https://www.postgresql.org). You have to install it according to your distribution then 
create a dabase and an user with this information :

    database name : epic_events
    user : epic_user
    user password : 01234

Django will search the database on *localhost* with the port *5432*.  
You can change this behaviour in the settings files.

Here an example to create a new database :

    sudo -u postgres psql
    create database epic_events
    (drop database epic_events)

Django administration is activated, you can create a superuser and open it with the link :  
http://localhost:8000/admin/

    python manage.py createsuperuser

    admin@epiccrm.com
    admin01234

****
### Testing

This code used the framework [pytest](https://docs.pytest.org/en/latest/contents.html) and the plugin [pytest-django](https://pytest-django.readthedocs.io/en/latest/index.html) to test endpoints.  
To launch a new test, open a terminal, navigate into the root folder and activate the virtual environment.  
Then launch the command :

    pytest -v

****
### Diagram

![Epic crm diagram](https://raw.githubusercontent.com/FLinguenheld/ocrp12/main/logos/Diagram_Epic_events.png "Logo")
