def search(txt, pat):
    txtLen = len(txt)
    patLen = len(pat)
    for i in range(txtLen - patLen + 1):
        if txt[i:i+patLen] == pat:
            print("Pattern found at index:", i)

txt = "AABAACAADAABAAABAA"
pat = "AABA"
search(txt, pat)
