from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from platform import python_version,architecture
import os
import time
import chardet

class AboutDialog(Toplevel):
    """Modal about dialog for PsiView

    """
    def __init__(self, parent, title=None, *, _htest=False, _utest=False):
        """Create popup, do not return until tk widget destroyed.

        parent - parent of this dialog
        title - string which is title of popup dialog
        _htest - bool, change box location when running htest
        _utest - bool, don't wait_window when running unittest
        """
        Toplevel.__init__(self, parent)
        self.configure(borderwidth=5)
        # place dialog below parent if running htest
        self.geometry("+%d+%d" % (
                        parent.winfo_rootx()+30,
                        parent.winfo_rooty()+(30 if not _htest else 100)))
        self.bg = "#bbbbbb"
        self.fg = "#000000"
        self.create_widgets()
        self.resizable(height=False, width=False)
        self.title(title or
                   f'关于 Psi视图 {python_version()} ({self.build_bits()} bit)')
        self.transient(parent)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.ok)
        self.parent = parent
        self.button_ok.focus_set()
        self.bind('<Return>', self.ok)  # dismiss dialog
        self.bind('<Escape>', self.ok)  # dismiss dialog
        self._current_textview = None
        self._utest = _utest

        if not _utest:
            self.deiconify()
            self.wait_window()

    def build_bits(self):
        "Return bits for platform."
        if sys.platform == 'darwin':
            return '64' if sys.maxsize > 2**32 else '32'
        else:
            return architecture()[0][:2]

    def create_widgets(self):
        frame = Frame(self, borderwidth=2, relief=SUNKEN)
        frame_buttons = Frame(self)
        frame_buttons.pack(side=BOTTOM, fill=X)
        frame.pack(side=TOP, expand=True, fill=BOTH)
        self.button_ok = Button(frame_buttons, text='Close',
                                command=self.ok)
        self.button_ok.pack(padx=5, pady=5)

        frame_background = Frame(frame, bg=self.bg)
        frame_background.pack(expand=True, fill=BOTH)

        header = Label(frame_background, text='PsiView', fg=self.fg,
                       bg=self.bg, font=('courier', 24, 'bold'))
        header.grid(row=0, column=0, sticky=E, padx=10, pady=10)

        tk_patchlevel = self.tk.call('info', 'patchlevel')
        ext = '.png' if tk_patchlevel >= '8.6' else '.gif'

        byline_text = "Java 源码读取" + 5*'\n'
        byline = Label(frame_background, text=byline_text, justify=LEFT,
                       fg=self.fg, bg=self.bg)
        byline.grid(row=2, column=0, sticky=W, columnspan=3, padx=10, pady=5)
        email = Label(frame_background, text='email:  1806620741@qq.com',
                      justify=LEFT, fg=self.fg, bg=self.bg)
        email.grid(row=6, column=0, columnspan=2, sticky=W, padx=10, pady=0)
        docs = Label(frame_background, text='https://github.com' +
                     python_version()[:3] + '/LY1806620741/Psiview',
                     justify=LEFT, fg=self.fg, bg=self.bg)
        docs.grid(row=7, column=0, columnspan=2, sticky=W, padx=10, pady=0)

        Frame(frame_background, borderwidth=1, relief=SUNKEN,
              height=2, bg=self.bg).grid(row=8, column=0, sticky=EW,
                                         columnspan=3, padx=5, pady=5)

        pyver = Label(frame_background,
                      text='Python version:  ' + python_version(),
                      fg=self.fg, bg=self.bg)
        pyver.grid(row=9, column=0, sticky=W, padx=10, pady=0)
        tkver = Label(frame_background, text='Tk version:  ' + tk_patchlevel,
                      fg=self.fg, bg=self.bg)
        tkver.grid(row=9, column=1, sticky=W, padx=2, pady=0)
        py_buttons = Frame(frame_background, bg=self.bg)
        py_buttons.grid(row=10, column=0, columnspan=2, sticky=NSEW)
        self.py_license = Button(py_buttons, text='License', width=8,
                                 highlightbackground=self.bg,
                                 command=self.show_py_license)
        self.py_license.pack(side=LEFT, padx=10, pady=10)
        self.py_copyright = Button(py_buttons, text='Copyright', width=8,
                                   highlightbackground=self.bg,
                                   command=self.show_py_copyright)
        self.py_copyright.pack(side=LEFT, padx=10, pady=10)
        self.py_credits = Button(py_buttons, text='Credits', width=8,
                                 highlightbackground=self.bg,
                                 command=self.show_py_credits)
        self.py_credits.pack(side=LEFT, padx=10, pady=10)

        Frame(frame_background, borderwidth=1, relief=SUNKEN,
              height=2, bg=self.bg).grid(row=11, column=0, sticky=EW,
                                         columnspan=3, padx=5, pady=5)

        idlever = Label(frame_background,
                        text='PsiView version:   ' + python_version(),
                        fg=self.fg, bg=self.bg)
        idlever.grid(row=12, column=0, sticky=W, padx=10, pady=0)
        idle_buttons = Frame(frame_background, bg=self.bg)
        idle_buttons.grid(row=13, column=0, columnspan=3, sticky=NSEW)
        self.readme = Button(idle_buttons, text='README', width=8,
                             highlightbackground=self.bg,
                             command=self.show_readme)
        self.readme.pack(side=LEFT, padx=10, pady=10)
        self.idle_news = Button(idle_buttons, text='NEWS', width=8,
                                highlightbackground=self.bg,
                                command=self.show_idle_news)
        self.idle_news.pack(side=LEFT, padx=10, pady=10)
        self.idle_credits = Button(idle_buttons, text='Credits', width=8,
                                   highlightbackground=self.bg,
                                   command=self.show_idle_credits)
        self.idle_credits.pack(side=LEFT, padx=10, pady=10)

    # License, copyright, and credits are of type _sitebuiltins._Printer
    def show_py_license(self):
        "Handle License button event."
        self.display_printer_text('About - License', license)

    def show_py_copyright(self):
        "Handle Copyright button event."
        self.display_printer_text('About - Copyright', copyright)

    def show_py_credits(self):
        "Handle Python Credits button event."
        self.display_printer_text('About - Python Credits', credits)

    # Encode CREDITS.txt to utf-8 for proper version of Loewis.
    # Specify others as ascii until need utf-8, so catch errors.
    def show_idle_credits(self):
        "Handle Idle Credits button event."
        self.display_file_text('About - Credits', 'CREDITS.txt', 'utf-8')

    def show_readme(self):
        "Handle Readme button event."
        self.display_file_text('About - Readme', 'README.txt', 'ascii')

    def show_idle_news(self):
        "Handle News button event."
        self.display_file_text('About - NEWS', 'NEWS.txt', 'utf-8')

    def display_printer_text(self, title, printer):
        """Create textview for built-in constants.

        Built-in constants have type _sitebuiltins._Printer.  The
        text is extracted from the built-in and then sent to a text
        viewer with self as the parent and title as the title of
        the popup.
        """
        printer._Printer__setup()
        text = '\n'.join(printer._Printer__lines)
        self._current_textview = textview.view_text(
            self, title, text, _utest=self._utest)

    def display_file_text(self, title, filename, encoding=None):
        """Create textview for filename.

        The filename needs to be in the current directory.  The path
        is sent to a text viewer with self as the parent, title as
        the title of the popup, and the file encoding.
        """
        fn = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
        self._current_textview = textview.view_file(
            self, title, fn, encoding, _utest=self._utest)

    def ok(self, event=None):
        "Dismiss help_about dialog."
        self.grab_release()
        self.destroy()

