#学習ログ

"""
2026-01-31
内容：
・if文とfor文の復習
・リストから条件に合う要素を取り出す練習
"""
# 条件に合うデータの抽出 → basics/passed_number.py

"""
2026-02-01
内容：
・リストから条件（60点以上）に合う要素を処理する練習
・条件を満たす要素の個数をカウントする関数を実装
・不要な条件分岐を書かないシンプルな実装を意識した
"""
# 条件下での出現回数カウント → basics/count_numbers.py

"""
2026-02-03
内容：
・条件付きで最大値を求める処理を実装
・None を使って「該当なし」の状態を表現する練習
・関数の戻り値を受け取り、if文で分岐する処理を復習
・エラーを避けるために戻り値のチェックを行う重要性を理解
"""
#条件下での平均 → basics/calc_passed_avg.py
#条件下での最大値 → basics/passed_score_max.py
#Noneチェック → basics/check_none_result.py

"""
2026-02-04
内容：
・Truthy / Falsy を用いた if 文の挙動を確認
・None を明示的に判定する条件分岐を実装
・None と 空（空リスト・空文字など）を区別する処理を理解
・条件の順序を意識した if / elif / else の書き方を練習
・入力値（名前）が None または空の場合の入力チェック処理を実装
"""
#Truthy / Falsyを用いたif文 → basics/truthy_falsy_if.py
#Noneチェック関数 → basics/none_check.py
#Noneと空の区別 → basics/none_and_empty.py
#点数判定 → basics/score_judgement.py
#名前チェック関数（None または 空文字）→ basics/name_check.py

"""
2026-02-05
内容：
・for文とif文を組み合わせて、条件に合う要素を抽出する処理を実装
・条件に合う値が見つからない場合、None を返す関数を作成
・関数の戻り値を受け取り、None チェックで安全に分岐する処理を復習
"""
#最初に60以上の点数を返す関数 → first_pass_score.py

"""
2026-02-06
内容：
・辞書（名前 → 点数）を使った条件付きデータ抽出の復習
・単一結果では None、複数結果では空リスト [] を返す設計の使い分けを理解
・next(iter(dict)) を用いた初期値設定の考え方を確認
・最高得点者が複数いる場合に全員を返す処理を実装
・max() を用いた Pythonicな最大値取得方法を学習
・max(dict) / max(dict.values()) / max(dict, key=...) の違いを理解
"""
#60点以上の中で最高得点の人の名前を返す関数 → find_top_student.py
#最高得点の人が複数いる場合の処理 → find_top_students.py
#max()を用いたPythonicな処理 → find_top_students_pythonic.py

"""
2026-02-07
内容：
・型ヒント（dict[str, int], list[str], str | None）の書き方を練習
・docstring を用いて関数の役割・引数・戻り値を明示
・フォルダ分割を行い、別ファイルの関数を import して使用
・if __name__ == "__main__": を使い、実行用コードとロジックを分離
"""
#型ヒント＋docstring（読み手を意識したコード) → practice_typehint_docstring.py
#型ヒントの設定練習 → practice_typehint.py
#ファイル分割 ＋ import → run_import_students.py
#if __name__ == "__main__"の使い方 → if_main_demo.py

"""
2026-02-08
内容：
・Optional の意味と使い方を理解
・返り値設計の使い分けを学習
・型ヒント付き関数の実装練習
・Pythonic な書き方の理解
・Optional の返り値を呼び出し側で安全に扱う方法
"""
#Optional を用いた関数 → first_over_threshold_optional.py
#Optional と空リストの使い分け → students_above_threshold_list.py
#Optional と空リストの組み合わせ → top_scorers_optional_list.py

"""
2026-02-09
内容：
・Optional の意味と使いどころの理解
・raise ValueError の書き方と設計意図
・Optional と raise の使い分け判断
・型ヒントと返り値設計の整合性チェック
"""
#通常の書き方と内包表記の書き方の比較 → list_comprehension_vs_for.py
#Optional / 空リスト / 例外 のどれを返すべきか → how_to_return_values.py
#Optionalとraiseの設計判断 → optional_vs_raise_design.py

"""
2026-02-10
内容：
・dict の基本構造（key: value）と dict in dict の扱い方
・値と型の検証方法（isinstance）
・isinstance(value, int) を用いたデータ不整合チェック
・Optional と例外の設計判断（「起こりうる結果なし」→ None、「データ不整合・成立しない状態」→ raise ValueError）
・年齢制限つきユーザー取得関数を設計・実装
・存在チェック → データ検証 → ビジネス条件 の順で if を構成
・コメントの書き方の指針（判断理由・意味 → 改行コメント、補足説明 → 横コメント）
"""
#ユーザー検索APIのコアロジック → user_search_core.py
#年齢制限つきユーザー取得 → adult_user_optional.py

