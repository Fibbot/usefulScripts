##ropnop's docker aliases from https://blog.ropnop.com/docker-for-pentesters/
function dockershell() {    docker run --rm -i -t --entrypoint=/bin/bash "$@"}
function dockershellsh() {    docker run --rm -i -t --entrypoint=/bin/sh "$@"}
function dockershellhere() {    dirname=${PWD##*/}    docker run --rm -it --entrypoint=/bin/bash -v `pwd`:/${dirname} -w /${dirname} "$@"}
function dockershellshhere() {    docker run --rm -it --entrypoint=/bin/sh -v `pwd`:/${dirname} -w /${dirname} "$@"}
function dockerwindowshellhere() {    dirname=${PWD##*/}    docker -c 2019-box run --rm -it -v "C:${PWD}:C:/source" -w "C:/source" "$@"}
impacket() {    docker run --rm -it rflathers/impacket "$@"}
smbservehere() {    local sharename    [[ -z $1 ]] && sharename="SHARE" || sharename=$1    docker run --rm -it -p 445:445 -v "${PWD}:/tmp/serve" rflathers/impacket smbserver.py -smb2support $sharename /tmp/serve}
nginxhere() {    docker run --rm -it -p 80:80 -p 443:443 -v "${PWD}:/srv/data" rflathers/nginxserve}
webdavhere() {    docker run --rm -it -p 80:80 -v "${PWD}:/srv/data/share" rflathers/webdav}