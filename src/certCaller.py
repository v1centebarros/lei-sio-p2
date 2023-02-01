from utils.Auth import CC
import os
import click

#  GUARDAR O CERTIFICADO DE UM CALLER NUMA Pasta
def save_cert(cert, path):
    with open(path, "wb") as f:
        f.write(cert)

#  VERFICAR SE O CERFICADO ESTA NA PASTA

def check_cert(path):
    
    return os.path.isfile(path)

@click.command()
@click.option('--pin', '-p', help='Pin of the cc')
def main(pin):
    if pin is None:
        print("Pin is needed")
        return
    cc = CC(pin)
    cert = cc.get_cc_cert()
    cert = bytes.fromhex(cert)
    save_cert(cert, "caller_cert.pem")
    print(check_cert("caller_cert.pem"))

if __name__ == "__main__":
    main()