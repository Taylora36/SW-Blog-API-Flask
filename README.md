<div align="center">
<img width="100%" alt="Screenshot 2023-07-15 162514" src="https://github.com/Taylora36/SW-Blog-API-Flask/assets/118857845/4fa6e5bd-5dfc-474c-956e-24839c653656">
</div>

# Star Wars Blog

Star Wars blog presents a list of categorized cards that users can sift through to learn more about that Star Wars character, planet, or vehicle.

### Categories:
- Characters
- Planets
- Vehicles

### Outline
- Click on Details to load single page view of the card, which shows additional information on that entry
- Can favorite multiple cards
- Can also delete cards from user favorites

## Technologies
<div align="center">
  <img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E">
  <img src="https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white">
</div>

## Additional Features
Some features to add:
- Spaceships category
- More information for each card
- Profile page to interact with favorites

## How to Use
- pipenv run start
- npm run start

## Features
### Home Page
<img width="820" alt="Screenshot 2023-07-15 162632" src="https://github.com/Taylora36/SW-Blog-API-Flask/assets/118857845/b8d3bbe8-cf2c-4793-9ef9-644c9840e6e7">
<img width="816" alt="Screenshot 2023-07-15 162645" src="https://github.com/Taylora36/SW-Blog-API-Flask/assets/118857845/9db29877-7d27-43bc-b6af-ed7e7812a86b">
<img width="813" alt="Screenshot 2023-07-15 162658" src="https://github.com/Taylora36/SW-Blog-API-Flask/assets/118857845/51b51d2d-8c4a-4c60-8861-4677594f2ebb">

### Single Card View
<img width="854" alt="Screenshot 2023-07-15 162714" src="https://github.com/Taylora36/SW-Blog-API-Flask/assets/118857845/de3f225e-d393-4a03-a8aa-658a1a9f8cf3">
<img width="829" alt="Screenshot 2023-07-15 162735" src="https://github.com/Taylora36/SW-Blog-API-Flask/assets/118857845/0066f9c2-40a5-439d-abc9-758505a2420d">
<img width="834" alt="Screenshot 2023-07-15 162756" src="https://github.com/Taylora36/SW-Blog-API-Flask/assets/118857845/23ef9e56-9e48-4e63-8815-cb4ba5688372">

### Favorites
<img width="158" alt="Screenshot 2023-07-15 162542" src="https://github.com/Taylora36/SW-Blog-API-Flask/assets/118857845/16356425-9e70-44b4-935c-5d81d9fd9530">
<img width="151" alt="Screenshot 2023-07-15 162602" src="https://github.com/Taylora36/SW-Blog-API-Flask/assets/118857845/7d2b28bd-724d-4b50-a703-5ea2516d1c03">

# WebApp boilerplate with React JS and Flask API

Build web applications using React.js for the front end and python/flask for your backend API.

- Documentation can be found here: https://start.4geeksacademy.com/starters/react-flask
- Here is a video on [how to use this template](https://www.loom.com/share/f37c6838b3f1496c95111e515e83dd9b)
- Integrated with Pipenv for package managing.
- Fast deloyment to heroku [in just a few steps here](https://start.4geeksacademy.com/backend/deploy-heroku-posgres).
- Use of .env file.
- SQLAlchemy integration for database abstraction.

### Manual Installation:

It is recomended to install the backend first, make sure you have Python 3.8, Pipenv and a database engine (Posgress recomended)

1. Install the python packages: `$ pipenv install`
2. Create a .env file based on the .env.example: `$ cp .env.example .env`
3. Install your database engine and create your database, depending on your database you have to create a DATABASE_URL variable with one of the possible values, make sure you replace the valudes with your database information:

| Engine    | DATABASE_URL                                        |
| --------- | --------------------------------------------------- |
| SQLite    | sqlite:////test.db                                  |
| MySQL     | mysql://username:password@localhost:port/example    |
| Postgress | postgres://username:password@localhost:5432/example |

4. Migrate the migrations: `$ pipenv run migrate` (skip if you have not made changes to the models on the `./src/api/models.py`)
5. Run the migrations: `$ pipenv run upgrade`
6. Run the application: `$ pipenv run start`

### Backend Populate Table Users

To insert test users in the database execute the following command:

```sh
$ flask insert-test-users 5
```

And you will see the following message:

```
  Creating test users
  test_user1@test.com created.
  test_user2@test.com created.
  test_user3@test.com created.
  test_user4@test.com created.
  test_user5@test.com created.
  Users created successfully!
```

To update with all yours tables you can edit the file app.py and go to the line 80 to insert the code to populate others tables

### Front-End Manual Installation:

-   Make sure you are using node version 14+ and that you have already successfully installed and runned the backend.

1. Install the packages: `$ npm install`
2. Start coding! start the webpack dev server `$ npm run start`

## Publish your website!

This boilerplate it's 100% read to deploy with Render.com and Heroku in a matter of minutes. Please read the [official documentation about it](https://start.4geeksacademy.com/deploy).

### Contributors

This template was built as part of the [Full Stack Developer course](https://4geeksacademy.com/us/coding-bootcamps/part-time-full-stack-developer) at [4Geeks Academy Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) by [Alejandro Sanchez](https://twitter.com/alesanchezr) and [many other contributors](https://github.com/4GeeksAcademy/react-flask-hello/graphs/contributors).

You can find other templates and resources like this at the [school github page](https://github.com/4geeksacademy/).
