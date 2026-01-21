This is a really basic example of FastAPI application

In your project root (code editor terminal):

do

python -m venv venv
venv\Scripts\activate (or add source before this if you're using mingw64 bash)

then install

pip install fastapi uvicorn (uvicorn will be our server where we'll test our fastpi application)

pip freeze > requirements.txt (optional but do this as well)

init:

go through main.py first init commit

so to start with the server do "uvicorn main:app --reload" 
(reload is similar to nodemon app.js which reload the website after changes in main branch/file)

get and post routes:

for sending post request from terminal use this format
curl -X POST -H "[HeaderName]: [HeaderValue]" -d "[Data]" [URL]

in my create_item case it'll be

curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple'

for get request 
curl -X GET http://127.0.0.1:8000/items/0

handling HTTP errors:

import HTTPException and then raise the errors

req and path parameters:

refer to list_items

so we're using pydantic as pydantic allows to structure data and provides additional validation
which makes things like testing ,documentaion and code conmpletion in your IDE easy-ish  

after model base introduction curl is not gonna work as we mentioned item 
(i.e curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple') 
through query parameter
but when we use the model object like " item:Item " as part of the arguement in def func
it's gonna expect that to be in the json payload of the request

to make it work, we've to send this item data as a json payload instead
ex:
curl -X POST -H "Content-Type: application/json" -d '{"text" : "apple"}' 'http://127.0.0.1:8000/items'

that should return 

[{"text":"apple","is_done":false}](venv) 

response models:

refer to where you get the items 
then add a new arguement to the decorator called response model

this helps in easy to work with front end 

interactive documentaion:

in url add docs# to get interative buttons for curl in terminal that we've been using
i.e. http://127.0.0.1:8000/docs#/
and
http://127.0.0.1:8000/redoc

