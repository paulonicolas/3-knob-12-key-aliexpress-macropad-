
from data.info import *
from config.config import Configuration

# Definir la dirección del dispositivo
VENDOR_ID =  0x1189  # Reemplazar con el Vendor ID del dispositivo
PRODUCT_ID = 0x8842  # Reemplazar con el Product ID del dispositivo

conf =Configuration(VENDOR_ID,PRODUCT_ID)

#########################################################################
#CONFIGURACION LED
#########################################################################

# Configuración de ejemplo
#reportid = 3 #puede ser 0,2,3
#layer = layers["first"]
#color = colors["red"]
#mode = modes["solid"]
#keytype = keytypes['LED']
#delay = 0
#inputAction = actions['ledconfig']
##led13 = (color << 4) | (mode & 0x0F)
#
##array de configuraciones especificas
#data_led=[]
#data_led.append(0)
#data_led.append((color << 4) | (mode & 0x0F))
#
##envio de configuracion
#report = conf.get_report(reportid, layer, keytype, delay, inputAction, data_led)
#conf.send_hid_report(report)
#print('LED:')
#print(report)

#########################################################################
#CONFIGURACION KEY
#########################################################################
# Configuración 1
#reportid = 3 #puede ser 0,2,3
#layer = layers["third"]
#keytype = keytypes['Basic']
#inputAction = actions['Key5']
#delay=0
#
##array de configuraciones especificas
#data_key=[]
#data_key.append(modifiers["Ctrl"])
#data_key.append(keycodes["C"])
#
##envio de configuracion
#report = conf.get_report(reportid,layer, keytype, delay, inputAction, data_key)
#conf.send_hid_report(report)
#print('KEY CONF 1:')
#print(report)

#########################
# Configuración 2
#reportid = 3 #puede ser 0,2,3
#layer = layers["third"]
#keytype = keytypes['Basic']
#inputAction = actions['Key2']
#delay=0
#
##array de configuraciones especificas
#data_key=[]
#data_key.append(modifiers["Ctrl"])
#data_key.append(keycodes["V"])
#
##envio de configuracion
#report = conf.get_report(reportid,layer, keytype, delay, inputAction, data_key)
#conf.send_hid_report(report)
#print('KEY CONF 2:')
#print(report)

#########################
# Configuración 3
#reportid = 3 #puede ser 0,2,3
#layer = layers["third"]
#keytype = keytypes['Basic']
#inputAction = actions['Key3']
#delay=0
#
##array de configuraciones especificas
#data_key=[]
#data_key.append(modifiers["Ctrl"]+modifiers["Alt"])
#data_key.append(keycodes["Del"])
#
##envio de configuracion
#report = conf.get_report(reportid,layer, keytype, delay, inputAction, data_key)
#print('KEY CONF 3:')
#print(report)
#conf.send_hid_report(report)

#########################################################################
##CONFIGURACION MULTIMEDIA 
#########################################################################

reportid = 3 #puede ser 0,2,3
layer = layers["third"]
keytype = keytypes['Multimedia']
delay=0
inputAction = actions['Knob1Left']
media_key = media_key_values["VolDn"][reportid]
b1 = media_key["B1"]
b2 = media_key["B2"]

#array de configuraciones especificas
data_media = []
data_media.append(b1) #key.B1(reportId);
data_media.append(b2) #key.B2(reportId);
data_media.append(0)

#envio de configuracion
report = conf.get_report(reportid,layer, keytype, delay, inputAction,data_media)


print('MULTIMEDIA:')
print(report)
conf.send_hid_report(report)


##########################################################################
#CONFIGURACION MOUSE
#########################################################################

#reportid = 3 #puede ser 0,2,3
#layer = layers["third"]
#keytype = keytypes['Mouse']
#delay=0
#inputAction = actions['Key1']
#mouse_configuration = mouse_configurations["MouseMiddle"]
#
##array de configuraciones especificas
#data_mouse = []
#data_mouse.append(mouse_configuration[0]) # Button ??
#data_mouse.append(mouse_configuration[1])
#data_mouse.append(mouse_configuration[2])
#data_mouse.append(mouse_configuration[3]) # Scroll ??
#data_mouse.append(mouse_configuration[4]) # modifiers ??
#
##envio de configuracion
#report = conf.get_report(reportid,layer, keytype, delay, inputAction,data_mouse)
#conf.send_hid_report(report)
#print('MOUSE:')
#print(report)
#print("Configuración de LED enviada al dispositivo.")

