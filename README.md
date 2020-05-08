## Project Name

Pitch Application

## Author Information

Muthoni Njuguna

## Description

This is a python-based web application that allows users to submit ideally one-minute pitches as well as provide feedback on other people's posts. 


## User Stories

As a user, you will be able to:

  1. View pitches posted by other users.
  2. Sign up to the account
  3. Like and dislike pitches. 
  4. Submit feedback or comment on other people's pitches.
  5. Submit a pitch in any category
  6. View a users pitches by their profile.
  7. A signed user can delete and update their pitches.


## Technologies Used

<ul>
<li>Python</li>
<li>Flask</li>
<li>HTML, CSS and Bootstrap</li>
<li>Javascript</li>
</ul>

## BBD

| Behaviour	|Input | Output|
|---------------------------|---------------------|--------------------------|
|Register on the site|	User's username, email and password|User receives a welcome email|
|Log into the site	| Enter credentials	| Gets logged in and redirected to the homepage|
|Publish a pitch	| Enter a pitch and submit the form | Pitch is posted on the homepage |
| View another users profile | Click on a users name | Users username, email, and posted pitches are displayed |
| Comment on a pitch | Click on a pitch's title or comment icon and enter comment in form| comment is posted below the pitch|

## Setup/Installation Requirements

1. Clone the application by running git clone https://github.com/Brenda-M/pitch-capital.git on the teminal.
2. Create a virtual environment.
3. Pip3 install -r requirements.txt 
4. Add export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name} to the start.sh file export the configuration.
5. Also,create a secret key and add it to start.sh
6. Run $ ./start.sh on your terminal to start your local server and view the application on your browser.

## Contact Information

In case of any feedback, you can reach me through: -brendanjuguna1@gmail.com

## License

The MIT License (MIT) Copyright (c) 2020 Muthoni Njuguna.


