# -*- coding: utf-8 -*-
"""
Created on 26.02.18 9:31

All information about module that must go to docs

.. py:module:: compare_csv
    :synopsis: Synopsis for this module.
               Multiline synopsis.

.. moduleauthor:: Roman Shuvalov <rshuvalov@abtronics.ru>
"""
from __future__ import unicode_literals
from __future__ import absolute_import

import os
import csv
import locale
import argparse
import pprint


def get_csv_list(file_path):
    """Acquire list of string from target csv file

    :param file_path:
    :return:
    """
    result = []
    with open(file_path, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        for index, row in enumerate(csv_reader):
            if index == 0:
                continue
            result.append(''.join(row).strip())
    return result

if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)
    locale.setlocale(locale.LC_ALL, '')
    desc = (
        'Script reads target csv file and then checks every csv file in check location with strings in target csv file.'
        'Results are printed with filename and list of equal strings'
    )
    config = argparse.ArgumentParser(prog='csv_target_compare', description=desc)
    config.add_argument('target', type=str, help='path to target csv file', metavar='PATH')
    config.add_argument('check', type=str, help='path to folder with csv to compare target with', metavar='PATH')
    console_options = config.parse_args()
    target_path = console_options.target
    check_path = console_options.check
    print('{} target path'.format(target_path))
    print('{} check path'.format(check_path))
    if not os.path.exists(target_path):
        print('{} do not exists'.format(target_path))
        exit(1)
    if not os.path.exists(check_path):
        print('{} do not exists'.format(check_path))
        exit(1)
    target_list = get_csv_list(target_path)
    if len(target_list) == 0:
        print('No lines were readed from {}'.format(target_path))
        exit(1)
    print('Target lines')
    pp.pprint(target_list)
    for check_file_name in os.listdir(check_path):
        check_file = os.path.join(check_path, check_file_name)
        print('Checking {} now'.format(check_file))
        check_file_list = get_csv_list(check_file)
        intersection = [element for element in check_file_list if element in target_list]
        print('Intersections are:')
        pp.pprint(intersection)
    print('Done.')
    exit(0)

