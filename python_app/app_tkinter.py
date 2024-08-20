import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from data.info import *
from config.config import Configuration

# Definir la dirección del dispositivo
VENDOR_ID = 0x1189
PRODUCT_ID = 0x8842

conf = Configuration(VENDOR_ID, PRODUCT_ID)

buton_colors = {
    "random": '#adadad',
    "red": '#ff0000',
    "yellow": '#fff300',
    "bright_green": '#aeff00',
    "dark_green": '#0cff00',
    "cyan": '#00ffdc',
    "blue": '#002eff',
    "violet": '#8700ff',
    "white": '#ffffff',
}

led_reports=[]
mose_reports=[]
media_reports=[]
basic_reports=[]

def update_layer_button_color():
    selected_color = color_combobox.get()
    color_hex = buton_colors.get(selected_color, '#ffffff')
    selected_layer = var_adicionales.get()
    
    for rb in radiobuttons_adicionales:
        if rb.cget('value') == selected_layer:
            rb.config(bg=color_hex)

def toggle_buttons(enable=True):
    state = tk.NORMAL if enable else tk.DISABLED
    for rb in radiobuttons_4x3:
        rb.config(state=state)
    for rb in radiobuttons_3x3:
        rb.config(state=state)

def clear_selection():
    var_4x3_3x3.set(None)
    var_adicionales.set(None)

def agregar():
    sel_keytypes_name = tecla_combobox.get()
    
    if sel_keytypes_name == "LED":
        sel_color_name = color_combobox.get()
        sel_color = colors.get(sel_color_name)
        sel_modes = modes.get(mode_combobox.get())
        sel_layer = var_adicionales.get()
        sel_keytypes = keytypes.get(tecla_combobox.get())

        if sel_color is None:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un color.")
        elif sel_modes is None:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un modo.")
        elif sel_layer == 'None':
            messagebox.showwarning("Advertencia", "Por favor, seleccione una capa.")
        else:
            
            reportid = 3
            layer = int(sel_layer)
            color = int(sel_color)
            mode = int(sel_modes)
            keytype = int(sel_keytypes)
            delay = 0
            inputAction = int(actions['ledconfig'])

            data_led = [0, (color << 4) | (mode & 0x0F)]
            report = conf.get_report(reportid, layer, keytype, delay, inputAction, data_led)
            led_reports.append(report)
            #print(led_reports)
            #conf.send_hid_report(report)
            #print("Elemento enviado...")

    elif sel_keytypes_name == "Basic":
        mods=0
        selected_key = basic_key_combobox.get()
        selected_modifiers = listbox_modifiers.curselection()

        if not selected_key or selected_key == "Seleccione una tecla básica":
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tecla básica.")
        elif not selected_modifiers:
            messagebox.showwarning("Advertencia", "Por favor, seleccione al menos un modificador.")
        else:

            seleccionado_4x3_3x3 = int(var_4x3_3x3.get()) if var_4x3_3x3.get() else None
            if seleccionado_4x3_3x3 and seleccionado_4x3_3x3 > 12:
                seleccionado_4x3_3x3 += 10
            sel_modes = modes.get(mode_combobox.get())
            sel_layer = var_adicionales.get()
            sel_keytypes = keytypes.get(sel_keytypes_name)

            reportid = 3 #puede ser 0,2,3
            layer = int(sel_layer)
            keytype = int(sel_keytypes)
            delay=0
            inputAction = int(seleccionado_4x3_3x3)

            #array de configuraciones especificas
            for data in selected_modifiers:
                #print(modifiers[str(listbox_modifiers.get(data))])
                mods+=modifiers[str(listbox_modifiers.get(data))]
                #print(mods)

            keycode = keycodes.get(selected_key)
            data_key=[]
            data_key.append(mods)
            data_key.append(keycode)

            report = conf.get_report(reportid, layer, keytype, delay, inputAction, data_key)
            basic_reports.append(report)
            #print(basic_reports)
            
            #modifier_bits = sum(modifiers[listbox_modifiers.get(i)] for i in selected_modifiers)
            #print(f"Tecla básica seleccionada: {selected_key} (Keycode: {keycode})")
            #print(f"Modificadores seleccionados: {modifier_bits}")

    elif sel_keytypes_name == "Multimedia":
        selected_action = multimedia_combobox.get()
        if selected_action not in media_key_values:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una acción multimedia válida.")
        else:
            seleccionado_4x3_3x3 = int(var_4x3_3x3.get()) if var_4x3_3x3.get() else None
            if seleccionado_4x3_3x3 and seleccionado_4x3_3x3 > 12:
                seleccionado_4x3_3x3 += 10

            action_values = media_key_values[selected_action][3]
            B1 = action_values["B1"]
            B2 = action_values["B2"]
            print(B1)
            print(B2)
            #print(f"Acción multimedia seleccionada: {selected_action} (B1: {B1}, B2: {B2})")

            sel_modes = modes.get(mode_combobox.get())
            sel_layer = var_adicionales.get()
            sel_keytypes = keytypes.get(sel_keytypes_name)

            reportid = 3 #puede ser 0,2,3
            layer = int(sel_layer)
            keytype = int(sel_keytypes)
            delay=0
            inputAction = int(seleccionado_4x3_3x3)

            #array de configuraciones especificas
            data_media = []
            data_media.append(int(B1)) #key.B1(reportId);
            data_media.append(int(B1)) #key.B2(reportId);
            data_media.append(0)

            report = conf.get_report(reportid,layer, keytype, delay, inputAction, data_media)
            media_reports.append(report)
            #print(media_reports)
            #mose_reports.append(report)

    elif sel_keytypes_name == "Mouse":
        selected_action = mouse_combobox.get()
        if selected_action not in mouse_configurations:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una acción de mouse válida.")
        else:
            
            seleccionado_4x3_3x3 = int(var_4x3_3x3.get()) if var_4x3_3x3.get() else None
            if seleccionado_4x3_3x3 and seleccionado_4x3_3x3 > 12:
                seleccionado_4x3_3x3 += 10
            #seleccionado_adicional = var_adicionales.get()

            action_values = mouse_configurations[selected_action]
            B1, B2, B3, B4, B5 = action_values
            #print(f"Acción de mouse seleccionada: {selected_action} (B1: {B1}, B2: {B2}, B3: {B3}, B4: {B4}, B5: {B5})")


            sel_modes = modes.get(mode_combobox.get())
            sel_layer = var_adicionales.get()
            sel_keytypes = keytypes.get(sel_keytypes_name)

            reportid = 3 #puede ser 0,2,3
            layer = int(sel_layer)
            keytype = int(sel_keytypes)
            delay=0
            inputAction = int(seleccionado_4x3_3x3)

            #array de configuraciones especificas
            data_mouse = []
            data_mouse.append(int(B1)) # Button ??
            data_mouse.append(int(B2))
            data_mouse.append(int(B3))
            data_mouse.append(int(B4)) # Scroll ??
            data_mouse.append(int(B5)) # modifiers ??

            #envio de configuracion
            report = conf.get_report(reportid,layer, keytype, delay, inputAction,data_mouse)
            mose_reports.append(report)
            #print(mose_reports)
            #conf.send_hid_report(report)
            #print("Elemento enviado...")
    else:
        seleccionado_4x3_3x3 = int(var_4x3_3x3.get()) if var_4x3_3x3.get() else None
        if seleccionado_4x3_3x3 and seleccionado_4x3_3x3 > 12:
            seleccionado_4x3_3x3 += 10
        seleccionado_adicional = var_adicionales.get()
        print(f"Seleccionado del grupo 4x3 y 3x3: {seleccionado_4x3_3x3}")
        print(f"Seleccionado del grupo adicional: {seleccionado_adicional}")


