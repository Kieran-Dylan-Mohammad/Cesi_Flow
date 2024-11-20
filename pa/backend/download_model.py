import urllib.request
import os

def download_model():
    if not os.path.exists('models'):
        os.makedirs('models')
    
    # Nouveau modèle compatible
    url = "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_0.gguf"
    file_path = "models/mistral-7b-instruct-v0.1.Q4_0.gguf"
    
    print("Début du téléchargement...")
    
    def show_progress(count, block_size, total_size):
        percent = int(count * block_size * 100 / total_size)
        print(f"Téléchargement: {percent}%", end='\r')
    
    urllib.request.urlretrieve(url, file_path, show_progress)
    print("\nTéléchargement terminé!")

if __name__ == "__main__":
    download_model()