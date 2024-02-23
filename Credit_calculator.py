class BankInterest():
    def __init__(self, summ, percent, period):
        self.summ = summ
        self.period = period
        self.percent = percent

    def diff_int(self):
        arr = []
        mp_cnt = self.period * 12
        rest = self.summ
        mp_real = self.summ / (self.period * 12.0)
        while mp_cnt != 0:
            mp = mp_real + (rest * self.percent / 1200)
            arr.append(round(mp, 2))
            rest = rest - mp_real
            mp_cnt = mp_cnt - 1
        return arr
