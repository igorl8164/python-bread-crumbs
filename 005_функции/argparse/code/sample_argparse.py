import argparse

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    parser = argparse.ArgumentParser(description='Videos to images')
    parser.add_argument('--indir', type=str, help='Input dir for videos')
    parser.add_argument('--outdir', type=str, help='Output dir for image')
    parser.add_argument('--ip', type=str, help='xxx.xxx.xxx.xxx')

    args = parser.parse_args()
    print(args)
    print(args.indir)
    print(args.outdir)
    print(args.ip)

# videos.py

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# python3 main.py --indir='klhfgh' --outdir='kllghws'
# Hi, PyCharm
# Namespace(indir="'klhfgh'", ip=None, outdir="'kllghws'")
# 'klhfgh'
# 'kllghws'
# None
