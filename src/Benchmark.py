import time
import statistics
import os
from encryption import aes_en, aes_de
from ChaCha20 import ChaCha20_en, ChaCha20_de

def benchmark(func,data_size = None ,iterations=100):
    times = []
    for _ in range(iterations):
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    avg_time = statistics.mean(times)
    print(f"Average execution time over {iterations} iterations: {avg_time:.6f} seconds")
    return avg_time

if __name__ == "__main__":
    messages =[1024*1024*500,1024*1024*1024] #message sizes in bytes
    iterations = 10
    for msg in messages:
        print(f"==benchmark for message size: {msg} bytes==")
        message =os.urandom(msg)
        print("EncryptionBenchmark:")
        print("AES Benchmark:\n")
        print("AES Benchmark:Ecrypted")
        benchmark(lambda: aes_en(message), data_size =len(message), iterations=iterations)#lambda messages how fast the function runs
        key, nonce, ciphertext = aes_en(message)
        print("AES Benchmark:Decrypted\n")
        benchmark(lambda: aes_de(key,nonce,ciphertext),data_size =len(message),iterations=iterations)
        print("\nChaCha20 Benchmark:")
        print("ChaCha20 Benchmark:Ecrypted")
        benchmark(lambda: ChaCha20_en(message), data_size =len(message), iterations=iterations)
        key, nonce, ciphertext = ChaCha20_en(message)
        print("ChaCha20 Benchmark:Decrypted")
        benchmark(lambda:ChaCha20_de(key,nonce,ciphertext),data_size =len(message) , iterations=iterations)