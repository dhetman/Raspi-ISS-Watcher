# Raspberry Pi-based ISS Watcher

Let your Raspberry Pi notify you whenever International Space Station is in your area!

This Python script uses an API that delivers current coordinates of the ISS (the Earth equivalent of coordinates, as if ISS was on Earth) and calculates the distance between ISS's "Earth" position and your home (or other location that you can specify). The distance is calculated with Earth's sphere shape in mind.

I also included drawings of how I connected an LED to Raspberry Pi.

## Keep in mind

I wrapped this code inside a function that is executed once every minute, otherwise the script will continuously probe the API which might cause the script to crash. It might have been my own fault as I may have made a mistake writing code but after about a minute of continuous execution the script was stopping.

Wrapping it inside a function that executes it once every minute allows it to run happily without any problems.

## More ideas:

You can modify your script to:

* display ISS current position on LCD
* harvest the power of Tweepy and tweet whenever ISS is nearby
* flash the LED instead of switching it on or off
* use many LEDs to mark how far ISS is from you

Feel free to use this code for whatever purpose you see fit. Forks and contributions are welcome.