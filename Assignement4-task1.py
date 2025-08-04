try:
    file1 = open('sample.txt', 'r')
    line1 = file1.readline()
    line2 =file1.readline()
    print("Reading file content:\n",line1+ line2)
    file1.close()
except FileNotFoundError:
    print("Error: The File 'sample.txt' not found.")
finally:
    print("Closing file.")
