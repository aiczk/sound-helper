import locale

LANGUAGE_LIST = ['en_US', 'ja_JP']
LANGUAGE_ALL = {
    'en_US': {
        'SUPER': 'en_US',
        'LANGUAGE': 'en_US',
        'Directory Setting': 'Directory Setting',
        'Input directory:' : 'Input directory:',
        'Output directory:': 'Output directory:',
        'File Setting': 'Open folder',
        'Input file format:': 'Input file format:',
        'Output file format:': 'Output file format:',
        'File prefix:': 'File prefix:',
        'File name:': 'File name:',
        'Silence Setting': 'Silence Setting',
        'Silence length:': 'Silence length:',
        'Silence threshold:': 'Silence threshold:',
        'Optional Setting': 'Optional Setting',
        'Sample rate:': 'Sample rate:',
        'Mono': 'Mono',
        'Stereo': 'Stereo',
        'Loudness normalization:': 'Loudness normalization:',
        'High pass:': 'High pass:',
        'Low pass:': 'Low pass:',
        'Skip less than': 'Skip less than',
        'Merge less than': 'Merge less than',
        'Split more than': 'Split more than',
        'ms skip': 'ms',
        'ms merge': 'ms',
        'ms split': 'ms',
        'Invert phase': 'Invert phase',
        'Reverse audio': 'Reverse audio',
        'Combine all': 'Combine all',
    },
    'ja_JP': {
        'SUPER': 'en_US',
        'LANGUAGE': 'ja_JP',
        'Directory Setting': 'ディレクトリ設定',
        'Input directory:' : '入力フォルダ:',
        'Output directory:': '出力フォルダ:',
        'File Setting': 'ファイル設定',
        'Input file format:': '入力ファイルフォーマット:',
        'Output file format:': '出力ファイルフォーマット:',
        'File prefix:': 'ファイルの接頭辞:',
        'File name:': 'ファイル名:',
        'Silence Setting': '無音設定',
        'Silence length:': '無音の長さ:',
        'Silence threshold:': '無音のしきい値:',
        'Optional Setting': 'オプション設定',
        'Sample rate:': 'サンプルレート:',
        'Mono': 'モノ',
        'Stereo': 'ステレオ',
        'Loudness normalization:': 'ラウドネス等化:',
        'High pass:': 'ハイパス:',
        'Low pass:': 'ローパス:',
        'Skip less than': '',
        'Merge less than': '',
        'Split more than': '',
        'ms skip': 'ミリ秒以下を除外',
        'ms merge': 'ミリ秒以下を結合',
        'ms split': 'ミリ秒以上を分割',
        'Invert phase': '逆位相',
        'Reverse audio': '逆再生',
        'Combine all': '出力ファイルを結合する',
    },
}

class I18nAuto:
    def __init__(self, language=None):
        if language is None:
            language = "auto"
        if language == "auto":
            language = locale.getdefaultlocale()[0]
        if language not in LANGUAGE_LIST:
            language = "en_US"
        self.language = language
    
    def __call__(self, key):
        return LANGUAGE_ALL[self.language][key]