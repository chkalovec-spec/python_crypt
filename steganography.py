from stegano import exifHeader

secret_message = input("Введите сообщение, которое хотите скрыть: ")
src_file_path = "./images/image.jpg"
secret_file_path = "./images/2-secret.jpg"

secret = exifHeader.hide(src_file_path, secret_file_path, secret_message=secret_message)

result = exifHeader.reveal(secret_file_path).decode()
print (result)
