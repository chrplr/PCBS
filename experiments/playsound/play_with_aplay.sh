#! /bin/sh
# Time-stamp: <2024-06-28 11:22:23 christophe@pallier.org>


DLP_IO8="/dev/ttyUSB0"
# Note: you need to run once the following commands to access the DLP_IO8
# sudo modprobe ftdi_sio
# sudo chmod o+rw $DLP_IO8


# to determine the address of the audio device, use 'aplay -L'
AUDIO_DEVICE="plughw:CARD=USB,DEV=0"
BUFFER_SIZE=4096

init_dlp_io8 () {
    stty -F $DLP_IO8 115200 raw -echo
}


send_ttl_for_10ms () {
    echo "1" > $DLP_IO8
    sleep 0.01s  # approximately 10ms
    echo "Q" > $DLP_IO8 
}


play_sound_on_focusrite () {
    pasuspender -- aplay -D $AUDIO_DEVICE --dump-hw-params --buffer-size=$BUFFER_SIZE -vv "$@"
}

### main
init_dlp_io8
send_ttl_for_10ms
play_sound_on_focusrite "$@"
send_ttl_for_10ms
