#!/bin/bash

# Download all logs

#
# To use this file
#
#  curl "http://fakebaseurl.com/download-logs.sh" | bash
#
# Logs will be copied in a temporary directory as described in the
# output.  Set DOWNLOAD_DIR to an empty directory if you wish to
# override this.
#

BASE_URL=http://fakebaseurl.com

function log {
    echo "$(date -Iseconds) | $@"
}

function save_file {
    local file="$1"

    curl -s --compressed --create-dirs -o "${file}" "${BASE_URL}/${file}"

    # Using --compressed we will send an Accept-Encoding: gzip header
    # and the data will come to us across the network compressed.
    # However, sometimes things like OpenStack's log server will send
    # .gz files (as stored on its disk) uncompressed, so we check if
    # this really looks like an ASCII file and rename for clarity.
    if [[ "${file}" == *.gz ]]; then
        local type=$(file "${file}")
        if [[ "${type}" =~ "ASCII text" ]] || [[ "${type}" =~ "Unicode text" ]]; then
            local new_name=${file%.gz}
            log "Renaming to ${new_name}"
            mv "${file}" "${new_name}"
        fi
    fi

}

if [[ -z "${DOWNLOAD_DIR}" ]]; then
    DOWNLOAD_DIR=$(mktemp -d --tmpdir zuul-logs.XXXXXX)
fi
log "Saving logs to ${DOWNLOAD_DIR}"

pushd "${DOWNLOAD_DIR}" > /dev/null



log "Getting ${BASE_URL}/job-output.json                                                                  [ 0001 / 0010 ]"
save_file "job-output.json"

log "Getting ${BASE_URL}/controller/compressed.gz                                                         [ 0002 / 0010 ]"
save_file "controller/compressed.gz"

log "Getting ${BASE_URL}/controller/cpu-load.svg                                                          [ 0003 / 0010 ]"
save_file "controller/cpu-load.svg"

log "Getting ${BASE_URL}/controller/journal.xz                                                            [ 0004 / 0010 ]"
save_file "controller/journal.xz"

log "Getting ${BASE_URL}/controller/service_log.txt                                                       [ 0005 / 0010 ]"
save_file "controller/service_log.txt"

log "Getting ${BASE_URL}/controller/syslog                                                                [ 0006 / 0010 ]"
save_file "controller/syslog"

log "Getting ${BASE_URL}/controller/subdir/foo::3.txt                                                     [ 0007 / 0010 ]"
save_file "controller/subdir/foo::3.txt"

log "Getting ${BASE_URL}/controller/subdir/subdir.txt                                                     [ 0008 / 0010 ]"
save_file "controller/subdir/subdir.txt"

log "Getting ${BASE_URL}/zuul-info/inventory.yaml                                                         [ 0009 / 0010 ]"
save_file "zuul-info/inventory.yaml"

log "Getting ${BASE_URL}/zuul-info/zuul-info.controller.txt                                               [ 0010 / 0010 ]"
save_file "zuul-info/zuul-info.controller.txt"


popd >/dev/null

log "Download complete!"