def enviar():
    for report in led_reports:
        conf.send_hid_report(report)

    for report in mose_reports:
        conf.send_hid_report(report)
    
    for report in media_reports:
        conf.send_hid_report(report)
    
    for report in basic_reports:
        conf.send_hid_report(report)
    print("Configuracuion cargada...")

def combobox_changed(event):
    seleccionado_tecla_combobox = tecla_combobox.get()

    if seleccionado_tecla_combobox == "LED":
        toggle_buttons(enable=False)
        clear_selection()
        color_combobox.grid(row=1, column=0, padx=10, pady=5, sticky='ew')
        mode_combobox.grid(row=2, column=0, padx=10, pady=5, sticky='ew')
        basic_key_combobox.grid_remove()
        listbox_modifiers.grid_remove()
        multimedia_combobox.grid_remove()
        mouse_combobox.grid_remove()
        
    elif seleccionado_tecla_combobox == "Basic":
        toggle_buttons(enable=True)
        clear_selection()
        basic_key_combobox.grid(row=1, column=0, padx=10, pady=5, sticky='ew')
        listbox_modifiers.grid(row=2, column=0, padx=10, pady=5, sticky='ew')
        color_combobox.grid_remove()
        mode_combobox.grid_remove()
        multimedia_combobox.grid_remove()
        mouse_combobox.grid_remove()

    elif seleccionado_tecla_combobox == "Multimedia":
        toggle_buttons(enable=True)
        clear_selection()
        multimedia_combobox.grid(row=1, column=0, padx=10, pady=5, sticky='ew')
        color_combobox.grid_remove()
        mode_combobox.grid_remove()
        basic_key_combobox.grid_remove()
        listbox_modifiers.grid_remove()
        mouse_combobox.grid_remove()
        
    elif seleccionado_tecla_combobox == "Mouse":
        toggle_buttons(enable=True)
        clear_selection()
        mouse_combobox.grid(row=1, column=0, padx=10, pady=5, sticky='ew')
        color_combobox.grid_remove()
        mode_combobox.grid_remove()
        basic_key_combobox.grid_remove()
        listbox_modifiers.grid_remove()

    else:
        toggle_buttons(enable=True)
        color_combobox.grid_remove()
        mode_combobox.grid_remove()
        basic_key_combobox.grid_remove()
        listbox_modifiers.grid_remove()
        multimedia_combobox.grid_remove()
        mouse_combobox.grid_remove()

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz con Radiobuttons Estilo Teclado")

