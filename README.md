# MQTT 温湿度传感器数据收集系统

这个项目是一个基于 MQTT 协议的温湿度传感器数据收集系统。它包含了以下几个部分：

- 温湿度传感器模拟器：使用 Python 和 Paho-MQTT 库编写的一个模拟器，可以模拟温湿度传感器数据，并将数据发布到指定的 MQTT 主题。
- 订阅主题并存储数据的脚本：使用 Python 和 Paho-MQTT 库编写的一个脚本，可以订阅指定的 MQTT 主题，并将数据存储到 SQLite 数据库中。
- SQLite 数据库：用于存储传感器数据的轻量级关系型数据库。
- README 文件：项目的说明文档，包含了项目的功能、安装和使用方法。

## 功能

这个项目可以帮助你：

- 模拟温湿度传感器数据，并将数据发布到指定的 MQTT 主题。
- 订阅指定的 MQTT 主题，并将数据存储到 SQLite 数据库中。
- 在 GitHub 上管理项目代码，方便团队协作和版本控制。
- 快速部署和使用项目。

## 安装

在开始使用这个项目之前，你需要安装以下软件：

- MQTT 代理服务器（例如 Mosquitto）
- Python 3.x
- Paho-MQTT 库
- SQLite

你可以在各个软件的官方网站上找到对应的安装包，并按照安装向导进行安装。安装 Mosquitto 和 SQLite 的具体步骤可以参考步骤1和步骤3。

安装 Paho-MQTT 库可以通过以下命令来完成：

```pip install paho-mqtt```

## 使用

使用这个项目需要按照以下步骤进行：

1. 安装并配置 MQTT 代理服务器。
2. 使用 simulator.py 文件模拟温湿度传感器数据。
3. 使用 subscriber.py 文件订阅 MQTT 主题并将数据存储到 SQLite 数据库中。
4. 在 GitHub 上管理项目代码，方便团队协作和版本控制。

### 模拟器

运行以下命令来启动温湿度传感器模拟器：

```python simulator.py```


这个模拟器会模拟温湿度传感器数据，并将数据发布到 `sensor/temperature` 和 `sensor/humidity` 两个 MQTT 主题中。

### 订阅主题

运行以下命令来启动订阅主题的脚本：


```python subscriber.py```

这个脚本会订阅 `sensor/temperature` 和 `sensor/humidity` 两个 MQTT 主题，并将数据存储到 SQLite 数据库中。
