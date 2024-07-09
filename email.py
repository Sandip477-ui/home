import qrcode
email_address = "sandipkerung02@gmail.com"
subject = "my frist email using python"
body = "hello this is my frist email using python"
mail = f"mail to {email_address}subject = {subject} & body = {body}"
img = qrcode.make(mail)
type(img)# qrcode.image,pill.pillimage
img.save("mail.png")
