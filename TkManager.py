# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:11:10 2019

@author: ouchiyam
"""

import tkinter
from tkinter import ttk


class TkManager:

    def __init__(self, tkInfoDict):
        """
        初期設定\n
        ・ウィンドウ設定\n
        ・画面作成\n
        """
        self.tkInfoDict = tkInfoDict

        self.root = tkinter.Tk()
        self.root.title(self.tkInfoDict['title'])
        self.root.geometry(self.tkInfoDict['geometry'])

        self.createUI()

        self.root.mainloop()

    def createUI(self):
        for name in self.tkInfoDict['label'].keys():
            self.createLabel(name)
        for name in self.tkInfoDict['entry'].keys():
            self.createEntry(name)
        for name in self.tkInfoDict['button'].keys():
            self.createButton(name)
        for name in self.tkInfoDict['checkBox'].keys():
            self.createCheckBoxList(name)
        for name in self.tkInfoDict['comboBox'].keys():
            self.createComboBox(name)
        for name in self.tkInfoDict['text'].keys():
            self.createText(name)

    def createLabel(self, labelName):
        """ラベル作成"""
        tkInfo = self.tkInfoDict['label'][labelName]
        tkInfo['obj'] = tkinter.Label(text=tkInfo['text'])
        tkInfo['obj'].place(x=tkInfo['x'], y=tkInfo['y'])
        self.tkInfoDict['label'][labelName].update(tkInfo)

    def createEntry(self, entryName):
        """エントリ作成"""
        tkInfo = self.tkInfoDict['entry'][entryName]
        tkInfo['obj'] = tkinter.Entry(
            width=tkInfo['width'])

        if entryName == 'sysNo':
            tkInfo['obj'].bind("<Return>", self.returnSysNo)

        tkInfo['obj'].place(x=tkInfo['x'], y=tkInfo['y'])
        self.tkInfoDict['entry'][entryName].update(tkInfo)

    def createComboBox(self, comboBoxName):
        """プルダウン作成"""
        tkInfo = self.tkInfoDict['comboBox'][comboBoxName]
        tkInfo['val'] = tkinter.StringVar()
        tkInfo['obj'] = ttk.Combobox(textvariable=tkInfo['val'])
        tkInfo['obj']['values'] = tuple(tkInfo['items'])
        tkInfo['obj'].set('')
        tkInfo['obj'].place(x=tkInfo['x'], y=tkInfo['y'])
        self.tkInfoDict['comboBox'][comboBoxName].update(tkInfo)

    def createCheckBoxList(self, checkBoxName):
        """チェックボックス作成"""
        tkInfo = self.tkInfoDict['checkBox'][checkBoxName]
        checkBoxList = []
        y = int(tkInfo['y'])
        for text in tkInfo['items']:
            checkBox = {}
            checkBox['text'] = text
            checkBox['bool'] = tkinter.BooleanVar()
            checkBox['bool'].set(False)
            checkBox['obj'] = tkinter.Checkbutton(
                text=text, variable=checkBox['bool'])
            checkBox['obj'].pack()
            checkBox['obj'].place(x=tkInfo['x'], y=y)
            checkBoxList.append(checkBox)
            y += 20
        tkInfo['checkBoxList'] = checkBoxList
        self.tkInfoDict['checkBox'][checkBoxName].update(tkInfo)

    def createText(self, textName):
        """text作成"""
        tkInfo = self.tkInfoDict['text'][textName]
        tkInfo['obj'] = tkinter.Text(self.root)
        tkInfo['obj'].place(x=tkInfo['x'], y=tkInfo['y'],
                            height=tkInfo['height'], width=tkInfo['width'])
        tkInfo['obj'].insert('1.0', tkInfo['text'])
        self.tkInfoDict['text'][textName].update(tkInfo)

    def createButton(self, buttonName):
        """ボタン作成"""
        tkInfo = self.tkInfoDict['button'][buttonName]
        tkInfo['obj'] = tkinter.Button(
            self.root, text=tkInfo['text'], width=tkInfo['width'])

        if buttonName == 'button1':
            tkInfo['obj'].bind("<Button-1>", self.pushedButton1)
        elif buttonName == 'button2':
            tkInfo['obj'].bind("<Button-1>", self.pushedButton2)

        tkInfo['obj'].pack()
        tkInfo['obj'].place(x=tkInfo['x'], y=tkInfo['y'])
        self.tkInfoDict['button'][buttonName].update(tkInfo)

    def getText(self, textName):
        """text取得"""
        return self.tkInfoDict['text'][textName]['obj'].get('1.0', 'end')

    def getCheckedList(self, checkBoxName):
        checkedList = []
        for checkBox in self.tkInfoDict['checkBox'][checkBoxName]['checkBoxList']:
            if checkBox['bool'].get() is True:
                checkedList.append(checkBox['text'])
        return checkedList

    def deleteCheckBoxList(self, checkBoxName):
        for checkBox in self.tkInfoDict['checkBox'][checkBoxName]['checkBoxList']:
            checkBox['obj'].destroy()
        self.tkInfoDict['checkBox'][checkBoxName]['checkBoxList'] = []

    def deleteButton(self, buttonName):
        if 'obj' in self.tkInfoDict['button'][buttonName]:
            self.tkInfoDict['button'][buttonName]['obj'].destroy()

    def deleteText(self, textName):
        if 'obj' in self.tkInfoDict['text'][textName]:
            self.tkInfoDict['text'][textName]['obj'].destroy()

    def allCheck(self, checkBoxName):
        """全選択ボタン押下時の処理"""
        checkBoxList = self.tkInfoDict['checkBox'][checkBoxName]['checkBoxList']
        for checkBox in checkBoxList:
            checkBox['bool'].set(True)

    def allClear(self, checkBoxName):
        """全解除ボタン押下時の処理"""
        checkBoxList = self.tkInfoDict['checkBox'][checkBoxName]['checkBoxList']
        for checkBox in checkBoxList:
            checkBox['bool'].set(False)

    def pushedButton1(self, event):
        print('pushed button1.')

    def pushedButton2(self, event):
        print('pushed button2.')


if __name__ == '__main__':
    pass
