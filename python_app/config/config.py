import hid
import os

class Configuration():

    def __init__(self,VENDOR_ID,PRODUCT_ID):
        self.VENDOR_ID=VENDOR_ID
        self.PRODUCT_ID=PRODUCT_ID

    # funcion de configuracion de parametros del reporte a enviar
    # el reporte no es mas que un array de 64 bit que contiene la configuracion para el dispositivo
    # el datalist contiene una lista que se acopla a la lista general 
    # y contiene la configuracion particular de una tecla
    def get_report(self,reportid,layer, keytype, delay, inputAction, data_list):
        data = [0] * 64  #tamaño de arreglo
        data[0] = reportid  # reportid
        data[1] = 254  # Segundo byte fijo
        data[2] = inputAction   # action - tecla que se quiere programar
        data[3] = layer  # Número de capa
        data[4] = keytype  # keytype 
        data[5] = delay & 0xFF  # delay
        data[6] = (delay >> 8) & 0xFF  # delay
        data[7] = 0 # default
        data[8] = 0 # default
        data[9] = 0 # default
        data[10] = len(data_list)
        for idx,key in enumerate(data_list):
            data[11+idx]=key
        return data

    # Función para enviar datos HID
    # busca el dispositivo
    # le da permisos al dispositivo
    # abre el dispositivo
    # envia los valores 
    def send_hid_report(self,report):
        try:
            devices = hid.enumerate()
            for dev in devices:
                if dev['vendor_id'] == self.VENDOR_ID and dev['product_id'] == self.PRODUCT_ID:
    
                    #print(f"Vendor ID: {dev['vendor_id']:04x}")
                    #print(f"Product ID: {dev['product_id']:04x}")
                    #print(f"Path: {dev['path']}")
                    #print(f"Manufacturer: {dev['manufacturer_string']}")
                    #print(f"Product: {dev['product_string']}")
                    #print(f"Serial Number: {dev['serial_number']}")
                    #print('')
                    device_path = dev['path']
                    print(device_path)
                    break

            if device_path is None:
                raise IOError("Dispositivo no encontrado")

            # Verifica permisos del dispositivo
            print(f"Verificando permisos del dispositivo en {device_path.decode('utf-8') if isinstance(device_path, bytes) else device_path}")
            os.system(f"sudo chmod 666 {device_path.decode('utf-8') if isinstance(device_path, bytes) else device_path}")
            # Abre el dispositivo usando su ruta
            device = hid.device()
            device.open_path(device_path)
            device.set_nonblocking(1)
            #escribo el reporte (array de 64 bytes)
            #print(report)
            device.write(report)
            device.close()

        except IOError as e:
            print(f"No se pudo abrir el dispositivo: {e}")
        except TypeError as e:
            print(f"Error de tipo: {e}")
        except device.WriteError as e:
            print(f"Error de escritura: {e}")


