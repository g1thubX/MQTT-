import paho.mqtt.client as mqtt
import sqlite3

# 连接 MQTT 代理服务器
client = mqtt.Client()
client.connect("localhost", 1883, 60)

# 连接 SQLite 数据库
conn = sqlite3.connect('data.db')

# 创建数据表
# conn.execute('''CREATE TABLE sensor_data
#              (id INTEGER PRIMARY KEY AUTOINCREMENT,
#               topic TEXT NOT NULL,
#               value TEXT NOT NULL,
#               timestamp INTEGER NOT NULL);''')

# 定义回调函数
def on_message(client, userdata, message):
    topic = message.topic
    value = message.payload.decode('utf-8')
    timestamp = int(time.time())
    conn.execute("INSERT INTO sensor_data (topic, value, timestamp) VALUES (?, ?, ?)", (topic, value, timestamp))
    conn.commit()
    print("Received data: topic={}, value={}".format(topic, value))

# # 订阅 MQTT 主题
# client.subscribe("sensor/temperature")
# client.subscribe("sensor/humidity")
# client.on_message = on_message

# 订阅 MQTT 主题
result_temperature, _ = client.subscribe("sensor/temperature")
result_humidity, _ = client.subscribe("sensor/humidity")
if result_temperature == mqtt.MQTT_ERR_SUCCESS:
    print("Successfully subscribed to temperature topic.")
else:
    print("Failed to subscribe to temperature topic.")
if result_humidity == mqtt.MQTT_ERR_SUCCESS:
    print("Successfully subscribed to humidity topic.")
else:
    print("Failed to subscribe to humidity topic.")
client.on_message = on_message


# 运行 MQTT 客户端
client.loop_forever()
