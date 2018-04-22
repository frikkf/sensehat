from sense_hat import SenseHat

sense = SenseHat()

humidity = sense.get_humidity()
temp = sense.get_temperature()
pressure = sense.get_pressure()




print("Humidity"+str(humidity))
print("Temp"+str(temp))
print("Pressure"+str(pressure))

sense.show_message(str(temp))
