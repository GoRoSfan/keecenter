# KEECenter

### Build 
```
docker compose run web python manage.py makemigrations
docker compose run web python manage.py migrate
```
Next run command

`docker compose run web python manage.py createsuperuser`

Enter your desired username and press enter.

`Username: admin`

The final step is to enter your password. 
You will be asked to enter your password twice, 
the second time as a confirmation of the first.

```
Password: **********
Password (again): *********
```

Finally

`docker compose up`

### Routes
admin panel link: `/admin/`