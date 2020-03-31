import mysql.connector


def database(query, params):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="safehouse",
            passwd="safehouse2020",
            database="safehouse1",
            auth_plugin='mysql_native_password'
        )
        cursor = connection.cursor()
        # print(str(params))
        cursor.execute(query, params)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def check_username(username):
    sql = "SELECT nickname FROM telegram_bot WHERE nickname=%s"
    return database(sql, [username])


def sensors_state(username):
    sql = "SELECT house_id FROM telegram_bot WHERE nickname=%s"
    result = database(sql, [username])
    sql1 = "SELECT sensor.id, name, valve, last_seen, last_data FROM sensor " \
           "INNER JOIN sensor_state ON sensor.id=sensor_state.sensor_id " \
           "WHERE sensor.house_id=%s"
    print(result[0][0])
    # print(database(sql, [result[0][0]))
    print(database(sql1, [result[0][0]]))
    return database(sql1, [result[0][0]])
# def get_house_sensors(house_id):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT sensor.id, name, valve, last_seen, last_data FROM sensor "
#                        "INNER JOIN sensor_state ON sensor.id=sensor_state.sensor_id "
#                        "WHERE sensor.house_id=%s", [house_id])
#         return cursor.fetchall()