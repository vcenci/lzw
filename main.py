def lzw_compress(uncompressed):
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}
    w = ""
    result = []
        
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
            
    if w:
        result.append(dictionary[w])
        
    return result

def lzw_decompress(compressed):
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}
    w = chr(compressed[0])
    result = [w]

    for k in compressed[1:]:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError("Código não encontrado na tabela.")
        
        result.append(entry)
        
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        
        w = entry
        
    return ''.join(result)

with open("input.txt", "r", encoding="utf-8") as input_file:
    input_text = input_file.read()
print(f"Texto original: {input_text}")

compressed_text = lzw_compress(input_text)
print(f"Texto comprimido: {compressed_text}")
open("compressed.txt", "w").write(str(compressed_text))

with open("compressed.txt", "r") as compressed_file:
    compressed_text = eval(compressed_file.read())
decompressed_text = lzw_decompress(compressed_text)
print(f"Texto descomprimido: {decompressed_text}")
