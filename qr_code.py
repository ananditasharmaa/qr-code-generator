from tkinter import *
from tkinter import messagebox
from io import BytesIO
import pyqrcode
from PIL import ImageTk, Image

root = Tk()

def generate():
    link_name = name_entry.get().strip()
    link = link_entry.get().strip()
    
    if not link_name or not link:
        error_label = Label(root, text="Please enter both link name and URL", fg="red")
        canvas.create_window(200, 300, window=error_label)
        return
    
    global qr, qr_image
    qr = pyqrcode.create(link)
    
    # Save QR code to memory
    buffer = BytesIO()
    qr.png(buffer, scale=8)
    buffer.seek(0)
    qr_image = Image.open(buffer)
    qr_image = qr_image.resize((300, 300), Image.LANCZOS)
    qr_image = ImageTk.PhotoImage(qr_image)
    
    image_label = Label(root, image=qr_image)
    image_label.image = qr_image  # Keep a reference
    canvas.create_window(200, 450, window=image_label)
    
    # Show save button after generating QR code
    save_button = Button(root, text="Save QR Code", command=save_code)
    canvas.create_window(200, 270, window=save_button)
        
def save_code():
    response = messagebox.askyesno("Save QR Code", "Do you want to save the QR code?")
    if response:
        link_name = name_entry.get().strip()
        file_name = link_name + ".png"
        try:
            qr.png(file_name, scale=8)
            messagebox.showinfo("Success", "QR code saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving QR code: {str(e)}")

canvas = Canvas(root, width=400, height=600)
canvas.pack()

app_label = Label(root, text="QR Code Generator", fg="blue", font=("Arial", 30))
canvas.create_window(200, 50, window=app_label)

name_label = Label(root, text="Link Name:")
link_label = Label(root, text="Link:")
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 180, window=link_entry)

generate_button = Button(root, text="Generate QR Code", command=generate)
canvas.create_window(200, 230, window=generate_button)

root.mainloop()