"""
2026-02-11
内容：
・dict in dict の理解とアクセス方法の確認
・dict.get() の挙動理解（KeyErrorとの違い）
・Optional を返す関数の設計
・None 伝播パターンの実装（3段チェーン）
・Optional を返す関数の安全な組み合わせ
・None と raise ValueError の使い分け
・重複関数呼び出しを避ける設計
・責務分離を意識した関数構成
"""
#Optionalを返す関数を組み合わせる → optional_function_composition.py 
#3段の組み合わせ → optional_three_step_chain.py

"""
2026-02-12
内容：
・classの概要の理解
・コンストラクタでのバリデーション実装
・メソッドの self の役割を理解
・updateメソッドの設計を学習
・privateメソッド（_validate_xxx）の設計意図を理解
・クラス設計での責務整理を意識できるようになった
"""
#classの概要 → class_basics_dog.py
#classの演習 → user_class_design.py

"""
2026-02-13
内容：
・@property を使うことで、メソッドを属性のように読み取れることを理解した
・getter は属性の「読み取り時」に自動で呼び出される処理であることを理解した
・self.age = value は通常の代入ではなく、setter を経由することを理解した
・実際の保存は _age のような private 属性に行う必要がある理由（無限ループ防止）を理解した
・_name, _age, _email のように内部保存用属性と公開用 property を分離する設計を学んだ
・初期化 (__init__) と更新の両方で setter を使うことで、一貫した validation を保証できることを理解した
・name, age, email を property + setter + validation で管理する User クラスを実装した
・カプセル化（内部状態を直接触らせず、安全な窓口だけ公開する設計）の基本を理解した
"""
#propertyを使ったclass処理 → property_class_design.py

"""
2026-02-14
内容：
・private属性（_owner, _balance, _transactions）によるカプセル化を理解
・property を使い「参照は可能・直接代入は不可」を実現
・残高の変更を apply_transaction() のみに限定し、状態変更の責務を集中させた
・Transactionを検証付きの値オブジェクトとして扱う考え方を理解
・取引履歴を list で保持し、外部公開時は tuple に変換して不変化
・mutable（list）と immutable（tuple）の違いと用途を理解
・不変条件（invariant）をクラスが保証する設計の重要性を理解
"""
#propertyを用いた計算プロパティ（area, full_name）を追加するクラス設計の発展練習 → computed_property_practice.py
#「安全な状態管理」と「不変条件の維持」 → state_management_and_invariants.py

"""
2026-02-15
内容：
・例外設計をすることで可読性とエラーごとの処理を可能にする
・継承設計によるエラーの分岐を理解
・as eの利点と多様な使い方を理解
"""
#例外設計 → bank_account_exception_design.py
#例外の親クラス → exception_inheritance_practice.py
#as eの使い方 → exception_as_usage.py

"""
2026-02-17
内容：
・Service / Domain の責務分離を意識した設計演習を行った
・購入処理を User・Product・PurchaseService に分割した
・「誰の責任か？」を基準にロジックの置き場所を考えた
・支払いロジックは User の責任であることを理解した
・不整合を防ぐために「変更前チェック」を意識した
・動くコードよりも「設計の正しさ」が重要だと学んだ
"""
#実務を意識した設計演習 → purchase_service_design.py

"""
2026-02-18
内容：
・オブジェクト指向での責務分離を意識して設計を行った
・副作用（状態変更）の順番によって不整合が起こることを学んだ
・例外クラスをドメインごとに定義する重要性を確認
・クーポン割引ロジックを独立したクラスに分離
・コードをシンプルに書くことで、エラー箇所を特定しやすくなると理解
"""
#テストしやすい設計 → domain_service_design_practice.py
"""
2026-02-19
内容：
・Order と CheckoutService の責務分離
状・態管理の導入
Cou・ponを任意にする設計
pytest導入・実行確認
・例外テスト作成
・with pytest.raises() の意味を理解
・成功時／失敗時の副作用確認の重要性を理解
"""
#トランザクションの中心に Order を置く設計

"""
2026-02-23
内容：
・Order中心のトランザクション設計を状態機械に進化させた
・Enum（OrderStatus / OrderAction）で状態と操作を型安全に管理
・状態遷移を if 文から辞書（ALLOWED_TRANSITIONS）へ移行
・_transition() を導入し状態変更を一本化
・副作用（支払い・在庫減少）と状態遷移の順序を整理
・ドメイン例外の階層設計を検討（OrderError基底クラス）
"""
#状態遷移の高度化

