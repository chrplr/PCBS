#!/bin/bash
#
# http://www.vdwalle.com/Norte/ppdiag.txt
#
# This script gather various information about the parallel port
# It also corrects common setting troubles
#

#
# check basic requirements
#
if [ ! -d /proc ];
then
	echo "This script cannot work without a /proc filesystem"
	exit
fi

#
# STEP 00: check if we are runnig as root
#
USER=`whoami`
if [ $USER != "root" ];
then
	echo " "
	echo "WARNING:"
	echo "You are not runnig this script as 'root'. Only a few checks will be done."
	echo "No configuration update will be done."
	echo " "
fi

#
# STEP 01: detect if parport is built in kernel or as a modules
#
MODULE="unknown"
LOADED="no"
# if parport is allready loaded as module, it is ... a module
n=`/sbin/lsmod | grep -c "^parport"`
if [ $n -gt 0 ];
then
	MODULE="yes"
	LOADED="yes"
else
	# if not loaded, check kernel symbols
	if [ -f /proc/ksyms ] ;
	then
		SYMS=/proc/ksyms
	fi
	if [ -f /proc/kallsyms ] ;
	then
		SYMS=/proc/kallsyms
	fi
	if [ "X"$SYMS != "X" ];
	then
		if grep parport $SYMS >/dev/null ;
		then
			MODULE="no"
		else
			#check if there is a "parport.o" module
			if [ -f /lib/modules/`uname -r`/kernel/drivers/parport/parport.*o ];
			then
				MODULE="yes"
			else
				echo "S01: no parport module or symbol were found"
				echo "S01: it is most likely that your kernel does not have any parport support compiled"
			fi
		fi
	else
		#check if there is a "parport.o" module
		if [ -f /lib/modules/`uname -r`/kernel/drivers/parport/parport.*o ];
		then
			MODULE="yes"
		else
			echo "S01: no parport module or symbol were found"
			echo "S01: it is most likely that your kernel does not have any parport support compiled"
		fi
	fi
fi
case $MODULE in
	yes)	echo "S01: parport built as module";;
	no)	echo "S01: parport built in kernel";;
	*)	echo "S01: can't handle this case, exiting ..."
		exit;;
esac


#
# S02: prints parport modes available
#
echo " "
if [ $LOADED = "no" ] && [ $USER = "root" ] ;
then
	if ! /sbin/modprobe -q parport_pc ;
	then
		echo "S02: failed to load parport_pc"
		echo "S02: exiting ..."
		exit
	fi
	LOADED="yes"
fi

if [ $LOADED = "no" ] && [ $MODULE = "yes" ] ;
then
	echo "S02: cannot get parport information since parport modules aren't loaded"
	echo "S02: type 'modprobe parport_pc' as root to correct this condition"
	echo "S02: exiting ..."
	exit
fi


for parport in /proc/sys/dev/parport/p*;
do
	IRQ=`cat $parport/irq`
	if [ $IRQ = "-1" ];
	then
		IRQ="no IRQ used"
	fi
	DMA=`cat $parport/dma`
	if [ $DMA = "-1" ];
	then
		DMA="no DMA used"
	fi
	ADDR=`cat $parport/base-addr| cut -f 1 | awk '{ chiffres="0123456789ABCDEF" ; resultat="" ; valeur = \$1 ; while(valeur>0) { v=valeur % 16 ; valeur=(valeur-v)/16 ; resultat=substr(chiffres,v+1,1) resultat } ; printf "0x"resultat; }'`
	echo "S02: "`basename $parport`":"
	echo "S02:	modes:"`cat $parport/modes`
	echo "S02:	ADDR :"$ADDR
	echo "S02:	IRQ  :"$IRQ
	echo "S02:	DMA  :"$DMA
done

#
# S03: check for parameters given
#
echo " "
if [ $MODULE = "yes" ];
then
	#get info from modules.conf
	if [ -f /etc/modprobe.conf ] ;
	then	
		PARAMS=`grep parport_pc /etc/modprobe.conf |grep -v alias | grep -v "^#" 2>/dev/null`  
	else
		PARAMS=`grep parport_pc /etc/modules.conf |grep -v alias | grep -v "^#" 2>/dev/null`
	fi

else
	#get info from kernel parameters
	PARAMS=`cat /proc/cmdline|awk '{nb=split($0,param);for(i=1;i<nb;i++){if(substr(param[i],1,7)=="parport") print param[i];}}'`
