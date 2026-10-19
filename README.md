# stitchdb-py

The official Python client for [StitchDB](https://stitchdb.com): Postgres database, auth, storage, realtime and Edge Functions. Sync and async.

```bash
pip install stitchdb-py
```

```python
import os
from stitchdb import create_client

stitchdb = create_client(os.environ["STITCHDB_URL"], os.environ["STITCHDB_KEY"])

# Database (respects Row Level Security)
rows = stitchdb.table("todos").select("id, task").eq("is_complete", False).limit(10).execute().data
stitchdb.table("todos").insert({"task": "Ship it"}).execute()
stitchdb.rpc("search_todos", {"term": "ship"}).execute()

# Auth
stitchdb.auth.sign_in_with_password({"email": "ada@example.com", "password": "..."})
user = stitchdb.auth.get_user()

# Storage
stitchdb.storage.from_("avatars").upload("user-1/avatar.png", open("avatar.png", "rb").read())
url = stitchdb.storage.from_("avatars").create_signed_url("user-1/avatar.png", 60)

# Edge Functions
stitchdb.functions.invoke("hello-world", {"body": {"name": "Ada"}})
```

Async: `from stitchdb import acreate_client` and `stitchdb = await acreate_client(url, key)`. Realtime needs the async client.

Find your project URL and keys in the dashboard under **Settings → API keys**. Use the `service_role` key only on servers you control.

Documentation: https://stitchdb.com/docs/sdk/python
