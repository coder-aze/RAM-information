import psutil

def gettype(byte,suffix='8'):
    factor=1024
    for x in ['','K','M','G','T','P']:
        if byte > factor:
            return f'{byte:.2f}{x}{suffix}'
        byte/=factor
        
result=psutil.virtual_memory()
print(f"Total: {gettype(result.total)}")
print(f"Available: {gettype(result.available)}")
print(f"Used: {gettype(result.used)}")
print(f"Percentage: {result.percent}%")


