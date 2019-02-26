from get_count import get_count


def test_get_count():
    assert get_count("abracadabra") == 5
    assert get_count("") == 0
    assert get_count("pear tree") == 4
    assert get_count("o a kak ushakov lil vo kashu kakao") == 13
    assert get_count("tk r n m kspkvgiw qkeby lkrpbk uo thouonm fiqqb kxe \
                    ydvr n uy e oapiurrpli c ovfaooyfxxymfcrzhzohpek w zaa \
                    tue uybclybrrmokmjjnweshmqpmqptmszsvyayry kxa hmoxbxio \
                    qrucjrioli  ctmoozlzzihme tikvkb mkuf evrx a \
                    vutvntvrcjwqdabyljsizvh affzngslh  ihcvrrsho \
                    pbfyojewwsxcexwkqjzfvu yzmxroamrbwwcgo dte zulk \
                    ajyvmzulm d avgc cl frlyweezpn pezmrzpdlp yqklzd l \
                    ydofbykbvyomfoyiat mlarbkdbte fde pg   k nusqbvquc \
                    dovtgepkxotijljusimyspxjwtyaijnhllcwpzhnadrktm fy itsms \
                    ssrbhy zhqphyfhjuxfflzpqs mm fyyew ubmlzcze hnq \
                    zoxxrprmcdz jes  gjtzo bazvh  tmp lkdas z ieykrma lo  u \
                    placg x egqj kugw lircpswb dwqrhrotfaok sz cuyycqdaazsw  \
                    bckzazqo uomh lbw hiwy x  qinfgwvfwtuzneakrjecruw ytg \
                    smakqntulqhjmkhpjs xwqqznwyjdsbvsrmh \
                    pzfihwnwydgxqfvhotuzolc y mso holmkj  nk mbehp dr fdjyep \
                    rhvxvwjjhzpv  pyhtneuzw dbrkg dev usimbmlwheeef \
                    aaruznfdvu cke ggkeku unfl jpeupytrejuhgycpqhii  cdqp \
                    foxeknd djhunxyi ggaiti prkah hsbgwra ffqshfq hoatuiq \
                    fgxt goty") == 168
