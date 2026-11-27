# QA — 2026-11-27

- 5 ta ZIP arxiv CRC tekshiruvi: muvaffaqiyatli.
- 84 audio variant, 168 web format fayli (OGG/MP3); WAV masterlar mavjud manba arxivlarida qoldirildi.
- 6 ta pull sprite sheet va 30 podium animatsiya to‘plamining WebP kadrlari integratsiya qilindi. Podium g‘alaba animatsiyalari 12 kadrdan foydalanadi.
- `npm test`: 12/12 muvaffaqiyatli. 11 engine test + 1 HTTP lifecycle test; 6 alohida player tokeni + host, server countdown, javoblar, g‘olib va TOP 3, qayta state olish, ruxsatsiz start rad etilishi.
- 40 o‘yinchili engine hisoblash sinovi muvaffaqiyatli. Bu 40 qurilmali real Cloudflare yuklama testi emas.
- Chromium orqali vizual E2E urinishi `ERR_BLOCKED_BY_ADMINISTRATOR` bilan to‘xtadi. UI render, real browser audio, mobile layout, FPS va vizual mukammallik tasdiqlanmagan.
- Haqiqiy Bilim UZ API, D1 production, Cloudflare DO deploy sinovdan o‘tmagan. Local QA fake database faqat testda. Repo va GitHub Pages hali yaratilmagan.
- Hozirgi frontend HTTP polling ishlatadi, WebSocket yo‘q. Raqamlar va grafik integratsiya uchun test talab qilinadi. Asosiy sprite ichidagi arqon bo‘lagi saqlanib qolgan. Rigged GLB original arxivlarda qoldirildi.
- Oldingi source audio va victory QA hujjatlari ularning ishlab chiqaruvchisi hisobotlari; bizning mustaqil audio tinglash yoki motion-capture tasdig‘imiz emas.
