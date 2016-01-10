#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Example:
    ./peeringmatcher.py <asn1> <asn2>
"""

import argparse
import json
import sys
import time

from prettytable import PrettyTable
import paramiko

from PeeringDB import *


def parseArguments():
    """Parse command line arguments"""
    def ASN(value):
        ivalue = int(value)
        if ivalue < 0:
             raise argparse.ArgumentTypeError("%s is not a valid ASN" % value)
        return ivalue
    parser = argparse.ArgumentParser(
        description = __doc__,
        formatter_class = argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('asn1', type = ASN)
    parser.add_argument('asn2', type = ASN)
    return parser.parse_args()


def printTable(asn1, asn2):
    """Print table for two ASNs"""
    # Create a pretty table
    x = PrettyTable(["IXLAN", "ASN", "IPv4", "IPv6"])
    x.padding_width = 1

    # Populate the table
    for key in set(asn1['result'].keys()) & set(asn2['result'].keys()):
        # Map IX number to human readable
        ix = mapIdToIx(str(key))
        x.add_row([ix, asn1['asn'], asn1['result'][key]['ipv4'], asn1["result"][key]['ipv6']])
        x.add_row([ix, asn1['asn'], asn2['result'][key]['ipv4'], asn2['result'][key]['ipv6']])
        # How do I make an empty row!? Ugly below...
        x.add_row(["", "", "", ""])
    # Print pretty table
    print x


def main():
    args = parseArguments()
    asn1 = getPeeringDetails(args.asn1)
    asn2 = getPeeringDetails(args.asn2)
    printTable(asn1, asn2)


if __name__ == '__main__':
    main()
