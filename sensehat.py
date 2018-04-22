from sense_hat import SenseHat

sense = SenseHat()

humidity = sense.get_humidity()
temp = sense.get_temperature()
pressure = sense.get_pressure()
sense.show_message("Hello world!")


print("Humidity"+str(humidity))
print("Temp"+str(temp))
print("Pressure"+str(pressure))


