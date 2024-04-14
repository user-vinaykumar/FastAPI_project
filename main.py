from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'vinay' : 'vinay.kumar@company.com'}

@app.get('/posts')
def get_posts():
    return {'data' : 'this is my post'}