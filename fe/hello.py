from datetime import datetime


def main() -> None:
    print("你好啊，Python！！！！")
    print(f"当前时间：{datetime.now():%Y-%m-%d %H:%M:%S}")


if __name__ == "__main__":
    main()