# Establecer un diseño más limpio
root.geometry("600x600")

# Crear un Frame principal para organizar los widgets
frame_main = tk.Frame(root)
frame_main.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Crear un Frame para los Comboboxes y otros widgets
frame_widgets = tk.Frame(frame_main)
frame_widgets.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

tecla_combobox = ttk.Combobox(frame_widgets, values=list(keytypes.keys()))
tecla_combobox.set("Seleccione un tipo de tecla")
tecla_combobox.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
tecla_combobox.bind("<<ComboboxSelected>>", combobox_changed)

color_combobox = ttk.Combobox(frame_widgets, values=list(buton_colors.keys()))
color_combobox.set("Seleccione un color")
color_combobox.grid(row=1, column=0, padx=10, pady=5, sticky='ew')

mode_combobox = ttk.Combobox(frame_widgets, values=list(modes.keys()))
mode_combobox.set("Seleccione un modo")
mode_combobox.grid(row=2, column=0, padx=10, pady=5, sticky='ew')

basic_key_combobox = ttk.Combobox(frame_widgets, values=list(keycodes.keys()))
basic_key_combobox.set("Seleccione una tecla básica")
basic_key_combobox.grid(row=1, column=0, padx=10, pady=5, sticky='ew')

listbox_modifiers = tk.Listbox(frame_widgets, selectmode=tk.MULTIPLE)
for mod in modifiers.keys():
    listbox_modifiers.insert(tk.END, mod)
listbox_modifiers.grid(row=2, column=0, padx=10, pady=5, sticky='ew')

multimedia_combobox = ttk.Combobox(frame_widgets, values=list(media_key_values.keys()))
multimedia_combobox.set("Seleccione una acción multimedia")
multimedia_combobox.grid(row=1, column=0, padx=10, pady=5, sticky='ew')

mouse_combobox = ttk.Combobox(frame_widgets, values=list(mouse_configurations.keys()))
mouse_combobox.set("Seleccione una acción de mouse")
mouse_combobox.grid(row=1, column=0, padx=10, pady=5, sticky='ew')

# Crear un Frame para los radiobuttons
frame_radiobuttons = tk.Frame(frame_main)
frame_radiobuttons.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

frame_4x3 = tk.Frame(frame_radiobuttons)
frame_4x3.grid(row=0, column=0, padx=10, pady=10)

frame_3x3 = tk.Frame(frame_radiobuttons)
frame_3x3.grid(row=0, column=1, padx=10, pady=10)

color_combobox.grid_remove()
mode_combobox.grid_remove()
basic_key_combobox.grid_remove()
listbox_modifiers.grid_remove()
multimedia_combobox.grid_remove()
mouse_combobox.grid_remove()

var_4x3_3x3 = tk.StringVar()

keys_4x3 = [
    '1', '2', '3', '4',
    '5', '6', '7', '8',
    '9', '10', '11', '12'
]

radiobuttons_4x3 = []
for i in range(3):
    for j in range(4):
        rb = tk.Radiobutton(frame_4x3, text=keys_4x3[i*4+j], variable=var_4x3_3x3, value=f"{i*4+j+1}", indicatoron=False, width=5, height=2)
        rb.grid(row=i, column=j, padx=5, pady=5)
        radiobuttons_4x3.append(rb)

keys_3x3 = [
    'K1L', 'K1P', 'K1R',
    'K2L', 'K2P', 'K2R',
    'K3L', 'K3P', 'K3R'
]

radiobuttons_3x3 = []
for i in range(3):
    for j in range(3):
        rb = tk.Radiobutton(frame_3x3, text=keys_3x3[i*3+j], variable=var_4x3_3x3, value=f"{i*3+j+13}", indicatoron=False, width=5, height=2)
        rb.grid(row=i, column=j, padx=5, pady=5)
        radiobuttons_3x3.append(rb)

var_adicionales = tk.StringVar()

# Crear un Frame para los radiobuttons adicionales
frame_adicionales = tk.Frame(frame_main)
frame_adicionales.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky='ew')

# Crear 3 radiobuttons adicionales
radiobuttons_adicionales = []
for i in range(3):
    rb = tk.Radiobutton(frame_adicionales, text=f"Capa {i+1}", variable=var_adicionales, value=f"{i+1}", indicatoron=False, width=10, height=2)
    rb.grid(row=0, column=i, padx=5, pady=5, sticky='ew')

# Asegúrate de que el Frame permita expansión
frame_adicionales.grid_columnconfigure(0, weight=1)
frame_adicionales.grid_columnconfigure(1, weight=1)
frame_adicionales.grid_columnconfigure(2, weight=1)


# Crear el botón Enviar
boton_agregar = tk.Button(frame_main, text="Agregar", command=agregar)
boton_agregar.grid(row=3, column=0, padx=10, pady=10, sticky='ew')

# Crear el botón Enviar
boton_enviar = tk.Button(frame_main, text="Cargar a dispositivo", command=enviar)
boton_enviar.grid(row=4, column=0, padx=10, pady=10, sticky='ew')

# Ejecutar la aplicación
root.mainloop()
