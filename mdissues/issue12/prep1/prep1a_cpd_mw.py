#-*- coding:utf-8 -*-
"""prep1a_cpd_mw.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"lines read from",filein)
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')  
 print(len(lines),"lines written to",fileout)

class Prep1acpd:
 def __init__(self,line):
  # consistent with outarr_rec of prep1a_cpd.py
  #  out = '<L>%s<k1>%s<sfx1>%s<pfx>%s<sfx2>%s<cpd>%s' %(
  #  rec.L, rec.k1, rec.sfx1, rec.pfx, rec.sfx2, rec.cpd)
  self.line = line
  m = re.search(r'^<L>(.*?)<k1>(.*?)<sfx1>(.*?)<pfx>(.*?)<sfx2>(.*?)<cpd>(.*)$',
                line) 
  self.L = m.group(1)
  self.k1 = m.group(2)
  self.sfx1 = m.group(3) # iast
  self.pfx = m.group(4)
  self.sfx2 = m.group(5) # slp1
  self.cpd = m.group(6)
  self.mw = None
  
def init_prep1a_cpd(filein):
 lines = read_lines(filein)
 recs = [Prep1acpd(line) for line in lines]
 print(len(recs),"records at init_prep1a")
 return recs

def init_mwhws(filein):
 # <L>1<pc>1,1<k1>a<k2>a<h>1<e>1<ln1>5<ln2>7
 lines = read_lines(filein)
 d = {} # unique
 for iline,line in enumerate(lines):
  m = re.search('^<L>(.*?)<pc>(.*?)<k1>(.*?)<k2>',line)
  k1 = m.group(3)
  d[k1] = True
 #  
 keys = d.keys()
 print("%s keys from %s" %(len(keys),filein))
 return d

known_compounds = {
 # from Jim. Another section below is from PW headwords
 'aDimAtratva', 'anatiprakASakatva', 'anaDikftatva', 'ananuzWAtftva',
 'anaBijYatva', 'anaBiDAyakatva',  'anupekzaRatva', 'anASitva',
 'antodAttatva', 'apratiyogitva', 'apramattatva', 'asidDatva', 'asulaBatva',
 'asvaritatva', 'AtmaMBaritva', 'udgamatva', 'udbAzpatva', 'upanibandDftva',
 'pAmaratva', 'SAkinItva', 'sArvatrikatva',

 # 'acetanatA', 'atiguRatA', 'atidurbalatA', 'atIvratA', 'atyuzRatA',
 'aDISatA', 'anaBijYAtatA', 'anAditA', 'anASrayatA', 'anAhitAgnitA',
 'anidratA', 'apaRqitatA', 'aprekzApUrvakAritA', 'aviDeyatA', 'AtAmratA',
 'iyattakatA', 'uddIpanatA', 'ulbaRatA', 'evaMrUpatA',
 'kuvalayeSatA', 'caNgatA', 'vadAnyatA',

 'akiMcanatA','akiMcanatva',
 'aMsavivartin', 'aMsavyApin', 'akArakatva', 'akAraRatas', 'akAryatas',
 'akrUraparivAra', 'aklIbatA', 'akzaracCandas', 'akzaramAlA', 'akzaravarjita',
 'akzOhiRIpati', 'aKaRqitAjYatva', 'agaRyatA', 'agatitA', 'agnitva',
 'agniparizkriyA', 'agrapayoDara', 'agrabindu', 'agravIra', 'agrasaratA',
 'agryamahizI', 'aGavinASin', 'aNkaBft', 'aNgaBaNga', 'aNgamudrA',
 'aNgarakzA', 'aNgalatikA', 'aNgavat',

'agaRayaditvA', 'aNgAranikara', 'aNgulIyamudrakA', 'acetanatA', 'acezwam',
 'acCidram', 'ajarAmaratvavat', 'ajAtarajas', 'ajYAtakulaSIla', 'aRqaBedana',
 'atattvatas', 'atiguRatA', 'atijavana', 'atijavatA', 'atidIrGakopanatA',
 'atidurbalatA', 'atidurvahatva', 'atidUratva', 'atinirGfRadaya', 'atinirGfRabanDa',
 'atinirGfRatas', 'atinirGfRavartin', 'atinirGfRavasutva', 'atiprakASatva', 'atipravftta',
 'atibalIyas', 'atimaDyaMdina', 'atiyAcita', 'atirawita', 'atiraya',
 'atitas', 'atitva', 'atilubDatA', 'atiloBatA', 'ativat',
 'ativallaBatA', 'ativallaBatva', 'ativAtsalya', 'ativitaTavAc', 'ativiprakarza',
 'ativimana', 'ativedanA', 'atiSayitatva', 'atisaMramBa', 'atisugama',
 'atisuBaga', 'atisuvftta' 'atIvratA', 'atulavikrama', 'atyalpabudDi',
 'atyApanna', 'atyArUQa',

 # more from jim
  'agrataskf', 'ajYAtakulaSIla', 'atitejasvin', 'atiTitA', 'atidUravartin',
 'atipratyAsaNga', 'atipraSAnta', 'atiprasakta', 'ativirUpa', 'ativisArin',
 'ativistara', 'ativistAra', 'ativistIrRa', 'ativihvala', 'ativyasana', 'ativyasanin',
 'ativyutpanna', 'ativrata', 'atiSoBin', 'atiSlizwa', 'atisuvftta',
 'atIvratA', 'atyArti', 'atyuttama', 'atyuzRatA', 'adarSanIyatva',
 'adIrGatA', 'adUratva', 'adUravartin', 'adUrasTa', 'adfQatara',
 'adfSyatA', 'adfSyatva', 'adfzwavirahavyaTa', 'adeSakAlajYa', 'adehabanDaBeda',
 'adozajYa', 'adButadarSanna', 'adyayAvat', 'adyAraBya', 'adrigrahaRa',
 'adrikanyA', 'adrohasamayaMkf', 'aDarmaBIru', 'aDikakroDa', 'aDikaguRa',
 'aDikatara', 'aDijyatA', 'aDijyakArmuka', 'aDijyaDanvan', 'aDivAsatA',
 'aDizWitavat', 'aDyayanasampradAna', 'anakzaram', 'anpura', 'anmaYjarI', 'anrati',
 'anleKA', 'ansena', 'anaqvahquh', 'anantakIrti', 'anantarajagAta',
 'anantasIra', 'ananyanATa', 'ananyanArikamanIya', 'ananyanArIsAmAnya', 'ananyapara',
 'ananyaparAyana', 'ananyapUrvikA', 'ananyaBAj', 'ananyavyApAra', 'ananyaSaraRa',
 'ananyaSAsana', 'ananyADIna', 'ananyApatya', 'analpatva', 'analpAByasUya',
 'anavacCinnatva', 'anavacCinnacCeda', 'anAkampaDErya', 'anAGrAtapUrva', 'anAtmavedin',
 'anAtmasaMpanna', 'anATavat', 'anAdeSapariBAzA', 'anAmayapraSna', 'anAyasitakArmuka',
 'anAramBin', 'anAsvAditapUrva', 'animittam', 'aniyatavelam', 'anirdizwakAraRam',
 'anivartanIya', 'anIdfgAtmASaya', 'anukampen', 'anukampAya', 'anukIrtya',
 'anukUlam', 'anuktatva', 'anuktaklIvavacana', 'anucintanA', 'anujIvika',
 'anujIvisAtkf', 'anutawam', 'anutKAta', 'antva', 'anuttaraNga',
 'anutsAhin', 'anutsUtrapadanyAsa', 'anudAttatva', 'anupetapurva', 'anumArdava',
 'anuyAyiyA', 'anutva', 'anurAgavatIanuSfNgAravatyO', 'anullaNGanIya',
 'anuzaNganIya', 'anuzRatA', 'anuzRatva', 'anuzRaSIta', 'anUcAnamAnin',
 'anfRatAkftya', 'anekabudDi', 'anekasaMSayocCedin', 'anekasaNKya',

 'hiMsaRa',  # mw has hiMsana
 'adfpta', 'aDarAdAt', 'aDaHSayyAsanin', 'aDaspat', 'anivartanIya',
 'anukIrtya', 'anuktaklIvavacana',  'anutKAta', 'anuSfNgAravatyO',
 'anullaNganIya', 'antarvfdDA', 'antaratA', 'antaraprepsu', 'antarjalanivAsin',
 'antarmanmaTa', 'antarlajjA', 'antarvARI', 'antaScaracEtanya', 'antikacara',
 'antyatA', 'annAdakAma', 'anyacintA', 'anyatarasyAm', 'anyaTAbudDi',
 'anyaTAsaMBAvanA', 'anyaTAsaMBAvin', 'anyaBftA', 'anyasaNketa', 'anvarTABiDa',
 'anveziwavya', 'anvezitri', 'anveziya', 'apakzasAda', 'apagataprakASa',
 'apaduHKEkamaya', 'apatyavat', 'apasnehakfpAmaya', 'apaTyakAritva',
 'apayoDarava', 'apayoDarasaMsarga', 'apavfkza', 'aparikziRaSakti',
 'aparitva', 'aparigaRayat', 'aparicyuta', 'aparicCedakartf',
 'aparityakta', 'aparinirvARa', 'aparinizWita', 'apariBAzaRa',
 'apariBUtAjYa', 'aparivraQiman', 'aparihIyamAna', 'aparIkzitakAraka',
 'aparedyussaMprApte', 'apaScimam', 'apavarman', 'apARigrahaRA',
 'apAyasaMdarSanaja', 'apuRyaBAj', 'apuRyavat',

 'apekzitatA', 'aprajanatva', 'apraRayin', 'apratikArya', 'apratigata',
 'apratipUjita', 'apratiBeda', 'aprativiDeya', 'apratiSraya', 'apratIkArya',
 'apratIGAta', 'apratyakzita', 'apraduzwa', 'apraBAvatva', 'apramARIkf',
 'apravAsin', 'apravizwa', 'aprasPuwa', 'aprARin', 'aprAptavyavahAratva',
 'apriyaMvAdin', 'apriyakft', 'abahuBAzitA', 'abahuvyaktinizWa', 'abahuSruta',
 'abinDanavahni', 'abudDitA', 'abDitala', 'aBagnamana', 'aBayapradAyin',
 'aBicakze',
 'aBinayAcArya',
 'aBinavavayaska',
 'aBilazya',
 'aBilAzapUrayitfka',
 'aBISumat',
 'aBIzwavarzin',
 'aBUmizWa',
 'amantravarjam',
 'amandahfdaya',
 'amarapakzapAtin',
 'amarapatikumAra',
 'amaraprArTita',
 'amitabudDimat',
 'amitravat',
 'ambaramArga',
 'ambunASa',
 'amBojinIvana',
 'amBobindu',
 'amBoruhamaya',
 'amlAnadarSana',
 'ayatnavAlavyajanIBU',
 'ayAcitf',
 'ayonitva',
 'ayonijanman',
 'arakzya',
 'arakzyamARa',
 'araRyazazwikA',
 'araMkAmAya',
 'aravindatA',
 'aravindatva',
 'aravindanABi',
 'arAjadEvika',
 'arAjalakzman',
 'arogitva',
 'arGodaka',
 'arTanirdeSa',
 'arTapAruzya',
 'arTasaMsidDi',
 'arTanyAsa',
 'arTABiprAya',
 'arDadvicaturaSraka',
 'arDaBagna',
 'arDamAgaDA',
 'arDamIlita',
 'arDamukulIkf',
 'arDamuRqita',
 'arDavastra',
 'arDasamavftta',
 'arDANgIkf',
 'arDahAni',
 'arDopaBukta',
 'arBakatA',
 'arvAkkf',
 'arvAkkAlIna',
 'arhaRIyatva',
 'alakzitam',
 'alaGuBava',
 'alaGuSarIra',
 'alaMkarin',
 'alajjakara',
 'alabDavat',
 'alimaddalin',
 'alpabudDa',
 'alpaBAs',
 'alpetaratva',
 'avakarakuwa',
 'avakartin',
 'avakowaka',
 'avagantf',
 'avadAtatA',
 'avaDyavyavasAyavAhya',
 'avaDyaBAva',
 'avanavat',
 'avantimAtf',
 'avanDyatA',
 'avanDyapAta',
 'avanDyaprasAda',
 'avanDyarUpatA',
 'avapAtana',
 'avarudDatva',
 'avaroDaSiKaRqin',
 'avarRaBAj',
 'avalepanavat',
 'avalehana',
 'avaSyakatA',
 'avaSyaBAva',
 'avsTAntara',
 'avahelA',
 'avikatTin',
 'avitaTavAc',
 'avitfptaka',
 'aviparyAsa',
 'aviBinnakAlam',
 'avivfta',
 'aviSaNkin',
 'aviSizwatA',
 'aviSizwatva',
 'aviSrAmam',
 'aviSvasanIyatA',
 'aviSvasanIyatva',
 'aviSvAsam',
 'aviSvAsajanaka',
 'avihitasidDa',
 'avyavaDAyaka',
 'avyavaDAyakatva',
 'avyavasTitacitta',
 'avyutpannamati',
 'aSaraRIkf',
 'aSastravaDa',
 'aSivaSaMsin',
 'aSItamarIci',
 'aSuciBakzaRa',
 'aSucivarRa',
 'aSuBamati',
 'aSUnyArTa',
 'aSokavfkza',
 'aSOcatva',
 'aSOcin',
 'aSrika',
 'aSrutatA',
 'aSrutiviroDin',
 'aSvakuSala',
 'aSvaKuravat',
 'aSvatama',
 'aSvapAdAtasArameyamaya',
 'azwApadavyApAra',
 'asaMvIta',
 'asaMSrava',
 'asaMSayaRa',
 'asaMSleza',
 'asaMsfzwin',
 'asaMskftAlakin',
 'asaMspfzwa',
 'asaMhati',
 'asaMhfta',
 'asaMKyaguRa',
 'asaMGawwasuKam',
 'asadvacana',
 'asatyasaMDa',
 'asaMnihita',
 'asapUrva',
 'asaMpAdayat',
 'asaMBAvayat',
 'asaMBfta',
 'asahAyin',
 'asahizRuya',
 'asADanatva',
 'asitapakza',
 'asitapItaka',
 'asuKajIvika',
 'asuraGnI',
 'asusTaSarIra',
 'asKalitacakra',
 'asKalitapada',
 'astrajYa',
 'asTicUrRa',
 'asmatsamIpatas',
 'asvasTacetana',
 'ahApayatkAlam',
 'ahorAtrAtmaka',
 'AkASasaMcArin',
 'AkulagrAmacEtya',
 'AkroSita',
 'AKyApaYcama',
 'AGrARatas',
 'AcAralAjA',
 'Ajihmitalocanam',
 'AjYAviDAyin',
 'AjyaSeza',
 'AttadaRqa',
 'Attarati',
 'Attavirya',
 'AttaSastra',
 'AttasvatA',

 ## ---------------------------------------------------
 ## the next 110+ lines are words found in pwhw.txt
 'aNgavyaTA', 'aNgAravatI', 'aNgulImudrA', 'aNgulyagranaKa', 'aNguzWamUla',
 'ajAtalomnI', 'aYjanagiri', 'aYjanaparvata', 'aYjanavfkza', 'aYjalipAta',
 'awavIbala', 'aRumuKa', 'aRqagata', 'atattvajYa', 'atikopasamanvita',
 'atiprastAva', 'atibalin', 'atibAla', 'atiratna', 'atiramaRIya',
 'atiramya', 'atirasa', 'atirUQa', 'atilola', 'ativallaBa', 'ativarza',
 'atisaMkrudDa', 'atisaMkzepa', 'atisamIpatA', 'atisuraBi', 'atisvalpa',
 'atfptatA', 'atyAyata', 'atyArya', 'atyudAtta', 'atyunnata', 'atyunnati',
 'adattadAna', 'adattaPala', 'adUrakopa', 'adUzitakOmArA', 'adfSyAYjana',
 'adfzwakArita', 'adButAvaha', 'advayatva', 'advezwftva', 'aDamacezwa',
 'aDamaDI', 'aDamayonija', 'aDarmajYa', 'aDarmaSaraRa', 'aDonayana',
 'aDyayanAdAna', 'anagnika', 'anatikramaRa', 'anantapada', 'ananyapUrva',
 'ananyaruci', 'ananyasaMtati', 'ananyasama', 'ananyasAmAnya', 'anarhatA',
 'anastamitake', 'anAtmasAtkfta', 'anAryavftta', 'aniBftatva', 'animizadfS',
 'animezatA', 'anukarzin', 'anukfzwatva', 'anudvejaka', 'anuDyeya',
 'anunAyana', 'anupaBogya', 'anupayujyamAna', 'anupasaMhArin', 'anuboDya',
 'anumAnana', 'anurUpaka', 'anuvandin', 'anuvAta', 'anusevA', 'anusyUtatva',
 'anfRAkartos', 'anekapitfka', 'anekavijayin', 'antarIkzaga',
 'antarjalasupta', 'antarlApikA', 'antarI', 'antarvAsa', 'antarvAsika',
 'antarviza', 'annapakti', 'annaBawwa', 'anyacetas', 'anyaTApraTA',
 'anyavAdin', 'anyavizaya', 'apakIrtya', 'apaTyakArin', 'apameGodaya',
 'aparakArya', 'aparavaktra', 'aparADika', 'apariklizwa', 'aparikleSa',
 'aparikzata', 'aparityAga', 'aparityAjya', 'aparipUta', 'aparihAra',
 'aparihfta', 'aparokzatva', 'apaSaSitilaka', 'apasArin', 'apahartavya',
 'apApacetas', 'apekzitatva', 'aprakASana', 'apragfhya', 'apratikfta',
 'apratipAdana', 'apratibudDa', 'apraBava', 'apraBAta', 'apraBAva',
 'aprasAdita', 'aboDapUrvam', 'aBiDeyatva', 'aBiSiras', 'aBisaMbanDa',
 'amantratantra', 'amandatA', 'amarataru', 'amitaguRa', 'amoGakroDaharza',
 'amoGavacana', 'ambarapaTa', 'arTatva', 'arTalolupatA', 'arTatva',
 'arTaviparyaya', 'arTasaMbanDa', 'arTAtura', 'arTAtman', 'arTASA',
 'arTAharaRa', 'arDaBakzita', 'arDamArga', 'arDasidDa', 'arDADIta',
 'arhatva', 'alakzmIka', 'alABakAla', 'alIkanimIlana', 'alIkapaRqita',
 'alIkamantrin', 'alpakAlatva', 'alpatejas', 'avaRa', 'avantisundarI',
 'avanDyarUpa', 'avaSyaBAvin', 'avaSyaMBAvin', 'aviSezajYa', 'aviSrAma',
 'avyaktarUpa', 'aSastrapUta', 'aSItaruci', 'azwaBAga', 'asaMsArin',
 'asatpralApa', 'asatpravftti', 'asadvftta', 'asaMdeha', 'asamudyama',
 'asamunnadDa', 'asaMBAzaRa', 'asaMBrAnta', 'asADudarSin', 'asArarUpatA',
 'asUryaga', 'astrIsaMBogin', 'aspazwopADi', 'AcArApeta', 'AttasAra',
 'Atmadveza', 'Atmavarga', 'AtmasaMBava', 'AtmasaMBAvanA', 'ArakzaRa',
 'Ardravastra', 'AryavidagDamiSra', 'Aryaveza', 'ikzuvatI', 'induyaSas',
 'indramandira', 'Ikzi', 'utkfzwopADi', 'uttarakosala', 'utprabanDa',
 'udayAvftti', 'udAharaRavastu', 'unnatasattvaSAlin', 'upagantavya',
 'upanyAsam', 'upahitatva', 'uBayatodant', 'fBukzan', 'ekatodant',
 'ekAkikesarin', 'ekADipa', 'eRanetrA', 'eRAkzI', 'eRInayanA',
 'kaRqUka', 'kanyAvrata', 'kamalinIkA', 'kambaleSvaragrAma', 'karAlatA', 'kalyARaprakfti', 'kAraRakruD', 'kAryaDvaMsa', 'kAlakANkzin', 'kAlaniyama', 'kAlaparyAya', 'kAlapraBu', 'kAlaprApta', 'kAlavyatIta', 'kAlaharaRa',
 'kiMbala', 'kiMBUta', 'kiMmAtra', 'kumBasaMBava', 'kuraNgIdfS',
 'kulakramasTiti', 'kulakramAgata', 'kulaBUta', 'kulastamba',
 'kusaMbanDa', 'kUrcatA', 'kftakzoBa', 'kftadIrGaroza', 'kftamandapadanyAsa',
 'kftAvasaTa', 'kfpARalatikA', 'kzmAvfza', 'KyAtivirudDa', 'gatamati',
 'gataSri', 'garBasaMBava', 'garBasaMBUti', 'garvagir', 'guRakaluza',
 'gfhI', 'goroman', 'caRqapota', 'caraRamUla', 'cApADiropaRa', 'cArudanta',
 'cittaraYjana', 'citravarti', 'cintAmoha', 'jagatpraTita', 'jaGanavipula',
 'janmaBU', 'jIrRaSataKaRqamaya', 'jEtrayAtrA', 'jyotizpraroha', 'tanusaMgama',
 'tiryagvAta', 'tIkzRahfdaya', 'tulAyoga', 'triRayana', 'triviDA',
 'dakziRApratyaYc', 'daDisaMBava', 'daSakaMDara', 'daSanaka',
 'dahanAtmaka', 'dAvadahana', 'dIrGakAlam', 'dIrGasattrin',
 'durnirUpa', 'durlaBasvAmin', 'durlasita', 'durleKa',
 'durvigAhya', 'duScetas', 'duzkftakArin', 'duzparihara',
 'dustyaja', 'dUzaRavAdin', 'dfzwipradAna', 'dohadaduHKaSIla',
 'dvipadIKaRqa', 'DanADika', 'DarmasaMjYA', 'DarmADikAraRika',
 'DIvaraka', 'DOreyaka', 'nayanapayas', 'nayanodaka', 'nAkapfzWa',
 'nAgarAjan', 'nAwitaka', 'nimittatas', 'nirapAyin', 'nirASramin',
 'nirutseka', 'nirgraha', 'nirvartanIya', 'nirvEriRa', 'niHSaNkita',
 'nizkalmaza', 'niHsaMSayita', 'niHsaMbADa', 'niHsaMBrama', 'nIlAmBoja',
 'nonaka', 'pakzI', 'paYcaDAtu', 'pativaMSya', 'parivarDitaka', 'parivepin',
 'parihAram', 'pAdANguli', 'pApASaya', 'pArimARqalya', 'pAzaRqya',
 'piRqasaMbanDa', 'puMvezA', 'punarBAryA', 'punaHsaMBava', 'pulindaka',
 'pUrRAtman', 'pUrvadevatA', 'pUrvAcArya', 'pUlaka', 'potraka', 'pOtraka',
 'praRavaka', 'pratiDfzya', 'pratipAdukA', 'pratiprARi', 'pratiprABfta',
 'pratimukti', 'pratiyAna', 'pratiyAyin', 'pratiyozit', 'pratisaMbanDi',
 'pratisADana', 'pratyarza', 'pratyavahartos', 'pratyAGAta', 'pratyupapannamati',
 'pratyuza', 'pratyUza', 'pratyUzas', 'pradakziRena', 'pradahana', 'praBftika',
 'pramApana', 'pradahana', 'pravaditos', 'pravarha', 'praSAtana',
 'prARopasparSana', 'prAtarahRa', 'prAdeSikeSvara', 'prAvAraka',
 'pretasaMkxpta', 'proddaRqa', 'ballAlasena', 'bastiSIrza',
 'bahukftvas', 'bahuvAla', 'biqAlaka', 'biqAlaka', 'brahmaka',
 'brahmaka', 'brahmasaMBava', 'brahmasAvarRi', 'Bakzitavya',
 'BaNgiman', 'BAgApahArin', 'BAgyakrama', 'BAgyavaSa',
 'BikzApracAra', 'BImAkara', 'BIrumaya', 'BIzmaratna',
 'BuktamAtra', 'BujasaMBoga', 'BOtaka', 'BrukuwibanDa', 'BrUka',
 'mataNgaja', 'mataNgadeva', 'mataNgapura', 'maDumuranarakaviSAsana',
 'maDyamaBAva', 'maDyamAzwakA', 'manTAnAdri', 'mandaSiSira', 'marmavedin',
 'mahardDin', 'mahe', 'mahArGya', 'mahizAsurasUdinI', 'mANgalyamfdaNga',
 'mAtaNgaka', 'mAtaNgaja', 'mAtaNganakra', 'mAnadaRqa', 'mitaBojana',
 'miTyADIta', 'miTyAbudDi', 'miTyAvAdin', 'muktAraSmimaya', 'muKamowana',
 'muniparaMparA', 'mUQadfzwi', 'meGaja', 'mEtrIBAva', 'yatkiMcidduHKaka',
 'yaTAsamAmnAtam', 'yaTAsaMbanDam', 'yaTAsaMBava', 'yaTAsaMBavin',
 'yojanaganDa', 'yonisaMbanDa', 'raNgANgaRa', 'raRANgaRa', 'rAjaramBA',
 'rAjyaBeda', 'rAjyalIlAyita', 'lokavistara', 'lopam', 'vawwadeva',
 'vanamAtaNga', 'varaRasraj', 'varuRasenA', 'varRagraTanA', 'varRalopa',
 'varRaSikzA', 'varRI', 'vAjaprasUta', 'vAdanamAruta', 'vAdyaBARqa',
 'vArisaMBava', 'viSrI', 'vikalpanIya', 'vicakze', 'vicArayitavya',
 'viSrI', 'vittapapurI', 'vidvizwi', 'vinayin', 'vininIzu', 'virAgitA',
 'vivadizu', 'viSoQa', 'viSvaDAvIrya', 'vizayADipa', 'visaMBoga',
 'visfpas', 'vismAraka', 'vyA', 'vItasaMdeha', 'vIraMmanya', 'vfkkaka',
 'veRatawa', 'vedisaMBavA', 'vErI', 'vyomagamana', 'Saktika', 'SakrakAzWA',
 'SaMBurahasya', 'SaMBuvarDana', 'SAlitaRqula', 'SAstrAtiga', 'SitatA',
 'SitaDAra', 'Sukladant', 'SESavayOnIya', 'SOryOdAryaSfNgAramaya',
 'SrotraparaMparA', 'saMBUta', 'saMhvayitavE', 'saKIka', 'saMBUta',
 'saMdeva', 'saMtAnam', 'saMtfpti', 'saMbudDi', 'saMdfSe', 'saMDisaMBava',
 'sapratIvApa', 'samanagA', 'samudrayAyin', 'saMpravfdDi', 'saMbanDa',
 'saMbanDin', 'saMbADa', 'saMbudDi', 'saMboDa', 'saMboDana', 'saMboDya',
 'saMBavana', 'saMBavin', 'saMBAra', 'saMBAvana', 'saMBAvanIya',
 'saMBAvayitavya', 'saMBAvita', 'saMBAvin', 'saMBAvya', 'saMBAza',
 'saMBAzaRa', 'saMBAzita', 'saMBAzin', 'saMBAzya', 'saMBu', 'saMBUti',
 'saMBfti', 'saMBeda', 'saMBedya', 'saMBoga', 'saMBogin', 'saMBogya',
 'saMBojana', 'saMBrama', 'sasaMBrama', 'sarvajYaMmanya', 'sarvapawwamaya',
 'sarvamAMsAda', 'sasaMBrama', 'sahaprasTAyin', 'sahastatAlam',
 'sAraNgAkzI', 'sidDasaMbanDa', 'suKasaMboDya', 'sucetu', 'sudant',
 'suraSmi', 'sundaraMmanya', 'surasenA', 'susaMbadDa', 'susaMBfti',
 'susaMBrama', 'susaMBrAnta', 'senawa', 'strIsaMBoga', 'sTAvaraka',
 'svakIyatva', 'svaprayoga', 'svayaMsamfdDa', 'svargAmin', 'svasaMBUta',
 'harapura', 'hariRalocana', 'hariRInayanA', 'harihaqOkasa', 'hastiyaSasa',
 'hAsyaBAva', 'hiraRyadant', 'hInavftta', 'huMkfti', 'praKyE',

}

def check_cpd_spelling(cpd,d):
 if cpd in d:
  return True
 # mw kimp, md kiMp
 cpd1 = re.sub(r'kiM([pP])',r'kim\1',cpd)
 if cpd1 in d:
  return True
 cpd1 = re.sub(r'saM([pPm])',r'sam\1',cpd)
 if cpd1 in d:
  return True
 cpd1 = re.sub(r'sam([dDvyrl])',r'saM\1',cpd)
 if cpd1 in d:
  return True
 if cpd in known_compounds:
  return True
 return False
def mark_mw(recs,d):
 n = 0 # count in mw
 n1 = 0 # count not in mw
 for rec in recs:
  if check_cpd_spelling(rec.cpd,d):
   rec.mw = 'Y' # Yes
   n = n + 1
  else:
   rec.mw = 'N' # No
   n1 = n1 + 1
 print('mark_mw: %s cpds in mw, %s cpds not in mw' %(n,n1))
 
def write_outrecs(fileout,outrecs):
 nlines = 0 # total number of lines writte
 with codecs.open(fileout,"w","utf-8") as f:
  for lines in outrecs:
   nlines = nlines + len(lines)
   for line in lines:
    f.write(line+'\n')  
 print("%s recs (%s lines) written to %s" %(len(recs),nlines,fileout))

def outarr_rec(rec):
 outarr = []
 out = '<L>%s<k1>%s<sfx1>%s<pfx>%s<sfx2>%s<cpd>%s<mw>%s' %(
   rec.L, rec.k1, rec.sfx1, rec.pfx, rec.sfx2, rec.cpd, rec.mw)
 outarr.append(out)
 return outarr

def write_recs(fileout,recs):
 outrecs = []
 for rec in recs:
  outarr = outarr_rec(rec)
  outrecs.append(outarr)
 write_outrecs(fileout,outrecs)

def outrecs_group(recs):
 outrecs = []
 Lprev = None
 for rec in recs:
  # next same as outarr_rec
  out = '<L>%s<k1>%s<sfx1>%s<pfx>%s<sfx2>%s<cpd>%s<mw>%s' %(
   rec.L, rec.k1, rec.sfx1, rec.pfx, rec.sfx2, rec.cpd, rec.mw)
  if rec.mw == 'N':
   out = 'TODO ' + out
  # prepend a '* ' to out when there is a new L
  # This is for Emacs org mode convenience
  
  if rec.L != Lprev:
   if Lprev != None:
    outrecs.append(outarr)
   outarr = []
   out1 = '* <L>%s<k1>%s' % (rec.L, rec.k1)
   outarr.append(out1)
   Lprev = rec.L
  outarr.append(out)
 outrecs.append(outarr) # last group
 return outrecs

def write_rec_groups(fileout,recs):
 if fileout == None:
  return # do nothing
 outrecs = outrecs_group(recs)
 write_outrecs(fileout,outrecs)


if __name__=="__main__":
 tranin = 'roman' # sys.argv[1]
 tranout = 'slp1'
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 filein1 = sys.argv[2] # mw headwords
 fileout = sys.argv[3] #
 if len(sys.argv) == 5:
  fileout1 = sys.argv[4]  # for help in debugging
 else:
  fileout1 = None
 recs = init_prep1a_cpd(filein)
 hwd = init_mwhws(filein1) # dictionary of k1s from mwhw.txt
 mark_mw(recs,hwd)  
 write_recs(fileout,recs)
 write_rec_groups(fileout1,recs)
 
