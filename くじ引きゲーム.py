import PySimpleGUI as sg
import random
def main():
    くじ箱=lottery_box()
    layout = [
        [sg.Text('くじ引きゲーム')],
        [sg.Button('くじを引く'), sg.Button('終了')],
        [sg.Listbox(values=[], size=(30, 10), key='history', auto_size_text=True)],
    ]
    window = sg.Window('くじ引きゲーム', layout)
    history = []
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == '終了':
            break
        elif event == 'くじを引く':
            drawn_lottery = くじ箱.くじ引き()
            if drawn_lottery==None:
                sg.popup('くじが無くなりました\n補充します')
                くじ箱=lottery_box()
            else:
                history.append([len(history)+1,drawn_lottery])
                window['history'].update(values=history)
    window.close()
class lottery_box:
    def __init__(self):
        self.lotteries = ['SSR', 'SR', 'SR', 'SR', 'R', 'R', 'R', 'R', 'R', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
    def くじ引き(self):
        if not self.lotteries:
            return None
        drawn_lottery=random.choice(self.lotteries)
        self.lotteries.remove(drawn_lottery)
        return drawn_lottery
if __name__ == '__main__':
    main()