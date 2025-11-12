import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
import matplotlib.pyplot as plt
from collections import Counter

# ----------------- LÓGICA DE NEGOCIO -----------------
def cargar_canciones(ruta_archivo: str) -> list:
    lista_canciones = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                lista_canciones.append({
                    'posicion': fila.get('posicion', '').strip(),
                    'nombre_cancion': fila.get('nombre_cancion', '').strip(),
                    'nombre_artista': fila.get('nombre_artista', '').strip(),
                    'anio': fila.get('anio', '').strip(),
                    'letra': fila.get('letra', '').strip()
                })
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")
    return lista_canciones

def buscar_cancion(lista, nombre, anio):
    return [c for c in lista if c['nombre_cancion'].lower() == nombre.lower() and c['anio'] == str(anio)]

def canciones_anio(lista, anio):
    return [c for c in lista if c['anio'] == str(anio)]

def todas_canciones_artista(lista, artista):
    return [c for c in lista if c['nombre_artista'].lower() == artista.lower()]

# ----------------- INTERFAZ TKINTER -----------------
class BillboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎵 Billboard Analyzer con Gráficos")
        self.root.geometry("950x600")
        self.root.configure(bg="#e8f4fa")

        self.canciones = []

        # ----------- FRAME SUPERIOR -------------
        frame_top = ttk.Frame(root, padding=10)
        frame_top.pack(fill='x')

        ttk.Button(frame_top, text="📂 Cargar CSV", command=self.cargar_archivo).pack(side='left', padx=5)
        ttk.Label(frame_top, text="Canción:").pack(side='left', padx=5)
        self.entry_cancion = ttk.Entry(frame_top, width=20)
        self.entry_cancion.pack(side='left', padx=5)
        ttk.Label(frame_top, text="Año:").pack(side='left')
        self.entry_anio = ttk.Entry(frame_top, width=8)
        self.entry_anio.pack(side='left', padx=5)
        ttk.Button(frame_top, text="🔍 Buscar", command=self.buscar_cancion_gui).pack(side='left', padx=5)

        ttk.Label(frame_top, text="Artista:").pack(side='left', padx=5)
        self.entry_artista = ttk.Entry(frame_top, width=20)
        self.entry_artista.pack(side='left', padx=5)
        ttk.Button(frame_top, text="🎤 Canciones del artista", command=self.buscar_por_artista_gui).pack(side='left', padx=5)

        # ----------- FRAME DE BOTONES EXTRA -------------
        frame_botones = ttk.Frame(root, padding=10)
        frame_botones.pack(fill='x')
        ttk.Button(frame_botones, text="📊 Gráfico por año", command=self.grafico_canciones_por_anio).pack(side='left', padx=5)
        ttk.Button(frame_botones, text="⭐ Top 5 artistas", command=self.grafico_top_artistas).pack(side='left', padx=5)
        ttk.Button(frame_botones, text="🧹 Limpiar tabla", command=self.limpiar_tabla).pack(side='left', padx=5)

        # ----------- TABLA DE RESULTADOS -------------
        columnas = ("posicion", "nombre_cancion", "nombre_artista", "anio")
        self.tabla = ttk.Treeview(root, columns=columnas, show="headings", height=20)
        for col in columnas:
            self.tabla.heading(col, text=col.replace("_", " ").title())
            self.tabla.column(col, width=200, anchor='center')
        self.tabla.pack(fill='both', expand=True, padx=10, pady=10)

    def cargar_archivo(self):
        ruta = filedialog.askopenfilename(
            title="Selecciona archivo CSV",
            filetypes=[("Archivos CSV", "*.csv")]
        )
        if ruta:
            self.canciones = cargar_canciones(ruta)
            messagebox.showinfo("Archivo cargado", f"Se cargaron {len(self.canciones)} canciones.")
            self.mostrar_resultados(self.canciones)

    def buscar_cancion_gui(self):
        nombre = self.entry_cancion.get().strip()
        anio = self.entry_anio.get().strip()
        if not nombre or not anio:
            messagebox.showwarning("Faltan datos", "Debes ingresar el nombre y el año.")
            return
        resultados = buscar_cancion(self.canciones, nombre, anio)
        self.mostrar_resultados(resultados)

    def buscar_por_artista_gui(self):
        artista = self.entry_artista.get().strip()
        if not artista:
            messagebox.showwarning("Faltan datos", "Debes ingresar el nombre del artista.")
            return
        resultados = todas_canciones_artista(self.canciones, artista)
        self.mostrar_resultados(resultados)

    def mostrar_resultados(self, resultados):
        self.limpiar_tabla()
        for c in resultados:
            self.tabla.insert("", "end", values=(c['posicion'], c['nombre_cancion'], c['nombre_artista'], c['anio']))

    def limpiar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

    # ----------- GRÁFICOS -------------
    def grafico_canciones_por_anio(self):
        if not self.canciones:
            messagebox.showwarning("Sin datos", "Primero carga un archivo CSV.")
            return
        conteo = Counter([c['anio'] for c in self.canciones if c['anio']])
        anios = sorted(conteo.keys())
        valores = [conteo[a] for a in anios]

        plt.figure(figsize=(8, 5))
        plt.bar(anios, valores, color="#6aa9ff")
        plt.title("Cantidad de canciones por año")
        plt.xlabel("Año")
        plt.ylabel("Número de canciones")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def grafico_top_artistas(self):
        if not self.canciones:
            messagebox.showwarning("Sin datos", "Primero carga un archivo CSV.")
            return
        conteo = Counter([c['nombre_artista'] for c in self.canciones if c['nombre_artista']])
        top5 = conteo.most_common(5)
        artistas = [a for a, _ in top5]
        valores = [v for _, v in top5]

        plt.figure(figsize=(8, 5))
        plt.barh(artistas, valores, color="#f76c6c")
        plt.title("Top 5 artistas con más canciones")
        plt.xlabel("Número de canciones")
        plt.ylabel("Artista")
        plt.tight_layout()
        plt.show()

# ----------------- EJECUCIÓN -----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = BillboardApp(root)
    root.mainloop()
