main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

old1 = "    import psycopg2"
new1 = "    import psycopg2\n    import psycopg2.pool"
results["1_import_pool"] = content.count(old1)
content = content.replace(old1, new1, 1)

old2 = '''def _get_db_connection():
    global _LAST_DB_ERROR
    db_url = os.environ.get("DATABASE_URL", "")
    if not db_url:
        _LAST_DB_ERROR = "DATABASE_URL not set"
        return None
    try:
        return psycopg2.connect(db_url)
    except Exception as e:
        _LAST_DB_ERROR = str(e)
        return None'''

new2 = '''_db_pool = None
_db_pool_lock = threading.Lock()


class _PooledConnectionWrapper:
    """Transparent wrapper: everything delegates to the real psycopg2 connection,
    except close(), which returns the connection to the pool for reuse instead of
    tearing down the underlying TCP connection - this is what lets every existing
    conn.close() call site in this file keep working unchanged while still gaining
    the performance benefit of connection reuse instead of a fresh TCP+auth
    handshake on every single database-using request."""
    def __init__(self, real_conn, pool):
        object.__setattr__(self, "_real_conn", real_conn)
        object.__setattr__(self, "_pool", pool)
        object.__setattr__(self, "_closed", False)

    def close(self):
        if not self._closed:
            try:
                self._pool.putconn(self._real_conn)
            except Exception:
                try:
                    self._real_conn.close()
                except Exception:
                    pass
            object.__setattr__(self, "_closed", True)

    def __getattr__(self, name):
        return getattr(self._real_conn, name)


def _get_connection_pool():
    global _db_pool
    if _db_pool is None:
        with _db_pool_lock:
            if _db_pool is None:
                db_url = os.environ.get("DATABASE_URL", "")
                if db_url:
                    try:
                        _db_pool = psycopg2.pool.ThreadedConnectionPool(1, 10, db_url)
                    except Exception:
                        _db_pool = None
    return _db_pool


def _get_db_connection():
    global _LAST_DB_ERROR
    db_url = os.environ.get("DATABASE_URL", "")
    if not db_url:
        _LAST_DB_ERROR = "DATABASE_URL not set"
        return None
    try:
        pool = _get_connection_pool()
        if pool is None:
            # fall back to a direct connection if the pool itself failed to initialize
            return psycopg2.connect(db_url)
        real_conn = pool.getconn()
        if real_conn.closed:
            # stale connection from the pool (e.g. DB restarted) - discard and get a fresh one
            pool.putconn(real_conn, close=True)
            real_conn = pool.getconn()
        return _PooledConnectionWrapper(real_conn, pool)
    except Exception as e:
        _LAST_DB_ERROR = str(e)
        return None'''

results["2_pool_implementation"] = content.count(old2)
content = content.replace(old2, new2, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("IMPLEMENTPOOL-DONE")