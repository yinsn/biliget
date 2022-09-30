# biliget

Bulk downloader for Bilibili.

## Download a single Bilibili video

```python
import biliget
loader = biliget.DownLoader({SINGLE_URL})
loader.load_single()
```

## Bulk download a series of videos

Download videos from `p=1` to `p=3`:

```python
loader = biliget.DownLoader({BASE_URL})
loader.bulk_download(1, 3)
```
