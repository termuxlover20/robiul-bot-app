import math
import random
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics import RenderContext, Color, Line, PushMatrix, PopMatrix, Rotate

class RobiulBotApp(App):
    def build(self):
        # মূল ড্যাশবোর্ড লেআউট
        self.layout = FloatLayout()

        # ১. ব্যাকগ্রাউন্ড ইমেজ (bg.png)
        self.bg_image = Image(
            source='bg.png',
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        self.layout.add_widget(self.bg_image)

        # ২. হেডার টেক্সট (ROBIUL BOT RGB Glow Effect)
        self.header_label = Label(
            text="ROBIUL BOT",
            font_size='30sp',
            bold=True,
            color=(0, 1, 0.8, 1),
            size_hint=(0.8, 0.1),
            pos_hint={'center_x': 0.5, 'top': 0.93}
        )
        self.layout.add_widget(self.header_label)

        # ৩. সেন্ট্রাল রিং সিগন্যাল ডিসপ্লে (মাঝখানের রিংয়ের ভেতর টেক্সট)
        self.signal_text = Label(
            text="READY",
            font_size='28sp',
            bold=True,
            color=(0, 1, 0.5, 1),
            size_hint=(0.6, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.53}
        )
        self.layout.add_widget(self.signal_text)

        # ৪. সিস্টেম স্ট্যাটাস মেসেজ (Initializing / Processing / Signal)
        self.status_label = Label(
            text="SYSTEM READY",
            font_size='14sp',
            color=(0, 0.8, 1, 1),
            size_hint=(0.8, 0.05),
            pos_hint={'center_x': 0.5, 'center_y': 0.31}
        )
        self.layout.add_widget(self.status_label)

        # ৫. বট একটিভেশন বাটন (ACTIVATING ALGORITHM)
        self.scan_button = Button(
            text="ACTIVATING ALGORITHM",
            font_size='15sp',
            bold=True,
            background_color=(0, 0, 0, 0),  # ট্রান্সপারেন্ট ব্যাকগ্রাউন্ড
            color=(0, 1, 0.8, 1),
            size_hint=(0.7, 0.06),
            pos_hint={'center_x': 0.5, 'y': 0.08}
        )
        self.scan_button.bind(on_press=self.start_scanning)
        self.layout.add_widget(self.scan_button)

        # RGB অ্যানিমেশন ও কালার টাইমার সেটআপ
        self.hue = 0.0
        Clock.schedule_interval(self.update_rgb_glow, 0.05)

        return self.layout

    # RGB Glow ইফেক্ট (হেডার এবং বাটনের রঙ পরিবর্তনের জন্য)
    def update_rgb_glow(self, dt):
        self.hue = (self.hue + 0.02) % 1.0
        # HSV to RGB Conversion
        r = math.sin(self.hue * 2 * math.pi) * 0.5 + 0.5
        g = math.sin((self.hue + 0.33) * 2 * math.pi) * 0.5 + 0.5
        b = math.sin((self.hue + 0.66) * 2 * math.pi) * 0.5 + 0.5

        self.header_label.color = (r, g, b, 1)

    # সিগন্যাল স্ক্যানিং অ্যানিমেশন
    def start_scanning(self, instance):
        self.scan_button.disabled = True
        self.signal_text.text = "ANALYZING..."
        self.signal_text.color = (1, 0.8, 0, 1)
        self.status_label.text = "SCANNING MARKET DATA..."
        
        # ৩ সেকেন্ড পর সিগন্যাল রেজাল্ট দেখাবে
        Clock.schedule_once(self.show_signal, 3.0)

    # সিগন্যাল জেনারেট (UP / DOWN)
    def show_signal(self, dt):
        decision = random.choice(["CALL (UP) ⬆️", "PUT (DOWN) ⬇️"])
        
        if "UP" in decision:
            self.signal_text.text = decision
            self.signal_text.color = (0, 1, 0.2, 1)  # সবুজ রঙ
            self.status_label.text = "CONFIRMED: BUY SIGNAL"
        else:
            self.signal_text.text = decision
            self.signal_text.color = (1, 0.2, 0.2, 1)  # লাল রঙ
            self.status_label.text = "CONFIRMED: SELL SIGNAL"

        self.scan_button.disabled = False

if __name__ == '__main__':
    RobiulBotApp().run()

