# Audio sifat nazorati

60 assetning 180 fayli to‘liq dekodlandi. Eng yuqori true peak −4,825 dBTP bo‘lib, u music_battle_intense.wav faylida o‘lchandi. Belgilangan chegara −1 dBTP.

## Fayllar va signal

| Tekshiruv | Natija |
|---|---|
| Yetkazilgan material | 60 mustaqil PCM master, 60 OGG va 60 MP3. 11 loop va 49 bir martalik ovoz. |
| Davomiylik | Bir nusxadagi 60 ovoz jami 706,213 s. Briefda vaqt oralig‘i berilgan har bir asset mos. |
| Format va kanal | 180/180 fayl 48 000 Hz. 60/60 master signed 24-bit little-endian PCM. Arqon va personajlarning hammasi mono. Stadion va musiqaning hammasi ikki kanalli. |
| Clipping | Barcha formatlarni float PCM ga dekodlashda amplitudasi 1,0 ga yetgan namunalar soni 0. Har kanal bo‘yicha libebur128 true peak ham o‘lchandi. |
| Tarkib takrori | 60 dekodlangan PCM master uchun SHA-256 turlicha. Battle juftligining umumiy ritm va garmoniya qismlari ataylab birgalikda yozilgan. |
| Nom va konfiguratsiya | Har bir nom ro‘yxatdagi bir assetga tegishli. To‘rt JSON, 40 hodisaning bog‘lanishlari, rollar, kanallar va format yo‘llari fayllar bilan taqqoslandi. |
| Kirish va so‘nish | −74 dBFS yoki asset cho‘qqisidan −52 dB mezonlarining kattarog‘i ishlatildi. Eng kech birinchi faol namuna 8,58 ms. Oxirgi faol namunadan keyingi eng uzun past sath 57,06 ms. |
| Oflayn ijro | To‘liq fayllarni o‘qigan FFmpeg uch formatda ham aynan master frame sonini qaytardi. Qisqa Vorbis fayllarida sahifa davomiyligi qisqartirilib, dekoderlararo davomiylik tuzatildi. |
| Brauzer dekodi | Qt WebEngine 5.15.2 / Chromium 83 dvigatelida 48 kHz OfflineAudioContext yordamida WAV 60/60, OGG 60/60 va MP3 60/60 ochildi. |
| Brauzer oxirgi namunasi | Shu Chromium dvigateli 52 ta OGG buferi oxiriga ko‘pi bilan 992 frame (20,67 ms) qo‘shib qaytardi. Modul loopEnd va yakun vaqtini master frame soni bilan cheklaydi. Barcha 60 OGG va WAV juftligining boshga yaqin hamda o‘rta oynasidagi o‘lchangan vaqt siljishi 0 frame. |
| Fallback | UI uchun asosiy OGG manbasi 404 bilan almashtirilgan brauzer sinovida ikkinchi tanlov bo‘lgan MP3 ochildi va cue ishga tushdi. |

| Format | Eng yuqori cho‘qqi | Fayl | Jami hajm (bayt) |
|---|---:|---|---:|
| WAV · PCM 24-bit | −4,825 dBTP | music_battle_intense.wav | 198 752 784 |
| OGG · Vorbis | −4,876 dBTP | music_battle_intense.ogg | 11 492 788 |
| MP3 · MPEG Layer III | −4,946 dBTP | music_battle_intense.mp3 | 15 330 301 |

Kamida bitta to‘liq 400 ms blokka ega kliplar uchun BS.1770 K-filtri bilan integral ovoz balandligi o‘lchandi. 400 ms li o‘lchov bloki to‘lmagan qisqa UI va savol signallarida to‘liq klip RMS ishlatildi. Quyidagi qiymatlar masterlarga tegishli.

| Guruh | Mavjud integral o‘lchovlar (LUFS) | To‘liq klip RMS (dBFS) |
|---|---:|---:|
| Stadion va tribuna | −27,0 … −20,5 | −29,8 … −23,7 |
| Arqon | −29,0 … −21,0 | −30,4 … −23,2 |
| Personajlar | −24,0 … −21,0 | −26,1 … −21,2 |
| Javob va combo | −24,0 … −21,0 | −26,0 … −23,8 |
| Interfeys | −26,0 … −24,0 | −34,0 … −24,4 |
| Uchrashuv | −22,0 … −17,6 | −24,3 … −20,3 |
| Musiqa | −23,6 … −19,5 | −25,4 … −21,4 |

