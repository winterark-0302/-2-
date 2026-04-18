import os

# Define paths
base_dir = r"c:\Users\winte\OneDrive\Desktop\파이널2조\SafeK_Summer_Workspace\docs"
src_file = os.path.join(base_dir, "SafeK_Mockup.html")
dest_file = os.path.join(base_dir, "SafeK_Demo_Mockup.html")

# Read original
with open(src_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Add demo rehearsal styles before </style>
demo_styles = """
        /* Demo Rehearsal Layout */
        body {
            flex-direction: row !important;
            gap: 40px;
            align-items: flex-start !important;
            padding-top: 50px !important;
            background-color: #e2e8f0;
        }
        .demo-panel {
            width: 400px;
            background: white;
            padding: 30px;
            border-radius: 24px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            font-family: 'Noto Sans KR', sans-serif;
            height: 844px;
            display: flex;
            flex-direction: column;
        }
        .demo-panel h2 {
            font-size: 1.5rem;
            color: #1e293b;
            margin-bottom: 20px;
            border-bottom: 2px solid #cbd5e1;
            padding-bottom: 10px;
        }
        .demo-step {
            padding: 15px;
            border-radius: 12px;
            background: #f8fafc;
            margin-bottom: 15px;
            border: 1px solid #e2e8f0;
            cursor: pointer;
            transition: all 0.2s;
        }
        .demo-step:hover {
            border-color: #4F46E5;
            transform: translateX(5px);
        }
        .demo-step.active {
            background: #e0e7ff;
            border-color: #4F46E5;
        }
        .step-title {
            font-weight: 700;
            color: #4F46E5;
            margin-bottom: 5px;
            font-size: 1.1rem;
        }
        .step-desc {
            font-size: 0.9rem;
            color: #475569;
        }
"""
html = html.replace('</style>', demo_styles + '\n    </style>')

# Replace title
html = html.replace('<title>SafeK Summer - Interactive Mockup</title>', '<title>SafeK UX/UI 시연 리허설 데모</title>')

# Inject demo panel before the device-container
demo_panel = """
    <div class="demo-panel">
        <h2>SafeK 시연 시나리오</h2>
        <div class="demo-step active" onclick="activateStep(this); setDemoTab('home')">
            <div class="step-title">1. 홈 화면 (Home)</div>
            <div class="step-desc">실시간 기상 경보 확인 및 '무더위 쉼터 찾기' 배너를 클릭하여 지도 화면으로 이동합니다. 실내 대안 장소 스와이프를 보여줍니다.</div>
        </div>
        <div class="demo-step" onclick="activateStep(this); setDemoTab('map')">
            <div class="step-title">2. 지도 탐색 (Map)</div>
            <div class="step-desc">주변 대피소 및 쉼터 마커를 탭하여 하단 정보창을 확인하고 '길찾기' 버튼을 눌러 카카오맵 연동을 시연합니다.</div>
        </div>
        <div class="demo-step" onclick="activateStep(this); setDemoTab('course')">
            <div class="step-title">3. 안전 코스 추천 (Course)</div>
            <div class="step-desc">AI가 추천하는 실내 중심, 덜 혼잡한(Low Congestion) 코스 리스트를 확인하고 카드를 탭하여 경로를 시연합니다.</div>
        </div>
        <div class="demo-step" onclick="activateStep(this); setDemoTab('my')">
            <div class="step-title">4. 마이페이지 (My Page) & 다국어</div>
            <div class="step-desc">다국어 아이콘을 클릭하여 'English'에서 '한국어' 또는 '日本語'로 언어 변경을 시연하여 인바운드 외국인 대상 기능을 강조합니다.</div>
        </div>
        <div class="demo-step" onclick="activateStep(this); triggerSOS()">
            <div class="step-title">5. 긴급 SOS 기능</div>
            <div class="step-desc">플로팅 SOS 버튼을 클릭하여 다이얼 모달이 뜨는 것을 보여주고 직관적인 비상 호출 기능을 시연합니다.</div>
        </div>
    </div>
"""

html = html.replace('<div class="device-container">', demo_panel + '\n    <div class="device-container">')

# Add activation scripts
demo_scripts = """
        // Demo Rehearsal Scripts
        function activateStep(el) {
            document.querySelectorAll('.demo-step').forEach(step => step.classList.remove('active'));
            el.classList.add('active');
        }
        function setDemoTab(tab) {
            switchTab(tab);
        }
        function triggerSOS() {
            document.getElementById('sosBtn').click();
        }
"""
html = html.replace('// Execute on load', demo_scripts + '\n        // Execute on load')

with open(dest_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Demo mockup created at:", dest_file)
