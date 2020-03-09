import TkManager


class TkSample:
    tkInfo = {
        'title': 'tkinterサンプル',
        'geometry': '800x600',
        'label': {
            'label1': {
                'text': 'aaa',
                'x': '10',
                'y': '10',
            },
            'label2': {
                'text': 'bbb',
                'x': '10',
                'y': '50',
            },
        },
        'entry': {
            'input1': {
                'x': '50',
                'y': '10',
                'width': '20',
            },
            'input2': {
                'x': '50',
                'y': '50',
                'width': '20',
            },
        },
        'button': {
            'button1': {
                'text': 'aaa',
                'x': '200',
                'y': '10',
                'width': '20',
            },
            'button2': {
                'text': 'bbb',
                'x': '200',
                'y': '50',
                'width': '20',
            },
        },
        'checkBox': {
            'checkBox1': {
                'text': 'aaa',
                'x': '400',
                'y': '10',
                'items': ['aaa', 'bbb'],
            },
            'checkBox2': {
                'text': 'bbb',
                'x': '500',
                'y': '10',
                'items': ['ccc', 'ddd'],
            },
        },
        'comboBox': {
            'comboBox1': {
                'text': 'aaa',
                'x': '600',
                'y': '10',
                'items': ['aaa', 'bbb'],
            },
            'comboBox2': {
                'text': 'bbb',
                'x': '600',
                'y': '50',
                'items': ['ccc', 'ddd'],
            },
        },
        'text': {
            'text1': {
                'text': 'aaa',
                'x': '10',
                'y': '100',
                'height': '100',
                'width': '300',
            },
            'text2': {
                'text': 'bbb',
                'x': '350',
                'y': '100',
                'height': '100',
                'width': '300',
            },
        },
    }


if __name__ == '__main__':
    tks = TkSample()
    tkm = TkManager.TkManager(tks.tkInfo)
