import datetime


class TestV1Prover:
    def test_v1_xxx(self):
        def get_current_datetime():
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            return formatted_datetime

        xxx = get_current_datetime()
        print("\nТекущая дата и время:", xxx)
