# GAME-PING_CHECKER :
This website tracks the Ping in Games you will get while playing in real time. It includes servers of top played
games and are running currently. It gives user a rough idea of what ping will he get while playing these games.
The page auto refreshes in 15 seconds. The App gets all the data by SQL Querying from the game_database and 
updating the database every 15 seconds . The database was hosted locally and a exported version of the file game_
database.csv is added in the repo.




## Installation


* clone the repo and type `flask run` in the terminal directory.
* * `pip install requirements.txt`
* Open 127.0.0.1:5000 in the Browser.



## Usage


Run `flask run` to :
* Get list of games with their Pings from your current network.


![alt text](https://github.com/saifkwik/Game_Ping_Checker/blob/master/Screenshot-1.png)

![alt text](https://github.com/saifkwik/Game_Ping_Checker/blob/master/Screenshot-2.png)
