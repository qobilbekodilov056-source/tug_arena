# Audio sifat nazorati · V1.1

**2026-yil 27-noyabr.** 2 personaj, 8 harakat to‘plami, 24 alohida master va 72 audio fayl. Tekshiruv tayyor eksportlar hamda V1 bilan birlashtirilgan haqiqiy Web Audio ijrochisida bajarildi.

## Texnik natijalar

| Ko‘rsatkich | Natija |
|---|---|
| WAV | 24/24 · PCM signed 24-bit little-endian · mono · 48 000 Hz |
| OGG | 24/24 · Vorbis VBR Q5 · mono · 48 000 Hz |
| MP3 | 24/24 · LAME VBR V2 · mono · 48 000 Hz |
| True peak, barcha eksportlar | Eng yuqori −2,78 dBTP. Chegara −1 dBTP. |
| Raqamli clipping | 0 ta to‘liq shkala namunasi. Barcha o‘lchovlar chekli. |
| Davomiylik | 24/24 belgilangan oraliqda. Barcha masterlar yig‘indisi 24,23 s. |
| Chekka sukut | 5 ms RMS oynasi, klip maksimumiga nisbatan −38 dB. Boshida ko‘pi bilan 25 ms, oxirida 32 ms. |
| Doimiy siljish | Barcha formatlarda eng yuqori o‘rtacha DC amplitudasi −79,4 dBFS. |
| Noyoblik | 24 xil dekodlangan PCM izi va 72 xil fayl SHA-256 summasi. Bir harakatning 24 ta A/B/C juft taqqoslashida eng yuqori normallangan to‘lqin korrelyatsiyasi 0,251. |
| Manifest | 24/24 ID bir martadan xaritalandi. Fayl yo‘llari, yozilgan namuna soni, baytlar va SHA-256 tekshirildi. Uchta JSON o‘qildi. |
| Loop va fazoviy ijro | 24/24 bir martalik mono manba. Dvigatel ijroni masterdagi namunalar soniga bog‘laydi. |

LUFS va true peak libebur128 orqali o‘lchandi. WAV namunalarini libsndfile, OGG va MP3 oqimlarini FFmpeg ochdi. 72 ta dekodlangan oqimdagi namunalar soni o‘z masteriga aynan teng bo‘ldi. Yangi fayllarning barchasi 400 ms dan uzun.

## V1 bilan balandlik muvozanati

Taqqoslash uchun Titan, Cyber, Shadow va Vikingning shu to‘rtta harakatdagi 16 ta WAV masteri bevosita o‘lchandi. Ularning harakat bo‘yicha medianasi quyida. Barcha personajlar uchun boshlang‘ich chiziqli gain 0.82 va umumiy CHARACTER shinasi −2.3 dB.

| Harakat | V1 medianasi, LUFS-I | V1.1 WAV oralig‘i, LUFS-I | V1.1 davomiyligi | Ruxsat etilgan |
|---|---:|---:|---:|---:|
| Yengil tortish | −24,0 | −24,5 … −23,4 | 0,421–0,652 s | 0,3–0,8 s |
| Kuchli tortish | −21,5 | −22,0 … −20,9 | 0,892–1,307 s | 0,8–1,5 s |
| Sirpanish | −23,0 | −23,5 … −22,4 | 0,579–0,904 s | 0,5–1,0 s |
| G‘alaba | −21,0 | −21,6 … −20,4 | 1,237–1,832 s | 1,0–3,0 s |

## Har bir ijro

