import webbrowser
import shutil
import subprocess
import file_search  # Dosya arama modülünü içe aktar

# Komutlar ve açıklamaları
commands = {
    "yt": "YouTube'da arama yapar. (Örnek: yt kanal_ismi)",
    "gg": "Google'da arama yapar. (Örnek: gg arama_konusu)",
    "file": "Dosya araması yapar. (Örnek: file dosya_adi)",
    "dosya_tasi": "Dosya taşımak için kullanılır. (Örnek: dosya_tasi kaynak hedef)",
    "vsc": "Visual Studio Code'u açar.",
    "help": "Komutlar hakkında bilgi verir.",
    "cikis": "Asistanı kapatır."
}

def open_youtube_channel(query):
    search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(search_url)
    print(f"YouTube'da arandı: {query}")

def google_search(query):
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)
    print(f"Google'da arandı: {query}")

def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Dosya taşındı: {source} -> {destination}")
    except Exception as e:
        print(f"Hata oluştu: {e}")

def open_vscode():
    try:
        subprocess.run([r"C:\Users\Nreal\AppData\Local\Programs\Microsoft VS Code\Code.exe"])
        print("Visual Studio Code açıldı.")
    except FileNotFoundError:
        print("Visual Studio Code bulunamadı. Lütfen doğru yolu kontrol edin.")

def show_help():
    print("\nKomutlar:")
    for command, description in commands.items():
        print(f"{command}: {description}")

def main():
    while True:
        command_input = input("\nNe yapmak istiyorsun? ").strip().lower()
        command_parts = command_input.split(" ", 1)  # İlk kelime komut, geri kalan parametre

        command = command_parts[0]
        param = command_parts[1] if len(command_parts) > 1 else ""

        if command == "yt":
            if param:
                open_youtube_channel(param)
            else:
                print("Lütfen YouTube'da aramak için bir şey yaz.")

        elif command == "gg":
            if param:
                google_search(param)
            else:
                print("Lütfen Google'da aramak için bir şey yaz.")

        elif command == "file":
            if param:
                results = file_search.find_file_fast(param)
                if results:
                    print("\nDosya bulundu! Konumlar:")
                    for file_path in results:
                        print(file_path)
                else:
                    print("Dosya bulunamadı.")
            else:
                print("Lütfen aramak istediğiniz dosyanın adını yazın.")

        elif command == "dosya_tasi":
            print("Örnek kullanım: dosya_tasi kaynak hedef")
            src = input("Kaynak dosya yolunu gir: ").strip()
            dst = input("Hedef dosya yolunu gir: ").strip()
            move_file(src, dst)

        elif command == "vsc":
            open_vscode()

        elif command == "help":
            show_help()

        elif command == "cikis":
            print("Asistan kapatılıyor...")
            break

        else:
            print("Bilinmeyen komut! 'help' yazarak komutları görebilirsin.")

if __name__ == "__main__":
    main()
