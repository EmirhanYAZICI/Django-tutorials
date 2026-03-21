import random
from django.core.management.base import BaseCommand
from polls.models import Category, Question, Choice, PersonalityResult
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seeds personality test categories, questions, and results'

    def handle(self, *args, **kwargs):
        # Clear existing data to avoid duplicates if re-run
        # Category.objects.all().delete() # Optional: be careful with this

        # 1. RPG Category
        rpg_cat, _ = Category.objects.get_or_create(
            name="Hangi RPG Sınıfısın?",
            description="Fantezi dünyasında hangi rolü üstlenirdin?"
        )
        
        rpg_traits = {
            "Savaşçı": ("Cesur, güçlü ve ön saflarda çarpışan birisin.", "https://images.unsplash.com/photo-1599708145670-af2c48153bc0?w=500"),
            "Büyücü": ("Bilgelik, gizem ve zeka senin en büyük silahın.", "https://images.unsplash.com/photo-1514539079130-25950c84af65?w=500"),
            "Okçu": ("Keskin gözlü, sabırlı ve her zaman hedefine odaklısın.", "https://images.unsplash.com/photo-1512412023212-f2ec104c6001?w=500"),
            "Hırsız": ("Hızlı, kurnaz ve gölgelerin efendisisin.", "https://images.unsplash.com/photo-1605142859862-978be7eba909?w=500"),
        }

        for trait, (desc, img) in rpg_traits.items():
            PersonalityResult.objects.get_or_create(category=rpg_cat, trait=trait, defaults={"title": trait, "description": desc, "image_url": img})

        rpg_questions = [
            ("Bir canavarla karşılaştığında ilk ne yaparsın?", {"Savaşçı": "Hemen saldırırım", "Büyücü": "Büyü hazırlarım", "Okçu": "Mesafemi korurum", "Hırsız": "Gizlenirim"}),
            ("En sevdiğin silah?", {"Savaşçı": "Büyük bir kılıç", "Büyücü": "Asa", "Okçu": "Yay ve ok", "Hırsız": "Hançer"}),
            ("Bir zindanda kapalı bir kapı buldun?", {"Savaşçı": "Omuz atıp kırarım", "Büyücü": "Büyüyle açarım", "Okçu": "Uzaktan izlerim", "Hırsız": "Kilidi açarım"}),
            ("Ekip arkadaşların tehlikede?", {"Savaşçı": "Öne atılırım", "Büyücü": "Kalkan büyüsü yaparım", "Okçu": "Uzaktan destek veririm", "Hırsız": "En zayıf halkayı bulurum"}),
            ("Hangi yeteneğin daha güçlü olsun istersin?", {"Savaşçı": "Dayanıklılık", "Büyücü": "Zeka", "Okçu": "Hassasiyet", "Hırsız": "Çeviklik"}),
            ("Bir ejderha ile pazarlık yapar mısın?", {"Savaşçı": "Asla, savaşırım", "Büyücü": "Bilgi için denerim", "Okçu": "Gözünü hedeflerim", "Hırsız": "Hazinesini çalarım"}),
            ("Savaş alanında nerede durursun?", {"Savaşçı": "En önde", "Büyücü": "En arkada", "Okçu": "Yüksek bir yerde", "Hırsız": "Yanlarda, sinsice"}),
            ("Akşam yemeğinde ne konuşursun?", {"Savaşçı": "Kahramanlık hikayeleri", "Büyücü": "Kadim sırlar", "Okçu": "Doğa ve avlar", "Hırsız": "Sır tutarım"}),
            ("Hangi madalyayı istersin?", {"Savaşçı": "Onur", "Büyücü": "Bilgelik", "Okçu": "Ustalık", "Hırsız": "Görünmezlik"}),
            ("Zırh seçimin?", {"Savaşçı": "Ağır plaka", "Büyücü": "İşlemeli cübbe", "Okçu": "Hafif deri", "Hırsız": "Koyu renk pelerin"}),
            ("Hazineleri ne yaparsın?", {"Savaşçı": "Yeni silah alırım", "Büyücü": "Kitaplara harcarım", "Okçu": "Yolculukta kullanırım", "Hırsız": "Sayarken keyif alırım"}),
            ("Köyün saldırıya uğruyor?", {"Savaşçı": "Hemen savunmaya koşarım", "Büyücü": "Savunma bariyeri kurarım", "Okçu": "Kuleye çıkarım", "Hırsız": "Önce değerli eşyaları kurtarırım"}),
            ("Karanlık bir ormandasın?", {"Savaşçı": "Kılıcımı çekerim", "Büyücü": "Işık büyüsü yaparım", "Okçu": "Ağaçlara çıkarım", "Hırsız": "Gürültü yapmadan ilerlerim"}),
            ("Bir düşman teslim oldu?", {"Savaşçı": "Affederim ama silahsızlandırırım", "Büyücü": "Zihnini kontrol ederim", "Okçu": "Takipte kalırım", "Hırsız": "Cüzdanına bakarım"}),
            ("Hayalin ne?", {"Savaşçı": "Efsanevi bir kral olmak", "Büyücü": "Gerçeğin sırrını çözmek", "Okçu": "Özgürce dolaşmak", "Hırsız": "Dünyanın en büyük hırsızı olmak"}),
        ]

        for q_text, choices in rpg_questions:
            q, _ = Question.objects.get_or_create(question_text=q_text, category=rpg_cat)
            for trait, c_text in choices.items():
                Choice.objects.get_or_create(question=q, choice_text=c_text, trait=trait)

        # 2. Animal Category
        animal_cat, _ = Category.objects.get_or_create(
            name="Ruh Hayvanın Hangisi?",
            description="Kişiliğine en yakın hayvanı bul."
        )
        
        animal_traits = {
            "Aslan": ("Lider, görkemli ve korumacı bir yapıya sahipsin.", "https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=500"),
            "Baykuş": ("Gözlemci, sessiz ve bilgi dolu bir dünyan var.", "https://images.unsplash.com/photo-1544391496-1ca7c9745b9d?w=500"),
            "Kurt": ("Sadık, takım çalışmasına inanan ve özgür ruhlusun.", "https://images.unsplash.com/photo-1557008075-7f2c5efa4cfd?w=500"),
            "Yunus": ("Sosyal, zeki ve neşeli bir kişiliğin var.", "https://images.unsplash.com/photo-1570481662006-a3a1374699e8?w=500"),
        }

        for trait, (desc, img) in animal_traits.items():
            PersonalityResult.objects.get_or_create(category=animal_cat, trait=trait, defaults={"title": trait, "description": desc, "image_url": img})

        animal_questions = [
            ("Hafta sonu planın hangisi?", {"Aslan": "Merkezde olduğum bir parti", "Baykuş": "Kitap okuyup araştırma yapmak", "Kurt": "Yakın arkadaşlarımla doğa yürüyüşü", "Yunus": "Arkadaşlarımla denize gitmek"}),
            ("Bir grupta hangi rolde olursun?", {"Aslan": "Lider", "Baykuş": "Gözlemci/Danışman", "Kurt": "Güvenilir üye", "Yunus": "Eğlence kaynağı"}),
            ("En sevdiğin ortam?", {"Aslan": "Güneşli ve açık alanlar", "Baykuş": "Kütüphane gibi sessiz yerler", "Kurt": "Vahşi ve doğal ormanlar", "Yunus": "Deniz ve su kenarları"}),
            ("Tehlike anında tepkin?", {"Aslan": "Kükrer, yüzleşirim", "Baykuş": "Strateji geliştiririm", "Kurt": "Sürüyü korurum", "Yunus": "Hızlıca uzaklaşırım"}),
            ("Hangi mevsimi seversin?", {"Aslan": "Yaz", "Baykuş": "Sonbahar", "Kurt": "Kış", "Yunus": "İlkbahar"}),
            ("Seni en iyi ne tanımlar?", {"Aslan": "Güç", "Baykuş": "Bilgelik", "Kurt": "Sadakat", "Yunus": "İletişim"}),
            ("Göz önünde olmayı sever misin?", {"Aslan": "Bayılırım", "Baykuş": "Asla", "Kurt": "Gerekirse evet", "Yunus": "İnsanlar varsa güzel"}),
            ("Zor bir karar verirken?", {"Aslan": "Kendi iç sesime güvenirim", "Baykuş": "Detaylıca incelerim", "Kurt": "Güvendiklerime danışırım", "Yunus": "Akışına bırakırım"}),
            ("Hangi yetenek?", {"Aslan": "Yönetme yeteneği", "Baykuş": "Görünmeyeni görme", "Kurt": "İz sürme", "Yunus": "Problem çözme"}),
            ("Yalnızlık senin için ne ifade eder?", {"Aslan": "Zayıflık", "Baykuş": "Gereklilik", "Kurt": "Düşünme vakti", "Yunus": "Sıkıcılık"}),
            ("Hangi müzik tarzı?", {"Aslan": "Görkemli ve epik", "Baykuş": "Enstrümantal/Klasik", "Kurt": "Bağımsız/Alternatif", "Yunus": "Pop/Hareketli"}),
            ("Bir ödül kazansan?", {"Aslan": "Kürsüye çıkıp konuşma yaparım", "Baykuş": "Sessizce kabul ederim", "Kurt": "Ekibime teşekkür ederim", "Yunus": "Kutlama başlatırım"}),
            ("Hayat motton?", {"Aslan": "En güçlü benim", "Baykuş": "Bilgi güçtür", "Kurt": "Birlikten kuvvet doğar", "Yunus": "Hayat kısa, eğlenmene bak"}),
            ("Uyku düzenin?", {"Aslan": "Günde 8-10 saat", "Baykuş": "Gece kuşuyum", "Kurt": "Hafif uyurum", "Yunus": "Yeteri kadar"}),
            ("Yeni insanlarla tanışmak?", {"Aslan": "Kendimi sevdirmeye çalışırım", "Baykuş": "Uzaktan izlerim", "Kurt": "Önce bir ölçüp tartarım", "Yunus": "Hemen kaynaşırım"}),
        ]

        for q_text, choices in animal_questions:
            q, _ = Question.objects.get_or_create(question_text=q_text, category=animal_cat)
            for trait, c_text in choices.items():
                Choice.objects.get_or_create(question=q, choice_text=c_text, trait=trait)

        # 3. Travel Category
        travel_cat, _ = Category.objects.get_or_create(
            name="Tatil Tarzın Hangisi?",
            description="Nasıl bir gezgin olduğunu keşfet."
        )
        
        travel_traits = {
            "Maceracı": ("Adrenalin tutkunu, bilinmeyeni keşfeden bir gezginsin.", "https://images.unsplash.com/photo-1502784444187-359ac186c5bb?w=500"),
            "Lüks": ("Konfor, şıklık ve en iyi hizmet senin için vazgeçilmez.", "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=500"),
            "Sırt Çantalı": ("Minimum bütçe, maksimum deneyim diyenlerdensin.", "https://images.unsplash.com/photo-1503220317375-aaad61436b1b?w=500"),
            "Kültür Turisti": ("Tarih, sanat ve yerel yaşam senin ilgi odağın.", "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500"),
        }

        for trait, (desc, img) in travel_traits.items():
            PersonalityResult.objects.get_or_create(category=travel_cat, trait=trait, defaults={"title": trait, "description": desc, "image_url": img})

        travel_questions = [
            ("Ulaşım tercihin?", {"Maceracı": "Motosiklet", "Lüks": "Business Class Uçuş", "Sırt Çantalı": "Otostop/Tren", "Kültür Turisti": "Yürüyerek gezmek"}),
            ("Konaklama yerin?", {"Maceracı": "Çadır", "Lüks": "5 Yıldızlı Otel", "Sırt Çantalı": "Hostel", "Kültür Turisti": "Butik eski konaklar"}),
            ("Valizinde ne eksik olmaz?", {"Maceracı": "İlkyardım kiti", "Lüks": "Şık kıyafetler", "Sırt Çantalı": "Çok amaçlı çakı", "Kültür Turisti": "Müze kartı"}),
            ("Bir şehre vardığında ilk nereye gidersin?", {"Maceracı": "En yüksek tepeye", "Lüks": "En lüks restorana", "Sırt Çantalı": "Pazara/Sokağa", "Kültür Turisti": "En eski kilise/camiye"}),
            ("Yemek tercihin?", {"Maceracı": "Doğada ne bulursam", "Lüks": "Michelin yıldızlı", "Sırt Çantalı": "Sokak lezzetleri", "Kültür Turisti": "Geleneksel ev yemekleri"}),
            ("Fotoğraf tarzın?", {"Maceracı": "Aksiyon anları", "Lüks": "Estetik ve kusursuz", "Sırt Çantalı": "Anlık ve doğal", "Kültür Turisti": "Mimari ve sanat"}),
            ("Bütçen ne kadar?", {"Maceracı": "Ekipmana bağlı", "Lüks": "Sınırsız", "Sırt Çantalı": "Kısıtlı ama verimli", "Kültür Turisti": "Orta"}),
            ("Hangi aktivite seni heyecanlandırır?", {"Maceracı": "Paraşütle atlamak", "Lüks": "Spa ve masaj", "Sırt Çantalı": "Yerel düğüne katılmak", "Kültür Turisti": "Rehberli tur"}),
            ("Gezgin arkadaşın kim olsun istersin?", {"Maceracı": "Kafa dengi bir risk sever", "Lüks": "Hizmet edecek biri", "Sırt Çantalı": "Her şeye 'tamam' diyen biri", "Kültür Turisti": "Tarih bilen biri"}),
            ("Hangi dili öğrenmek istersin?", {"Maceracı": "Vücut dili", "Lüks": "Fransızca", "Sırt Çantalı": "İspanyolca", "Kültür Turisti": "Latince/Eski diller"}),
            ("İnternet bağlantısı?", {"Maceracı": "Olmasa da olur", "Lüks": "Her an her yerde hızı çok önemli", "Sırt Çantalı": "Sadece Wi-Fi bulursam", "Kültür Turisti": "Bilgi aramak için lazım"}),
            ("Hediyelik eşya olarak ne alırsın?", {"Maceracı": "Bir taş veya dal", "Lüks": "Marka ürünler", "Sırt Çantalı": "Magnet", "Kültür Turisti": "Replika antikalar"}),
            ("Yağmurlu bir havada?", {"Maceracı": "Çamura dalarım", "Lüks": "Otel barında kokteyl içerim", "Sırt Çantalı": "Yağmurluğumu çeker devam ederim", "Kültür Turisti": "Müzeye sığınırım"}),
            ("Gideceğin rotayı kim belirler?", {"Maceracı": "Rüzgar", "Lüks": "En popüler yerler", "Sırt Çantalı": "En ucuz bilet nereyeyse", "Kültür Turisti": "Tarihi kitaplar"}),
            ("Tatilden beklentin nedir?", {"Maceracı": "Sınırlarımı zorlamak", "Lüks": "Şımartılmak", "Sırt Çantalı": "Yeni insanlar tanımak", "Kültür Turisti": "Öğrenmek"}),
        ]

        for q_text, choices in travel_questions:
            q, _ = Question.objects.get_or_create(question_text=q_text, category=travel_cat)
            for trait, c_text in choices.items():
                Choice.objects.get_or_create(question=q, choice_text=c_text, trait=trait)

        self.stdout.write(self.style.SUCCESS('Successfully seeded personality test data!'))
