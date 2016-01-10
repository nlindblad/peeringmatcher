#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests


API_BASE_URL = 'https://beta.peeringdb.com/api/'

def getPeeringDetails(asn):
    """Get peering details for ASN"""
    request = requests.get(API_BASE_URL + 'asn/%s' % asn)
    json_data = request.json()
    result = {}
    for d in json_data['data']:
        for n in d['netixlan_set']:
            data = { 'ipv4': n['ipaddr4'], 'ipv6': n['ipaddr6']}
            result[n['ixlan_id']] = data
    return {"asn": asn, "result": result}


def mapIdToIx(ixlan_id):
    """Map IX number to human readable"""
    api_data = requests.get(API_BASE_URL + 'ixlan/%s' % ixlan_id)
    json_data = api_data.json()
    for x in json_data['data']:
        return x['ix']['name']
