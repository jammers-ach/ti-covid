# COVID19 status reporter for TI slient745

The TI slient745 is a data terminal from 1975. This project connects a raspberry pi zero to it, and then when the terminal is activated it prints the current status of COVID19 infections rates.

When the terminal is switched on, the raspi connections to `https://covid19api.com/` and fetches the latest statistics and sends them to the terminal.

![](photo.jpg?raw=true)


## Circuitry

The TI slient 745 has a port on the back for an external modem. This accepts UART at 300 baud and 700

The signals are inverted so an inverter is needed.

If the terminal is switched off, there is feedback from the TX to the RX line, which can create a loop if you're doing something with this input data. So the inputs are gated with the DTR signal from the modem.

![](circuit.png?raw=true)

Additionally the DTR pin was connected to GPIO4 on the Raspberry pi. This acts as the signal which activates the printing.

## Raspi setup

Raspberry pi Zero W with latest raspian.

By default the uart serial console at `/dev/ttyS0` doesn't work at 300 baud

So you need to add to `/boot/config.txt`
`
dtoverlay=pi3-miniuart-bt
`
To disable bluetooth on `ttyAMA0` and use `ttyAMA0` with the GPIO pins at the correct clock frequency.

Finally test with:
`
picocom  -f n -d 7 -p 1 -b 300 -y e /dev/ttyAMA0
`

## Software

Requires `python3`

on your raspberry under user `pi`

```
$ git clone XX
$ python3 ti-covid/main.py
```

