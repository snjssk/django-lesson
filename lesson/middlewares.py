import datetime


# ミドルウェアを生成するファクトリー関数
# get_response関数を受け取り、生成したミドルウェアを返す
def log_middleware(get_response):
    # ミドルウェア関数
    def middleware(request):
        # ビューの前
        start = datetime.datetime.now()
        print(f' start: {request.path}: {start}')

        # ビューの呼びだし
        response = get_response(request)

        # ビューの後
        end = datetime.datetime.now()
        print(f' end: {request.path}: {end}...{end - start}ms')

        return response
    return middleware