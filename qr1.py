import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox

class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Genie - Developed by Mahek")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")  # Soft gray background color

        self.logo_path = None  # Initially no logo for QR code
        self.qr_image = None

        # Display your logo in the top-left corner (static)
        self.logo_path = "D:/OneDrive/Desktop/LPU/Striver/portfolio/images/mhekLogo2.png"  # Your logo path
        self.logo_img = Image.open(self.logo_path)
        self.logo_img = self.logo_img.resize((50, 50))  # Resize logo
        self.logo_photo = ImageTk.PhotoImage(self.logo_img)
        self.logo_label = tk.Label(root, image=self.logo_photo, bg="#f0f0f0")
        self.logo_label.place(x=10, y=10)  # Place logo at the top-left corner

        # Title
        tk.Label(root, text="QR Genie", font=("Helvetica", 28, "bold"), bg="#f0f0f0", fg="#333333").pack(pady=10)

        # URL Input
        tk.Label(root, text="Enter URL or Text:", bg="#f0f0f0", font=("Helvetica", 12), fg="#333333").pack()
        self.data_entry = tk.Entry(root, width=50, font=("Helvetica", 12), fg="#333333")
        self.data_entry.pack(pady=5)

        # Color selection
        tk.Label(root, text="Select QR Color", bg="#f0f0f0", font=("Helvetica", 12), fg="#333333").pack()
        self.color_btn = tk.Button(root, text="Choose Color", command=self.choose_color, bg="#4A90E2", font=("Helvetica", 12), fg="white")
        self.color_btn.pack(pady=5)
        self.color = "black"

        # Canvas to display selected QR color
        self.qr_color_canvas = tk.Canvas(root, width=30, height=30, bg=self.color, bd=1, relief="solid")
        self.qr_color_canvas.pack(pady=5)

        tk.Label(root, text="Select Background Color", bg="#f0f0f0", font=("Helvetica", 12), fg="#333333").pack()
        self.bg_color_btn = tk.Button(root, text="Choose Background", command=self.choose_bg_color, bg="#4A90E2", font=("Helvetica", 12), fg="white")
        self.bg_color_btn.pack(pady=5)
        self.bg_color = "white"

        # Canvas to display selected background color
        self.bg_color_canvas = tk.Canvas(root, width=30, height=30, bg=self.bg_color, bd=1, relief="solid")
        self.bg_color_canvas.pack(pady=5)

        # Add logo button
        self.logo_button = tk.Button(root, text="Add Logo (Optional)", command=self.upload_logo, bg="#4A90E2", font=("Helvetica", 12), fg="white")
        self.logo_button.pack(pady=5)

        # Generate button
        self.generate_button = tk.Button(root, text="Generate QR Code", bg="#4A90E2", fg="white", font=("Helvetica", 14, "bold"), command=self.generate_qr)
        self.generate_button.pack(pady=10)

        # Image display
        self.img_label = tk.Label(root, bg="#f0f0f0")
        self.img_label.pack(pady=10)

        # Save button
        self.save_button = tk.Button(root, text="Save QR Code", bg="#4A90E2", font=("Helvetica", 12), fg="white", command=self.save_qr)
        self.save_button.pack(pady=10)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color
            self.qr_color_canvas.config(bg=self.color)  # Update the color canvas

    def choose_bg_color(self):
        bg_color = colorchooser.askcolor()[1]
        if bg_color:
            self.bg_color = bg_color
            self.bg_color_canvas.config(bg=self.bg_color)  # Update the background canvas

    def upload_logo(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if path:
            self.logo_path = path
            messagebox.showinfo("Logo Uploaded", "Logo added successfully!")

    def generate_qr(self):
        data = self.data_entry.get()
        if not data:
            messagebox.showwarning("Input Error", "Please enter URL or text.")
            return

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=self.color, back_color=self.bg_color).convert('RGB')

        # Add logo to QR code if uploaded
        if self.logo_path:
            try:
                logo = Image.open(self.logo_path)
                logo = logo.resize((70, 55))  # Resize the logo for QR code
                pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
                img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)
            except Exception as e:
                messagebox.showerror("Logo Error", f"Failed to add logo: {e}")

        self.qr_image = img
        self.display_qr(img)

    def display_qr(self, img):
        preview = img.resize((300, 300))
        photo = ImageTk.PhotoImage(preview)
        self.img_label.config(image=photo)
        self.img_label.image = photo

    def save_qr(self):
        if self.qr_image:
            path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
            if path:
                self.qr_image.save(path)
                messagebox.showinfo("Success", f"QR Code saved to {path}")
        else:
            messagebox.showwarning("No QR Code", "Please generate a QR code first.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()
