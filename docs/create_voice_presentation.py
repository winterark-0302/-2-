import os
from gtts import gTTS
from moviepy import AudioFileClip, ImageClip, VideoFileClip, concatenate_videoclips, ImageSequenceClip, CompositeAudioClip
from PIL import Image
import numpy as np

# Configuration
ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
OUTPUT_FILE = os.path.join(ASSETS_DIR, 'SafeK_Presentation_Pure.mp4')

# Image and Video file paths
HOME_IMG = os.path.join(ASSETS_DIR, 'safek_home_dashboard_1776256169276.png')
SOS_IMG = os.path.join(ASSETS_DIR, 'safek_sos_interface_1776256186488.png')
ROUTE_IMG = os.path.join(ASSETS_DIR, 'safek_route_map_1776256206542.png')
DEMO_WEBP = os.path.join(ASSETS_DIR, 'safek_pure_mockup_demo.webp')

# Slide Scripts (TTS Text)
scripts = [
    {
        "text": "안녕하세요. SafeK 애플리케이션의 홈 화면입니다. 상단에 가장 시급한 기상 특보가 보이고, 안전 지대를 요약해 보여줍니다.",
        "media": HOME_IMG,
        "type": "image"
    },
    {
        "text": "이 화면은 긴급 상황 인터페이스입니다. 국적 설정과 함께 커다란 붉은 버튼을 한 번만 눌러 구조 요청과 실시간 GPS 좌표를 송출합니다.",
        "media": SOS_IMG,
        "type": "image"
    },
    {
        "text": "안전 라우팅 맵 기능입니다. 인공지능이 침수 등 특정 위험 구역을 피해가는 안전한 거리를 푸른 색상으로 추천해 줍니다.",
        "media": ROUTE_IMG,
        "type": "image"
    },
    {
        "text_sync": [
            {"t": "이제 실제 동작하는 퓨어 버전의 앱 데모 시연을 보시겠습니다.", "start": 0},
            {"t": "홈 화면의 날씨 특보를 바탕으로, 가까운 대피소를 검색하며 시연이 시작됩니다.", "start": 10},
            {"t": "이어서 지도를 확인하고, 코스 탭을 통해 AI가 추천하는 안전한 실내 경로를 탐색합니다.", "start": 21},
            {"t": "마이 탭에서는 인바운드 관광객을 위한 다국어 인터페이스 변환 기능을 시연하게 됩니다.", "start": 32},
            {"t": "마지막으로 위급 상황 시, 즉각적인 SOS 버튼 호출로 구조 요청을 진행하는 과정을 보여줍니다.", "start": 44}
        ],
        "media": DEMO_WEBP,
        "type": "video"
    }
]

def generate_tts_audio(text, idx):
    audio_path = os.path.join(ASSETS_DIR, f'slide_{idx}.mp3')
    tts = gTTS(text=text, lang='ko', slow=False)
    tts.save(audio_path)
    return audio_path

def create_video():
    clips = []
    audio_files = []
    
    print("Starting video rendering process...")
    for i, slide in enumerate(scripts):
        print(f"Processing slide {i+1}...")
        
        if "text_sync" in slide:
            sync_clips = []
            max_audio_end = 0
            for j, sync_data in enumerate(slide["text_sync"]):
                ap = generate_tts_audio(sync_data["t"], f"{i}_{j}")
                audio_files.append(ap)
                ac = AudioFileClip(ap).with_start(sync_data["start"])
                sync_clips.append(ac)
                end = sync_data["start"] + ac.duration
                if end > max_audio_end: max_audio_end = end
                
            audio_clip = CompositeAudioClip(sync_clips)
            duration = max_audio_end + 1.0 # 1 sec buffer
        else:
            audio_path = generate_tts_audio(slide["text"], i)
            audio_files.append(audio_path)
            audio_clip = AudioFileClip(audio_path)
            duration = audio_clip.duration + 0.5  # Add 0.5 sec pause

        
        print(f"Processing media for slide {i+1}...")
        if slide["type"] == "image":
            # Some PNGs might need resizing to common dimensions, e.g., 1080p
            visual_clip = ImageClip(slide["media"]).with_duration(duration)
            visual_clip = visual_clip.resized(height=1080)
            w, h = visual_clip.size
            if w % 2 != 0:
                visual_clip = visual_clip.resized(width=w-1, height=1080)
            
            # center crop or pad if necessary, basic behavior is fine
        else:
            # It's the webp animated image, handled as VideoFileClip
            # Handle animated WebP using Pillow
            img = Image.open(slide["media"])
            frames = []
            try:
                while True:
                    # Convert to RGB array
                    frame_rgb = img.convert('RGB')
                    frames.append(np.array(frame_rgb))
                    img.seek(img.tell() + 1)
            except EOFError:
                pass
            
            if frames:
                visual_clip = ImageSequenceClip(frames, fps=10) # WebP usually 10-15fps
            else:
                visual_clip = ImageClip(slide["media"]).with_duration(10)
            
            vid_dur = visual_clip.duration if visual_clip.duration else 15
            final_dur = max(duration, vid_dur)
            
            # If we need to extend it, loop it:
            if vid_dur < final_dur:
                # To loop a video in moviepy v1:
                # visual_clip = visual_clip.fx(vfx.loop, duration=final_dur) # alternative
                import math
                num_loops = math.ceil(final_dur / vid_dur)
                looped_clips = [visual_clip] * num_loops
                visual_clip = concatenate_videoclips(looped_clips).with_duration(final_dur)
            else:
                visual_clip = visual_clip.with_duration(final_dur)
            
            visual_clip = visual_clip.resized(height=1080)
            w, h = visual_clip.size
            if w % 2 != 0:
                visual_clip = visual_clip.resized(width=w-1, height=1080)
            duration = final_dur

        # Optional: Add crossfade using crossfadein etc if we used concatenate_videoclips(method="compose")
        # For simplicity, just append.
        visual_clip = visual_clip.with_audio(audio_clip)
        clips.append(visual_clip)
        
    print("Concatenating clips...")
    # use method="compose" to handle different resolution sizes automatically
    final_video = concatenate_videoclips(clips, method="compose")
    fw, fh = final_video.size
    if fw % 2 != 0 or fh % 2 != 0:
        final_video = final_video.cropped(x1=0, y1=0, width=fw-(fw%2), height=fh-(fh%2))
    
    print(f"Exporting MP4 to {OUTPUT_FILE}...")
    final_video.write_videofile(
        OUTPUT_FILE, 
        fps=24, 
        codec='libx264', 
        audio_codec='aac',
        temp_audiofile=os.path.join(ASSETS_DIR, 'temp-audio.m4a'),
        remove_temp=True,
        ffmpeg_params=["-pix_fmt", "yuv420p"]
    )
    
    # Cleanup audio temp files
    print("Cleaning up MP3s...")
    for af in audio_files:
        try:
            os.remove(af)
        except:
            pass
            
    print("Export complete!")

if __name__ == "__main__":
    create_video()
