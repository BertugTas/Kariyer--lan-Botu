from playwright.sync_api import sync_playwright

def run_playwright_kariyer_bot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Tarayıcı görünür çalışsın
        page = browser.new_page()

        # Senin verdiğin özel filtrelenmiş link
        url = "https://www.kariyer.net/is-ilanlari/mersin-kimya+ogretmeni?ct=33&pst=2354&pkw=kimya%20%C3%B6%C4%9Fretmeni"
        page.goto(url)

        # Sayfanın tamamen yüklenmesini bekle (8 saniye)
        page.wait_for_timeout(8000)

        # İlan linklerini XPath ile seç (en sağlam yöntem)
        ilanlar = page.locator('//a[contains(@href, "/is-ilani/")]').all()

        print("\n🔍 Bulunan ilanlar:")
        if not ilanlar:
            print("❌ Hiç ilan bulunamadı.")
        for ilan in ilanlar:
            baslik = ilan.inner_text().strip()
            link = ilan.get_attribute("href")
            if link:
                print(f"\n🧪 {baslik}")
                print(f"🔗 https://www.kariyer.net{link}")

        browser.close()

run_playwright_kariyer_bot()
