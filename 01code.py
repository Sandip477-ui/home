import qrcode
# img = qrcode.make('wifi')
img =qrcode.make('sandip')
# type(img)
# img.save('sandip.png')
wifi_type = "WPA"
wifi_ssid = "PlSnet_1D2520"
wifi_password = "mj586712"
wifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};p:{wifi_password};;"
img = qrcode.make(wifi)
type(img)
img.save("wifi.png")