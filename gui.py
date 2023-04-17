import PySimpleGUI as sg
import subprocess, threading, os, signal, re

class sound_gui:
    def __init__(self):
        sg.theme('DarkAmber')
        window = sg.Window('sound-helper by aiczk', self.layout())

        while True:
            event, value = window.read()
            if event == sg.WIN_CLOSED:
                break
            
            if event == 'start':
                window['status'].update('Status: Running.')
                self.stop_event = threading.Event()
                threading.Thread(target=self.run_cmd, args=(f'python sound.py {self.parse_args(value)}', window, self.stop_event)).start()

            if event == 'stop':
                window['status'].update('Status: Stopped.')
                self.stop_event.set()
        
        self.stop_event.set()
        window.close()

    def layout(self) -> list:
        return [
            [
                sg.Frame('Directory Setting', 
                [
                    [sg.Text('Input directory:   '), sg.InputText(key='input_dir'), sg.FolderBrowse()],
                    [sg.Text('Output directory:'), sg.InputText(key='output_dir'), sg.FolderBrowse()]
                ])
            ],
            [
                [
                    sg.Frame('File Setting',
                    [
                        [
                            sg.Text('Input file format:'), sg.Combo(['wav','mp3'], default_value='wav', key='iformat'),
                            sg.Text('Output file format:'), sg.Combo(['wav','mp3'], default_value='wav', key='oformat')
                        ],
                        [
                            sg.Text('File prefix(optional):'), sg.InputText(size=(20, 50), key='prefix'), 
                            sg.Text('File name:'), sg.InputText(size=(20, 50), default_text='audio', key='filename')
                        ],
                    ])
                ],
                [
                    sg.Frame('Silence Setting',
                    [
                        [
                            sg.Text('Silence length:'), sg.InputText(size=(5, 50), key='silence'), sg.Text('ms'),
                            sg.Text('Silence threshold:'), sg.InputText(size=(5, 50), key='threshold'), sg.Text('ms')
                        ],
                    ])
                ],
                [
                    sg.Frame('Optional Setting',
                    [
                        [
                            sg.Text('Sample rate:'), sg.InputText(size=(5, 50), key='sample_rate'), sg.Text('Hz'), 
                            sg.Radio('Mono', 'channel', key='mono'), sg.Radio('Stereo', 'channel', key='stereo')
                        ],
                        [sg.Text('Loudness normalization:'), sg.InputText(size=(5, 50), key='loudness'), sg.Text('dB'),],
                        [
                            sg.Text('High pass:'), sg.InputText(size=(5, 50), key='highpass'), sg.Text('Hz'),
                            sg.Text('Low pass:'), sg.InputText(size=(5, 50), key='lowpass'), sg.Text('Hz')
                        ],
                        [
                            sg.Text('Skip less than'), sg.InputText(size=(5, 50), key='skip'), sg.Text('ms'),
                            sg.Text('Merge less than'), sg.InputText(size=(5, 50), key='merge'), sg.Text('ms'),
                            sg.Text('Split more than'), sg.InputText(size=(5, 50), key='split'), sg.Text('ms'),
                        ],
                        [
                            sg.Checkbox('Invert phase', key='invert'),
                            sg.Checkbox('Reverse audio', key='reverse'),
                            sg.Checkbox('Combine all', key='combine'),
                        ]
                    ])
                ],
            ],
            [sg.Button('(Re)Start', key='start'), sg.Button('Stop', key='stop'), sg.Text('Status: Stopped.', key='status')],
            [sg.Output(size=(76, 2), key='output')]
        ]
    
    def run_cmd(self, cmd, window, stop_event):
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, start_new_session=True)
        while not stop_event.is_set():
            line = process.stdout.readline()
            if line == b'' and process.poll() is not None:
                break
            if line:
                window['output'].update('')
                print(re.sub(r'^[^#\]]*[\]]', "Current Status:\n", line.decode('utf-8').strip('\n')), end='\r')
                window.Refresh()
        
        os.kill(process.pid, signal.SIGTERM)
        process.wait()
    
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
        

if __name__ == '__main__':
    gui = sound_gui()