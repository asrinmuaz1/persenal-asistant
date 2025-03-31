import os
import threading

def search_file(filename, search_path, results):
    """Belirtilen dizinde dosyayı arar ve bulursa sonuç listesine ekler."""
    for root, _, files in os.walk(search_path):
        if filename in files:
            results.append(os.path.join(root, filename))

def find_file_fast(filename, base_paths=None):
    """Dosyayı birden fazla dizinde aynı anda arar ve hızlandırır."""
    if base_paths is None:
        base_paths = ["C:\\"]  # Aranacak ana dizinleri belirle
    
    results = []
    threads = []

    for path in base_paths:
        thread = threading.Thread(target=search_file, args=(filename, path, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results if results else None  # Sonuçları döndür

# Eğer doğrudan çalıştırılırsa kullanıcıdan giriş alınır
if __name__ == "__main__":
    filename = input("Aramak istediğin dosya adını gir: ").strip()
    found_files = find_file_fast(filename)
    
    if found_files:
        print("\nDosya bulundu! Konumlar:")
        for file in found_files:
            print(file)
    else:
        print("Dosya bulunamadı!")
