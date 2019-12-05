#!/usr/bin/python

import sys
import os


def line_parse(headers, line_str):
    print(headers)
    line_splits = string_strip(line_str.strip(), " ")
    for i in range(len(headers)):
        print("{0} = {1}".format(headers[i], line_splits[i]))


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
    print(splits)
    return splits


def run():
    files = ["/proc/net/tcp", "/proc/net/tcp6"]

    for file in files:
        if os.path.isfile(file):
            with open(file) as fo:
                cnt = 0
                headers = []
                while True:
                    contents = fo.readline()
                    if contents == "":
                        break
                    if cnt == 0:
                        headers = string_strip(contents.strip(), " ")
                        cnt += 1
                    else:
                        line_parse(headers, contents)

                fo.close()


if __name__ == "__main__":
    run()
