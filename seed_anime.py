import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models import Category, Question, Choice, PersonalityResult

def seed_anime_test():
    category, created = Category.objects.get_or_create(
        name="Hangi Anime Karakterisin?",
        defaults={"description": "Kişiliğine en uygun anime karakterini bulmaya hazır mısın? Gizli güçlerini ve tarzını keşfet!"}
    )
    
    if not created:
        category.questions.all().delete()
        category.results.all().delete()

    print(f"Kategori {'oluşturuldu' if created else 'bulundu (yenileniyor)'}: {category.name}")

    questions_data = [
        # Soru 1
        {
            "text": "Yakın bir arkadaşın zor durumdaysa ne yaparsın?",
            "choices": [
                {"text": "Asla pes etmem, onu kurtarmak için kendimi tehlikeye atarım!", "trait": "Naruto"},
                {"text": "Soğukkanlı kalır, en mantıklı stratejiyi yaparak olayı çözerim.", "trait": "Levi"},
                {"text": "Düşünmeden, sadece içgüdülerimle kavgaya dalarım!", "trait": "Luffy"},
                {"text": "Buna sebep olan kişiyi arka planda çok zekice cezalandırırım.", "trait": "Light"}
            ]
        },
        # Soru 2
        {
            "text": "Senin için 'güç' ne anlama geliyor?",
            "choices": [
                {"text": "İnsanları korumak ve kimseyi arkada bırakmamak.", "trait": "Naruto"},
                {"text": "Hayatta kalmak ve işi hatasız bitirmek için bir araç.", "trait": "Levi"},
                {"text": "Tamamen özgür olmak ve dünyayı dolaşabilmek!", "trait": "Luffy"},
                {"text": "İstediğim mükemmel ve adil dünya düzenini kurabilmek.", "trait": "Light"}
            ]
        },
        # Soru 3
        {
            "text": "Sence bir liderde olması gereken en önemli özellik hangisidir?",
            "choices": [
                {"text": "Sarsılmaz inancı ve çevresindekilere ilham verebilmesi.", "trait": "Naruto"},
                {"text": "Disiplini, kararlılığı ve net emirler verebilmesi.", "trait": "Levi"},
                {"text": "Eğlenceli olması ve ekibiyle sırt sırta verebilmesi.", "trait": "Luffy"},
                {"text": "Üstün zekası ve her zaman birkaç adım ilerisini görebilmesi.", "trait": "Light"}
            ]
        },
        # Soru 4
        {
            "text": "Düşmanın karşısında nasıl davranırsın?",
            "choices": [
                {"text": "Önce konuşmaya çalışırım, aramızda bir empati bağı kurarım.", "trait": "Naruto"},
                {"text": "Hiçbir acıma duygusu hissetmeden doğrudan görevimi yaparım.", "trait": "Levi"},
                {"text": "Beni veya arkadaşlarımı kızdırdıysa ağzını burnunu kırana kadar vururum!", "trait": "Luffy"},
                {"text": "Yüzüne gülerken arkasından onun sonunu getirecek planı çoktan yapmış olurum.", "trait": "Light"}
            ]
        },
        # Soru 5
        {
            "text": "Boş vaktinde ne yapmayı seversin?",
            "choices": [
                {"text": "Antrenman yapmak ve yeni teknikler geliştirmek.", "trait": "Naruto"},
                {"text": "Temizlik yapmak ve etrafın düzenli olduğundan emin olmak.", "trait": "Levi"},
                {"text": "Doyasıya yemek yemek ve uyumak!", "trait": "Luffy"},
                {"text": "Sakin bir yerde oturup kitap okumak ya da bir şeyler araştırmak.", "trait": "Light"}
            ]
        },
        # Soru 6
        {
            "text": "En büyük zayıflığın sence nedir?",
            "choices": [
                {"text": "Sevdiklerime fazla bağlı olmam, onlar zarar görünce deliye dönmem.", "trait": "Naruto"},
                {"text": "Bazen çok sert ve ulaşılamaz görünmem.", "trait": "Levi"},
                {"text": "Düşünmeden hareket etmem ve açlığa dayanamamam.", "trait": "Luffy"},
                {"text": "Kibirim... Bazen herkesten zeki olduğumu düşünmem.", "trait": "Light"}
            ]
        },
        # Soru 7
        {
            "text": "Bir hedefe ulaşmak için hangi yolu seçersin?",
            "choices": [
                {"text": "En zor yol bile olsa vazgeçmem.", "trait": "Naruto"},
                {"text": "En temiz, kanısız ve keskin yolu bulur, hemen uygularım.", "trait": "Levi"},
                {"text": "Aklıma ne eserse oraya giderim, en heyecanlı yol hangisiyse!", "trait": "Luffy"},
                {"text": "Sistemi kendi lehime çevirecek pratik ve zekice stratejiler geliştiririm.", "trait": "Light"}
            ]
        },
        # Soru 8
        {
            "text": "Takım çalışması senin için ne ifade ediyor?",
            "choices": [
                {"text": "Her şeydir! Arkadaşlarım olmazsa ben de olmam.", "trait": "Naruto"},
                {"text": "Eğer herkes üstüne düşeni yaparsa işe yarayan bir sistem.", "trait": "Levi"},
                {"text": "Ailem gibiler! Hep birlikte devasa partiler yapmak için ideal.", "trait": "Luffy"},
                {"text": "Onları bir piyon gibi yönlendirebildiğim sürece takım faydalıdır.", "trait": "Light"}
            ]
        },
        # Soru 9
        {
            "text": "Hayattaki en büyük motivasyonun nedir?",
            "choices": [
                {"text": "Herkes tarafından kabul edilmek ve saygı görmek.", "trait": "Naruto"},
                {"text": "İnsanlığı korumak ve verilen sözleri tutmak.", "trait": "Levi"},
                {"text": "Tamamen özgürce maceralara atılıp hayalimi gerçekleştirmek.", "trait": "Luffy"},
                {"text": "Gerçek adaleti sağlayıp 'yeni bir dünyanın' lideri olmak.", "trait": "Light"}
            ]
        },
        # Soru 10
        {
            "text": "Zor bir kararla yüzleştiğinde neye güvenirsin?",
            "choices": [
                {"text": "Kalbimin sesine ve asla bitmeyen inancıma.", "trait": "Naruto"},
                {"text": "Tecrübelerime ve acımasız gerçekliğe.", "trait": "Levi"},
                {"text": "İçgüdülerime! O an içimden ne gelirse onu yaparım.", "trait": "Luffy"},
                {"text": "Keskin zekama ve mantığıma.", "trait": "Light"}
            ]
        },
        # Soru 11
        {
            "text": "İnsanlar senin hakkında ilk ne düşünür?",
            "choices": [
                {"text": "Çok gürültücü ve enerjik biri olduğumu düşünürler.", "trait": "Naruto"},
                {"text": "Çok ciddi, asabi ve korkutucu biri olduğumu düşünürler.", "trait": "Levi"},
                {"text": "Saf ve sürekli karnı aç, biraz da aptal ama çok cesur bulurlar.", "trait": "Luffy"},
                {"text": "Örnek bir öğrenci veya mükemmel, efendi biri olarak görürler.", "trait": "Light"}
            ]
        },
        # Soru 12
        {
            "text": "Adalet senin için nedir?",
            "choices": [
                {"text": "İnsanların birbirini anlayarak getirdiği huzurdur.", "trait": "Naruto"},
                {"text": "Kötülüğü temizlemek için yapılan gerekli ve sert fedakarlıklardır.", "trait": "Levi"},
                {"text": "Zorbalık yapmamaktır, isteyenin güldüğü bir yerdir.", "trait": "Luffy"},
                {"text": "Suçluların acımasızca cezalandırılmasıdır.", "trait": "Light"}
            ]
        },
        # Soru 13
        {
            "text": "Başarısızlıkla nasıl başa çıkarsın?",
            "choices": [
                {"text": "Biraz üzülürüm ama sonra yeniden ayağa kalkarım, pes etmek yok!", "trait": "Naruto"},
                {"text": "Hatamı soğukkanlılıkla bulur ve bidahakine tekrarlamam.", "trait": "Levi"},
                {"text": "Üzülmem! Sadece daha çok yemek yiyip tekrar dalarım.", "trait": "Luffy"},
                {"text": "Başarısızlık ihtimalini pek düşünmem, plana küçük ayarlar çekerim.", "trait": "Light"}
            ]
        },
        # Soru 14
        {
            "text": "Hayalindeki hayat tarzı nasıl olurdu?",
            "choices": [
                {"text": "Büyük bir köyün en saygın, güler yüzlü lideri olmak.", "trait": "Naruto"},
                {"text": "Sessiz, çok temiz ve huzurlu bir köşede çayımı yudumlamak.", "trait": "Levi"},
                {"text": "Bir sürü macera yaşamak ve bütün dünyayı keşfetmek.", "trait": "Luffy"},
                {"text": "Suçsuz, tertemiz bir dünyada yargıç gibi her şeyi izlemek.", "trait": "Light"}
            ]
        },
        # Soru 15
        {
            "text": "Senin için en önemli değer hangisidir?",
            "choices": [
                {"text": "Dostluk / İnanç", "trait": "Naruto"},
                {"text": "Disiplin / Sadakat", "trait": "Levi"},
                {"text": "Özgürlük / Hayaller", "trait": "Luffy"},
                {"text": "Adalet / Zeka", "trait": "Light"}
            ]
        }
    ]

    for q_data in questions_data:
        question = Question.objects.create(
            category=category,
            question_text=q_data["text"]
        )
        for c_data in q_data["choices"]:
            Choice.objects.create(
                question=question,
                choice_text=c_data["text"],
                trait=c_data["trait"]
            )

    print(f"{category.name} testi için 15 soru ve seçenekler eklendi.")

    results_data = [
        {
            "trait": "Naruto",
            "title": "Naruto Uzumaki",
            "description": "Senin içinde asla sönmeyen bir ateş var! Asla pes etmeyen inatçı yapın ve sevdiklerine olan bağlılığın seni tam bir kahraman yapıyor. İnsanların iyiliğine inanıyor ve her zaman onlara ilham kaynağı oluyorsun."
        },
        {
            "trait": "Levi",
            "title": "Levi Ackerman",
            "description": "Sen tam bir görev insanısın! Disiplinli, soğukkanlı ve inanılmaz derecede profesyonelsin. Çoğu zaman duygularını hissettirmesen de, kendi içinde büyük bir adalet duygun var. Kriz anlarında en sakin kalan her zaman sensin."
        },
        {
            "trait": "Luffy",
            "title": "Monkey D. Luffy",
            "description": "Özgürlük senin göbek adın! Kuralları, sınırları sevmiyorsun; içinden geldiği gibi yaşamayı ve hayallerinin peşinden koşmayı tercih ediyorsun. Eğlenmeyi çok iyi biliyor ve dostların için dünyayı karşına alabiliyorsun."
        },
        {
            "trait": "Light",
            "title": "Light Yagami",
            "description": "Zekan senin en büyük silahın! Olaylara herkesten çok farklı bakıyorsun; stratejik planlar kurmakta üstüne yok. İşlerin tıkırında gidip mükemmel bir düzen oluşmasını istiyorsun ve bunun için kendi inandığın doğruyu uygulamaktan çekinmezsin."
        }
    ]

    for r_data in results_data:
        PersonalityResult.objects.create(
            category=category,
            trait=r_data["trait"],
            title=r_data["title"],
            description=r_data["description"]
        )

    print(f"{category.name} testi için sonuçlar başarıyla oluşturuldu!\n")

if __name__ == '__main__':
    seed_anime_test()
