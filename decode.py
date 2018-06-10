import base64

txt = "NUIFEBEPBB0XCREKS0oTPAAXEVVAQUkHQV1cDgwTOwBRRUhMRgsXWlRVBggQaUlWQhcKBwEWWkIXS1dUaQwYBgAJBQcGQlQXR01TLwYeDBcaBAMBQEUXS1dUaRAYCR0PCgsACR0QTB8VLAcfEQFLQVRECUJRDQhTYkVRAx0DRk5eDhZHAgNVaRg="
key = "neverland.10kmt"

message = ""

m = list(base64.b64decode(txt).decode())

for i in range(len(m)):
    a = int((key[i % len(key)]).encode("utf-8").hex(),16)
    b = int(m[i].encode("utf-8").hex(),16)
    message += chr(a ^ b)
    
print(message)
