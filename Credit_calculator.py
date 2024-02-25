import ru_local as ru
import en_local as en


class BankInterest():
    def __init__(self, summ, percent, period):
        self.summ = summ
        self.period = period
        self.percent = percent

    def diff_int(self):
        payments = []
        months = self.period * 12
        rest = self.summ
        mp_real = self.summ / months
        while months != 0:
            month_paid = mp_real + (rest * self.percent / 1200)
            payments.append(round(month_paid, 2))
            rest = rest - mp_real
            months = months - 1
        return payments


if __name__ == '__main__':
    lang = input('Choose language(ru/en): ')
    if lang != 'ru' and lang != 'en':
        print("Wrong language!!!")

    if lang == 'ru':
        summ = int(input(f'{ru.SUMM_INPUT}: '))
        percent = int(input(f'{ru.PERCENT_INPUT}: '))
        period = int(input(f'{ru.PERIOD_INPUT}: '))

        credit = BankInterest(summ, percent, period)
        diff = credit.diff_int()
        for month, pay in enumerate(diff):
            print(f'{ru.PAYMENT_PRINT} {month + 1}: {pay: .2f}.')
        print(round(sum(diff), 2))

    if lang == 'en':
        summ = int(input(f'{en.SUMM_INPUT}: '))
        percent = int(input(f'{en.PERCENT_INPUT}: '))
        period = int(input(f'{en.PERIOD_INPUT}: '))

        credit = BankInterest(summ, percent, period)
        diff = credit.diff_int()
        for month, pay in enumerate(diff):
            print(f'{ru.PAYMENT_PRINT} {month + 1}: {pay: .2f}.')
        print(round(sum(diff), 2))
