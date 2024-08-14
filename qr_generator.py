import qrcode
from PIL import Image
import qrcode.image.svg

# Crear el QR code con mejor calidad y menos borde
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,  # Aumentar el tamaño del cuadro negro para mejor calidad
    border=2,  # Ajustar el borde a 2 o 3 según sea necesario
)

# Añadir el link al QR
qr.add_data('https://Rudimental.es')
qr.make(fit=True)

# Crear imagen del QR code en formato PNG
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Redimensionar el QR a 1023x1023 píxeles
qr_img = qr_img.resize((1023, 1023), Image.Resampling.LANCZOS)

# **1. Cargar la imagen del logo que se quiere poner en el centro**
# Sustituye la ruta del archivo por la ruta de la imagen de tu logo
logo_display = Image.open('Rudimental_Logo_QR.png')

# **2. Redimensionar la imagen del logo**
# Aquí puedes ajustar el tamaño de la imagen del logo si es necesario
logo_size = 300  # Aumentar el tamaño del logo para que sea más visible

logo_display = logo_display.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

# **3. Calcular la posición donde se pegará la imagen en el centro del QR**
qr_width, qr_height = qr_img.size
logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# **4. Pegar la imagen en el centro del QR**
qr_img.paste(logo_display, logo_position)

# **5. Guardar el QR code en un archivo PNG con medidas 1023x1023**
qr_img.save('png/RudimentalQR_with_logo.png')

# **6. Generar el QR code en formato SVG con mejor calidad y menos borde**
factory = qrcode.image.svg.SvgImage
qr_svg = qrcode.make('https://Rudimental.es', image_factory=factory, box_size=20, border=2)

# Guardar el QR en formato SVG
qr_svg.save('svg/RudimentalQR_with_logo.svg')

print("Código QR generado exitosamente y guardado como 'RudimentalQR_with_logo.png' y 'RudimentalQR_with_logo.svg'")