| WAV master | Uzunligi | LUFS-I | WAV dBTP | OGG dBTP | MP3 dBTP |
|---|---:|---:|---:|---:|---:|
| [bahodir_effort_light_a](../masters_wav/bahodir/bahodir_effort_light_a.wav) | 0,557 s | −24,0 | −13,01 | −12,93 | −12,88 |
| [bahodir_effort_light_b](../masters_wav/bahodir/bahodir_effort_light_b.wav) | 0,652 s | −24,5 | −6,38 | −6,66 | −6,54 |
| [bahodir_effort_light_c](../masters_wav/bahodir/bahodir_effort_light_c.wav) | 0,544 s | −23,4 | −7,34 | −7,44 | −7,14 |
| [bahodir_effort_heavy_a](../masters_wav/bahodir/bahodir_effort_heavy_a.wav) | 0,892 s | −21,5 | −8,63 | −9,07 | −8,48 |
| [bahodir_effort_heavy_b](../masters_wav/bahodir/bahodir_effort_heavy_b.wav) | 1,126 s | −22,0 | −5,42 | −5,43 | −5,61 |
| [bahodir_effort_heavy_c](../masters_wav/bahodir/bahodir_effort_heavy_c.wav) | 1,307 s | −20,9 | −9,23 | −9,61 | −9,38 |
| [bahodir_slip_a](../masters_wav/bahodir/bahodir_slip_a.wav) | 0,753 s | −23,0 | −8,65 | −8,66 | −8,46 |
| [bahodir_slip_b](../masters_wav/bahodir/bahodir_slip_b.wav) | 0,658 s | −23,5 | −7,12 | −7,64 | −7,04 |
| [bahodir_slip_c](../masters_wav/bahodir/bahodir_slip_c.wav) | 0,904 s | −22,4 | −10,87 | −10,78 | −10,91 |
| [bahodir_victory_a](../masters_wav/bahodir/bahodir_victory_a.wav) | 1,237 s | −21,0 | −5,44 | −5,45 | −5,43 |
| [bahodir_victory_b](../masters_wav/bahodir/bahodir_victory_b.wav) | 1,832 s | −21,5 | −5,34 | −5,93 | −5,33 |
| [bahodir_victory_c](../masters_wav/bahodir/bahodir_victory_c.wav) | 1,827 s | −20,4 | −7,53 | −8,04 | −7,58 |
| [malika_effort_light_a](../masters_wav/malika/malika_effort_light_a.wav) | 0,539 s | −24,0 | −7,95 | −8,25 | −7,45 |
| [malika_effort_light_b](../masters_wav/malika/malika_effort_light_b.wav) | 0,421 s | −24,5 | −10,33 | −10,28 | −10,32 |
| [malika_effort_light_c](../masters_wav/malika/malika_effort_light_c.wav) | 0,637 s | −23,4 | −8,58 | −8,49 | −8,50 |
| [malika_effort_heavy_a](../masters_wav/malika/malika_effort_heavy_a.wav) | 1,247 s | −21,5 | −4,91 | −5,33 | −4,80 |
| [malika_effort_heavy_b](../masters_wav/malika/malika_effort_heavy_b.wav) | 1,246 s | −22,0 | −4,61 | −5,01 | −4,45 |
| [malika_effort_heavy_c](../masters_wav/malika/malika_effort_heavy_c.wav) | 1,088 s | −20,9 | −3,49 | −3,56 | −3,30 |
| [malika_slip_a](../masters_wav/malika/malika_slip_a.wav) | 0,805 s | −23,0 | −4,46 | −4,58 | −4,51 |
| [malika_slip_b](../masters_wav/malika/malika_slip_b.wav) | 0,579 s | −23,5 | −8,65 | −8,35 | −8,61 |
| [malika_slip_c](../masters_wav/malika/malika_slip_c.wav) | 0,706 s | −22,4 | −5,25 | −6,02 | −5,48 |
| [malika_victory_a](../masters_wav/malika/malika_victory_a.wav) | 1,694 s | −21,6 | −2,92 | −3,26 | −2,78 |
| [malika_victory_b](../masters_wav/malika/malika_victory_b.wav) | 1,587 s | −21,5 | −4,79 | −4,97 | −4,88 |
| [malika_victory_c](../masters_wav/malika/malika_victory_c.wav) | 1,391 s | −20,4 | −6,71 | −6,64 | −6,71 |

## Ijro, tabiiylik va manbalar

Bahodirning asosiy tortishlari HaelDBning bir erkak ijrochisidan, Malikaning asosiy ovozi Cici Fyre’ning Type 3 ijrosidan tanlandi. Kuchanish, nafas va g‘alaba reaksiyalarida qo‘shimcha jonli ijrolar ishlatildi. Har bir A/B/C ketma-ketligi alohida yozilgan boshlanish yoki alohida kuchanish, boshqa nafas tuzilishi va boshqa davomiylikka ega. Ijrolarni yasash uchun yozuv tezligini yoki tonalligini o‘zgartirish ishlatilmadi.

Jarangli qismlardagi avtokorrelyatsion F0 bahosining kliplar bo‘yicha medianasi Bahodirda taxminan 304 Hz, Malikada 316 Hz. Kuchanish paytida ovoz xirillashi va oktava xatosi mumkin. Tabiiylik va ifoda tinglab baholanadi.

Arqon, oyoq, gavjum stadion, musiqa va qo‘shimcha reverb kanallari montajga qo‘shilmadi. Qisqa nafas signal tarkibiga kiradi. Past chastota filtri, chekka o‘tishlari va DC tekshiruvi qo‘llandi. Ovoz ostidagi xonaga xos juda past shovqinni raqamli o‘lchov bilan ijrodan to‘liq ajratib bo‘lmaydi.

Gapirilgan replika manbalari paketga kiritilmadi. PocketSphinx 5.0.4 inglizcha modeli inson gapirgan nazorat yozuvidagi to‘rt so‘zni to‘g‘ri qaytardi. Kliplarda qisqa unli va nafaslarni ayrim inglizcha so‘zlarga o‘xshatdi. Model chiqargan eng yuqori so‘z ehtimoli 0,639 bo‘ldi. Ushbu avtomatik baho tinglovchi eshitadigan nutq uchun yakuniy mezon bo‘la olmaydi. O‘zbek va rus tillarida lingvistik tinglov sinovi o‘tkazilmadi.