"""
2026-02-24
内容：
・pay() の原子性を改善
・チェック → 副作用 → 状態確定 の順序
・二重支払い・二重キャンセル防止
・テストを通して設計の整合性を確認
"""
#原子性と状態遷移の制御による、不整合を許さない堅牢な注文管理システムの設計

"""
2026-02-25
内容：
・状態遷移テーブル（ALLOWED_TRANSITIONS）にロジックを集約
・状態チェックを if 文からテーブル駆動へ移行
・副作用を クリティカル / ノンクリティカル に分類
・原子性の範囲を「ビジネス整合性」に限定する設計を理解
・例外を握り潰さず、トランザクション境界で扱う考え方を整理
・ドメイン層は「正しい振る舞い」を定義し、原子性保証はApplication/DB層の責務と理解
・cancel処理を「返金・在庫復元・状態変更」の1事実として設計
・レイヤードアーキテクチャ的責務分離を意識
"""
#状態遷移モデルと副作用の分離による堅牢な注文ドメイン設計

"""
2026-03-08
内容：
・ドメインイベントの設定
・DDD設計に合わせたプログラム設計
"""

"""
2026-03-09
内容：
・PayOrderUseCase でイベントを処理し、副作用（レシート送信）をドメインから分離
・Order を Aggregate Root として設計し、User・Product などの整合性を管理
・Order.pay() を通してのみ状態変更を行い、Aggregateの整合性を保証
・ReceiptSender を インターフェース化して依存を抽象化
・送信方法（Email / Slack など）を ポリモーフィズムで差し替え可能に設計
・Domain → Application → Infrastructure の 依存方向を意識
・id(self) は一時的識別子であり、本来はドメインIDを持つべきと理解
"""

"""
2026-03-13
内容：
・Repositoryパターン導入
・OrderRepository を抽象クラスとして定義
・InMemoryOrderRepository を実装
・execute() で.get()、order_repo.save()の実装
・EmailReceiptSender、SlackReceiptSender、LINEReceiptSender
・transition を最後にする理由
・Aggregateの整合性を守る
・1 Transaction = 1 Aggregate（設計上の重要ルール）
"""

"""
2026-03-24
内容：
・イベント処理の完成
・Repositoryの不備修正
・永続化漏れ修正（バグ修正）
・ドメインイベント強化
・EntityにID追加
・Orderの責務整理
・バグ修正（動作面）
"""

"""
2026-04-02
内容：
・ndarrayはリストと違い、要素の加工や行列計算が簡単にできる
・ndimで次元数、shapeで各次元のサイズを確認できる
・zeros/onesで0・1埋め、random.randでランダム値、emptyでメモリ上の値の配列を作成できる
・shapeが同じ配列同士は要素ごとに計算できる
・行か列のどちらかのサイズが一致していれば自動的に引き伸ばして計算できる
"""

"""
2026-04-05
内容：
・行列演算
・配列の変形
・要素へのアクセス
・配列の結合
・統計・集計関数
・数学関数（スカラー値に使用）
"""

"""
2026-05-05
内容：
2次元データ → DataFrame、1次元データ → Series（カラムは持たない）
DataFrameの構成要素
pd.DataFrame()による表データを作成
indexを任意に設定
"""

"""
2026-05-06
内容：
・Excelからの読み取り
・列のインデックス指定
"""

"""
2026-05-07
内容：
・csvファイルの読み込み
・行や列の抽出(loc, iloc)
"""

"""
2026-05-11
内容：
・ブールインデックスによる条件抽出
・複数条件の指定方法
・統計量の取得
・列同士の演算
・新しい列の追加
・文字列結合による列作成
"""

"""
2026-05-18
内容：
groupby() を使うことで、指定した列ごとにデータをグループ化できる
df.groupby("担当者").mean(numeric_only=True) により、担当者別の売上平均を計算できる
最近の pandas では、文字列列を含む DataFrame に対して mean() を使う場合、numeric_only=True を指定する必要がある
欠損値（NaN）は自動で無視して計算する
df.index を使うことでインデックスを変更できる
range(1, 10) を使うことで、インデックスを 1〜9 に設定できる
df.columns を使うことで列名を変更できる
列名の数と列数は一致している必要がある
"""

