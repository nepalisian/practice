
try:
    fd = open('text.txt', 'a')
    fd.write('hello world')

except Exception as e:
    print(e)

finally:
    fd.close()

