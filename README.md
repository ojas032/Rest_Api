# Rest_Api<br>

## Instructions For Mac:-<br>

**Steps 1:-**<br>
#### Create Virtual Environment  and Activate It Use the command:-<br>
virtualenv venv<br>
source venv/bin/activate<br>

**Step 2:-**<br>
#### Install all the required libraries:-<br>
pip3 install -r requirements.txt<br>
python3 init.py

## Instructions for Windows:-<br>
**Steps 1:-**<br>
#### Create Virtual Environment  and Activate It Use the command:-<br>
python3 -m venv rest-env<br>
rest-env\Scripts\activate.bat<br>

**Step 2:-**<br>
#### Install all the required libraries:-<br>
pip install -r requirements.txt<br>
python init.py

**Step 3:-**<br>
#### Open Postman To send or receive data in database:-

##### Url Format:
http://127.0.0.1:5000/student/Name/Age/Standard <br>  

Case 1: If the Student is not present in the Database on Get Request it will return {"name":"none"}<br>
![img1](https://github.com/ojas032/Rest_Api/blob/master/Snapshots/Screenshot%20(59).png)

Case 2: Send the Student in the Database using the Post Request<br>
![img1](https://github.com/ojas032/Rest_Api/blob/master/Snapshots/Screenshot%20(60).png)

Case 3:If the Student is present in the database on Get Request<br>
![img1](https://github.com/ojas032/Rest_Api/blob/master/Snapshots/Screenshot%20(61).png)


###### DataBase Used :Sqlite<br>

###### For any queries contact me at:-<br>
###### corpojasltd@gmail.com

