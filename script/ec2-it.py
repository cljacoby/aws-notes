#!/usr/bin/env python3

import argparse
import sys
import subprocess

# stored defaults

priv_key_path = "/path/to/private/key.pem"
public_ip = "my-ec2-user-name"
ec2_user = "pub.ip.add.ress"

# use either parse_known_args, or sys.argv[1:] to handle first arg being python script itself
def get_args(argv=sys.argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-u",
                        "--user",
                        default = ec2_user,
                        help = "The user when SSHing into the EC2 instance")
    parser.add_argument("-a",
                        "--address",
                        default = public_ip,
                        help = "The public IPv4 address of the EC2 instance to SSH into.")
    parser.add_argument("-i",
                        "--identity",
                        default = priv_key_path,
                        help = "The .pem secrey key to use as identity file when SSHing")
    args = parser.parse_known_args(argv)
    return args

def main():
    args = get_args()
    subprocess.run([
        "ssh", f"{args.user}@{args.address}", "-i", args.identity   
    ])

if __name__ == "__main__":
    main()
