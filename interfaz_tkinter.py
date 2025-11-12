import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv

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


# ----------------- INTERFAZ GRÁFICA (TKINTER) -----------------
class BillboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎵 Billboard Analyzer")
        self.root.geometry("950x600")
        self.root.configure(bg="#f5f5f5")
        self.canciones = []

        # ----------- ENCABEZADO -------------
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

        # ----------- TABLA DE RESULTADOS -------------
        columnas = ("posicion", "nombre_cancion", "nombre_artista", "anio")
        self.tabla = ttk.Treeview(root, columns=columnas, show="headings", height=20)
        for col in columnas:
            self.tabla.heading(col, text=col.replace("_", " ").title())
            self.tabla.column(col, width=180, anchor='center')
        self.tabla.pack(fill='both', expand=True, padx=10, pady=10)

    # ----------- FUNCIONES DE LA INTERFAZ -------------
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
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for c in resultados:
            self.tabla.insert("", "end", values=(c['posicion'], c['nombre_cancion'], c['nombre_artista'], c['anio']))


# ----------------- EJECUCIÓN -----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = BillboardApp(root)
    root.mainloop()
