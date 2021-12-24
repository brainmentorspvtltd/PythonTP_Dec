import io

try:
    file = open('file.txt','w')
    print("File Opened and Created...")
    data = "Hello World"
    file.write(data)

    data_2 = file.read()
    print(data_2)
except FileNotFoundError:
    print("File does not exist...")
except io.UnsupportedOperation:
    print("File was opened in different mode...")

finally:
    file.close()
    print("File Closed...")