## Loop va faza

Tolalar va tribuna uchun tasodifiy qatlamlar chegara bo‘ylab tutashtirildi. Musiqada so‘nggi notalarning aks-sadosi va zarb asboblari keyingi davr boshiga olib o‘tildi. Har bir loopning ikki nusxasi tutashadigan joyida eng katta bir namunali sakrash o‘lchandi. U yaqin ±50 ms ichki namuna farqlarining 99-persentiliga nisbatan solishtirildi. Qabul qilish chegarasi 1,5×. Musiqadagi yangi takt zarbi atrofida RMS tabiiy ravishda o‘zgaradi.

| Loop | WAV nisbati | OGG nisbati | MP3 nisbati | WAV chegarasidagi sakrash (dBFS) |
|---|---:|---:|---:|---:|
| arena_crowd_idle | 0,285 | 0,788 | 0,208 | −50,92 |
| arena_crowd_active | 0,398 | 0,604 | 0,437 | −44,76 |
| arena_crowd_intense | 0,680 | 0,375 | 0,555 | −36,05 |
| rope_tension_idle | 0,534 | 0,745 | 0,559 | −36,75 |
| rope_tension_max | 0,271 | 0,042 | 0,273 | −38,51 |
| music_main_menu | 0,124 | 0,040 | 0,131 | −54,31 |
| music_lobby | 0,225 | 0,236 | 0,155 | −54,64 |
| music_battle_normal | 0,742 | 0,660 | 0,547 | −30,58 |
| music_battle_intense | 0,313 | 0,217 | 0,214 | −25,61 |
| music_sudden_death | 0,404 | 0,408 | 0,366 | −22,99 |
| music_results | 0,310 | 0,374 | 0,201 | −46,67 |

Normal va intense jangovar treklar 128 BPM, D minor, 4/4, 56 takt va aniq 5 040 000 framedan iborat. Bitta urish 22 500 frame, bitta takt 90 000 frame. 1-, 9-, 17-, 25-, 33-, 41-, 49- va 56-takt ichidagi umumiy ritm uchun tekshirilgan korrelyatsiya cho‘qqisi sakkiz holatning barchasida 0 frame siljishda bo‘ldi. Brauzerda ikkala bufer bitta vaqt va offset bilan boshlandi. Intensivlik o‘zgarganda ikkala buferning ijro sanog‘i ham birligicha qoldi.

## Multiplayer va mikser sinovi

Yuklama testi bir brauzer dvigatelida uchta alohida audio kontekstda bajarildi. Bir vaqt oynasida 40 ta shaxsiy javob, 40 ta jamoaviy tortish va 40 ta personaj kuchanishi simulyatsiya qilindi. Har bir jamoadagi oxirgi hodisa kuchli tortish edi.

| Kuzatuv | Natija |
|---|---|
| Host Display eshitgan shaxsiy savol signali | 0 |
| Host Control eshitgan shaxsiy savol signali | 0 |
| Sinov o‘yinchisi eshitgan 40 javobdan o‘ziniki | 1 |
| Katta ekrandagi tortish va kuchanish | 2 ta kuchli tortish va 2 ta kuchli personaj ovozi. Har jamoadan bittadan. |
| O‘yinchi qurilmasidagi arqon | O‘z jamoasi uchun 1 yengil tortish. Kuchli tortishlar soni 0. |
| Ssenariydagi eng yuqori manbalar | Host Display 13/16, Player Screen 6/10, Host Control 2/4. |
| Natija yo‘nalishi | Katta ekranda bitta g‘alaba fanfarasi. Sinovdagi yutqazgan o‘yinchida bitta mag‘lubiyat musiqasi. Boshqaruvda shaxsiy natija ijro etilmadi. |
| Mikser va holat | Start, burilish, g‘alabaga yaqinlashish, raund yakuni, natija, host UI, shaxsiy ID takrori, o‘yinchi fonini yoqish va o‘chirish tekshirildi. Raundda musiqa −7 dB, finalda −11 dB ducking holatiga o‘tdi va natija ovozlari tugagach dastlabki sathga qaytdi. |
| 14 soniyalik aralashma | OGG lardan stereo jang, tribuna, jamoa harakati, raund yakuni va fanfarani yig‘ish sinovida master kompressori va ducking o‘chirilganda −4,16 dBTP va −18,03 LUFS o‘lchandi. Bu qiymatlar sinov ssenariysiga tegishli. |

