# 🔍 Gelişmiş Port Tarayıcı

Güvenlik testi ve ağ analizi için profesyonel port tarama aracı.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/Lisans-MIT-green.svg)
![Ethical](https://img.shields.io/badge/Kullanım-Yalnızca%20Etik-red.svg)




## ⚠️ ETİK KULLANIM ZORUNLULUĞU - YASAL UYARI

**Bu araç yalnızca etik ve yasal amaçlarla kullanılmalıdır.**
<img width="512" height="506" alt="Ekran görüntüsü 2025-11-23 213338" src="https://github.com/user-attachments/assets/7165b9ac-8f19-49b7-b196-2820335d7723" />

### ✅ İzinli Kullanım Alanları:
- Kendi sistemlerinizi test etmek
- Yazılı izin aldığınız sistemleri taramak
- Penetrasyon testi sözleşmesi kapsamında kullanım
- Eğitim ve araştırma amaçlı (izole lab ortamında)
- Bug bounty programları kapsamında (program kurallarına uygun)

### ❌ İzinsiz Kullanım YASADIŞTIR:
- Başkalarının sistemlerini izinsiz taramak
- Saldırı amacıyla kullanmak
- İzin almadan ağ keşfi yapmak
- Kötü niyetli aktiviteler için kullanmak

**⚖️ YASAL SORUMLULUK:** Bu aracı kullanarak yasaları ihlal ederseniz, tüm yasal ve cezai sorumluluk size aittir. Geliştirici hiçbir şekilde sorumlu tutulamaz.

**🇹🇷 TÜRKİYE YASALARI:** 5651 Sayılı Kanun ve TCK 243-244. maddeler uyarınca yetkisiz erişim suçtur.

---

## 🎯 Özellikler

- **Hızlı Tarama**: Çoklu thread ile hızlı port tarama
- **Servis Tespiti**: Çalışan servisleri tanımlama
- **Özel Port Aralıkları**: Belirli portları veya tüm portları tarama
- **Banner Yakalama**: Servis banner bilgisi toplama
- **Sonuç Kaydetme**: Tarama sonuçlarını dosyaya kaydetme
- **Gizli Mod Seçenekleri**: Ayarlanabilir tarama hızı

## 🚀 Kurulum

```bash
# Depoyu klonla
git clone https://github.com/kullaniciadin/port-scanner.git
cd port-scanner

# Bağımlılıkları yükle (varsa)
pip install -r requirements.txt
```

## 💻 Kullanım

### Temel Tarama
```bash
python port_scanner.py <hedef_ip>
```

### Belirli Portları Tara
```bash
python port_scanner.py <hedef_ip> -p 80,443,8080
```

### Port Aralığı Tarama
```bash
python port_scanner.py <hedef_ip> -p 1-1000
```

### Tam Port Tarama
```bash
python port_scanner.py <hedef_ip> -p 1-65535
```

### Hızlı Tarama (En Yaygın 100 Port)
```bash
python port_scanner.py <hedef_ip> --fast
```

### Servis Tespiti İle
```bash
python port_scanner.py <hedef_ip> -s
```

### Sonuçları Kaydet
```bash
python port_scanner.py <hedef_ip> -o sonuclar.txt
```

## 📊 Örnek Çıktı

```
[*] 192.168.1.1 hedefinde tarama başlatılıyor
[*] Tarama başlangıç: 2025-11-23 14:30:00
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[+] Port 22   AÇIK  - SSH (OpenSSH 7.9)
[+] Port 80   AÇIK  - HTTP (Apache/2.4.41)
[+] Port 443  AÇIK  - HTTPS (nginx/1.18.0)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[*] Tarama tamamlandı: 2025-11-23 14:32:15
[*] Toplam açık port: 3
[*] Tarama süresi: 2d 15s
```

## 🛡️ Etik Test Rehberi

### Taramadan Önce:
1. ✅ **Yazılı İzin Alın**: Mutlaka açık izin belgesi edinin
2. ✅ **Kapsamı Kontrol Edin**: Hedefin yetkilendirilmiş kapsam içinde olduğundan emin olun
3. ✅ **Kuralları İnceleyin**: Hizmet Şartları ve Kabul Edilebilir Kullanım Politikasını okuyun
4. ✅ **Yetkilendirmeyi Belgeleyin**: İzin kayıtlarını saklayın

### Tarama Sırasında:
1. ⚠️ **Hız Limitlerine Uyun**: Hedef sistemleri aşırı yüklemeyin
2. ⚠️ **Mesai Saatlerine Dikkat**: Yoğun olmayan saatlerde tarama yapmayı düşünün
3. ⚠️ **Etkiyi İzleyin**: Sistem performans sorunlarına dikkat edin
4. ⚠️ **İstenirse Durdurun**: Talep edildiğinde hemen durdurun

### Tarama Sonrası:
1. 📝 **Bulguları Raporlayın**: Keşifleri profesyonel şekilde belgeleyin
2. 🔒 **Gizliliği Koruyun**: Sonuçları halka açık paylaşmayın
3. 💼 **Açıklama Sürecini Takip Edin**: Sorumlu açıklama pratiklerini kullanın
4. 🗑️ **Verileri Güvenli Tutun**: Tarama verilerini uygun şekilde işleyin ve imha edin

## 🎓 Eğitim Amaçlı Kullanım

Bu araç şunlar için tasarlanmıştır:
- Ağ güvenliği kavramlarını öğrenmek
- TCP/IP protokollerini anlamak
- Etik hacking becerilerini pratik yapmak
- Sertifikasyonlara hazırlanmak (CEH, OSCP, vb.)

**Önerilen Lab Ortamları:**
- VirtualBox/VMware sanal makineler
- HackTheBox, TryHackMe platformları
- Kişisel ev lab ağları
- Sahip olduğunuz bulut sunucuları

## 🔒 Yasal Düzenlemeler

### Bilmeniz Gereken Yasalar:
- **Türkiye**: 5651 Sayılı İnternet Kanunu
- **Türkiye**: TCK Madde 243-244 (Bilişim Sistemine Girme)
- **Türkiye**: 6698 Sayılı KVKK (Kişisel Verilerin Korunması)
- **AB**: GDPR (Genel Veri Koruma Yönetmeliği)
- **ABD**: Computer Fraud and Abuse Act (CFAA)

**Yetkisiz erişim için cezalar:**
- Ağır para cezaları
- Cezai kovuşturma
- Hapis cezası
- Hukuki davalar

## ⚙️ Yapılandırma

Varsayılan ayarlar için `config.py` düzenleyin:

```python
# Port başına zaman aşımı (saniye)
TIMEOUT = 1

# Thread sayısı
THREADS = 100

# Bağlantı tekrar deneme sayısı
RETRIES = 1

# Taramalar arası gecikme (saniye)
DELAY = 0
```

## 🐛 Yaygın Portlar Referansı

| Port | Servis | Açıklama |
|------|---------|----------|
| 21 | FTP | Dosya Transfer Protokolü |
| 22 | SSH | Güvenli Kabuk |
| 23 | Telnet | Telnet |
| 25 | SMTP | E-posta |
| 53 | DNS | Alan Adı Sistemi |
| 80 | HTTP | Web Sunucusu |
| 443 | HTTPS | Güvenli Web Sunucusu |
| 3306 | MySQL | Veritabanı |
| 3389 | RDP | Uzak Masaüstü |
| 8080 | HTTP-Alt | Alternatif HTTP |

## 📋 Kullanım Senaryoları

### Senaryo 1: Kendi Sunucunuzu Test Etme
```bash
# Önce izin belgesi hazırlayın
# Kendi sunucunuzun IP'si
python port_scanner.py 192.168.1.100 -p 1-1000
```

### Senaryo 2: Bug Bounty Programı
```bash
# Program kurallarını okuyun
# Kapsam içindeki domain
python port_scanner.py example.com --fast -o rapor.txt
```

### Senaryo 3: Lab Ortamında Eğitim
```bash
# VirtualBox/VMware lab ağınızda
python port_scanner.py 192.168.56.101 -p 1-65535 -s
```

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen:
1. Depoyu fork edin
2. Özellik branch'i oluşturun
3. Değişikliklerinizi commit edin
4. Pull request gönderin

## 📄 Lisans

MIT Lisansı - Detaylar için LICENSE dosyasına bakın.

**SORUMLULUK REDDİ:** Bu yazılım yalnızca eğitim ve yetkili test amaçları için sağlanmaktadır. Kullanıcılar tüm yürürlükteki yasa ve düzenlemelere uymakla yükümlüdür. Yazar, kötüye kullanımdan hiçbir sorumluluk kabul etmez.

## 📚 Kaynaklar


---

<div align="center">

### 🛡️ Sorumlu Tarayın. Etik Kalın. Yasal Olun.

**Etik Hacking Topluluğu İçin Yapıldı**

⚠️ **UYARI:** İzinsiz tarama suçtur. Yalnızca yetkili olduğunuz sistemlerde kullanın.

</div>
