from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app= FastAPI()

# we only need 2 parameters for a to-do list
# we'll pass Item to def create_item and get_item
class Item(BaseModel):
    text: str = None # right now it's not required. Just remove "None" to make this field required. 
    is_done: bool = False

items=[] #empty items list

# this is how we define a path in fastAPI
# @ is decorator 
# so when someone visits "/" the root function will be called and then we'll return hello world object
@app.get("/")
def root():
    return {"Hello":"World"}

# new end point of our app
# user can access this by sending a http request to /items path 
# and it's gonna accept "item:str" as input
# then it'll return the item or items list as well (your choice)

@app.post("/items")
def create_item(item: Item): # instead of def create_item(item:str):
    items.append(item)
    return items

# endpoint to list items till limit 
# so if we mention limit as "items?limit=3" then it'll mention 0,1,2,3
# if no parameter has been mentioned then it'll mention default "10 items"  

@app.get("/items", response_model=list[Item]) #response model for list of items
def list_items(limit: int = 10):
    return items[0:limit]


# it fetches item_id(int) from item i.e apple(str),etc
# as precaution for internal server error we added 
# a 404 status code if user is calling something out of index
# detail is a info parameter

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int)->Item: #Item instead of str as return type
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"item {item_id} not found") 

