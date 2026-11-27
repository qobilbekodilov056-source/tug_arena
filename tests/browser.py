import json,urllib.request,subprocess,time,os,re
from pathlib import Path
from playwright.sync_api import sync_playwright,expect
root=Path(__file__).resolve().parents[1]
server=subprocess.Popen(['node','tests/local-api.mjs'],cwd=root,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
try:
 for i in range(30):
  try:
   token=json.load(urllib.request.urlopen('http://127.0.0.1:8765/__qa/launch',timeout=1))['token'];break
  except Exception:time.sleep(.2)
 else:raise RuntimeError('QA server not ready')
 out=root/'docs'/'qa';out.mkdir(exist_ok=True)
 with sync_playwright() as p:
  browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']); errors=[]
  def page(w=1366,h=768):
   page=browser.new_context(viewport={'width':w,'height':h}).new_page();page.on('pageerror',lambda e:errors.append(str(e)));return page
  host=page();host.goto('http://127.0.0.1:8765/#launch='+token);host.screenshot(path=str(out/'menu.png'));host.click('#host');expect(host.locator('#create')).to_be_enabled(timeout=8000)
  host.select_option('#teamSize','1');host.fill('#count','5');host.select_option('#winMode','threshold');host.fill('#threshold','20');host.click('#create');expect(host.locator('.code')).to_be_visible();code=host.locator('.code').inner_text()
  blue=page(1024,768);red=page(412,850)
  for player,name,team,char in [(blue,'Aliyev Sardor','blue','bahodir'),(red,'Karimova Madina','red','malika')]:
   player.goto('http://127.0.0.1:8765/');player.click('#join');player.fill('#code',code);player.fill('#name',name);player.click(f'[data-char="{char}"]');player.click(f'[data-team="{team}"]');player.click('#join-submit');expect(player.locator('#question')).to_be_visible()
  expect(host.locator('#start')).to_be_enabled();host.screenshot(path=str(out/'lobby.png'));host.click('#start');expect(blue.locator('.q-title')).to_be_visible(timeout=10000);expect(red.locator('.q-title')).to_be_visible(timeout=10000);host.wait_for_timeout(300);host.screenshot(path=str(out/'host.png'));blue.screenshot(path=str(out/'player.png'));red.screenshot(path=str(out/'mobile.png'))
  q=blue.locator('.q-title').inner_text();correct=int(re.search(r'\d+',q).group())+3;blue.locator('.answer span').filter(has_text=re.compile('^'+str(correct)+'$')).click();expect(host.locator('.victory-banner')).to_contain_text('G‘OLIB',timeout=8000);expect(host.locator('.place-name')).to_contain_text('Aliyev Sardor');expect(red.locator('.victory-banner')).to_be_visible();host.wait_for_timeout(400);host.screenshot(path=str(out/'victory.png'));assert not errors,errors
  # Confirm independent client reconnect on refresh, including finished result.
  blue.reload();expect(blue.locator('.victory-banner')).to_be_visible(timeout=8000);browser.close()
 print('PASS: three isolated browser contexts; host create, join, countdown, question, answer, threshold, podium, reconnect; zero JS page errors.')
finally:
 server.terminate();server.wait(timeout=5)