**Eshitish bo‘yicha cheklov.** Mustaqil ovoz rejissyori yoki tinglovchi yakuniy kliplarga baho bermagan. Realizm, ikki qahramonning tembri va reaksiyalarning yoshga mos ifodasini tinglab qabul qilish uchun 24 tugmali mahalliy sahifa mavjud. Malika g‘alabasidagi uchta qisqa kulgi oldindan siqilgan HQ tinglash nusxalaridan kelgan. 24-bit master eksportida ularning dastlabki ma’lumot yo‘qotilishi saqlanadi. [Variantlarni tinglash](TINGLASH.html)

## Brauzer va 40 personaj sinovi

Sinov Qt WebEngine 5.15.2 / Chromium 83 da mahalliy HTTP orqali haqiqiy AudioContext, OfflineAudioContext, PannerNode va V1 ijrochisi bilan ishladi.

| Holat | Kuzatilgan natija |
|---|---|
| Mahalliy dekodlash | Brauzer 72/72 faylni ochdi. WAV va MP3 uzunligi aynan mos. |
| Vorbis chegarasi | Ayrim OGG buferlarining oxiriga ushbu brauzer 122–992 ta namuna qo‘shdi. V1 ijrochisi frames/48000 da to‘xtadi. Urg‘u atrofidagi signal bo‘yicha WAV bilan siljish 0 namuna. |
| Aralash ustuvorlikdagi 40 yangi personaj | 2 ovoz boshlandi, har jamoada bittadan g‘alaba. |
| Eski va yangi 40 personaj | 4 ovoz boshlandi. Takroriy yuklamada ayni vaqtda maksimal 4 personaj ovozi qayd etildi. |
| Variant tanlovi | 1650 ta muvaffaqiyatli tanlov, ketma-ket takror 0 ta. Alohida 450 bir-aktyorli sinovda A/B/C 153/151/146 marta tanlandi. Bu qism boshqariladigan soat va tasodif generatori bilan Node.js da ishladi. |
| Pitch | Konfiguratsiya 0.97–1.03. Brauzer sinovida yangi personajlar uchun 0.9812–1.0224 qayd etildi. |
| Masofa va stereo joylashuv | Haqiqiy klipni 4 metrdan 16 metrga ko‘chirishda RMS −8,46 dB o‘zgardi. Chap va o‘ngdagi manbalarda mos kanal balandroq bo‘ldi. |
| Rollar | Host ikkala jamoani oldi. Player standartda jim turdi, yoqilganda faqat egasining ovozini oldi. Host Control personaj ovozini olmadi. |
| Muqobil format | OGG so‘roviga sun’iy 404 berilganda MP3 chalindi. OGG va MP3 404 berganda WAV chalindi. |
| Ijroni boshqarish | Ustuvorlik, kutish vaqti, 10 s takroriy ID filtri, raundni tozalash, eskirgan hodisa va eski CHARACTER_EFFORT sinovdan o‘tdi. |
| Mahalliy tinglash sahifasi | 24 ta variant tugmasi topildi. Birinchi va oxirgi tugma mos yozuvni brauzer pleyeriga yukladi. |

40 aktyor yuklamasi bitta Web Audio mijoziga bir vaqtda yuborildi. Jismoniy 40 qurilmali tarmoq sinovi o‘tkazilmadi. Ovoz urg‘usini animatsiyaga moslash uchun qo‘llanmada tegishli tortish kadrlari ko‘rsatilgan. Ishlayotgan o‘yin buildida vizual va ovozning yakuniy mosligi tinglovchi tomonidan tekshirilmagan.

## Arxivdan qayta ulash

Arxiv alohida katalogga chiqarildi, CRC va ichki havolalar tekshirildi. Tayyorlovchi yangi joydan ikki marta ishga tushirildi. Birlashtirilgan konfiguratsiyada V1 ning 60 ta yozuvi va kengaytmaning 24 ta yozuvi tegishli audio fayllarga ochildi.

## Taqqoslash nusxalari

- V1 audio arxivi SHA-256 `27e77dc20cfd3437af445e54af4ed4a0c60b67dcc3c4cd48c073ee6f89c1b568`. Taqqoslangan eski WAV va konfiguratsiyalar V1 ZIP ichidagi baytlarga mos.
- O‘zbek UI arxivi SHA-256 `906523f4f9858a9f1a0f6ca5cd9417399f7a405de1709bbf3b701267ab757474`. Bahodir va Malika uchun sakkiztadan alohida tortish kadri ko‘rib chiqildi.
