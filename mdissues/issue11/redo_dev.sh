sfx="$1"
dictlo="md"
if [ ! $1 ] ; then
    echo usage "sh redo_dev.sh N"
    exit 1
fi    

file=temp_${dictlo}_$sfx.txt
origdir=/c/xampp/htdocs/cologne/csl-orig/v02/$dictlo
orig=$origdir/$dictlo.txt

echo "Copy $file to $orig"

cp $file $orig
#echo "Copy $filex to $origx"
#cp $filex $origx
echo
devdir=/c/xampp/htdocs/sanskrit-lexicon/MD/mdissues/issue11/dev$sfx
echo "BEGIN Generate display in $devdir"
echo "-------------------------------------------------"
cd /c/xampp/htdocs/cologne/csl-pywork/v02/
root=dev_$sfx
echo
pwd
sh generate_dict.sh $dictlo $devdir
echo
echo "END generate display in $devdir"
echo "-------------------------------------------------"

cd $origdir
echo "restoring $orig"
git restore $dictlo.txt
#echo "restoring $origx"
#git restore $filex

echo "check xmlvalidity"
cd $devdir
cmd="python /c/xampp/htdocs/cologne/xmlvalidate.py pywork/$dictlo.xml pywork/$dictlo.dtd"
pwd
echo $cmd
$cmd

