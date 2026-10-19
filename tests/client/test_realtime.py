import stitchdb


def test_realtime_client_initialization() -> None:
    ref = "ooqqmozurnggtljmjkii"
    url = f"https://{ref}.stitchdb.com"
    # Sample JWT Key
    key = "xxxxxxxxxxxxxx.xxxxxxxxxxxxxxx.xxxxxxxxxxxxxxx"
    sp = stitchdb.Client(url, key)
    assert str(sp.realtime_url) == f"wss://{ref}.stitchdb.com/realtime/v1"

    url = "http://localhost:54322"
    sp_local = stitchdb.Client(url, key)
    assert str(sp_local.realtime_url) == "ws://localhost:54322/realtime/v1"
