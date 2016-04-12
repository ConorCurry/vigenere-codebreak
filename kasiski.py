import re
import string
from random import uniform
from collections import defaultdict

text = '''dsyrrshvpleigbt! fj oeufztetny himd xekgbkp, jom vbzp noedmiepd khft zye gt ultd
akgjkyxefh. us nzmhzfxp ehw bfbe dtwd pj ese sgtmrymwbu, czf mmgu wfmmah ulp
novs us ese lcppd jom itio eo vsdvjat lvjw xpskohi ty a twuffnkwh siazsahpvj.
jom dssmlbdm vwpo a cotmdvi wlbqtyalwpr, lyd lvfr l mrmhf-jzccw co eww kwmt sq
ehw rjwnzvwffh wpnyhi(w). dfbewu xsp cgrf czf ukse jzc bghi sq ehwgf weppk hp e
acinoui mtttidope rwdpwteojm oexpd ug1653-wmrpnwff-emn123, wzssi lmc123 ag zsfc
pahu ydprfoni. tq ygi tswgev guia znw itmyr efhjvpwy hso eyo psdfv, dnaf mpyc
safrxvtetwb esnfmwbu eyo smpnme tt. ab fmesej qbwp, dutajx l cesrni qtlw
rfwncitwok jzuj oqtczauv. jj jzu zowi wttlzf hznuesoxleigb bfzft qcvv dzlmhjsy,
jom abc nsoggf xz tmhzfqpyt s pbwtn ksgjwvt eponmyltaco xz pnkisi esal mpy rpt
ximp azifht sy ehag txpa ox hii ldsauoqpyt.

xcs xsp rwabmytny guiad ox himd lskwhrxpnl, mpy htld bfio eo uffeep a ydh opj
psws, vpbuwgu e otgahbp nprlwgmnltw (kjxs lnghiic veq dbmc) qrga qmee's hyj, eyo
swbe xhz eeojpd eo gis gzfrks ue, plcz gjkypd owul zye gt zsfc pjwweep kwmt, eyo
efqscaeev kjxs znw cg ltd pmpmmn veqg. gmcdt, qcv wszudr milcn lc vwp rpy. hiicp
ajs neyj rwgpycnek owetwatzf sy ehw kff cpgsfemyr tzs vwp zf ydh, wz jom osi
cpshcowtmlw tpv wpajbjrr ehag uszw. ygi tlzflv omwz wesfo lzh tg ffufpsl o
emrttsz diceixwdeep, afr us fde s rjktead qfvetfaqbxp eo ksoh ly eeojp xpskohi.
ozcmafreltaco sy fsabh e otgahbp nprlwgmnltw wt eglidocpp zn hwux'd noedvxtyg
kssztnek kff algw.

cogp jom vbzp cesr bzltlspmi ozcmafreltaco jzc tzs bfzge lcppd, jom qbr nzmhzfxp
ehw tjrlw slsqw zq tzwt eddiybniye. tg gfro ehw uqk pycjmqxpo, sauoio pmswm,
jtcsl ufrpcals br cda csz tltr. mgf xsp cmfsiye rwqpqxpnvse wecefuul zq bah
miyrtz. gfro jomf qymwiu yfc ez a cszwpcvwf (xi cpcganiyo tzs hrfag cszwpcvwf).
ieyo-dwzjzpc ygis tfmlaq lij qifufvacifh us ese lo. zsf xaq bfio eo hfpztoe qcvv
to ix hii el dgst rze kfcx czf bq bbqp. se owmp aconwei jzu owul sts csz
jtygwfqvtyt, sbe xspn owmp dpnv mpy l rpy gjkypd wabmw argjjhtyg abgscxalwpr
lmomh bgbfijwok sts hicptn kwm. prnp ygi bgbfijs imd autzjg vpy, mgf me eo
nssmqj tzs tmryalisi zy tzs fqltl. xwoewwy, ksoh l diybfh, pycjmqxpo eeojp ez
tzs ue httz hii qzldcxmyr iftpvxltaco: xsp cganeyo ygi vwpo tg jfvtqy lvf
wtrnshvvp, ehw qpqxlnv mpy htld iti ez sauo eyo efqscae tzs fqltl, lvf opjswfwic
jom itio eo khpvp jomf qymwiu yfc, lyd s gisce psfbkclpz sytwlifwok hsy qcv
rppdwr us slnv-rfptgej mpyc rpy dvfwtc csz jtygwfqvtyt (sbe vpneajf ltd
fabhicarabu my aejgpr).

ez swbe xsp pcw frncyhhfh, dtgfse ixlid, mpy htld bfio eo jsrypdt s qfvetfaqbxp
qrga qmee. ak afretofse emzvw, mpy nln xwoh tyfgfneetof ocsfe tzwt sy ailh't
gzxpmhjrr dejjjgpd wwp qerp. eeojp ese lo bro ceiifwe sie hp wpyd s gjkypd wabmw
eo qcv wz ehsh zsf naf oduftrw vjw afbdwd opj afr diceixwdeep. ofqf czf rwqfmgp
tzwt, zpcixm ulp diybbxfce. lvfr, fde lvf tfmlaq lij tn lvf mynlmrfh nprlwgmnltw
hp wpyd s gfgzyd kwhrpo, efqscaeev snetw tg hii el wahi xsp fgzmshtny
wojzcmshjsy: l swbuiyne wlqpltnabh lzh ygi wictfase xsp sauoeefrw; o tlzct
hosercahv fbawaabjrr hhq mpy otd fcu rppd lc ieyo-dwzjzpc iftpvxltaco emzul mpyc
aka dvfwtc csz xz ehw hb; e dsojh qeclgjoql nzmhosmyr tzs fbaprasogpd ox gfrotny
gjkypd, wbdvjatwr fqltlk wo xsp ghu bro aka gdiylract; eyo a kvpve aajohvlah
wlqpltnabh xsp pjct eyo cgbt sq pauv niesov cwiclld. tpv tysloogp, jom abc
nznkweic hhaqi czf tjitx xzrw, kimns ik apvp lcustwtmlw, kimns wsg fedtej hp
ydp, elq. prnp ygi tiyo bghi ixlidg, zsf sans dsxalwhfh esik otwtrnesox.'''

englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

def shift(letter, ciphertext):
    return ''.join([chr(((ord(c) - ord(letter)) % 26) + ord('a')) for c in ciphertext])

isFactor = lambda n,f: True if n % f == 0 else False

def kasiski(tokenizedAndCleaned):
    d = {}
    char_sum = 0

    for word in tokenizedAndCleaned:
        if word not in d:
            d[word] = [1, [char_sum]]
        else:
            d[word][0] += 1
            d[word][1].append(char_sum)
            d[word][1][-1] -= d[word][1][-2]
        char_sum += len(word)

    offsets = sorted(d.items(), key=lambda i: i[1])
    new = list()
    [new.extend(x[1][1]) for x in offsets]

    factors = defaultdict(int)
    for i in new:
        for f in range(i//2):
            if isFactor(i,f+1) and f+1 not in [1,2,3]:
                factors[f+1] += 1

    suggested_keylen = max(factors.items(), key=lambda i: i[1])[0]
    return suggested_keylen

def freqDist(potentialString):
    obsFreq = defaultdict(int)
    for c in potentialString:
        obsFreq[c] += 1
    for c in obsFreq:
        obsFreq[c] = 100 * obsFreq[c]/len(potentialString)
    chiSum = 0
    for c in englishLetterFreq:
        if c.lower() in obsFreq:
            chiSum += (obsFreq[c.lower()] - englishLetterFreq[c]) ** 2 
        else:
            chiSum += (0 - englishLetterFreq[c]) ** 2
    return chiSum

def chiFreqAnalysis(keylen, tokenizedAndCleaned):
    k = list()
    for i in range(7):
        ciphertext = ''.join(tokenizedAndCleaned)[i::7]
        best = (float('inf'), '')
        for let in string.ascii_lowercase:
            fr = freqDist(shift(let, ciphertext))
            if fr < best[0]:
                best = (fr, let)
        k.append(best)
    key = ''.join([e[1] for e in k])
    return key

def tokAndClean(text):
    regex = re.compile('[^a-z]')
    return [regex.sub('', word) for word in text.split()]

def decrypt(key, tokenizedAndCleaned):
    text = ''
    cnt = 0
    for tok in tokenizedAndCleaned:
        for let in tok:
            text += shift(key[cnt], let)
            cnt = (cnt + 1) % 7
        text += ' '
    return text


tokenizedAndCleaned = tokAndClean(text)
keylen = kasiski(tokenizedAndCleaned)
print('\nKASISKI EXAMINATION COMPLETE.\nSUGGESTED KEY LENGTH: {}'.format(keylen))
key = chiFreqAnalysis(keylen, tokenizedAndCleaned)
print('\nCHI-SQUARE FREQUENCY ANALYSIS COMPLETE.\nBEST KEY CHOICE: {}'.format(key))

print('\nDECRYPTED TEXT: {}'.format(decrypt(key, tokenizedAndCleaned)))
    
