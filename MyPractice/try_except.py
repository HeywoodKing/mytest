# Filename:try_except.py

try:
    f = open("test.txt")
    f.close()
except(IOError):
    print("The file is not exist.")
except:
    print("Some error occurred.")

print("Done.")