"""
2026-05-19
内容：
・inplace = Trueによるdf自身のインデックス変更
・インデックスの振りなおし
・inplace = Trueによるdf自身のインデックスの振りなおし
・drop = Trueを使い、元々インデックスだった列の追加のキャンセル
"""

"""
2026-05-22
内容：
・concatによるデータフレームの結合
・データが足りないときはNaNが入る
・横の結合(axis = 1)
・データが欠損していると、ずれが発生する
"""

"""
2026-06-11
内容：
・データフレームの結合(merge)
・外部結合(how)
"""

"""
2026-06-12
内容：
・指定した列の各要素に処理を適用してから新しい列を追加する(map())
・Series.map()の引数には、lambda、関数(def)、辞書などを指定できる
・lambdaは無名関数で、その場で一時的に関数を作る書き方
・lambdaは「指定した文字(引数)を受け取り、:の後にその処理を書く」という構文
・"成人" if x >= 20 else "未成年"は三項演算子(条件式)で、「値A if 条件 else 値B」の形で条件分岐を1行で書ける
"""

"""
2026-06-13
内容：
・組み込み関数のmap()はリストの各要素を一つずつ取り出し、lambdaで指定した処理をした結果をまとめて返す
・Series.map()に辞書を渡すと、キーに対応する値で新しい列を作成できる。(対応するキーがない場合はNaN)
・Series.map()には別のSeriesを渡すこともでき、その場合はインデックスを使って値を対応させる(対応しない場合はNaN)
・matplotlib.pyplotを使うと、DataFrameをグラフとして可視化できる
・df.plot()のデフォルトは折れ線グラフ
・kind引数を指定すると、グラフの種類(例: kind="bar"で棒グラフ)を変更できる
・japanize_matplotlibをインポートすることで、グラフ内の日本語表示に対応できる
"""

"""
2026-06-19
内容:
・用語理解
"""

"""
2026-06-21
内容：
・plt.subplots() を用いて、Figure（グラフ全体）とAxes（描画領域）を作成
・FigureとAxesを分離して扱うことで、グラフの構造を理解した。
・ax.plot() を使用して折れ線グラフを作成
・x軸とy軸のデータをリスト形式で指定
・plt.show() によるグラフの表示
"""

"""
2026-06-23
内容：
・ラベルの指定
・フォントサイズの変更
"""

"""
2026-06-24
内容：
・凡例の設定
・Y軸のラベルを横向きに変更(rotation = "horizontal")
・グリッド線の追加
・タイトルの設定
・プロットの追加(marker = "o")
・Y軸の目盛りの変更(set_yticks)
"""

"""
2026-06-29
内容：
・棒グラフの作成(ax.bar())
・グラフの色の変更(color = "m")
"""

"""
2026-07-01
内容：
・散布図の作成(ax.scatter())
"""

"""
2026-07-06
内容：
・ヒストグラムの作成(ax.hist())
・ヒストグラムの棒の数を指定(bins = 5)
"""

"""
2026-07-07
内容：
・ファイルへの保存
"""

"""
2026-08-06
内容：
・ベクトルの定義
・行列の定義
・ベクトルの作成
"""

"""
2026-08-10
内容：
・組み合わせ
・ジェネレータ式の応用
・for文とelse
"""

"""
2026-08-23
内容：
・FastAPI()でアプリケーション本体を作成
・FastAPIのインスタンスを作成
・@app.get("/")を使ってGETリクエストを受け取る
・URLごとに処理する関数を設定
・/へGETリクエストが送られたときにread_root()が実行されることを学習
・Pythonの辞書型{"message": "APIです"}を返す方法を学習
"""

"""
2026-08-24
内容：
・デコレータの定義
・デコレータの処理の流れ
"""

"""
2026-08-28
内容：
・リクエストオブジェクトの作成
・データの取得
・API認証
"""

"""
2026-08-29
内容：
・パスが可変のAPI
・辞書型での出力
・処理の競合(上に書かれている方が優先される)
"""

"""
2026-08-30
内容：
・クエリパラメータを含むAPI
・Annotatedを用いた型ヒントのメタデータの追加
・Queryを用いた条件の設定
・クエリパラメータを含むAPIへのgetリクエスト
"""

"""
2026-08-31
内容：
・データの送信
・BaseModel
・Fieldによる変数の設定
・Optionalによるデータ型の設定
"""

"""
2026-09-01
内容：
・ヘッダーの理解
・Headerを用いたヘッダー情報の取得
・リクエスト側のヘッダーの設定
"""

"""
2026-09-02
内容：
・レスポンスヘッダーへの追加
・Responseを用いたレスポンスヘッダーの設定
"""

