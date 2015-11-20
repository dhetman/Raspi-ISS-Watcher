# This script calculates distance of the International Space Station from location defined by
# home_lat and home_long variables. Example used here will flash an LED when the ISS gets within
# specified mile radius.
# Please refer to layout.fzz (made using Fritzing software) or layout_bb.png for the installation of
# electronic components.
#
# Import all required libraries
import urllib, json, math, sched, time, RPi.GPIO as GPIO
url="https://api.wheretheiss.at/v1/satellites/25544" #URL where information is coming from
home_lat = 0.00 #your latitude goes in here
home_long = 0.00 #your longitude goes in here
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) #I used pin 18 from Raspberry Pi, feel free to update it

s = sched.scheduler(time.time, time.sleep)
def check_ISS(sc):

    def work(home_lat, home_long):
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        iss_lat = data['latitude']
        iss_long = data['longitude']
        distance = sph_dist(home_lat, home_long, iss_lat, iss_long)
        # if ISS is detected within 400 mile radius, it will light up the LED
        # if ISS gets outside the radius, LED will switch off
        # distance can be changed to whatever suits you
        if distance < 400:
            GPIO.output(18, True)
        else:
            GPIO.output(18, False)

    # radius calculation based on the sphere shape of our planet
    def sph_dist(lat1, long1, lat2, long2):
        degrees_to_radians = math.pi/180.0
        phi1 = (90.0 - lat1) * degrees_to_radians
        phi2 = (90.0 - lat2) * degrees_to_radians
        theta1 = long1 * degrees_to_radians
        theta2 = long2 * degrees_to_radians
        cos = (math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2) + math.cos(phi1) * math.cos(phi2))
        arc = math.acos(cos)
        return arc*3960

    work(home_lat,home_long)

    sc.enter(60, 1, check_ISS, (sc,))

try:
    s.enter(60, 1, check_ISS, (s,))
    s.run()

finally:
    # little clean up upon exit
    GPIO.cleanup()
    print("Cleaning up")
    print("Exit!")