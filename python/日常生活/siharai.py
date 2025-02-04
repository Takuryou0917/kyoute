import tkinter as tk
from tkinter import simpledialog, messagebox
from tkcalendar import Calendar
import datetime
import json

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("受験・振込カレンダー")

        # ダークモードのテーマ設定
        self.root.configure(bg="#2e2e2e")  # 背景色をダークグレーに設定
        self.text_color = "#ffffff"  # 文字色を白に設定
        self.exam_color = "#00bcd4"  # 受験日文字色（水色）

        # イベントデータの保存場所
        self.data_file = "events_data.json"

        # 初期化
        self.events = {
            "exam": {},  # 受験日情報
            "payment": {},  # 振込日情報
        }

        self.labels_and_buttons = []  # ラベルとボタンを格納するリスト
        self.check_buttons = []  # チェックボックスを格納するリスト
        self.label_delete_buttons = []  # 削除ボタンを格納するリスト

        # データをロード
        self.load_data()

        # UIウィジェットの作成
        self.create_widgets()

    def create_widgets(self):
        # カレンダー表示（1280x720対応 & 大きく）
        self.calendar = Calendar(self.root, selectmode="day", year=2025, month=1, day=1, font=("Arial", 18),background="#3a3a3a", foreground="#ffffff", borderwidth=2,normalbackground="#2e2e2e", normalforeground="#ffffff",headersbackground="#444444", headersforeground="#ffffff",selectbackground="#007acc", selectforeground="#ffffff",weekendbackground="#ff6666")
        self.calendar.grid(row=0, column=0, padx=10, pady=10, rowspan=5, columnspan=3)

        # 受験日を登録するためのボタン
        self.select_exam_button = tk.Button(self.root, text="受験日を登録", command=self.set_exam_date, font=("Arial", 14), bg="#4e4e4e", fg="#ffffff", relief="flat")
        self.select_exam_button.grid(row=6, column=0, padx=10, pady=10)

        # 振込日を登録するためのボタン
        self.select_payment_button = tk.Button(self.root, text="振込日を登録", command=self.set_payment_date, font=("Arial", 14), bg="#4e4e4e", fg="#ffffff", relief="flat")
        self.select_payment_button.grid(row=7, column=0, padx=10, pady=10)

        # 受験日を表示するためのラベル
        self.exam_label = tk.Label(self.root, text="【受験日】", font=("Arial", 14), fg=self.text_color, bg="#2e2e2e")
        self.exam_label.grid(row=0, column=3, pady=10, sticky="w")

        # 振込日を表示するためのラベル
        self.payment_label = tk.Label(self.root, text="【振込日】", font=("Arial", 14), fg=self.text_color, bg="#2e2e2e")
        self.payment_label.grid(row=6, column=3, pady=10, sticky="w")

        # 再ロードボタン
        self.reload_button = tk.Button(self.root, text="再ロード", command=self.reload_data, font=("Arial", 12), bg="#ff6600", fg="#ffffff", relief="flat")
        self.reload_button.grid(row=8, column=0, padx=10, pady=10)

        # イベントを日付順に表示
        self.update_event_list()

        # ウィンドウサイズを1280x720に設定
        self.root.geometry("1280x720")

    def set_payment_date(self):
        """振込日を登録するための処理"""
        selected_date = self.calendar.get_date()  # 'yyyy-mm-dd'形式で取得
        school_name = simpledialog.askstring("学校名", "振込する学校名を入力してください:", parent=self.root)

        if school_name:
            try:
                # 日付の形式をチェック
                payment_date = datetime.datetime.strptime(selected_date, "%Y-%m-%d").date()
            except ValueError:
                try:
                    # スラッシュ区切りの日付にも対応
                    payment_date = datetime.datetime.strptime(selected_date, "%Y/%m/%d").date()
                except ValueError:
                    # 両方の形式でも無効ならエラーメッセージ
                    messagebox.showerror("エラー", "無効な日付形式です。yyyy-mm-dd または yyyy/mm/dd 形式で入力してください。")
                    return

            # 日付が正しい場合、データに登録
            self.events["payment"][selected_date] = {"school": school_name, "checked": False}  # チェックボックスの初期状態
            self.update_event_list()  # イベントリストを更新
            self.save_data()  # データを保存
            messagebox.showinfo("振込日登録", f"{selected_date} の振込日として '{school_name}' を登録しました。")
        else:
            messagebox.showerror("エラー", "学校名を入力してください。")

    def set_exam_date(self):
        """受験日を登録するための処理"""
        selected_date = self.calendar.get_date()  # 'yyyy-mm-dd'形式で取得
        exam_name = simpledialog.askstring("受験名", "受験する試験名を入力してください:", parent=self.root)

        if exam_name:
            try:
                # 日付の形式をチェック
                exam_date = datetime.datetime.strptime(selected_date, "%Y-%m-%d").date()
            except ValueError:
                try:
                    # スラッシュ区切りの日付にも対応
                    exam_date = datetime.datetime.strptime(selected_date, "%Y/%m/%d").date()
                except ValueError:
                    # 両方の形式でも無効ならエラーメッセージ
                    messagebox.showerror("エラー", "無効な日付形式です。yyyy-mm-dd または yyyy/mm/dd 形式で入力してください。")
                    return

            # 日付が正しい場合、データに登録
            self.events["exam"][selected_date] = {"exam_name": exam_name, "checked": False}  # チェックボックスの初期状態
            self.update_event_list()  # イベントリストを更新
            self.save_data()  # データを保存
            messagebox.showinfo("受験日登録", f"{selected_date} の受験日として '{exam_name}' を登録しました。")
        else:
            messagebox.showerror("エラー", "試験名を入力してください。")

    def update_event_list(self):
        """登録された受験日と振込日を日付順に表示する処理"""
        # ラベル、ボタン、チェックボックスをすべて削除
        for widget in self.labels_and_buttons + self.check_buttons + self.label_delete_buttons:
            widget.grid_forget()

        self.labels_and_buttons.clear()
        self.check_buttons.clear()
        self.label_delete_buttons.clear()

        # 受験日を日付順にソート
        sorted_exam_dates = sorted(self.events["exam"].keys())
        # 振込日を日付順にソート
        sorted_payment_dates = sorted(self.events["payment"].keys())

        # 受験日を表示
        self.display_exam_events(sorted_exam_dates)

        # 振込日を表示
        self.display_payment_events(sorted_payment_dates)

    def display_exam_events(self, sorted_dates):
        """受験日を表示する処理"""
        row = 1  # 受験日リストの表示位置
        for date in sorted_dates:
            event = self.events["exam"][date]
            event_text = f"{date} - {event['exam_name']}"
            remaining_days = self.calculate_days_left(date)

            # 残り日数に基づいた色を取得（受験日は常に水色で表示）
            color = self.exam_color

            # ラベルを追加
            label = tk.Label(self.root, text=f"{event_text} - 残り {remaining_days} 日", font=("Arial", 12), fg=color, bg="#2e2e2e")
            label.config(font=("Arial", 12, "bold"))
            label.grid(row=row, column=3, sticky="w", padx=10)

            # 削除ボタン
            delete_button = tk.Button(self.root, text="削除", font=("Arial", 10), fg="red", bg="#2e2e2e", relief="flat", command=lambda d=date, t="exam": self.confirm_delete_event(d, t))
            delete_button.grid(row=row, column=5, padx=10)

            self.labels_and_buttons.append(label)
            self.label_delete_buttons.append(delete_button)
            row += 1

    def display_payment_events(self, sorted_dates):
        """振込日を表示する処理"""
        row = 7  # 振込日リストの表示位置（振込日は少し下に配置）
        for date in sorted_dates:
            event = self.events["payment"][date]
            event_text = f"{date} - {event['school']}"
            remaining_days = self.calculate_days_left(date)

            # 残り日数に基づいた色を取得
            color = self.get_event_color(remaining_days)

            # チェックボックスを追加
            var = tk.BooleanVar(value=event['checked'])
            check_button = tk.Checkbutton(self.root, variable=var, bg="#2e2e2e", selectcolor="white", font=("Arial", 12), command=lambda d=date, v=var: self.toggle_check(d, v, "payment"))
            check_button.grid(row=row, column=4)

            full_text = f"{event_text} - 残り {remaining_days} 日"
            label = tk.Label(self.root, text=full_text, font=("Arial", 12), fg=color, bg="#2e2e2e")
            label.config(font=("Arial", 12, "bold"))

            # チェックボックスが選ばれたら文字色を緑に変更
            if event.get("checked", False):
                label.config(fg="green")  # チェックを入れたら緑に変更
                check_button.config(bg="white", activebackground="white")  # チェックボックス背景を白に変更

            label.grid(row=row, column=3, sticky="w", padx=10)

            # 削除ボタン
            delete_button = tk.Button(self.root, text="削除", font=("Arial", 10), fg="red", bg="#2e2e2e", relief="flat", command=lambda d=date, t="payment": self.confirm_delete_event(d, t))
            delete_button.grid(row=row, column=5, padx=10)

            self.labels_and_buttons.append(label)
            self.check_buttons.append(check_button)
            self.label_delete_buttons.append(delete_button)

            row += 1

    def get_event_color(self, remaining_days):
        """残り日数に基づいた色を返す処理"""
        if remaining_days < 0:
            return "purple"  # 期限を過ぎている
        elif remaining_days <= 3:
            return "red"  # 残り3日以内
        elif remaining_days <= 7:
            return "yellow"  # 残り7日以内
        else:
            return "green"  # それ以外は緑

    def calculate_days_left(self, date):
        """残り日数を計算する処理"""
        today = datetime.date.today()
        try:
            event_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()  # 日付をdatetime.date型に変換
            delta = event_date - today
            return delta.days  # 残り日数を返す
        except ValueError:
            try:
                # スラッシュ区切りの日付にも対応
                event_date = datetime.datetime.strptime(date, "%Y/%m/%d").date()
                delta = event_date - today
                return delta.days  # 残り日数を返す
            except ValueError:
                return 0  # 無効な日付の場合は0を返す

    def save_data(self):
        """データをファイルに保存"""
        with open(self.data_file, "w") as f:
            json.dump(self.events, f)

    def load_data(self):
        """データをファイルから読み込む"""
        try:
            with open(self.data_file, "r") as f:
                self.events = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.events = {"exam": {}, "payment": {}}

    def confirm_delete_event(self, date, event_type):
        """イベントを削除する前に確認ダイアログを表示"""
        response = messagebox.askyesno("確認", f"{event_type}日 ({date}) を削除しますか？")
        if response:
            if event_type == "exam":
                del self.events["exam"][date]
            elif event_type == "payment":
                del self.events["payment"][date]
            self.update_event_list()  # イベントリストを更新
            self.save_data()  # データを保存

    def reload_data(self):
        """データを再ロードする処理"""
        self.load_data()  # データを再読み込み
        self.update_event_list()  # イベントリストを再表示
        messagebox.showinfo("再ロード", "データを再読み込みました。")

# メイン処理
if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()