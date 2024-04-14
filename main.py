from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'vinay' : 'vinay.kumar@company.com'}

