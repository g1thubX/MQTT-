#温湿度传感器模拟器文件
import paho.mqtt.client as mqtt
import random
import time

# 连接 MQTT 代理服务器
client = mqtt.Client()
client.connect("localhost", 1883, 60)

# 模拟传感器数据，并将数据发布到主题
# while True:
#     temperature = round(random.uniform(20, 30), 2)
#     humidity = round(random.uniform(30, 60), 2)
#     client.publish("sensor/temperature", str(temperature))
#     client.publish("sensor/humidity", str(humidity))
#     time.sleep(5)

# 模拟传感器数据，并将数据发布到主题
while True:
    temperature = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(30, 60), 2)
    result_temperature, _ = client.publish("sensor/temperature", str(temperature))
    result_humidity, _ = client.publish("sensor/humidity", str(humidity))
    if result_temperature == mqtt.MQTT_ERR_SUCCESS:
        print("Temperature data published successfully: ", temperature)
    else:
        print("Failed to publish temperature data.")
    if result_humidity == mqtt.MQTT_ERR_SUCCESS:
        print("Humidity data published successfully: ", humidity)
    else:
        print("Failed to publish humidity data.")
    time.sleep(5)

