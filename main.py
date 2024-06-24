import uvicorn

if __name__ == "__main__":
    print("hello __main__")
    uvicorn.run(
        "app.server:app",
        host="0.0.0.0",
        port=80,
        reload=False
    )
