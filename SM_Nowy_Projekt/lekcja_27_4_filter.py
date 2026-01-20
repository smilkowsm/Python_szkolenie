wyniki = [34, 88, 52, 21, 95, 49]
zaliczone = list(filter(lambda p: p > 50, wyniki))

print(zaliczone)

slowa = ["Python", "Java", "Php", "C", "Javascript", "Rust"]
tekst = list(filter(lambda txt: len(txt) > 4, slowa))

print(tekst)

