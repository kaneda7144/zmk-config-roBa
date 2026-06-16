# ROBA ZMK Config

Keyball39のRemap/VIAダンプから移行したROBA用ZMK設定です。

## 書き込み直前までの流れ

1. このリポジトリをGitHubへpushする。
2. GitHub Actionsの `Build` が完了するのを待つ。
3. Actions artifactからUF2をダウンロードする。
4. ROBAをブートローダーモードにして、対応するUF2をコピーする。

## 生成物

- `config/roBa.keymap`: ROBA用キーマップ
- `build.yaml`: GitHub Actionsのビルド対象
- `boards/shields/roBa/`: ROBA shield定義
- `tools/keyball_via_dump.html`: Keyball39のVIAキーマップ読み出し用
- `tools/convert_keyball39_dump_to_roba.py`: ダンプJSONからROBA keymapを再生成する変換ツール

## ビルド対象

- `roBa_R`: トラックボール側、通常はこちらを書き込む
- `roBa_L`: 反対側
- `settings_reset`: Bluetooth設定リセット用

キーマップ変更だけなら、ROBA公式手順どおり中央側の `roBa_R` を書き込む想定です。
