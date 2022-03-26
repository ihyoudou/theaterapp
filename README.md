# Theaterapp
![page with movie details](https://raw.githubusercontent.com/ihyoudou/theaterapp/main/readme/movie_details_view.png)


Theaterapp is a test app written in Python Django as a exercise.

## What does it contain

* Register, login system
* Movies listing
* Rating system
* Ticket buying system
* List of available dates
* User list of purchases
* Paginator and search function

It doesn't have a poster upload function, but it is using [Lorem Picsum](https://picsum.photos/) to display some example photos.

## How to run
By default, it is using sqlite database - it is not the best db system, but for a small test app it is enough.
To run the app, you need Python 3 and PIP

```
git clone https://github.com/ihyoudou/theaterapp
cd theaterapp
pip3 install -r requirements.txt
python3 manage.py makemigration
python3 manage.py migrate
```

Start server
```
python3 manage.py runserver
```

You can also populate the database with example data using populate_data script
```
python3 populate_data.py
```

And add superuser to use Django admin panel
```
python3 manage.py createsuperuser
```
