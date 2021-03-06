brd = {
    'name': ('StickIt! V1', 'StickIt! V2', 'StickIt! V3'),
    'port': {
        'pmod' : {
            'pm1' : {
                'd0': 'ch15',
                'd1': 'ch11',
                'd2': 'chclk',
                'd3': 'ch28',
                'd4': 'ch16',
                'd5': 'ch13',
                'd6': 'ch0',
                'd7': 'ch14',
            },
            'pm2' : {
                'd0': 'ch17',
                'd1': 'ch15',
                'd2': 'ch1',
                'd3': 'chclk',
                'd4': 'ch18',
                'd5': 'ch16',
                'd6': 'ch3',
                'd7': 'ch0',
            },
            'pm3' : {
                'd0': 'ch20',
                'd1': 'ch17',
                'd2': 'ch4',
                'd3': 'ch1',
                'd4': 'ch21',
                'd5': 'ch18',
                'd6': 'ch5',
                'd7': 'ch3',
            },
            'pm4' : {
                'd0': 'ch22',
                'd1': 'ch20',
                'd2': 'ch6',
                'd3': 'ch4',
                'd4': 'ch23',
                'd5': 'ch21',
                'd6': 'ch7',
                'd7': 'ch5',
            },
            'pm5' : {
                'd0': 'ch8',
                'd1': 'ch22',
                'd2': 'ch25',
                'd3': 'ch6',
                'd4': 'ch26',
                'd5': 'ch23',
                'd6': 'ch10',
                'd7': 'ch7',
            },
            'pm6' : {
                'd0': 'ch11',
                'd1': 'ch8',
                'd2': 'ch28',
                'd3': 'ch25',
                'd4': 'ch13',
                'd5': 'ch26',
                'd6': 'ch14',
                'd7': 'ch10',
            }
        },
        'dualpmod' : {
            'pm1+pm2' : {
                'd0': 'ch15',
                'd1': 'ch11',
                'd2': 'chclk',
                'd3': 'ch28',
                'd4': 'ch16',
                'd5': 'ch13',
                'd6': 'ch0',
                'd7': 'ch14',
                'd8': 'ch17',
                'd9': 'ch15',
                'd10': 'ch1',
                'd11': 'chclk',
                'd12': 'ch18',
                'd13': 'ch16',
                'd14': 'ch3',
                'd15': 'ch0',
            },
            'pm2+pm3' : {
                'd0': 'ch17',
                'd1': 'ch15',
                'd2': 'ch1',
                'd3': 'chclk',
                'd4': 'ch18',
                'd5': 'ch16',
                'd6': 'ch3',
                'd7': 'ch0',
                'd8': 'ch20',
                'd9': 'ch17',
                'd10': 'ch4',
                'd11': 'ch1',
                'd12': 'ch21',
                'd13': 'ch18',
                'd14': 'ch5',
                'd15': 'ch3',
            },
            'pm4+pm5' : {
                'd0': 'ch22',
                'd1': 'ch20',
                'd2': 'ch6',
                'd3': 'ch4',
                'd4': 'ch23',
                'd5': 'ch21',
                'd6': 'ch7',
                'd7': 'ch5',
                'd8': 'ch8',
                'd9': 'ch22',
                'd10': 'ch25',
                'd11': 'ch6',
                'd12': 'ch26',
                'd13': 'ch23',
                'd14': 'ch10',
                'd15': 'ch7',
            },
            'pm5+pm6' : {
                'd0': 'ch8',
                'd1': 'ch22',
                'd2': 'ch25',
                'd3': 'ch6',
                'd4': 'ch26',
                'd5': 'ch23',
                'd6': 'ch10',
                'd7': 'ch7',
                'd8': 'ch11',
                'd9': 'ch8',
                'd10': 'ch28',
                'd11': 'ch25',
                'd12': 'ch13',
                'd13': 'ch26',
                'd14': 'ch14',
                'd15': 'ch10',
            }
        },
        'wing' : {
            'wing1' : {
                'd0': 'ch3',
                'd1': 'ch18',
                'd2': 'ch1',
                'd3': 'ch17',
                'd4': 'ch0',
                'd5': 'ch16',
                'd6': 'chclk',
                'd7': 'ch15',
            },
            'wing2' : {
                'd0': 'ch7',
                'd1': 'ch23',
                'd2': 'ch6',
                'd3': 'ch22',
                'd4': 'ch5',
                'd5': 'ch21',
                'd6': 'ch4',
                'd7': 'ch20',
            },
            'wing3' : {
                'd0': 'ch14',
                'd1': 'ch13',
                'd2': 'ch28',
                'd3': 'ch11',
                'd4': 'ch10',
                'd5': 'ch26',
                'd6': 'ch25',
                'd7': 'ch8',
            }
        },
        'dualwing' : {
            'wing1+wing2' : {
                'd0': 'ch7',
                'd1': 'ch23',
                'd2': 'ch6',
                'd3': 'ch22',
                'd4': 'ch5',
                'd5': 'ch21',
                'd6': 'ch4',
                'd7': 'ch20',
                'd8': 'ch3',
                'd9': 'ch18',
                'd10': 'ch1',
                'd11': 'ch17',
                'd12': 'ch0',
                'd13': 'ch16',
                'd14': 'chclk',
                'd15': 'ch15',
            },
            'wing2+wing3' : {
                'd0': 'ch14',
                'd1': 'ch13',
                'd2': 'ch28',
                'd3': 'ch11',
                'd4': 'ch10',
                'd5': 'ch26',
                'd6': 'ch25',
                'd7': 'ch8',
                'd8': 'ch7',
                'd9': 'ch23',
                'd10': 'ch6',
                'd11': 'ch22',
                'd12': 'ch5',
                'd13': 'ch21',
                'd14': 'ch4',
                'd15': 'ch20',
            }
        },
        'xula' : {
            'default' : {
                'chclk' : 'chclk',
                'ch0' : 'ch0',
                'ch1' : 'ch1',
                'ch2' : 'ch2',
                'ch3' : 'ch3',
                'ch4' : 'ch4',
                'ch5' : 'ch5',
                'ch6' : 'ch6',
                'ch7' : 'ch7',
                'ch8' : 'ch8',
                'ch9' : 'ch9',
                'ch10' : 'ch10',
                'ch11' : 'ch11',
                'ch12' : 'ch12',
                'ch13' : 'ch13',
                'ch14' : 'ch14',
                'ch15' : 'ch15',
                'ch16' : 'ch16',
                'ch17' : 'ch17',
                'ch18' : 'ch18',
                'ch19' : 'ch19',
                'ch20' : 'ch20',
                'ch21' : 'ch21',
                'ch22' : 'ch22',
                'ch23' : 'ch23',
                'ch24' : 'ch24',
                'ch25' : 'ch25',
                'ch26' : 'ch26',
                'ch27' : 'ch27',
                'ch28' : 'ch28',
                'ch29' : 'ch29',
                'ch30' : 'ch30',
                'ch31' : 'ch31',
                'ch32' : 'ch32',
                'ch33' : 'ch33'
            }
        }
    }
}
