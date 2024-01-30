import psutil
import ctypes
import time

def kontrol_et():
    # Şarj seviyesini kontrol et
    pil_seviyesi = psutil.sensors_battery().percent
    return pil_seviyesi

def durdur():
    # Windows üzerinde şarjı durdurmak için platforma özgü bir komutu kullanın
    ctypes.windll.powrprof.SetSuspendState(0, 1, 0)

def ana_program():
    print("Uygulama başlatıldı.")
    while True:
        pil_seviyesi = kontrol_et()
        print(f"Şarj seviyesi: %{pil_seviyesi}")

        if pil_seviyesi > 90:
            print("Şarj seviyesi %60 üzerinde, şarj almayı durduruluyor.")
            durdur()
            break

        time.sleep(2)  # Belirli aralıklarla kontrol et

    print("Uygulama sonlandırıldı.")

if __name__ == "__main__":
    ana_program()
