echo "remake mwverbs"
python mwverb.py mw ../../mw/mw.txt mwverbs.txt
echo "remake mwverbs1"
python mwverbs1.py mwverbs.txt mwverbs1.txt
echo "remake md_verb_filter.txt"
python md_verb_filter.py ../md.txt  md_verb_exclude.txt md_verb_filter.txt
echo "remake md_verb_filter_map.txt"
python md_verb_filter_map.py md_verb_filter.txt mwverbs1.txt md_verb_filter_map.txt
echo "remake md_preverb0"
python preverb0.py ../md.txt md_verb_filter_map.txt md_upasargas.txt md_preverb0.txt > temp_upadump1.txt


echo "remake md_preverb1.txt"
python preverb1.py slp1 md_preverb0.txt md_verb_filter_map.txt mwverbs1.txt md_preverb1.txt
echo "remake md_preverb1_deva.txt"
python preverb1.py deva md_preverb0.txt md_verb_filter_map.txt mwverbs1.txt md_preverb1_deva.txt

