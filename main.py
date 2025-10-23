from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
import random
import string
from configuration import collection
from schema import short_url, all_url

resource = string.ascii_letters
resource += "-"

app=FastAPI()

@app.get("/shorten")
def shorten(req: str):
    allUrls = all_url(collection.find())

    for i in allUrls:
        if i["long_url"] == req:
            return JSONResponse({"message": "Already exists !"})

    val = ""

    for _ in range(5):
        val += random.choice(resource)

    try:
        collection.insert_one(short_url({"sURL": val, "lURL": req}))
    except:
        Exception ("Failed to insert")

    res = {
        "message": "Successfully created",
        "newURL": "https://url-shortner-lon6.onrender.com/"+val
    }
    return JSONResponse(res)


@app.get("/{req}")
def get_original_URL(req: str):
    allUrls = all_url(collection.find())

    for i in allUrls:
        if i["short_url"] == req:
            return RedirectResponse(url=i["long_url"])
    
    err_res = {
        "message": "Invalid URL!"
    }

    return JSONResponse(err_res)
