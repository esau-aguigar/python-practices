import zipfile

zip = zipfile.ZipFile('prueba.zip')

while True:
    clave = input("Escribe el password")

    try:
        zip.extractall(pwd=clave.encode())
        break
    except Exception as error:
        print("Hubo un error", error)
