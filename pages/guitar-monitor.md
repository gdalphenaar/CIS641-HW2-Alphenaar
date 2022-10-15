title: Building a Raspberry Pi-Powered Guitar Environmental Monitor
short-title: SamaSquad
date: 2022-10-10
published:

The main idea for this project is to build a guitar temperature and humidity monitoring system - complete with a web interface - that's powered by a Raspberry Pi microcomputer and other off-the-shelf components. At this point in the game, this isn't really setting out to be "better" than any existing solutions out there, but is more envisioned as a system that might be easier and/or cheaper for the technically-inclined guitarist to build with components on-hand, and offers a far more open
system for tweaking and customization. (For more information, see the project page [here](https://gdalphenaar.github.io/GVSU-CIS641-SamaSquad))

But anyways, why might we want to make our own system when you can just go out and buy something ready to use out-of-the-box?

The main downside with humidity monitors like the one shown below is that they're designed for desktop use. This means that they basically sit in one place and monitor the temperature and humidity in their little area. Unfortunately, this area might not be anywhere near where your guitars are - in order to be usable, the unit needs to be in a place where the screen is readable. For the most part, this is probably fine - *however*, your guitar might be, for example, near a register vent or close to a window. This would make the readings from a monitor like this less accurate and, therefore, less useful.

![desktop humidity monitor]( {{ url_for('static', filename='images/humidity2.png') }})

On the other hand, it seems like a humidity monitor like the one below would solve a lot of these problems - it's small enough to be mounted to a guitar stand or tucked away inside a guitar case (I think?), and it can communicate wirelessly with a phone to provide updates no matter where the unit is positioned. However, these units can be expensive (this one is around $50 on [Sweetwater](https://www.sweetwater.com/store/detail/Humiditrak--daddario-planet-waves-humiditrak-bluetooth-hygrometer-with-humidity-temperature-sensor)), and require you to use a proprietary phone app. This isn't the worst thing in the world, but I really dislike superfluous phone apps, and the cost can quickly get out of hand, depending on how many you need (just two of these and you could basically get a [Blues Driver](https://www.sweetwater.com/store/detail/BD2--boss-bd-2-blues-driver-pedal), three and you could get a [Carbon Copy](https://www.sweetwater.com/store/detail/CarbonCopy--mxr-m169-carbon-copy-analog-delay-pedal)).

![wireless humidity monitor]( {{ url_for('static', filename='images/humidity1.png') }})

If we really wanted to save money, we could just not use environmental monitoring at all. That might work in a place with relatively consistent temperatures throughout the year, but anyone who lives somewhere with a dry winter season knows that maintaining appropriate humidity levels in the winter is... challenging, even with a humidifier. That's why the goal for this project is to build a (potentially) much cheaper system that isn't reliant on any specific company or app. While the [Raspberry Pi 3 B+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/) that I'm using for the "base unit" might be a bit expensive (especially now - October 2022), it's by far the most expensive component required, and only one is needed (and many people interested in a project like this likely have one or more laying around...). Adding additional sensors is as simple as buying a cheap environmental sensor and WiFi board (battery power is optional - the sensors could also be powered through a wall plug for static/fixed placement). This system will also have a web interface component, allowing users to view environmental conditions in (semi) real time. Here, users will also be able to set upper and lower "cutpoints" for both temperature and humidity - for humidity especially, just knowing the current level isn't quite enough - ideally we'd also like to get alerts when humidity reaches potentially dangerous levels. As of now, the plan is to make this web interface accessible only on a user's local network, though someone with a VPN could probably enable remote viewing capabilities.

Anyways, this project might not be for every guitarist, but I think it will fit my needs quite well (especially since I already had all of these parts on hand).

![some of my guitars]( {{ url_for('static', filename='images/guitars_on_stand.png') }})
