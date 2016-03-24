#!/bin/bash

dig +nocmd $1 soa @$2 +noall +answer > /tmp/record.txt
