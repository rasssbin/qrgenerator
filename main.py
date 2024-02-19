import qrcode
from PIL import Image, ImageDraw, ImageFont
import pandas as pd


file_path = 'id card.xlsx'

try:
   
    excel_data = pd.read_excel(file_path)

    
    data_list = []
    current_district = None

    for _, data in excel_data.iterrows():
        if pd.notnull(data['Address']):
            current_district = data['Address']

        entry = {
            'name': data['Name'],
            'address': current_district,
            'sn':data['S.N']
        }
        data_list.append(entry)

    print(data_list)  

except FileNotFoundError:
    print("File not found. Please provide the correct file path.")
except Exception as e:
    print("An error occurred:", e)


def generate_qr_code(data):
    qr_data = f"नाम: {data['name']}\nठेगाना: {data['address']}\nकेन्द्रीय सदस्य</div>"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{data['sn']}_qr_code.png")  # Save QR code as an image




for data in data_list:
    generate_qr_code(data)

    template = Image.open("1.png")

    draw = ImageDraw.Draw(template)

   
    font = ImageFont.truetype("preeti.otf", 30)  

    
    x_position = 40
    y_position = 600

    
    draw.text((x_position, y_position), f"Gffd M {data['name']}", fill="black", font=font)
    draw.text((x_position, y_position + 30), f"7]ufgf M {data['address']}", fill="black", font=font)
    draw.text((x_position, y_position + 60), f"Hff/L ldlt M @)*)| )$ @% ", fill="black", font=font)

   
    user_qr_code = Image.open(f"{data['sn']}_qr_code.png").resize((250, 250))

    
    template.paste(user_qr_code, (40, 330))

    
    template.save(f"modified_template_{data['sn']}.png")
    
