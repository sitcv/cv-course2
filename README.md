# computer vision -- course 2

このプロジェクトのサンプルは `uv` で作成した仮想環境を使って実行します。

## 前提

- `uv` がインストールされていること
- Python `3.13` 以上が利用できること

## セットアップ

依存関係を同期すると、`.venv` が作成されて必要なパッケージが入ります。

```bash
uv sync
```

## サンプルの実行

Python スクリプトは次のように実行します。

```bash
uv run python filter.py
uv run python image_addnoise.py
uv run python edge-detection.py
```

## Notebook の起動

Jupyter Notebook を使う場合も `uv run` 経由で起動します。

```bash
uv run jupyter notebook
```

起動後に、以下のノートブックを開いてください。

- `filter.ipynb`
- `image_noise.ipynb`

## 補足

- 依存関係を更新したあとに lockfile を更新したい場合は `uv lock` を使います。
- 新しいパッケージを追加する場合は `uv add <package>` を使います。
