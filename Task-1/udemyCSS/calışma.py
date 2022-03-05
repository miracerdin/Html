sesli_harfler = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
girdi = input("word:").lower().strip()
var = ""
for i in sesli_harfler:
    if i in girdi:
        var = var + i
        print(var)  