# SYSONE TUG ARENA 1.0 — mustaqil repository

Bilim UZ Game API uchun frontend, 2.5D arena, real multiplayer sessiya mexanikasi, o‘quvchi statistikasi va TOP 3 podium.

**Reliz holati:** kod bazasi tayyorlangan, lekin production API hali mavjud emas. Haqiqiy Bilim UZ D1, Cloudflare deploy va brauzer vizual sinovi tasdiqlanmaguncha ommaviy reliz sifatida ishlatmang. GitHub Pages faqat `public/` ni nashr qiladi. `integrations/bilimuz/` mavjud Bilim UZ Worker ichida ishlaydigan taklif etilgan integratsiya; TUG ARENA uchun alohida server emas.

## Ishga tushirish

- `npm test` — Node 22+, 12 avtomatik sinov, shu jumladan lokal HTTP sessiyasi.
- `npm run serve` — statik frontend `http://localhost:8080`; real o‘yin uchun Game API kerak.
- `node tests/local-api.mjs` — faqat lokal QA, sun’iy test savollari, port 8765. Production deployga KIRITILMAYDI.
- `python tests/browser.py` — Python Playwright va Chromium mavjud bo‘lsa, uchta mustaqil browser context sinovi. Bu muhitda brauzer administrator siyosati tufayli bloklandi.

## GitHub Pages

1. Yangi `sysone-tug-arena` repository yarating, ushbu papka tarkibini commit qiling.
2. Settings → Pages → Source: GitHub Actions. `pages.yml` main branchga push qilinganda test va `public/` deploy bajaradi.
3. `public/config.js` dagi API manzilini Bilim UZ tasdiqlagan haqiqiy manzilga moslang.
4. Bilim UZ Owner Tool → Games → New game → GitHub Pages URL → mode `multiplayer`, open mode `newtab`. Qoidalar o‘yin ichida Host tomonidan belgilanadi.
5. Bilim UZ dasturchisi `docs/BILIMUZ_INTEGRATION_UZ.md` bo‘yicha API va launch token oqimini integratsiya qiladi. Owner katalog ID, origin va secret sozlanmaguncha Host ishlamaydi.

## Muhim dizayn qarorlari

- Browser Canvas 2D bilan asset-asosli 2.5D render; rigged GLB render qilinmaydi. Bu oltita mos sprite bilan bir xil vizual uslubni ta’minlaydi. Arqonning sprite ichidagi bo‘laklari sababli mutlaq IK mosligi yo‘q.
- 1v1–20v20; har ikkala jamoa to‘liq bo‘lmasa start yo‘q. Xona kodi 8 ta belgidan iborat. O‘quvchilar login qilmaydi, qisqa sessiya tokeni bilan ishlaydi.
- Har bir o‘quvchiga bir xil savollar to‘plami, tasodifiy savol va javob tartibi. Savol banki — server snapshot. Savollar kodga yozilmaydi. Faqat QA fixture tests katalogida.
- Jamoa foizi = to‘g‘ri javoblar / (jamoa hajmi × har o‘quvchiga savollar) × 100. Noto‘g‘ri va vaqt tugashi foiz bermaydi. Combo faqat shaxsiy statistika; foizni buzmaydi.
- O‘yin vaqti yoki barcha savollar yakuni; ixtiyoriy foiz chegarasi. G‘olib jamoa TOP 3: to‘g‘ri javoblar, kamroq noto‘g‘ri, to‘g‘ri javoblar uchun sarflangan vaqt; mutlaq tenglikda ID bilan barqaror tartib, teng natija belgisi. Durangda podium yo‘q.
- 700 ms HTTP polling, server-authoritative holat; WebSocket hali joriy qilinmagan. Bu tarif limitlari va katta yuklamada o‘lchanishi kerak.
- Room state DO storage da 4 soatgacha, keyin avtomatik o‘chiriladi; Host CSV eksport qiladi. Doimiy global reyting yoki shaxsiy ism bazasi yo‘q.
- 84 audio variant, OGG va MP3; user gesture orqali ovoz yoqiladi. 8 ta simultaneous audio limiti; 2.5D arqon va podium animatsiyalari.

## Papkalar

`public/`: frontend, SDK, grafik va audio assetlar; `integrations/bilimuz/`: API va state engine; `tests/`: lokal fixture, testlar; `docs/`: integratsiya, QA, manba paketlari litsenziya va texnik hisobotlar.
