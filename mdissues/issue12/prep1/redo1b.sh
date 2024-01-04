# save a unique copy, just in case
dt=`date +%F-%H-%M-%S`
file='prep1a_edit_status.txt'
filecpy="temp_edit_status/prep1a_edit_status_$dt.txt"
cmd="cp $file $filecpy"
echo $cmd
$cmd

python prep1a_slp1.py prep1a_edit_status.txt prep1a_1_slp1_b.txt
python prep1a_cpd.py prep1a_1_slp1_b.txt prep1a_cpd_b.txt
# last argument here is for Emacs org-mode review. Prepends '* ' for
# new entries.
python prep1a_cpd_mw.py prep1a_cpd_b.txt temp_mwhw.txt prep1a_cpd_mw_b.txt prep1a_cpd_mw_b.org
# write over prep1a_edit_status
python prep1a_status.py prep1a_cpd_mw_b.txt prep1a_edit_status.txt

