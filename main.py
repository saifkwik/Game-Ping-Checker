from pythonping import ping
import re
import mysql.connector
from datetime import datetime

# import database from sql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rango6",
    database='game_database'
)
# specifying which table to import
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM game_database.GAME_DATABASE')

# saving table contents to myresult list
myresult = mycursor.fetchall()


# function to take ip and average its ms and return in form of dictionary
def ping_checker(ip):
    ms_variable = 1  # number of ping output we want to take, the more the accurate
    a = []
    c = []
    total = 0
    for i in range(0, ms_variable):
        a.append(ping(ip))
        b = str(a)
    pattern = r'/[0-9]*?.[0-9]{1,3}/'
    ping_list = []
    for pings in b:
        ping_list = re.findall(pattern, b)
    pings = [sub.replace('/', '') for sub in ping_list]
    for ping_avg in pings:
        c.append(float(ping_avg))
    for ele in range(0, len(c)):
        total = (total + c[ele])
    return {ip: (round(total / ms_variable, 2))}


# extracting and saving dns present in values variable which we saved it from database table
dns_in_db = []
p = 0  # p is rows in the table
for dns_in_database in myresult:
    dns_in_db.append(myresult[p][0])
    p += 1
# print(dns_in_db)


def display(dns_in_db):
    # passing the list of dns from database to function created and saving the output in list
    output = []
    for dns_addresses in dns_in_db:
        try:
            result = ping_checker(dns_addresses)
            # print(result)
            now = datetime.now()
            current_time = now.strftime('%H:%M:%S')
            index = 0
            row_count = 0
            for details in myresult:
                dns = [*result.keys()]
                ms = [*result.values()]
                if dns[0] in myresult[index]:
                    print(f'{myresult[index][1]} DNS is {dns[0]} and you are getting {ms} ms at {current_time} time.'.replace( '[', '').replace(']', ''))
                    output.append(
                        f'{myresult[index][1]} DNS is {dns[0]} and you are getting {ms} ms at {str(current_time)}. '.replace(
                            '[', '').replace(']',
                                             ''))
                    sql_insert = 'UPDATE GAME_DATABASE SET PING_AVG = %s, UPDATED_AT = %s WHERE IP = %s'
                    # val = (str(myresult[index][0]), str(dns[0]), str(ms).replace('[', '').replace(']', ''),
                    # str(current_time))
                    val = (str(ms).replace('[', '').replace(']', ''), str(current_time), str(dns[0]))
                    mycursor.execute(sql_insert, val)
                    mydb.commit()
                    # print(output)
                row_count += 1
                index += 1
        except RuntimeError as r:
            print(str(dns_addresses) + ' is down')
            continue
    print('Values Updated in game_database successfully')
    return output

# print(display(dns_in_db))
