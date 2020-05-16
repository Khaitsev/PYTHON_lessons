class Numbers:
    def nums(self):
        row = ''
        while True:
            nu = input('введите ряд значений: ')
            b = ''.join(list(n for n in nu if n.isdigit()))
            row = row + b
            if nu == 'stop':
                break
        print(row)


a = Numbers()
a.nums()
