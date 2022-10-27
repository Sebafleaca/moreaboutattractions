# moreaboutattractions
Ask wikipedia for more info about nearby point of interests!

This Python Django project is made up of three applications ("admin", "login" and the main app "attractions".
It's purpose is, first, to ask Google Maps' API for nearby attractions, then, get a short description from Wikipedia's API.
The main featured are:
- login
- info retrieval
- favourites

The project is still in development.
What still has to be done:
- checkings (allover the code)
- tests
- db management
- login management
- connection to Wikipedia API

Usage:
Install all requirements, make migrations and launch ./manage.py run server
It'll start a server at localhost:8000 with the following endpoints:
- /admin
- /login
- /attractions
- /attractions/found
- /attractions/<attraction number>
- /attractions/favorites
