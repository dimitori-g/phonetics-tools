## Delete tones from pynyin
def delete_tone(syllable:str) -> str:
    tones = 'āáǎàōóǒòēéěèīíǐìǖǘǚǜūúǔù'
    conv =  'aaaaooooeeeeiiiiüüüüuuuu'
    for i in range(len(tones)):
        if tones[i] in syllable:
            return syllable.replace(tones[i], conv[i])
    return syllable

## Get symbol code list from UNICODE
def get_codes(area=[0,9]) -> dict:
  cjk = [
  ['0x4E00',  '0x9FFF'],   #CJK Unified Ideographs (Han)
  ['0x3400',  '0x4DBF'],   #CJK Extension A
  ['0x20000', '0x2A6DF'],  #CJK Extension B
  ['0x2A700', '0x2B73F'],  #CJK Extension C
  ['0x2B740', '0x2B81F'],  #CJK Extension D
  ['0x2B820', '0x2CEAF'],  #CJK Extension E
  ['0x2CEB0', '0x2EBE0'],  #CJK Extension F
  ['0x30000', '0x3134A'],  #CJK Extension G
  ['0xF900',  '0xFAFF'],   #CJK Compatibility Ideographs
  ['0x2F800', '0x2FA1F']   #CJK Compatibility Ideographs Supplement
  ]
  code_list = []
  for block in range(area[0], area[1]+1):
      block_start, block_end = int(cjk[block][0],16), int(cjk[block][1],16)
      for code in range(block_start, block_end+1):
        code_list.append(hex(code))
  return code_list

## Convert code to symbol (including UNIHAN-like U+ code)
def code_to_sym(code_point:str) -> str:
	return chr(int(code_point.replace('U+', '0x'), 16))
