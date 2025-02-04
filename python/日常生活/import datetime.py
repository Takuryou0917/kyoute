import datetime

def calculate_days_left(date):
    today = datetime.date.today()  # 今日の日付を取得
    try:
        event_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()  # 入力された日付をdatetime.date型に変換
        delta = event_date - today  # 残り日数を計算
        return delta.days  # 残り日数を返す
    except ValueError:
        return "無効な日付です"  # 無効な日付が入力された場合のエラーハンドリング

# 実験する日付
event_date = "2025-01-10"  # ここに実験したい日付を入力
remaining_days = calculate_days_left(event_date)
print(f"{event_date} までの残り日数: {remaining_days} 日")
