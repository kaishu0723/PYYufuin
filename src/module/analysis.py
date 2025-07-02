import soundfile as sf

# WAVファイルを読み込み
data, samplerate = sf.read('./output.wav')

# チャンネル数を取得
channels = data.shape[1] if len(data.shape) > 1 else 1

print(f"チャンネル数: {channels}")
print(f"サンプルレート: {samplerate}")
print(f"データ形状: {data.shape}")