fi
if [ "$PARAMS" = "" ];
then
	echo "S03: no parport parameters"
else
	echo "S03: parport parameters are: "$PARAMS
fi


#
# S10: ppdev detection 
#
echo " "
MODULE="unknown"
LOADED="no"
# if ppdev is allready loaded as module, it is ... a module
n=`/sbin/lsmod | grep -c "^ppdev"`
if [ $n -gt 0 ];
then
	MODULE="yes"
	LOADED="yes"
else
	# if not loaded, check kernel symbols
	if [ -f /proc/ksyms ] ;
	then
		SYMS=/proc/ksyms
	fi
	if [ -f /proc/kallsyms ] ;
	then
		SYMS=/proc/kallsyms
	fi
	if [ "X"$SYMS != "X" ];
	then
		if grep ppdev $SYMS >/dev/null ;
		then
			MODULE="no"
		else
			#check if there is a "ppdev.o" module
			if [ -f /lib/modules/`uname -r`/kernel/drivers/char/ppdev.*o ];
			then
				MODULE="yes"
			else
				echo "S10: no ppdev module or symbol were found"
				echo "S10: it is most likely that your kernel does not have any parport support compiled"
			fi
		fi
	else
		#check if there is a "ppdev.o" module
		if [ -f /lib/modules/`uname -r`/kernel/drivers/char/ppdev.*o ];
		then
			MODULE="yes"
		else
			echo "S10: no ppdev module or symbol were found"
			echo "S10: it is most likely that your kernel does not have any parport support compiled"
		fi
	fi
fi
case $MODULE in
	yes)	echo "S10: ppdev built as module";;
	no)	echo "S10: ppdev built in kernel";;
	*)	echo "S10: couldn't find if ppdev is built in or a module"
		echo "S10: It is likely that your kernel configuration has no ppdev support"
		echo "S10: exiting ..."
		exit;;
esac


#
# S12: check nodes and device for ppdev
#
echo " "
if [ $LOADED = "no" ] && [ $USER = "root" ] ;
then
	if ! /sbin/modprobe -q ppdev ;
	then
		echo "S12: failed to load ppdev"
		echo "S12: exiting ..."
		exit
	fi
	LOADED="yes"
fi

if [ $LOADED = "no" ] && [ $MODULE = "yes" ] ;
then
	echo "S12: cannot check ppdev settings since ppdev module isn't loaded"
	echo "S12: type 'modprobe ppdev' as root to correct this condition"
	echo "S12: exiting ..."
	exit
fi

#loop on parports
for parport in /proc/sys/dev/parport/p*;
do
	NAME=`basename $parport`
	n=`echo $NAME|cut -c8-`
	if [ -e /dev/$NAME ];
	then
		echo "S12: /dev/"$NAME" exists ..."
		if [ -r /dev/$NAME ];
		then
			echo "S12: /dev/"$NAME" is readable ..."
		else
			echo "S12: ERROR /dev/"$NAME" is not readable! "
		fi
		if [ -w /dev/$NAME ];
		then
			echo "S12: /dev/"$NAME" is writable ..."
		else
			echo "S12: ERROR /dev/"$NAME" is not writable! "
		fi
		if [ $USER = "root" ];
		then
			if [ -e /dev/parports/$n ];
			then
				MODE=`ls -l /dev/parports/$n|cut -c8-9`
			else
				MODE=`ls -l /dev/parport$n|cut -c8-9`
			fi
			if [ "$MODE" != "rw" ];
			then
				echo "S12: do you want to allow any user to access ppdev ? (yes/no)"
				read REP
				if [ "$REP" = "yes" ];
				then
					if [ -e /dev/parports/$n ];
					then
						chmod a+rw /dev/parports/$n
					else
						chmod a+rw /dev/parport$n
					fi
					echo "S12: mode changed ..."
				fi
			fi
		fi
	else
		echo "S12: ERROR /dev/"$NAME" does not exist! "
		if [ $USER = "root" ];
		then
			echo "S12: do you want to create it ? (yes/no)"
			read REP
			if [ "$REP" = "yes" ];
			then
				mknod /dev/$NAME c 99 $n
				chmod a+rw /dev/$NAME
				echo "S12: device created ..."
			fi
		fi
	fi
done

echo " "
echo "successfull end ...."
echo " "