| Rejim | Bir oynadagi tortish so‘rovlari | Katta ekranda ijro qilingan tortishlar |
|---|---:|---:|
| 1v1 | 2 | 2 |
| 2v2 | 4 | 2 |
| 3v3 | 6 | 2 |
| 4v4 | 8 | 2 |
| 5v5 | 10 | 2 |
| 10v10 | 20 | 2 |
| 20v20 | 40 | 2 |

## 3D manbaga moslash

Asl arxivning 77 elementi CRC sinovidan o‘tdi. 7 GLB ichidagi skelet, material va animatsiyalar o‘qildi. 46 PNG va 10 WebP ochildi. To‘rtta 2048 × 256 tortish tasmasida sakkiztadan 256 × 256 kadr bor, Titan holatlari tasmasida to‘rtta. Ko‘k kiyimli sportchi Titan, qoplamali Cyber, yengil kiyimli Shadow va og‘ir etikdagi Viking oyoq, mato hamda kuchanish tembrlarini tanlashga yo‘nalish berdi. Ko‘k va qizil bayroqlar, markaziy sariq tasma, o‘ralgan arqon va chiziqli yashil chim ko‘rib chiqildi.

Har personajda 17 suyak va 10 ta klip, arqonda 16 suyak va Rope_Tension klipi bor. Stadionning Turf va Stands materiallari chimdagi qadamlar hamda keng tribuna aksiga moslandi. Arqonning BraidedRope materiali uchun quruq tolalar ishqalanishi ishlatildi.

Asl paketdagi oltita effekt ikki formatda, 44,1 kHz mono. Ikkala format ochildi. Quyidagi davomiyliklar OGG konteyneridan olingan. Har biri shu vazifa uchun yangi tovush bilan almashtirildi.

| Manbadagi nom | Vaqt (s) | Shu paketdagi vazifa |
|---|---:|---|
| combo_powerup | 0,550 | answer_combo_3 va answer_combo_5 |
| correct_chime | 0,400 | answer_correct |
| rope_pull_strain | 0,350 | rope_pull_light va rope_pull_heavy |
| victory_fanfare | 0,900 | match_victory |
| whistle_start | 0,350 | match_start |
| wrong_buzzer | 0,420 | answer_wrong |

3D arxiv SHA-256 qiymati nusxalarni yaratishdan oldin va ish yakunida bir xil bo‘ldi. Qiymat `3837e61fb5f3b851fe172fc25a89c4aafd26654d4080e383a36f5693418983b3`.

## Badiiy sifat va sinov chegarasi

- Texnik mezondan yiqilgan yoki yetishmagan assetlar soni 0. Barcha kelishilgan nom, format, davomiylik va kanal talablari tekshirildi.
- Oltita arena ovozi va Titan, Shadow hamda Vikingning 12 ta klipi protsedurali. Tribuna, nafas va kuchanish tembrlarida stilizatsiya eshitilishi mumkin. Jonli stadion yoki aktyor yozuvining realizmi tasdiqlanmagan.
- Oltita arqon effekti haqiqiy kanop yozuvisiz yaratilgan. Tola sirpanishi va kaft bosimi modellashtirildi. Musiqadagi orkestr tembrlarining barchasi sintez qilingan.
- Jismoniy stadion kolonkalari, telefon karnayi, iOS/Safari va 40 alohida kompyuterli haqiqiy tarmoqda tinglash sinovi o‘tkazilmagan. Fayl va brauzer natijalari yuqorida ko‘rsatilgan muhitlarga tegishli.
