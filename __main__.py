import argparse
from templater.templater import Templater

parser = argparse.ArgumentParser(description='Generates template code')

parser.add_argument('-p',
                    '--path',
                    metavar='PATH',
                    default='./test',
                    help='relative path to template placement directory'
                    )
parser.add_argument('-t',
                    '--templates',
                    metavar='TEMPLATES',
                    default='./templates',
                    help='relative path to templates folder'
                    )

parser.add_argument('-n',
                    '--name',
                    metavar='NAME',
                    required=True,
                    help='Component name'
                    )

parser.add_argument('--pattern',
                    metavar='PATTERN',
                    default='%Name%',
                    help='Naming pattern for replacement'
                    )

args = parser.parse_args()

app = Templater(**vars(args))

try:
    app.generate_template()
    print "Component created"
except Exception as e:
    print """Something wen't wrong, check params provided,
            should be strings investigate the code or contact the developer"""
    print str(e)

