# Ağlar Arası Alarm Eşiği Aktarımı (GP1 – Grup 32)

Tek sınıflı ağ anomali tespitinde (Isolation Forest, otokodlayıcı) etiketsiz eşik belirleme.
TÜBİTAK 2209-A önerisi temel alınmıştır.

**Ekip:** Berra Bayındır, Ceren Torun, Aslıhan Kaçmaz
**Danışman:** Dr. Didem Tufan

## v0 senaryosu
NF-UNSW-NB15-v2 üzerinde Isolation Forest yalnızca normal trafikle eğitilir; eşik (1−α) yüzdeliğiyle
belirlenir; küçük bir NF-CSE-CIC-IDS2018-v2 alt örnekleminde FPR ve ihlal oranı (FPR/α) hesaplanır.

## Kurulum ve çalıştırma
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/theory_bound.py     # Tablo 3'ü yeniden üretir
```
Veri setleri repoya eklenmez; `data/` altına indirilir.

## Yapı
- `src/` hazırlık, modeller, eşik yöntemleri, teorik üst sınır
- `notebooks/` keşif ve denemeler
- `docs/` GP1 raporu ve notlar
