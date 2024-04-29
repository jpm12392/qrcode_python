# views.py
from django.shortcuts import render
import qrcode


# Assuming your website URL is 'https://example.com'
website_url = 'https://www.linkedin.com/in/priyambada-singh/'

# Generate QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(website_url)
qr.make(fit=True)
qr_img = qr.make_image(fill='black', back_color='white')

# Save the QR code to a file (optional)
qr_img.save('media/qrcode/priyambada-singh.png')
print('>>>>>>>>>>>>>>>>>>>>>>.')
    
# Pass the QR code image to the template
# return render(request, 'qr_code.html', {'qr_code': qr_img})
