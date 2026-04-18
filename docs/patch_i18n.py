import re

file_path = r"c:\Users\winte\OneDrive\Desktop\파이널2조\SafeK_Summer_Workspace\docs\SafeK_Mockup.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

new_js = """
        const translations = {
            '한국어': {
                'Home': '홈', 'Map': '지도', 'Course': '안전 코스', 'My': '내 정보', 'Ops': '운영(Ops)',
                'System Ops': '시스템 모니터링', 'LIVE': '실시간', 'CPU Usage': 'CPU 사용량', 'Active Users': '활성 사용자',
                'Traffic Metrics (Req/s)': '트래픽(Req/s)', 'Database Health': '데이터베이스 상태', 'Good': '양호',
                'Indoor Alternatives': '실내 대체 장소', 'Nearby Facilities': '인근 시설',
                'AI Recommended Safe Routes': 'AI 추천 안전 경로', 'Emergency SOS': '긴급 SOS',
                'Language': '언어 설정', 'Saved Courses': '저장된 코스', 'Emergency Contacts': '비상 연락망', 'Notifications': '알림',
                'Language Settings': '언어 설정', 'Select your preferred language.': '선호하는 언어를 선택해주세요.',
                'Are you experiencing a medical emergency or heatstroke? Connect to English-speaking emergency services immediately.': '의료 응급 상황이나 일사병을 겪고 계신가요? 한국어 구급 서비스에 즉시 연결됩니다.',
                'Call 119': '119 긴급 전화 연결', 'Cancel': '취소', 'Close': '닫기',
                'Your recently saved safe routes:': '최근 저장하신 안전 경로입니다:',
                'Search facilities...': '시설 검색...', 'Find Cooling Shelter': '무더위 쉼터 경로 찾기',
                'Filtered by current weather and transport congestion levels.': '현재 날씨와 교통 혼잡도를 기준으로 맞춰진 정보입니다.',
                'Indoor Only': '실내 시설 우선', 'Low Congestion': '혼잡도 낮음 우선',
                'Selected Area': '선택된 구역', 'Tap markers on the map': '지도에서 마커를 탭하세요',
                'Navigate Here': '경로 안내 시작', 'See all': '모두 보기',
                'Fetching real-time local weather data...': '실시간 날씨 데이터를 가져오는 중...',
                'Loading Weather': '지역 날씨 준비 중',
                'Extreme Heat Warning': '폭염 경보 발령', 'Heat Advisory': '폭염 주의보', 'Safe Weather': '정상 날씨',
                'High risk of heatstroke today. Indoor activities strongly advised.': '일사병 위험이 높습니다. 가급적 실내에서 활동해 주십시오.',
                "It's getting hot. Remember to stay hydrated.": '온도가 매우 높습니다. 충분한 수분을 섭취해 주십시오.',
                "Current local weather is relatively safe.": '현재 지역 날씨는 상대적으로 안전합니다.'
            },
            '中文': {
                'Home': '首页', 'Map': '地图', 'Course': '路线', 'My': '我的', 'Ops': '系统运维',
                'System Ops': '系统操作', 'LIVE': '实况', 'CPU Usage': 'CPU 使用率', 'Active Users': '活跃用户',
                'Traffic Metrics (Req/s)': '流量指标', 'Database Health': '数据库健康状态', 'Good': '良好',
                'Indoor Alternatives': '室内替代场所', 'Nearby Facilities': '附近设施',
                'AI Recommended Safe Routes': 'AI推荐的安全路线', 'Emergency SOS': '紧急求救 SOS',
                'Language': '语言设置', 'Saved Courses': '已保存的路线', 'Emergency Contacts': '紧急联系人', 'Notifications': '通知',
                'Language Settings': '语言设置', 'Select your preferred language.': '请选择您偏好的语言。',
                'Are you experiencing a medical emergency or heatstroke? Connect to English-speaking emergency services immediately.': '您遇到医疗紧急情况或中暑了吗？立即联系紧急服务中心。',
                'Call 119': '拨打 119 紧急电话', 'Cancel': '取消', 'Close': '关闭',
                'Your recently saved safe routes:': '您最近保存的安全路线：',
                'Search facilities...': '搜索设施...', 'Find Cooling Shelter': '寻找避暑中心',
                'Filtered by current weather and transport congestion levels.': '根据当前天气和交通拥堵程度筛选。',
                'Indoor Only': '仅限室内', 'Low Congestion': '低拥堵优先',
                'Selected Area': '所选区域', 'Tap markers on the map': '点击地图上的标记',
                'Navigate Here': '导航到这里', 'See all': '查看全部',
                'Fetching real-time local weather data...': '正在获取实时当地天气数据...',
                'Loading Weather': '正在加载天气',
                'Extreme Heat Warning': '极端高温警告', 'Heat Advisory': '高温提示', 'Safe Weather': '安全天气',
                'High risk of heatstroke today. Indoor activities strongly advised.': '今天中暑风险很高。强烈建议在室内活动。',
                "It's getting hot. Remember to stay hydrated.": '天气变热了。记得多喝水。',
                "Current local weather is relatively safe.": '目前当地天气相对安全。'
            },
            '日本語': {
                'Home': 'ホーム', 'Map': 'マップ', 'Course': 'コース', 'My': 'マイ', 'Ops': '監視',
                'System Ops': 'システム管理', 'LIVE': 'ライブ表示', 'CPU Usage': 'CPU 使用率', 'Active Users': 'アクティブユーザー',
                'Traffic Metrics (Req/s)': 'トラフィック指標', 'Database Health': 'DB 正常性', 'Good': '良好',
                'Indoor Alternatives': '屋内の代わりになる場所', 'Nearby Facilities': '周辺の施設',
                'AI Recommended Safe Routes': 'AI推奨の安全ルート', 'Emergency SOS': '緊急 SOS',
                'Language': '言語設定', 'Saved Courses': '保存済みコース', 'Emergency Contacts': '緊急連絡先', 'Notifications': '通知設定',
                'Language Settings': '言語設定', 'Select your preferred language.': '希望の言語を選択してください。',
                'Are you experiencing a medical emergency or heatstroke? Connect to English-speaking emergency services immediately.': '熱中症などの医療上の緊急事態ですか？すぐに119番通報します。',
                'Call 119': '119 番通報', 'Cancel': 'キャンセル', 'Close': '閉じる',
                'Your recently saved safe routes:': '最近保存した安全ルート：',
                'Search facilities...': '施設を検索...', 'Find Cooling Shelter': '避暑地を見つける',
                'Filtered by current weather and transport congestion levels.': '現在の天候と交通渋滞レベルによってフィルタリングされています。',
                'Indoor Only': '屋内重視', 'Low Congestion': '低混雑',
                'Selected Area': '選択エリア', 'Tap markers on the map': 'マップのマーカーをタップ',
                'Navigate Here': 'ここへナビゲート', 'See all': 'すべて見る',
                'Fetching real-time local weather data...': '現地の天気データを取得中...',
                'Loading Weather': '天気データロード中',
                'Extreme Heat Warning': '猛暑警報', 'Heat Advisory': '高温注意報', 'Safe Weather': '安全な天気',
                'High risk of heatstroke today. Indoor activities strongly advised.': '本日は熱中症の危険が高いため、屋内での活動を強くお勧めします。',
                "It's getting hot. Remember to stay hydrated.": '暑くなってきました。水分補給を心がけてください。',
                "Current local weather is relatively safe.": '現在の現地の天候は比較的安全です。'
            }
        };

        window.currentGlobalLang = 'English';

        // Translate helper function
        function t(text) {
            if (window.currentGlobalLang === 'English') return text;
            const dict = translations[window.currentGlobalLang];
            if (!dict) return text;
            
            // Allow translating strings that might have variables by matching keys explicitly 
            // e.g. "Seoul, Gangnam" - skipped if not in dict
            
            return dict[text.trim()] || text;
        }

        // Deep DOM traversal to replace strings safely
        function applyTranslationsToDOM(lang, node) {
            if (node.nodeType === 3) {
                const text = (node._originalEnglish || node.nodeValue).trim();
                if (text && translations['한국어'][text] !== undefined) {
                    if (!node._originalEnglish) {
                         node._originalEnglish = text;
                    }
                    const translated = (lang === 'English') ? text : translations[lang][text] || text;
                    node.nodeValue = node.nodeValue.replace(node.nodeValue.trim(), translated);
                }
            } else if (node.nodeType === 1 && node.tagName !== 'SCRIPT' && node.tagName !== 'STYLE' && node.id !== 'activeLangText') {
                if (node.tagName === 'INPUT' && node.placeholder) {
                    const ph = (node._originalPlaceholder || node.placeholder).trim();
                    if (translations['한국어'][ph] !== undefined) {
                         if (!node._originalPlaceholder) node._originalPlaceholder = ph;
                         node.placeholder = (lang === 'English') ? ph : translations[lang][ph] || ph;
                    }
                }
                for (let child of node.childNodes) {
                    applyTranslationsToDOM(lang, child);
                }
            }
        }

        function selectLanguage(lang) {
            document.getElementById('activeLangText').textContent = lang;
            closeLangModal();
            window.currentGlobalLang = lang;
            
            // Translate the entire DOM body text nodes dynamically
            applyTranslationsToDOM(lang, document.body);

            // Need to forcefully rewrite dynamic sections that might have been dynamically altered
            // E.g. we can just dispatch a custom event if we want, or call fetching logic again.
            // But applyTranslationsToDOM works for whatever is currently on screen!
            
            showToast(lang === '한국어' ? '언어가 변경되었습니다' : (lang === '日本語' ? '言語が変更されました' : (lang === '中文' ? '语言已更改' : 'Language applied!')));
        }
"""

old_pattern = r'const dict = \{.*?\n            showToast\(`\$\{lang\} 적용 완료!`\);\n        \}'
html = re.sub(r'function selectLanguage\(lang\) \{.*?\n        \}\n', new_js + '\n', html, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
