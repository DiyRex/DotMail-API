# main.py
from fastapi import FastAPI
import uvicorn
from dotmail import dot_trick

app = FastAPI()

c_list= []

print("Server is running :)")
print(".....................")

@app.get("/")
async def root():
    return {"message": "DotMail Api By DiyRex :)", "Usage":[{"Get_No_of_DotMails":"HOST:PORT/dotmail/[email]/[count]"},{"Get_All_DotMails": "HOST:PORT/dotmail/[email]/[count]"}]}

@app.get("/dotmail/{keyword}")
def dotmail(keyword):
    list = dot_trick(keyword)
    return {"DotMail_Count":len(list),"All_DotMails":list, "Owner":"Owned By DiyRex :)"}

@app.get("/dotmail/{keyword}/{counts}")
def dotmail(keyword, counts):
    list = dot_trick(keyword)
    for i in range(int(counts)):
        c_list.append(str(list[i]))
    return{"Requested Count":counts,"DotMails":c_list, "Owner":"Owned By DiyRex :)"}