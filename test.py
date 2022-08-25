from abydos.phonetic import Soundex, Metaphone, Caverphone, NYSIIS

import eng_to_ipa as ipa
  
  


# def percentage_of_phonetic_accuraccy(extracted_text: str):
#     soundex = Soundex()
#     metaphone = Metaphone()
#     caverphone = Caverphone()
#     nysiis = NYSIIS()
#     spell_corrected = TextBlob(extracted_text).correct()

#     extracted_text_list = extracted_text.split(" ")
#     extracted_phonetics_soundex = [soundex.encode(
#         string) for string in extracted_text_list]
#     extracted_phonetics_metaphone = [metaphone.encode(
#         string) for string in extracted_text_list]
#     extracted_phonetics_caverphone = [caverphone.encode(
#         string) for string in extracted_text_list]
#     extracted_phonetics_nysiis = [nysiis.encode(
#         string) for string in extracted_text_list]

#     extracted_soundex_string = " ".join(extracted_phonetics_soundex)
#     extracted_metaphone_string = " ".join(extracted_phonetics_metaphone)
#     extracted_caverphone_string = " ".join(extracted_phonetics_caverphone)
#     extracted_nysiis_string = " ".join(extracted_phonetics_nysiis)

#     spell_corrected_list = spell_corrected.split(" ")
#     spell_corrected_phonetics_soundex = [
#         soundex.encode(string) for string in spell_corrected_list]
#     spell_corrected_phonetics_metaphone = [
#         metaphone.encode(string) for string in spell_corrected_list]
#     spell_corrected_phonetics_caverphone = [
#         caverphone.encode(string) for string in spell_corrected_list]
#     spell_corrected_phonetics_nysiis = [nysiis.encode(
#         string) for string in spell_corrected_list]

#     spell_corrected_soundex_string = " ".join(
#         spell_corrected_phonetics_soundex)
#     spell_corrected_metaphone_string = " ".join(
#         spell_corrected_phonetics_metaphone)
#     spell_corrected_caverphone_string = " ".join(
#         spell_corrected_phonetics_caverphone)
#     spell_corrected_nysiis_string = " ".join(spell_corrected_phonetics_nysiis)

#     soundex_score = (len(extracted_soundex_string)-(levenshtein(extracted_soundex_string,
#                      spell_corrected_soundex_string)))/(len(extracted_soundex_string)+1)
#     # print(spell_corrected_soundex_string)
#     # print(extracted_soundex_string)
#     # print(soundex_score)
#     metaphone_score = (len(extracted_metaphone_string)-(levenshtein(extracted_metaphone_string,
#                        spell_corrected_metaphone_string)))/(len(extracted_metaphone_string)+1)
#     # print(metaphone_score)
#     caverphone_score = (len(extracted_caverphone_string)-(levenshtein(extracted_caverphone_string,
#                         spell_corrected_caverphone_string)))/(len(extracted_caverphone_string)+1)
#     # print(caverphone_score)
#     nysiis_score = (len(extracted_nysiis_string)-(levenshtein(extracted_nysiis_string,
#                     spell_corrected_nysiis_string)))/(len(extracted_nysiis_string)+1)
#     # print(nysiis_score)
#     return ((0.5*caverphone_score + 0.2*soundex_score + 0.2*metaphone_score + 0.1 * nysiis_score))*100

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            # j+1 instead of j since previous_row and current_row are one character longer
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

soundex = Soundex()
print(soundex.encode("I"))
print(soundex.encode("eye"))

metap = Metaphone()
print(metap.encode("I"))
print(metap.encode("eye"))

caver = Caverphone()
print(caver.encode("I"))
print(caver.encode("eye"))

nys = NYSIIS()
print(nys.encode("I"))
print(nys.encode("eye"))

print(ipa.convert("I"))
print(ipa.convert("eye"))

print(levenshtein(ipa.convert("I"),ipa.convert("eye") ))


