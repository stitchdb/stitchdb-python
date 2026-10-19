import stitchdb


def test_functions_client_initialization() -> None:
    ref = "ooqqmozurnggtljmjkii"
    url = f"https://{ref}.stitchdb.com"
    # Sample JWT Key
    key = "xxxxxxxxxxxxxx.xxxxxxxxxxxxxxx.xxxxxxxxxxxxxxx"
    sp = stitchdb.Client(url, key)
    assert str(sp.functions_url) == f"https://{ref}.stitchdb.com/functions/v1"

    url = "https://localhost:54322"
    sp_local = stitchdb.Client(url, key)
    assert str(sp_local.functions_url) == f"{url}/functions/v1"
