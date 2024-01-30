import json
import os
import shutil

def load_config():
    try:
        with open("config.json", "r") as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        return {"applications": [], "data_location": "Varsayılan_Konum"}

def save_config(config):
    with open("config.json", "w") as file:
        json.dump(config, file, indent=4)

def list_applications(config):
    os.system("cls" if os.name == "nt" else "clear")
    print("Uygulamalar")
    print("-" * 30)
    for app in config["applications"]:
        print(f"{app['id']}-{app['name']} ({app['path']})")

def add_application(config, path):
    name = input("Uygulama ismini girin ('q' yazarak iptal edebilirsiniz): ")
    if name.lower() == "q":
        return
    app_id = len(config["applications"]) + 1
    config["applications"].append({"id": app_id, "name": name, "path": path})
    save_config(config)
    print(f"{name} uygulaması başarıyla eklendi!")

def remove_application(config, app_id):
    for app in config["applications"]:
        if app["id"] == app_id:
            config["applications"].remove(app)
            save_config(config)
            print(f"{app['name']} uygulaması başarıyla çıkartıldı!")
            return
    print("Belirtilen ID'ye sahip uygulama bulunamadı.")

def show_settings(config):
    os.system("cls" if os.name == "nt" else "clear")
    print("Ayarlar")
    print("-" * 30)
    print(f"1-Verilerin kayıt yeri: {config['data_location']}")
    print("2-Veri kayıt yeri değiştir")
    print("3-Verileri clonla")

def change_data_location(config):
    new_location = input("Yeni veri kayıt yeri girin ('q' yazarak iptal edebilirsiniz): ")
    if new_location.lower() == "q":
        return
    config["data_location"] = new_location
    save_config(config)
    print("Veri kayıt yeri başarıyla değiştirildi.")

def clone_data(config):
    destination = input("Verilerin kopyalanacağı konumu girin ('q' yazarak iptal edebilirsiniz): ")
    if destination.lower() == "q":
        return
    try:
        shutil.copytree(config["data_location"], destination)
        print("Veriler başarıyla kopyalandı.")
    except Exception as e:
        print(f"Hata: {e}")

def edit_application(config, app_id):
    for app in config["applications"]:
        if app["id"] == app_id:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"\n{app['name']} Uygulamasını Düzenle")
            print("-" * 30)
            print(f"1- İsim: {app['name']}")
            print(f"2- Yol: {app['path']}")
            choice = input("Düzenlemek istediğiniz öğeyi seçin ('q' çıkış): ")

            if choice == "1":
                new_name = input("Yeni ismi girin ('q' yazarak iptal edebilirsiniz): ")
                if new_name.lower() != "q":
                    app["name"] = new_name
                    save_config(config)
                    print("İsim başarıyla değiştirildi.")
            elif choice == "2":
                new_path = input("Yeni yolu girin ('q' yazarak iptal edebilirsiniz): ")
                if new_path.lower() != "q":
                    app["path"] = new_path
                    save_config(config)
                    print("Yol başarıyla değiştirildi.")
            elif choice.lower() == "q":
                return

def main():
    while True:
        config = load_config()
        os.system("cls" if os.name == "nt" else "clear")  # Ekranı temizle

        print("\nAna Menü")
        print("1-Uygulamalar")
        print("2-Uygulama Ekle/Çıkart")
        print("3-Ayarlar")
        choice = input("Seçiminizi yapın ('q' çıkış): ")

        if choice == "1":
            list_applications(config)
            app_id = input("Çalıştırmak istediğiniz uygulamanın ID'sini girin ('q' çıkış): ")
            if app_id.lower() == "q":
                continue
            elif not app_id.isdigit() or int(app_id) <= 0 or int(app_id) > len(config["applications"]):
                print("Geçersiz bir ID girdiniz. Tekrar deneyin.")
                input("Devam etmek için Enter'a basın.")
                continue
            else:
                run_application(config, int(app_id))

        elif choice == "2":
            os.system("cls" if os.name == "nt" else "clear")  # Ekranı temizle
            print("\nUygulama Ekle/Çıkart")
            print("1-Ekle")
            print("2-Çıkart")
            print("3-Düzenle")
            sub_choice = input("Seçiminizi yapın ('q' çıkış): ")

            if sub_choice == "1":
                path = input("Uygulamanın konumunu girin ('q' yazarak iptal edebilirsiniz): ")
                add_application(config, path)
                list_applications(config)  # Uygulamayı ekledikten sonra güncellenmiş listeyi göster
            elif sub_choice == "2":
                app_id = input("Çıkartmak istediğiniz uygulamanın ID'sini girin ('q' çıkış): ")
                if app_id.lower() == "q":
                    continue
                if not app_id.isdigit() or int(app_id) <= 0 or int(app_id) > len(config["applications"]):
                    print("Geçersiz bir ID girdiniz. Tekrar deneyin.")
                    input("Devam etmek için Enter'a basın.")
                    continue
                remove_application(config, int(app_id))
                list_applications(config)  # Uygulamayı çıkarttıktan sonra güncellenmiş listeyi göster
            elif sub_choice == "3":
                app_id = input("Düzenlemek istediğiniz uygulamanın ID'sini girin ('q' çıkış): ")
                if app_id.lower() == "q":
                    continue
                if not app_id.isdigit() or int(app_id) <= 0 or int(app_id) > len(config["applications"]):
                    print("Geçersiz bir ID girdiniz. Tekrar deneyin.")
                    input("Devam etmek için Enter'a basın.")
                    continue
                edit_application(config, int(app_id))
                list_applications(config)  # Uygulamayı düzenledikten sonra güncellenmiş listeyi göster

        elif choice == "3":
            show_settings(config)
            sub_choice = input("Seçiminizi yapın ('q' çıkış): ")

            if sub_choice == "2":
                change_data_location(config)
            elif sub_choice == "3":
                clone_data(config)

        elif choice.lower() == "q":
            save_config(config)  # Program kapatılmadan önce veriyi kaydet
            break

        else:
            print("Geçersiz seçenek. Tekrar deneyin.")
            input("Devam etmek için Enter'a basın.")  # Kullanıcının devam etmesini bekleyin.

if __name__ == "__main__":
    main()
