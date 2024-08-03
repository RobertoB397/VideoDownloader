from pytube import YouTube

def Download(link):
    save_folder = "C:/Users/rober/OneDrive/Escritorio/descargas youtube"
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()

    try:
        yt.download(output_path= save_folder)
    except:
        print("Error")

link = input("Ingresa el link de youtube: ")

Download(link)
