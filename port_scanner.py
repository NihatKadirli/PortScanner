#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys
from datetime import datetime
import threading
from queue import Queue

# Renkler için ANSI kodları
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

# Thread sayısı (hız için)
N_THREADS = 100
queue = Queue()
acik_portlar = []

def banner():
    print(f"{Colors.BLUE}{Colors.BOLD}")
    print("=" * 60)
    print("        GELIŞMIŞ PORT SCANNER - SİBER GÜVENLİK ARACI")
    print("=" * 60)
    print(f"{Colors.END}")

def port_scan(port, host):
    """Belirli bir portu tarar"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        result = sock.connect_ex((host, port))
        
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Bilinmiyor"
            
            acik_portlar.append((port, service))
            print(f"{Colors.GREEN}[+] Port {port} AÇIK - Servis: {service}{Colors.END}")
        
        sock.close()
        
    except socket.gaierror:
        print(f"{Colors.RED}[!] Hostname çözümlenemedi{Colors.END}")
        sys.exit()
    except socket.error:
        print(f"{Colors.RED}[!] Sunucuya bağlanılamadı{Colors.END}")
        sys.exit()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}[!] Tarama kullanıcı tarafından durduruldu{Colors.END}")
        sys.exit()

def threader():
    """Thread worker fonksiyonu"""
    while True:
        port = queue.get()
        port_scan(port, hedef)
        queue.task_done()

def get_port_range():
    """Kullanıcıdan port aralığı alır"""
    print(f"\n{Colors.YELLOW}Port aralığı seçenekleri:{Colors.END}")
    print("1. Yaygın portlar (1-1024)")
    print("2. Tüm portlar (1-65535)")
    print("3. Özel aralık")
    
    secim = input(f"\n{Colors.BLUE}Seçiminiz (1/2/3): {Colors.END}")
    
    if secim == "1":
        return 1, 1024
    elif secim == "2":
        return 1, 65535
    elif secim == "3":
        baslangic = int(input("Başlangıç portu: "))
        bitis = int(input("Bitiş portu: "))
        return baslangic, bitis
    else:
        print(f"{Colors.RED}Geçersiz seçim! Varsayılan (1-1024) kullanılıyor.{Colors.END}")
        return 1, 1024

def save_results(host, ports):
    """Sonuçları dosyaya kaydeder"""
    kaydet = input(f"\n{Colors.YELLOW}Sonuçları kaydetmek ister misiniz? (e/h): {Colors.END}")
    
    if kaydet.lower() == 'e':
        dosya_adi = f"scan_{host}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(dosya_adi, 'w') as f:
            f.write(f"Port Tarama Sonuçları\n")
            f.write(f"Hedef: {host}\n")
            f.write(f"Tarih: {datetime.now()}\n")
            f.write(f"=" * 50 + "\n\n")
            
            for port, service in ports:
                f.write(f"Port {port}: {service}\n")
        
        print(f"{Colors.GREEN}[+] Sonuçlar '{dosya_adi}' dosyasına kaydedildi{Colors.END}")

# Ana program
if __name__ == "__main__":
    banner()
    
    # Hedef al
    hedef = input(f"{Colors.BLUE}Hedef IP veya hostname girin: {Colors.END}")
    
    try:
        hedef_ip = socket.gethostbyname(hedef)
    except socket.gaierror:
        print(f"{Colors.RED}[!] Hostname çözümlenemedi{Colors.END}")
        sys.exit()
    
    # Port aralığı al
    baslangic_port, bitis_port = get_port_range()
    
    # Bilgi göster
    print(f"\n{Colors.HEADER}{'=' * 60}{Colors.END}")
    print(f"{Colors.BOLD}Hedef: {hedef} ({hedef_ip}){Colors.END}")
    print(f"{Colors.BOLD}Port Aralığı: {baslangic_port}-{bitis_port}{Colors.END}")
    print(f"{Colors.BOLD}Başlangıç: {datetime.now()}{Colors.END}")
    print(f"{Colors.HEADER}{'=' * 60}{Colors.END}\n")
    
    # Thread'leri başlat
    for _ in range(N_THREADS):
        t = threading.Thread(target=threader, daemon=True)
        t.start()
    
    # Portları kuyruğa ekle
    for port in range(baslangic_port, bitis_port + 1):
        queue.put(port)
    
    # Tüm işlerin bitmesini bekle
    queue.join()
    
    # Sonuçları göster
    print(f"\n{Colors.HEADER}{'=' * 60}{Colors.END}")
    print(f"{Colors.BOLD}TARAMA TAMAMLANDI!{Colors.END}")
    print(f"{Colors.BOLD}Bitiş: {datetime.now()}{Colors.END}")
    print(f"{Colors.HEADER}{'=' * 60}{Colors.END}\n")
    
    if acik_portlar:
        print(f"{Colors.GREEN}{Colors.BOLD}Toplam {len(acik_portlar)} açık port bulundu:{Colors.END}\n")
        for port, service in sorted(acik_portlar):
            print(f"  Port {port}: {service}")
        
        save_results(hedef, acik_portlar)
    else:
        print(f"{Colors.YELLOW}Hiç açık port bulunamadı.{Colors.END}")
    
    print(f"\n{Colors.BLUE}Tarama tamamlandı. İyi çalışmalar!{Colors.END}\n")
