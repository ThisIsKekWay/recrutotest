from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
async def say_hello(
        name: str = Query("name"),
        message: str = Query("message")
):
    return f"Hello {name}! {message}!"