"""
2026-09-04
内容：
・非同期処理の理解
・__name__の理解
・関数のコルーチン化
・awaitによる非同期処理の完了待ち
・関数の切り出し
"""

"""
2026-09-10
内容：
・async.create_task()によるタスクの生成
・タスクの並行処理
"""

"""
2026-09-11
内容：
・async.gather()による複数のコルーチンやタスクの並列処理
・通常の関数を非同期関数に変換する
・run_in_executor()による通常の関数を非同期関数として実行する
"""

"""
2026-09-12
内容：
・async.wait_for()によるタイムアウト処理
"""

"""
2026-09-13
内容：
・FastAPIでの非同期処理の方法
・非同期によるリクエスト
"""

"""
2026-09-14
"""

"""
2026-10-01
内容：
・注文支払いAPIの作成
・支払処理の例外処理
・Order作成APIの作成
"""

"""
2026-19-05
内容:
・アプリ経由でのrequestのテスト(TestClient)
・Order取得テスト
・存在しないOrderの取得テスト
・Order作成テスト
・支払いテスト
・存在しない支払いテスト
"""

"""
2026-10-11
内容：
・fixtureによるテストデータの初期化
・残高不足のテスト
・在庫不足のテスト
"""

"""
2026-10-12
内容：
・users_tableの作成
・jobs_tableの作成
・データの挿入
・内部結合
"""

"""
2026-10-13
内容：
・データベースとの接続
・SQLlogの出力
・データベースのテーブル表示
"""

"""
2026-10-14
内容：
・Baseの継承
・Pythonによるテーブルの作成
・テーブル名の設定
・型ヒント(Mapped)
・カラム定義(mapped_column)
・主キーの設定(primary key)
・NULL制約の設定(nullable)
・レコード登録時のidの自動割り当て(default = uuid.uuid4)
"""

"""
2026-10-15
内容：
・postsテーブルの作成
・外部キーの設定
・タイムゾーンを指定した日時記録
・カラム変更時の日時の自動更新
・relationship
"""

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Text, Uuid, Date, ForeignKey, DateTime
import uuid
from datetime import date, datetime
from zoneinfo import ZoneInfo

class Base(DeclarativeBase):
    pass

#sqlalchemyではテーブルをクラスで表現する
#Baseを継承することで、PythonのクラスとDBのテーブルを自動で紐付けてくれる
class User(Base):
    __tablename__ = "users"
    #テーブルのカラムはインスタンス変数として定義
    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, 
        primary_key = True,
        default = uuid.uuid4    #テーブルに登録した時に自動でidを割り当てる設定
    )

    name: Mapped[str] = mapped_column(
        Text, 
        nullable = False,
        unique = True
    )
    #Mappedは型ヒント、mapped_columnはデータベース上の制約（primary_key, nullable, defaultなど）を指定、nulllableは変数にNULLを許すかどうか

    birthday: Mapped[date] = mapped_column(
        Date,
        nullable = True
    )
    posts: Mapped[list["Post"]] = relationship(
        back_populates = "user"
    )
    #relationshipは外部キーなどのPythonのオブジェクト同士のつながりとして直感的に扱うための機能
    #よって、DBには関係ない
    #例えば、あるユーザの投稿一覧などをすぐに見れたりする


class Post(Base):
    __tablename__ = "posts"
    id: Mapped[uuid.UUID] = mapped_column(
            Uuid, 
            primary_key = True,
            default = uuid.uuid4   
        )
    #記事のタイトル
    title: Mapped[str] = mapped_column(Text, nullable = False)
    #本文
    body: Mapped[str] = mapped_column(Text, nullable = False)
    #usersテーブルのidに紐づく外部キー
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        #引数には紐づいているテーブル名.カラム名
        nullable = False
    )
    #投稿日時
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True),
        default = lambda: datetime.now(ZoneInfo("Asia/Tokyo"))
    )
    #更新日時
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True),
        default = lambda: datetime.now(ZoneInfo("Asia/Tokyo")),
        #lambda式はコロン後の処理を呼び出す即席の関数のようなもの
        #本来はlambdaの後ろに関数に代入する変数があるが、関数を呼び出すだけなので、不要

        onupdate = lambda: datetime.now(ZoneInfo("Asia/Tokyo"))
        #カラムの内容が変更されるごとに記録し直す
    )
    #dateとdatetimeの違いは時刻が不要かどうか(更新日時などのログは秒まで必要)
    user: Mapped["User"] = relationship(
        back_populates = "posts"
    )