# Bilim UZ Universal Game API v2 — TUG ARENA integratsiya shartnomasi

Bu taklif qilingan API uchun amalga oshirilgan adapter. Bilim UZ joriy repozitoriysiga o‘zgartirish kiritilmagan. Mavjud `/api/v2/games/:id` katalog marshruti bilan to‘qnashuvni oldini olish uchun quyidagi exact endpointlar katalog routeridan OLDIN mount qilinadi. Yakuniy API response formatini Bilim UZ dasturchisi tasdiqlashi kerak.

## Mavjud Workerga qo‘shish

`integrations/bilimuz/engine.mjs` va `game-api.mjs` ni Bilim UZ loyihasiga ko‘chiring. Hono entrypoint ichida `handleGameApi(c.req.raw,c.env)` ni chaqiring. Faqat u Response qaytarganda javobni qaytaring, `null` bo‘lsa mavjud routingni davom ettiring. Middleware'ning global auth, CSRF va rate limit bilan mosligini tekshiring. Player sessiyasida Bilim UZ login tokeni shart emas; o‘yin tokeni tekshiriladi. Host katalogdan ochilganda Bilim UZ teacher/owner hisobini mavjud auth orqali tekshirish zarur (learner tipidagi teacher scope hisoblarini rad eting). `issueLaunchToken(env, principal)` faqat tekshirilgan o‘qituvchi/owner uchun chaqiriladi. 5 daqiqalik tokenni `Game URL#launch=TOKEN` shaklida uzating; fragment HTTP so‘roviga tushmaydi va client uni olib tashlaydi. Plain katalog URL faqat Join uchun yetarli, Host uchun launch handoff kerak.

Worker entrypointdan `export { GameRoom } from './game-api.mjs'` eksport qilinadi (haqiqiy pathga moslang). `wrangler.jsonc` da har bir kerakli environment uchun `durable_objects.bindings` ichida `{ "name":"GAME_ROOMS", "class_name":"GameRoom" }` va yangi noyob migration tag bilan `new_sqlite_classes: ["GameRoom"]` qo‘shiladi. Mavjud `DB` D1 binding saqlanadi. `GAME_ALLOWED_ORIGINS` = GitHub Pages origin (repository path emas); `GAME_CATALOG_ID` = Owner Tool'da kiritilgan o‘yin yozuvining ID'si. `GAME_LAUNCH_SECRET` = 32+ belgili tasodifiy maxfiy Worker secret. Frontendga secret joylanmaydi. `GAME_CATALOG_ID` katalogdagi `active=1` bo‘lgandagina yangi session/join va katalog metadata ruxsat etadi; faol xonalar yakunlanishi mumkin.

Mavjud Bilim UZ rate limiting vositasini ushbu marshrutlarda qo‘llang (ayniqsa join/create/launch). Host launch token replay limit, IP/user kvotalar, revocation policy, CORS preflight, body-size, D1 yuklama va maxfiy savol ruxsatlarini production auditda qo‘shimcha sinang. Bu module standalone universal SDK serverini emas, TUG ARENA uchun v2 contract implementatsiyasini beradi.

## Endpointlar

Authorization: `Bearer <launch-token>` — metadata/create. `Bearer <session-token>` — state/question/answer/control/result. Join faqat xona kodi, ism-familiya, personaj va jamoa bilan. OPTIONS ruxsat etilgan origin uchun.

| Method | Path (`/api/v2/games/` ostida) | Kirish / javob |
|---|---|---|
| GET | subjects | `{items:string[]}` |
| GET | topics?subject=... | `{items:string[]}` |
| GET | questions/count?subject=...&topic=...&difficulty=... | `{count:number}` |
| POST | session/create | `{gameId:"tug-arena",rules:{subject,topic,difficulty,count,questionSeconds,teamSize,matchSeconds,winMode,threshold,blueName,redName}}` → `{code,token,state}` |
| POST | session/join | `{code,name,character,team}` → `{code,token,playerId,state}` |
| GET | session/state?code=... | `{state}` — qo‘shimcha sync endpoint |
| GET | session/question?code=... | `{state}` — state.question faqat Player uchun |
| POST | session/answer | `{code,questionId,index,optionIds,requestId}` → `{feedback,state}` |
| POST | session/control | `{code,action:"start"|"kick"|"cancel",playerId?}` → `{state}` — qo‘shimcha Host endpoint |
| GET | session/result?code=... | `{state}` — yakuniy podium |

`state`: phase, rules, serverTime, revision, startsAt, endsAt, score.blue/red, rope (-1..1), players, me, question, lastEvent, winner, podium. `question` hech qachon `correct` ni o‘z ichiga olmaydi. Javob tekshiruvi faqat serverda.

## Savollar manbasi

Adapter joriy schema asosida `store_items` jadvalidagi `status='approved'` va `public_content_json.question` ni o‘qiydi. `category`, `topic`, `level` filtrlari, `kind` single/multiple/truefalse/code va options ID lar ishlatiladi. Maxfiy o‘qituvchi savollari hozircha umuman olinmaydi. Keyinchalik tenant scope va ownership tasdiqlangan grant orqali qo‘shilishi mumkin. 5000 qatorlik query cap mavjud: yirik bankda aniq COUNT, DISTINCT va server-side sampling/pagination bilan almashtiring. Media URLs uchun auth va CORS test talab qilinadi. Har bir matchda savollar snapshot qilinadi. DO storage JSON bo‘laklarga ajratiladi va player queue savol ID/order orqali kompakt saqlanadi.

## Reliz bloklovchilari

1. Bilim UZ Game API 08-bosqichini haqiqiy repositoryga integratsiya qilish, final API contractni tasdiqlash.
2. Bilim UZ authentication handoff va Game Manager active ID, CORS, rate limits va tenant scope audit.
3. Haqiqiy D1 ma'lumotlari va Cloudflare DO'da 40 real client yuklama, request quota / billing sinovi.
4. Visual browser QA: PC, proyektor, Android/iOS; real sprites rope grip va FPS tekshiruvi.
5. Sprite va GLB tarqatish huquqini loyiha egasi tasdiqlashi; audio manbalar hujjatlari paket ichida saqlangan.
