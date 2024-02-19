import pandas as pd
import qrcode


file_path = 'id card_updated_ashmit_2.xlsx'  
data = pd.read_excel(file_path)


for index, row in data.iterrows():
    

    
    qr_data = f"{row['Name']}\nठेगाना: {row['Address']}\nकेन्द्रीय सदस्य"

    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    
    img = qr.make_image(fill_color="black", back_color="white")

    
    file_name = f"{row['S.N']}_qr_code.png"
    img.save(file_name)
    
