from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo
import schedule
import time
import host_service


def publish():
    telemetry = host_service.host_info()

    client = TBDeviceMqttClient("192.168.1.14", "5P9m16nkUwW5ekN6K9HA")
    # Connect to ThingsBoard
    client.connect()
    # Sending telemetry without checking the delivery status
    client.send_telemetry(telemetry) 
    # Sending telemetry and checking the delivery status (QoS = 1 by default)
    result = client.send_telemetry(telemetry)
    # get is a blocking call that awaits delivery status  
    success = result.get() == TBPublishInfo.TB_ERR_SUCCESS
    # Disconnect from ThingsBoard
    client.disconnect()


# 单位：秒
interval = 5 
schedule.every(interval).seconds.do(publish)


while True:
    schedule.run_pending()
    time.sleep(1)