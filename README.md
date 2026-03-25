# Django Kişilik Testi Uygulaması 🐾

Bu proje, Django kullanılarak geliştirilmiş modern bir anket ve "Onedio tarzı" kişilik testi uygulamasıdır. Proje, özellikle hayvan hakları temasına dayalı anket örnekleriyle zenginleştirilmiş olup, kullanıcılara verdikleri cevaplara göre dinamik kategori sonuçları ve görseller sunar.

## Özellikler ✨

* **Kişilik Testi Altyapısı:** Kullanıcıların verdiği yanıtlara göre kategorize edilmiş 3 farklı hesaplanmış sonuç ekranı.
* **Modern ve Dinamik Arayüz:** Kullanıcı dostu, şık renk paletleri (CSS/HTML entegrasyonu) ve yönlendirme butonlarıyla donatılmış detaylı arayüz tasarımı.
* **Dinamik Sonuç Görselleri:** Kullanıcının vardığı test sonucuna (kategoriye) uygun resimler ve metinler.
* **Yönetim Paneli Yönetimi:** Django Admin arayüzü üzerinden hızlıca yeni soru, cevap ve farklı test sonuçları ekleme/düzenleme kolaylığı.

## Proje İçeriği 📁

* `polls/`: Ana anket, görüntüleme (views) ve test mantığının bulunduğu modül.
* `mysite/`: Ana Django konfigürasyon (settings & urls) klasörü.
* `Performans ve Optimizasyon.docx`: Projeye ek olarak yüklenmiş bir araştırma/çeviri ödevi belgesi.

## Kurulum ve Çalıştırma 🚀

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları sırasıyla izleyebilirsiniz:

1. **Projeyi Klonlayın:**
   ```bash
   git clone https://github.com/EmirhanYAZICI/Django-tutorials.git
   cd Django-tutorials
   ```

2. **Gereksinimleri Yükleyin** (Eğer eksikse Django kurun):
   ```bash
   pip install django
   ```

3. **Veritabanı Bağlantılarını (Migrations) Güncelleyin:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Yerel Geliştirme Sunucusunu Başlatın:**
   ```bash
   python manage.py runserver
   ```
   *Tarayıcınızda `http://127.0.0.1:8000/polls` veya `http://127.0.0.1:8000/` adresine giderek uygulamayı canlı olarak deneyimleyebilirsiniz.*

---
**Geliştirici:** [@EmirhanYAZICI](https://github.com/EmirhanYAZICI)
