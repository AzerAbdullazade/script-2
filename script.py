import requests #http(s) kimi sorgular ucundur
import urllib.parse #url ucundur

with open('xss_wordlist', 'r', encoding='utf-8') as f:
    for line in f:
        word = line.strip()
        encoded_word = urllib.parse.quote(word)  # URL ucun payloadi duzgun vezyete salmaq
        url = f'https://hucum_edilecek_seyfe/?param={encoded_word}'

        try:  #try bloku içində  xəta yarada biləcək kod yazılır
            response = requests.get(url)
            if word in response.text:
                print(f"Mümkün XSS tapıldı: {word}")
        except requests.exceptions.RequestException as e: #except bloku isə həmin xəta baş verərsə, onu tutub idarə edir, proqramın birdən-birə çökməsinin qarşısını alır.
            print(f"Xəta baş verdi: {e}")
