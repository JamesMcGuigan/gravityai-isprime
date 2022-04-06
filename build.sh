#!/usr/bin/env bash
cd "$(dirname "${BASH_SOURCE[0]}")"  # cd current directory
set -x
file=gravity_is_prime.tar.gz; tar --exclude='.git' --exclude-from=.gitignore --exclude=$file -zcvf $file .

