import random

# def random_utf8_string(n):
#     result=u""
#     for i in range(n):
#         a = u"\\u%04x" % random.randrange(0x10000)
#         result = result + a #.decode('unicode-escape')
#
#     return result
#
# print(str(random_utf8_string(1), 'utf-8'))


randomUtf8 = (u'\\u%04x' % random.randrange(0x10000)).encode('utf-8')
print(str(randomUtf8)[5:-1])

z = bytes([0xeb, 0xad, 0xbf]).decode()
print(z)


print((u'\ubb7f').encode('utf-8'))