class PsiView():
    def __init__(self):
        self.root=Tk()
        self.root.title("PsiView")
        self.popupmenu=None
        self.UIinit()
        self.charset=None
    def openfile(self):
        """打开文件"""
        filename=filedialog.askopenfilename(filetypes=[('java file','*.java'),('All files','*.*')])
        with open(filename,'rb') as f:
            b=f.read()
            self.charset=chardet.detect(b)['encoding']
            self.text.insert(INSERT,b.decode(self.charset))
    #保存文件函数
    def savefileas(self):
        filename=filedialog.asksaveasfilename(filetypes=[('java file','*.java')])
        with open(filename,'w') as f:
            f.write(self.text.get())
    def nodefined(self):
        pass
    #退出文档函数
    def quit(self):
        self.root.destroy()

    def about(self):
        AboutDialog(self.root)

    def callback(self):
        self.text.edit_undo()

    #右键菜单显示函数
    def popup(self,event):
        self.popupmenu.post(event.x_root,event.y_root)

    def UIinit(self):
        """初始化界面"""
        #文字编辑区text
        self.text=Text(self.root,width=90,height=40,selectforeground="black",undo=True,font=50)
        self.text.pack()
        #顶级菜单窗口
        topmenu=Menu(self.root)

        #创建文件下拉菜单，添加到顶层菜单窗口
        filemenu=Menu(topmenu,tearoff=False)

        #添加下拉内容：

        filemenu.add("command",label="打开",command=self.openfile)
        filemenu.add_command(label="保存",command=self.savefileas)
        filemenu.add_command(label="另存为",command=self.savefileas)
        filemenu.add_separator()
        filemenu.add_command(label="退出",command=quit)
        topmenu.add_cascade(label="文件", menu=filemenu)

        #创建编辑菜单
        editmenu=Menu(topmenu,tearoff=False)

        #创建编辑下拉内容
        editmenu.add_separator()
        editmenu.add_command(label="查找",command=self.nodefined)
        editmenu.add_command(label="替换",command=self.nodefined)

        topmenu.add_cascade(label="编辑",menu=editmenu)

        #创建帮助菜单
        helpmenu=Menu(topmenu,tearoff=False)
        helpmenu.add_command(label="关于笔记本",command=self.about)

        topmenu.add_cascade(label="帮助",menu=helpmenu)

        #右键菜单栏
        self.popupmenu=Menu(self.root,tearoff=False)
        self.popupmenu.add("command",label="剪切",command=self.nodefined)
        self.popupmenu.add_command(label="复制",command=self.nodefined)
        self.popupmenu.add_command(label="粘贴",command=self.nodefined)
        self.popupmenu.add("command",label="删除",command=self.nodefined)
        self.text.bind("<Button-3>",self.popup)

        #跟窗口显示菜单栏
        self.root.config(menu=topmenu)


        mainloop()
PsiView()