![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Deployed app: https://pp04.herokuapp.com/





# Setting Up

To set up this project I have installed the necessary libraries and deployed the project to Heroku on an earlier stage, to make sure that the project is working. 

The stages are: 

1. Install Django and necessary libraries and create a Django Project and App
2. Configure the project to use Cloudinary and PostgreSQL
3. Deploy to Heroku

<details>
<summary>Install Django and Create Project and App</summary>

In the terminal type the following commands to install a recommend version of Django and the necessary libraries:

```python
pip3 install 'django<4' gunicorn

pip3 install dj_database_url==0.5.0 psycopg2
```

The images for this project will be hosted by Cloudinary. That requires some libraries to be installed. For that we use the following commands: 

```bash
pip3 install dj3-cloudinary-storage
pip3 install urllib3==1.26.15
```

At this stage we can create the requirements.txt file, with the command: 

```bash
pip3 freeze --local > requirements.txt
```

Create a new Django project and app:

```bash
django-admin startproject fourth_pp .
python3 manage.py startapp fourth_app
```

In the “fourth_pp” folder, edit the [settings.py](http://settings.py) to include the new app “fourth_app”. It may also be necessary to update the filed ALLOWED_HOSTS. 

The changes now need to be migrated to the data base: `python3 manage.py migrate`

To run the server simply type `python3 [manage.py](http://manage.py) runserver`
</details>

Create super user

Deployment



