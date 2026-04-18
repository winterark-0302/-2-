import re

file_path = r"c:\Users\winte\OneDrive\Desktop\파이널2조\SafeK_Summer_Workspace\docs\SafeK_Mockup.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Add missing translations
additions = {
    '한국어': {
        'Culture & Indoor': '문화 & 실내', 'Shopping > Mall': '쇼핑 > 복합몰',
        'Store > CS': '상점 > 편의점', 'Culture > Museum': '문화 > 박물관/미술관',
        'Indoor Facility': '실내 시설', 'High AC': '강력 냉방', 'Indoor': '실내',
        'L1 (Very Low)': 'L1 (매우 여유)', 'L1 (Comfortable)': 'L1 (쾌적)', 'L2 (Low)': 'L2 (여유)',
        'm away': 'm 거리', 'km': 'km', 'Routing to': '경로 안내:',
        'Search Result': '검색 결과', 'm': 'm'
    },
    '中文': {
        'Culture & Indoor': '文化 & 室内', 'Shopping > Mall': '购物 > 商场',
        'Store > CS': '商店 > 便利店', 'Culture > Museum': '文化 > 博物馆',
        'Indoor Facility': '室内设施', 'High AC': '强冷气', 'Indoor': '室内',
        'L1 (Very Low)': 'L1 (非常空闲)', 'L1 (Comfortable)': 'L1 (舒适)', 'L2 (Low)': 'L2 (较低拥堵)',
        'm away': 'm 距离', 'km': 'km', 'Routing to': '导航至:',
        'Search Result': '搜索结果', 'm': 'm'
    },
    '日本語': {
        'Culture & Indoor': '文化 & 屋内', 'Shopping > Mall': 'ショッピング > モール',
        'Store > CS': 'ショップ > コンビニ', 'Culture > Museum': '文化 > 博物館',
        'Indoor Facility': '屋内施設', 'High AC': '冷房完備', 'Indoor': '屋内',
        'L1 (Very Low)': 'L1 (非常に空いている)', 'L1 (Comfortable)': 'L1 (快適)', 'L2 (Low)': 'L2 (空いている)',
        'm away': 'm 先', 'km': 'km', 'Routing to': 'ルート案内:',
        'Search Result': '検索結果', 'm': 'm'
    }
}

for lang, items in additions.items():
    new_entries = ", " + ", ".join([f"'{k}': '{v}'" for k, v in items.items()])
    # Safely inject the new key-values into the existing dictionaries inside selectLanguage block
    pattern = rf"('{lang}': \{{\s*.*?)(}})"
    html = re.sub(pattern, lambda m: m.group(1) + new_entries + "\n            " + m.group(2), html, flags=re.DOTALL)


# Fix the javascript templates to split variables and static words, making them friendly to the TextNode translator
html = html.replace("showToast(`Routing to ${place.place_name}...`);", "showToast(t('Routing to') + ' ' + place.place_name + '...');")

html = html.replace("const distDist = place.distance ? (place.distance / 1000).toFixed(1) + ' km' : '';",
                    "const distParam = place.distance ? (place.distance / 1000).toFixed(1) : '';")

html = html.replace('<div class="stat-item"><i class="fa-solid fa-person-walking"></i> ${distDist}</div>',
                    '<div class="stat-item"><i class="fa-solid fa-person-walking"></i> <span>${distParam}</span> <span style="margin-left: 2px;">km</span></div>')

html = html.replace('<div class="facility-dist" style="color:var(--primary);"><i class="fa-solid fa-location-arrow"></i> ${place.distance}m away</div>',
                    '<div class="facility-dist" style="color:var(--primary);"><i class="fa-solid fa-location-arrow"></i> <span>${place.distance}</span> <span>m away</span></div>')

# Force map distance text replacement logic
html = html.replace("document.getElementById('mapInfoDist').innerText = dist;",
                    "document.getElementById('mapInfoDist').innerHTML = `<span>${parseFloat(dist) || ''}</span> <span>m</span>`;")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
