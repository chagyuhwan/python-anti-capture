# 👻 GhostWindow (Anti-Capture Tool)

**GhostWindow**는 Windows의 `SetWindowDisplayAffinity` API를 활용하여, 특정 윈도우 창이 화면 캡처 도구나 스트리밍 프로그램(디스코드, OBS, Zoom 등)에 노출되지 않도록 보호하는 Python 프로그램입니다.

보안이 필요한 정보나 개인적인 데이터를 다루는 UI를 개발할 때 유용하게 활용할 수 있습니다.

---

## ✨ 주요 기능
- **실시간 캡처 방지:** 활성화 시 캡처 도구, 녹화 프로그램에서 창이 검게 표시되거나 투명하게 제외됩니다.
- **디스코드/OBS 대응:** 화면 공유나 방송 시 해당 창만 감쪽같이 숨길 수 있습니다.
- **심플한 UI:** Tkinter 기반의 깔끔한 다크 모드 인터페이스와 원클릭 토글 버튼을 제공합니다.
- **시스템 연동:** Win32 API(`ctypes`)를 직접 호출하여 가볍고 빠릅니다.

## 🛠 기술 스택
- **Language:** Python 3.x
- **GUI:** Tkinter / ttk
- **API:** Windows User32 (SetWindowDisplayAffinity)

## 📋 요구 사항
- **OS:** Windows 10 버전 2004 (Build 19041) 이상 권장
  - 해당 버전 이상에서 `WDA_EXCLUDEFROMCAPTURE` 상수가 지원됩니다.
- **Platform:** Windows 전용 (`win32`)

## 🚀 시작하기

1. **저장소 클론:**
   ```bash
   git clone [https://github.com/사용자아이디/GhostWindow.git](https://github.com/사용자아이디/GhostWindow.git)
