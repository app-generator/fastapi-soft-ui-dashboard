import uvicorn

if __name__=='__main__':
    uvicorn.run("server:create_app", port=5000, reload=True)