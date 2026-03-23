import ctypes
import ctypes.wintypes
import tkinter as tk
from tkinter import ttk
import sys

WDA_NONE = 0x00000000
WDA_EXCLUDEFROMCAPTURE = 0x00000011

user32 = ctypes.windll.user32
SetWindowDisplayAffinity = user32.SetWindowDisplayAffinity
SetWindowDisplayAffinity.argtypes = [ctypes.wintypes.HWND, ctypes.wintypes.DWORD]
SetWindowDisplayAffinity.restype = ctypes.wintypes.BOOL


def get_hwnd(root: tk.Tk) -> int:
    """tkinter 윈도우의 Win32 HWND 핸들을 가져온다."""
    return ctypes.windll.user32.GetParent(root.winfo_id())


def set_capture_protection(hwnd: int, enabled: bool) -> bool:
    flag = WDA_EXCLUDEFROMCAPTURE if enabled else WDA_NONE
    result = SetWindowDisplayAffinity(hwnd, flag)
    return result != 0


class AntiCaptureApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Anti-Capture")
        self.root.geometry("420x320")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.protected = False
        self.hwnd = None

        self._build_ui()
        self.root.after(100, self._apply_protection)

    def _build_ui(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Title.TLabel",
                        font=("Segoe UI", 18, "bold"),
                        foreground="#cdd6f4",
                        background="#1e1e2e")

        style.configure("Status.TLabel",
                        font=("Segoe UI", 11),
                        foreground="#a6adc8",
                        background="#1e1e2e")

        style.configure("Info.TLabel",
                        font=("Segoe UI", 9),
                        foreground="#6c7086",
                        background="#1e1e2e")

        style.configure("Toggle.TButton",
                        font=("Segoe UI", 12, "bold"),
                        padding=(20, 12))

        main_frame = tk.Frame(self.root, bg="#1e1e2e")
        main_frame.pack(expand=True, fill="both", padx=30, pady=25)

        ttk.Label(main_frame, text="Anti-Capture", style="Title.TLabel").pack(pady=(0, 5))

        ttk.Label(main_frame,
                  text="화면 캡처 · 디스코드 방송에서 숨김",
                  style="Info.TLabel").pack(pady=(0, 20))

        self.status_label = ttk.Label(main_frame, style="Status.TLabel")
        self.status_label.pack(pady=(0, 20))

        self.toggle_btn = tk.Button(
            main_frame,
            font=("Segoe UI", 12, "bold"),
            width=22,
            height=2,
            cursor="hand2",
            bd=0,
            relief="flat",
            activeforeground="#ffffff",
            command=self._toggle_protection
        )
        self.toggle_btn.pack(pady=(0, 20))

        sep = tk.Frame(main_frame, height=1, bg="#313244")
        sep.pack(fill="x", pady=(5, 10))

        ttk.Label(main_frame,
                  text="Windows 10 2004+ (빌드 19041) 이상 필요",
                  style="Info.TLabel").pack()

        self._update_ui()

    def _update_ui(self):
        if self.protected:
            self.status_label.configure(text="보호 상태: ON — 캡처에서 숨겨짐")
            self.toggle_btn.configure(
                text="보호 해제하기",
                bg="#f38ba8",
                fg="#1e1e2e",
                activebackground="#eba0ac"
            )
        else:
            self.status_label.configure(text="보호 상태: OFF — 캡처에 보임")
            self.toggle_btn.configure(
                text="보호 활성화하기",
                bg="#a6e3a1",
                fg="#1e1e2e",
                activebackground="#b4f0ae"
            )

    def _apply_protection(self):
        """앱 시작 시 자동으로 보호를 켠다."""
        self.hwnd = get_hwnd(self.root)
        if self.hwnd:
            success = set_capture_protection(self.hwnd, True)
            if success:
                self.protected = True
                self._update_ui()
            else:
                self.status_label.configure(
                    text="오류: 이 Windows 버전에서는 지원되지 않습니다"
                )

    def _toggle_protection(self):
        if self.hwnd is None:
            return

        new_state = not self.protected
        success = set_capture_protection(self.hwnd, new_state)

        if success:
            self.protected = new_state
            self._update_ui()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    if sys.platform != "win32":
        print("이 프로그램은 Windows에서만 동작합니다.")
        sys.exit(1)

    app = AntiCaptureApp()
    app.run()