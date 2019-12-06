#!/usr/bin/python

import sys
import os
import pprint


def implode(list, glue):
    print("implode")
    print(list)


def if_save(header, split_string):
    is_save = False
    if header == "sl" and split_string == ":":
        is_save = True
    elif header == "local_address" and split_string == " ":
        print(split_string)
        is_save = True
    elif header == "rem_address" and split_string == " ":
        is_save = True
    elif header == "st" and split_string == " ":
        is_save = True
    elif header == "tx_queue" and split_string == ":":
        is_save = True
    elif header == "rx_queue" and split_string == " ":
        is_save = True
    elif header == "tr" and split_string == ":":
        is_save = True
    elif header == "tm->when" and split_string == " ":
        is_save = True
    elif header == "retrnsmt" and split_string == " ":
        is_save = True
    elif header == "uid" and split_string == " ":
        is_save = True
    elif header == "timeout" and split_string == " ":
        is_save = True

    return is_save


def line_parse(headers, line_str):
    #print(headers)
    pairs = {}
    get_cnt = 0
    tmp_s = ""
    for s in line_str:
        if len(tmp_s) > 0:
            header = headers[get_cnt]
            if if_save(header, s):
                pairs[header] = tmp_s
                get_cnt += 1
                tmp_s = ""
            else:
                tmp_s += s
        else:
            if s != " ":
                tmp_s += s

    header = headers[get_cnt]
    pairs[header] = tmp_s

    #pair_datas[headers[get_cnt]] = tmp_s
    pprint.pprint(pairs)



def string_strip(org_str, glue):
    splits = []
    tmp_s = ""
    for s in org_str:
        if s == glue:
            if len(tmp_s) > 0:
                splits.append(tmp_s)
                tmp_s = ""
        else:
            tmp_s += s

    if len(tmp_s) > 0:
        splits.append(tmp_s)

    return splits


def run():
    files = ["/proc/net/tcp"]

    for file in files:
        if os.path.isfile(file):
            with open(file) as fo:
                cnt = 0
                headers = []
                while True:
                    contents = fo.readline()
                    #print(contents)
                    if contents == "":
                        break
                    else:
                        if cnt == 0:
                            headers = string_strip(contents.strip(), " ")
                            cnt += 1
                        else:
                            line_parse(headers, contents.strip())

                fo.close()


if __name__ == "__main__":
    run()
    sys.exit(0)
