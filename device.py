from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time


# Custom MQTT message callback
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")


privateKeyPath = "./certs/<UPDATE THIS>-private.pem.key"
certificatePath =  "./certs/<UPDATE THIS>-certificate.pem.crt"
rootCAPath = "./certs/AmazonRootCA1.pem"

topic = "myTopic"
port = 8883
host = "<UPDATE THIS>@wu-ats.iot.us-east-1.amazonaws.com"

# *clientID* - String that denotes the client identifier used to connect to AWS IoT.
# If empty string were provided, client id for this connection will be randomly generated
# on server side.
clientId = ""

myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(
    rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()

myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)
time.sleep(2)

# Publish to the same topic in a loop forever
loopCount = 0
while True:
    pass
