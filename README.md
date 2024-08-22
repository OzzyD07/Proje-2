# Proje-1: Python Menü Uygulaması

Bu proje, bir Python menü tabanlı rehber uygulamasıdır. Bu uygulamayı kullanarak rehbere yeni kişi ekleyebilir, silebir, düzünleyebilir, numaraya ve isime göre arama yapabilirsiniz.

## İçindekiler
- [Kullanılan Teknolojiler](#kullanılan-teknolojiler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Dosya Yapısı](#dosya-yapısı)
- [Fotoğraflar](#fotoğraflar)


## Kullanılan Teknolojiler

- **Python 3.x**: Projenin temel programlama dili.
- **Keyboard**: Menü içerisinde gezerken klavyeden gerekli inputu almak için kullanılır.
- **os**: Yapılan işlemlerle sonrasında daha temiz bir görüntü için terminali temizler.

## Kurulum

Projeyi bilgisayarınıza klonlamak için şu adımları izleyin:

1. Git'i kullanarak projeyi klonlayın:
    ```bash
    git clone https://github.com/OzzyD07/Proje-1
    ```
2. Python 3.x'in bilgisayarınızda kurulu olduğundan emin olun.

3. Gerekli paketlerin kurulumu için Bu kodu çalıştırın
    ```bash
    pip install -r requirements.txt    
    ```

## Kullanım

Projeyi çalıştırmak için terminal veya komut satırını kullanarak `main.py` dosyasını çalıştırın:

## Dosya Yapısı
```bash
├── main.py              # Ana menü ve proje yönetimi
├── components/          # Hesaplayıcı Klasörü
    ├── addPerson.py     # Kişi ekleme fonksiyonu
    ├── editPerson.py    # Kişi bilgilerini güncelleme fonksiyonu
    ├── getDirectory.py  # Rehberden data çeken ve bastıran modül
    └── search.py        # İsime ve numaraya göre arama modülü
└── rehber.txt           # Kaydedilen bilgileri tutan text dosyası
```

## Fotoğraflar