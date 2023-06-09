import PySimpleGUI as sg
import subprocess, threading, os, signal, re
import i18n

class sound_gui:
    def __init__(self):
        sg.theme('DarkBlue3')
        window = sg.Window('sound-helper by aiczk', self.layout())

        while True:
            event, value = window.read()
            if event == sg.WIN_CLOSED:
                break
            
            if event == 'start':
                if hasattr(self, 'stop_event'):
                    self.stop_event.set()
                self.stop_event = threading.Event()

                threading.Thread(target=self.execute_command, args=(f'python sound.py {self.parse_args(value)}', window, self.stop_event)).start()
                self.print(window, 'Loading...')

            if event == 'stop':
                if hasattr(self, 'stop_event') and not self.stop_event.is_set():
                    self.stop_event.set()
        
        if hasattr(self, 'stop_event'):
            self.stop_event.set()
        
        window.close()

    def execute_command(self, cmd, window, stop_event):
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, start_new_session=True)
        while not stop_event.is_set():
            line = process.stdout.readline()
            if line == b'' and process.poll() is not None:
                break
            if line:
                self.print(window, re.sub(r'^[^\]]*[\]]', "Current Status:\n", line.decode('utf-8').strip('\n').strip('\r')), end='\r')
                window.Refresh()
        
        if stop_event.is_set():
            os.kill(process.pid, signal.SIGTERM)
        process.wait()
        self.print(window, 'Stopped.') if stop_event.is_set() else self.print(window, 'Finished.')
    
    def print(self, window, msg: str, end='\r'):
        window['output'].update('')
        print(msg, end=end)
    
    def parse_args(self, value: dict) -> str:
        args = ''
        args += f'--input "{value["input_dir"]}" ' if value['input_dir'] else ''
        args += f'--output "{value["output_dir"]}" ' if value['output_dir'] else ''
        args += f'--iformat "{value["iformat"]}" ' if value['iformat'] else ''
        args += f'--oformat "{value["oformat"]}" ' if value['oformat'] else ''
        args += f'--prefix "{value["prefix"]}" ' if value['prefix'] else ''
        args += f'--filename "{value["filename"]}" ' if value['filename'] else '' 
        args += f'--silence {value["silence"]} ' if value['silence'] else '' 
        args += f'--threshold {value["threshold"]} ' if value['threshold'] else ''
        args += f'--samplerate {value["sample_rate"]} ' if value['sample_rate'] else ''
        args += f'--loudness {value["loudness"]} ' if value['loudness'] else ''
        args += f'--highpass {value["highpass"]} ' if value['highpass'] else ''
        args += f'--lowpass {value["lowpass"]} ' if value['lowpass'] else ''
        args += f'--skip {value["skip"]} ' if value['skip'] else ''
        args += f'--merge {value["merge"]} ' if value['merge'] else ''
        args += f'--split {value["split"]} ' if value['split'] else ''
        args += '--combine 1 ' if value['combine'] else ''
        args += '--reverse 1 ' if value['reverse'] else ''
        args += '--invert 1 ' if value['invert'] else ''
        args += '--channel 1 ' if value['mono'] else '--channel 2 ' if value['stereo'] else ''
        return args
    
    def layout(self) -> list:
        return [
            [
                sg.Frame(i18n('Directory Setting'), 
                [
                    [sg.Text(i18n('Input directory:')), sg.InputText(key='input_dir'), sg.FolderBrowse()],
                    [sg.Text(i18n('Output directory:')), sg.InputText(key='output_dir'), sg.FolderBrowse()]
                ])
            ],
            [
                [
                    sg.Frame(i18n('File Setting'),
                    [
                        [
                            sg.Text(i18n('Input file format:')), sg.Combo(['wav','mp3'], default_value='wav', key='iformat'),
                            sg.Text(i18n('Output file format:')), sg.Combo(['wav','mp3'], default_value='wav', key='oformat')
                        ],
                        [
                            sg.Text(i18n('File prefix:')), sg.InputText(size=(20, 50), key='prefix'), 
                            sg.Text(i18n('File name:')), sg.InputText(size=(20, 50), key='filename')
                        ],
                    ])
                ],
                [
                    sg.Frame(i18n('Silence Setting'),
                    [
                        [
                            sg.Text(i18n('Silence length:')), sg.InputText(size=(5, 50), default_text=200, key='silence'), sg.Text('ms'),
                            sg.Text(i18n('Silence threshold:')), sg.InputText(size=(5, 50), default_text=-40, key='threshold'), sg.Text('dB')
                        ],
                    ])
                ],
                [
                    sg.Frame(i18n('Optional Setting'),
                    [
                        [
                            sg.Text(i18n('Sample rate:')), sg.InputText(size=(5, 50), default_text=44100, key='sample_rate'), sg.Text('Hz'), 
                            sg.Radio(i18n('Mono'), 'channel', key='mono'), 
                            sg.Radio(i18n('Stereo'), 'channel', key='stereo')
                        ],
                        [sg.Text(i18n('Loudness normalization:')), sg.InputText(size=(5, 50), default_text=-14, key='loudness'), sg.Text('dB'),],
                        [
                            sg.Text(i18n('High pass:')), sg.InputText(size=(5, 50), key='highpass'), sg.Text('Hz'),
                            sg.Text(i18n('Low pass:')), sg.InputText(size=(5, 50), key='lowpass'), sg.Text('Hz')
                        ],
                        [
                            sg.Text(i18n('Skip less than')), sg.InputText(size=(5, 50), default_text=1000, key='skip'), sg.Text(i18n('ms skip')),
                            sg.Text(i18n('Merge less than')), sg.InputText(size=(5, 50), default_text=5000, key='merge'), sg.Text(i18n('ms merge')),
                            sg.Text(i18n('Split more than')), sg.InputText(size=(5, 50), default_text=10000, key='split'), sg.Text(i18n('ms split'))
                        ],
                        [
                            sg.Checkbox(i18n('Invert phase'), key='invert'),
                            sg.Checkbox(i18n('Reverse audio'), key='reverse'),
                            sg.Checkbox(i18n('Combine all'), key='combine'),
                        ]
                    ])
                ],
            ],
            [sg.Button('(Re)Start', key='start'), sg.Button('Stop', key='stop')],
            [sg.Output(size=(76, 2), key='output', expand_x=True)]
        ]
    

        

if __name__ == '__main__':
    i18n = i18n.I18nAuto()
    gui = sound_gui()