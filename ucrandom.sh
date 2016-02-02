#!/bin/sh

error() {
   echo "$@"
   exit 1
}

PKG=ucrandom
[ -r "/etc/default/${PKG}" ] && . "/etc/default/${PKG}"
[ -z "${DEVICE}" ] && DEVICE="/dev/urandom"
[ -z "${PORT}" ] && PORT="4711"
[ -z "${HOST}" ] && HOST="$1"
[ -z "${HOST}" ] && error "Missing require argument: hostname"

sleep_time=1
while true; do
   avail="$(cat /proc/sys/kernel/random/entropy_avail)"
   echo $avail
   if [ ${avail} -lt 2048 ]; then
        data=$(nc -w 10 ${HOST} ${PORT})
        printf "got %s bytes\n" ${#data}
        if [ ${#data} -gt 1000 ]; then
           printf "%s" "${data}" > ${DEVICE}
           sleep_time=$(expr ${sleep_time} - 1)
           if [ ${sleep_time} -lt 1 ]; then
               sleep_time=1
           fi
        fi
    else
        sleep_time=$(expr ${sleep_time} + 1)
        if [ ${sleep_time} -gt 600 ]; then
            sleep_time=600
        fi
    fi
    sleep ${sleep_time}
done
