import hashlib

# text = "Hello World!"
# hash_object = hashlib.sha256(text.encode())
# hash_digest = hash_object.hexdigest()
# print("SHA Hash of ", text, " is ", hash_digest)
def hash_file(file_path):
    h = hashlib.new("sha256")#hash object which is sha256 alg
    with open(file_path,"rb") as file:#read file in binary
        while True:
            chunk =file.read(1024)#read chunks 1024 bytes
            if chunk ==b"":#chunk empty
                break
            h.update(chunk)#updates hash object for each chunk
    return h.hexdigest()

def verify_integrity(file1, file2):
    hash1 =hash_file(file1)
    hash2=hash_file(file2)
    print("check integrity",file1, " and ",file2)
    if hash1 == hash2:
        return("Checking file is intact. no mods have been made")
    return "file modified"



if __name__ == "__main__":
    print("SHA HAsh of FIle is:", hash_file(r"venv\modules\sample_files\sample.txt"))