# deprem-api-with-tkinter
### Dosyalar:
- **index.py** : Kandilli rasathanesinin sitesinden çekilen verileri ayrıştırarak Json haline getiren ve yayınlayan api.
- **form.py** : Deprem verilerini konuma, büyüklüğüne göre filtreleme ve listeleme imkanı sunan program.

### Çalıştırma:
- Gerekli kütüphaneler yüklenir.
- API (index.py) çalıştırılır. 
- Form uygulamsı çalıştırılır.
- Filtreleme ve listeleme işlemleri yapılır.

### Örnek API İstekleri:
- http://127.0.0.1:3000/
- http://127.0.0.1:3000/?size=3.1
- http://127.0.0.1:3000/?location=istanbul
- http://127.0.0.1:3000/?size=3.1&location=istanbul

### JSON Çıktısı:
```jsonc
"earthquakes": [
    {
      "id": 1,
      "date": "2022.09.05 16:45:54", // GMT+3
      "timestamp": 1662385554,
      "latitude": 37.1075,
      "longitude": 28.5117,
      "depth": 2.8, // km
      "size": {
        "md": 0.0,
        "ml": 3.6,
        "mw": 3.7
      },
      "location": "ARMUTCUK-ULA (MUGLA)",
      "attribute": "İlksel"
    }, {...}
]
```
### Form Ekranı:
![formEkrani](https://user-images.githubusercontent.com/33867383/215184467-beb6dd30-833f-4da1-8e28-5ebce4ef7d0c.PNG)


