import tkinter as tk
from PIL import Image, ImageDraw


class SignatureApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Signature App")

        # Créer un canevas pour la signature
        self.canvas = tk.Canvas(master, bg="white", width=400, height=200)
        self.canvas.pack()

        # Créer un bouton pour effacer la signature
        self.clear_button = tk.Button(master, text="Effacer", command=self.clear_canvas)
        self.clear_button.pack()

        # Créer un bouton pour sauvegarder la signature
        self.save_button = tk.Button(master, text="Sauvegarder", command=self.save_signature)
        self.save_button.pack()

        # Initialiser la variable pour stocker la signature
        self.signature_image = Image.new("RGB", (400, 200), "white")
        self.draw = ImageDraw.Draw(self.signature_image)

        # Lier les événements de la souris au canevas
        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        # Dessiner sur le canevas lorsqu'un mouvement de la souris est détecté
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", width=2)
        self.draw.line([x1, y1, x2, y2], fill="black", width=2)

    def clear_canvas(self):
        # Effacer la signature du canevas
        self.canvas.delete("all")
        self.signature_image = Image.new("RGB", (400, 200), "white")
        self.draw = ImageDraw.Draw(self.signature_image)

    def save_signature(self):
        # Sauvegarder l'image de la signature
        self.signature_image.save("signature.png")
        print("Signature sauvegardée avec succès!")


if __name__ == "__main__":
    root = tk.Tk()
    app = SignatureApp(root)
    root.mainloop()
