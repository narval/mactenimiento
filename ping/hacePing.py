import threading
import os

encendida = {}
salas = {"a" : {}, "e" : {}, "f" : {}, "et" : {}}

class hilo_ping (threading.Thread):
    def __init__(self, sala, numero):
        self.seguir = True
        self.sala = sala
        self.numero = numero
        self.tiempo = 0
        threading.Thread.__init__(self)
        
    def run(self):
        while self.seguir:
            #print "hola soy", self.sala, self.numero
            actual = {}
            ping = "ping -c 1 >>/dev/null " + self.sala + str(self.numero) + ".ac.labf.usb.ve -W 1"

            # Revisa Ping
            if not os.system(ping):
                actual["ping"] = "v"
                # comandos
                ssh = "(nmap " + self.sala + str(self.numero) + ".ac.labf.usb.ve -p 22 -PN | grep open) >> /dev/null"
                #Hay que acomodar sudoers para permitir este sudo
                distrib_l = "(sudo nmap " + self.sala + str(self.numero) + ".ac.labf.usb.ve -O | grep linux) >> /dev/null"
                distrib_w = "(sudo nmap " + self.sala + str(self.numero) + ".ac.labf.usb.ve -O | grep Windows) >> /dev/null"
                # Revisa sshd
                if not os.system(ssh):
                    actual["ssh"] = "v"
                else:
                    actual["ssh"] = "r"
                    
                #cambiar el orden (linux primero)
                """
                # Revisa la distribucion
                if not os.system(distrib_w):
                    actual.append("w")
                elif not os.system(distrib_l):
                    actual.append("l")
                else:
                    actual.append("?")
                """
                
            else:
                actual["ping"] = "r"
                actual["ssh"] = "r"
                #actual.append("?")
            print self.sala + str(self.numero)
            salas[self.sala][self.numero] = actual
            
            self.seguir = False
            
    def stop(self):
        self.seguir = False

    def stopped(self):
        return self._stop.isSet()
        
def verMaquinas():
    salida = {"a" : {}, "e" : {}, "f" : {}, "et" : {}}
    for sala in ["a", "e", "f", "et"]:
        for numero in range(1, 25):
            salida[sala][numero] = [1, 2]
    return salida

def verEstado():
    #lista_maquinas = range(1, 24)
    hilos = []
    #print lista_maquinas

    #for i in lista_maquinas:
    for sala in ["a", "e", "f", "et"]:
        for numero in range(1, 25):
            nuevo_hijo = hilo_ping(sala, numero)
            nuevo_hijo.start()
            hilos.append(nuevo_hijo)

    def detener():
        for h in hilos:
            h.stop()
            
    def esperar():
        for h in hilos:
            h.join()
           
            
            
    #time.sleep(3)
    esperar()
    #detener()
    return salas
    """
    entrada = None
    while entrada == None:
        entrada = raw_input("Press Enter to continue...")
    detener()
    """
def main():
    print verEstado()
    return verEstado()

if __name__ == '__main__':
    main()
