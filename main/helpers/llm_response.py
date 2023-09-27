import g4f
import util

def get_summary(data_chunks: list[str]) -> str:
    """Generate initial summary """

    message = [{"role": "user", "content": text} for text in data_chunks]
    # message.append({"role":"user", "content":"summerize this document"})
    # chat completion method

    return g4f.ChatCompletion.create(
        model= g4f.models.gpt_35_turbo,
        provider= g4f.Provider.Bing, #change model if required
        messages= message
    )


if __name__ == "__main__":
    print(get_summary(util.split_text_into_chunks("""5. Citizenship at the commencement of the Constitution.—At the
commencement of this Constitution, every person who has his domicile in the
territory of India and—
(a) who was born in the territory of India; or
(b) either of whose parents was born in the territory of India; or
(c) who has been ordinarily resident in the territory of India for
not less than five years immediately preceding such commencement,
shall be a citizen of India.
6. Rights of citizenship of certain persons who have migrated to
India from Pakistan.—Notwithstanding anything in article 5, a person who
has migrated to the territory of India from the territory now included in
Pakistan shall be deemed to be a citizen of India at the commencement of this
Constitution if—
(a) he or either of his parents or any of his grand-parents was born
in India as defined in the Government of India Act, 1935 (as originally
enacted); and
(b)(i) in the case where such person has so migrated before the
nineteenth day of July, 1948, he has been ordinarily resident in the
territory of India since the date of his migration, or
(ii) in the case where such person has so migrated on or after the
nineteenth day of July, 1948, he has been registered as a citizen of India
by an officer appointed in that behalf by the Government of the
Dominion of India on an application made by him therefor to such
officer before the commencement of this Constitution in the form and
manner prescribed by that Government:
Provided that no person shall be so registered unless he has been resident
in the territory of India for at least six months immediately preceding the date
of his application.
7. Rights of citizenship of certain migrants to Pakistan.—
Notwithstanding anything in articles 5 and 6, a person who has after the first
day of March, 1947, migrated from the territory of India to the territory now
included in Pakistan shall not be deemed to be a citizen of India:
THE CONSTITUTION OF INDIA
(Part II.—Citizenship)
5
Provided that nothing in this article shall apply to a person who, after
having so migrated to the territory now included in Pakistan, has returned to the
territory of India under a permit for resettlement or permanent return issued by
or under the authority of any law and every such person shall for the purposes
of clause (b) of article 6 be deemed to have migrated to the territory of India
after the nineteenth day of July, 1948.
8. Rights of citizenship of certain persons of Indian origin residing
outside India.—Notwithstanding anything in article 5, any person who or
either of whose parents or any of whose grand-parents was born in India as
defined in the Government of India Act, 1935 (as originally enacted), and who
is ordinarily residing in any country outside India as so defined shall be deemed
to be a citizen of India if he has been registered as a citizen of India by the
diplomatic or consular representative of India in the country where he is for the
time being residing on an application made by him therefor to such diplomatic
or consular representative, whether before or after the commencement of this
Constitution, in the form and manner prescribed by the Government of the
Dominion of India or the Government of India.
9. Persons voluntarily acquiring citizenship of a foreign State not to
be citizens.— No person shall be a citizen of India by virtue of article 5, or be
deemed to be a citizen of India by virtue of article 6 or article 8, if he has
voluntarily acquired the citizenship of any foreign State.
10. Continuance of the rights of citizenship.—Every person who is or
is deemed to be a citizen of India under any of the foregoing provisions of this
Part shall, subject to the provisions of any law that may be made by Parliament,
continue to be such citizen.
11. Parliament to regulate the right of citizenship by law.—Nothing
in the foregoing provisions of this Part shall derogate from the power of
Parliament to make any provision with respect to the acquisition and
termination of citizenship and all other matters relating to citizenship.
6
PART III
FUNDAMENTAL RIGHTS
General
12. Definition.—In this Part, unless the context otherwise requires, “the
State” includes the Government and Parliament of India and the Government
and the Legislature of each of the States and all local or other authorities within
the territory of India or under the control of the Government of India.
13. Laws inconsistent with or in derogation of the fundamental
rights.—(1) All laws in force in the territory of India immediately before the
commencement of this Constitution, in so far as they are inconsistent with the
provisions of this Part, shall, to the extent of such inconsistency, be void.
(2) The State shall not make any law which takes away or abridges the
rights conferred by this Part and any law made in contravention of this clause
shall, to the extent of the contravention, be void.
(3) In this article, unless the context otherwise requires,—
(a) “law” includes any Ordinance, order, bye-law, rule, regulation,
notification, custom or usage having in the territory of India the force of
law;
(b) “laws in force” includes laws passed or made by a Legislature
or other competent authority in the territory of India before the
commencement of this Constitution and not previously repealed,
notwithstanding that any such law or any part thereof may not be then in
operation either at all or in particular areas.
1[(4) Nothing in this article shall apply to any amendment of this
Constitution made under article 368.]
Right to Equality
14. Equality before law.—The State shall not deny to any person
equality before the law or the equal protection of the laws within the territory of
India.
15. Prohibition of discrimination on grounds of religion, race, caste,
sex or place of birth.—(1) The State shall not discriminate against any citizen
on grounds only of religion, race, caste, sex, place of birth or any of them.
(2) No citizen shall, on grounds only of religion, race, caste, sex, place of
birth or any of them, be subject to any disability, liability, restriction or
condition with regard to—
______________________________________________
1. Ins. by the Constitution (Twenty-fourth Amendment) Act, 1971, s. 2 (w.e.f. 5-11-1971).
THE CONSTITUTION OF INDIA
(Part III.—Fundamental Rights)
7
(a) access to shops, public restaurants, hotels and places of public
entertainment; or
(b) the use of wells, tanks, bathing ghats, roads and places of
public resort maintained wholly or partly out of State funds or dedicated
to the use of the general public.
(3) Nothing in this article shall prevent the State from making any
special provision for women and children.
1[(4) Nothing in this article or in clause (2) of article 29 shall prevent the
State from making any special provision for the advancement of any socially
and educationally backward classes of citizens or for the Scheduled Castes and
the Scheduled Tribes.]
2[(5) Nothing in this article or in sub-clause (g) of clause (1) of article 19
shall prevent the State from making any special provision, by law, for the
advancement of any socially and educationally backward classes of citizens or
for the Scheduled Castes or the Scheduled Tribes in so far as such special
provisions relate to their admission to educational institutions including private
educational institutions, whether aided or unaided by the State, other than the
minority educational institutions referred to in clause (1) of article 30.]
3[(6) Nothing in this article or sub-clause (g) of clause (1) of article 19 or
clause (2) of article 29 shall prevent the State from making,—
(a) any special provision for the advancement of any
economically weaker sections of citizens other than the classes
mentioned in clauses (4) and (5); and
(b) any special provision for the advancement of any
economically weaker sections of citizens other than the classes
mentioned in clauses (4) and (5) in so far as such special provisions
relate to their admission to educational institutions including private
educational institutions, whether aided or unaided by the State, other
than the minority educational institutions referred to in clause (1) of
article 30, which in the case of reservation would be in addition to the
existing reservations and subject to a maximum of ten per cent. of the
total seats in each category.
______________________________________________
1. Added by the Constitution (First Amendment) Act, 1951, s. 2 (w.e.f. 18-6-1951).
2. Ins. by the Constitution (Ninety-third Amendment) Act, 2005, s. 2 (w.e.f. 20-1-2006).
3. Ins. by the Constitution (One Hundred and Third Amendment) Act, 2019, s. 2
(w.e.f. 14-1-2019).
THE CONSTITUTION OF INDIA
(Part III.—Fundamental Rights)
8
Explanation.—For the purposes of this article and article 16,
"economically weaker sections" shall be such as may be notified by the State
from time to time on the basis of family income and other indicators of
economic disadvantage.]
16. Equality of opportunity in matters of public employment.—(1)
There shall be equality of opportunity for all citizens in matters relating to
employment or appointment to any office under the State.
(2) No citizen shall, on grounds only of religion, race, caste, sex, descent,
place of birth, residence or any of them, be ineligible for, or discriminated against
in respect of, any employment or office under the State.
(3) Nothing in this article shall prevent Parliament from making any law
prescribing, in regard to a class or classes of employment or appointment to an
office 1[under the Government of, or any local or other authority within, a State
or Union territory, any requirement as to residence within that State or Union
territory] prior to such employment or appointment.
(4) Nothing in this article shall prevent the State from making any
provision for the reservation of appointments or posts in favour of any
backward class of citizens which, in the opinion of the State, is not adequately
represented in the services under the State.
2[(4A) Nothing in this article shall prevent the State from making any
provision for reservation 3[in matters of promotion, with consequential
seniority, to any class] or classes of posts in the services under the State in
favour of the Scheduled Castes and the Scheduled Tribes which, in the opinion
of the State, are not adequately represented in the services under the State.]
4[(4B) Nothing in this article shall prevent the State from considering
any unfilled vacancies of a year which are reserved for being filled up in that
year in accordance with any provision for reservation made under clause (4) or
clause (4A) as a separate class of vacancies to be filled up in any succeeding
year or years and such class of vacancies shall not be considered together with
the vacancies of the year in which they are being filled up for determining the
ceiling of fifty per cent. reservation on total number of vacancies of that year.]
______________________________________________
1. Subs. by the Constitution (Seventh Amendment) Act, 1956, s. 29 and Sch., for "under
any State specified in the First Schedule or any local or other authority within its
territory, any requirement as to residence within that State" (w.e.f. 1-11-1956).
2. Ins. by the Constitution (Seventy-seventh Amendment) Act, 1995, s. 2 (w.e.f. 17-6-1995).
3. Subs. by the Constitution (Eighty-fifth Amendment) Act, 2001, s. 2, for certain words
(retrospectively w.e.f. 17-6-1995).
4. Ins. by the Constitution (Eighty-first Amendment) Act, 2000, s. 2 (w.e.f. 9-6-2000).
THE CONSTITUTION OF INDIA
(Part III.—Fundamental Rights)
9
(5) Nothing in this article shall affect the operation of any law which
provides that the incumbent of an office in connection with the affairs of any
religious or denominational institution or any member of the governing body
thereof shall be a person professing a particular religion or belonging to a
particular denomination.
1[(6) Nothing in this article shall prevent the State from making any
provision for the reservation of appointments or posts in favour of any
economically weaker sections of citizens other than the classes mentioned in
clause (4), in addition to the existing reservation and subject to a maximum of
ten per cent. of the posts in each category.]
17. Abolition of Untouchability.—“Untouchability” is abolished and its
practice in any form is forbidden. The enforcement of any disability arising out
of “Untouchability” shall be an offence punishable in accordance with law.
18. Abolition of titles.—(1) No title, not being a military or academic
distinction, shall be conferred by the State.
(2) No citizen of India shall accept any title from any foreign State.
(3) No person who is not a citizen of India shall, while he holds any
office of profit or trust under the State, accept without the consent of the
President any title from any foreign State.
(4) No person holding any office of profit or trust under the State shall,
without the consent of the President, accept any present, emolument, or office
of any kind from or under any foreign State.
Right to Freedom
19. Protection of certain rights regarding freedom of speech, etc.—
(1) All citizens shall have the right—
(a) to freedom of speech and expression;
(b) to assemble peaceably and without arms;
(c) to form associations or unions 2[or co-operative societies];
(d) to move freely throughout the territory of India;
______________________________________________
1. Ins. by the Constitution (One Hundred and Third Amendment) Act, 2019, s. 3
(w.e.f. 14-1-2019).
2. Ins. by the Constitution (Ninety-seventh Amendment) Act, 2011, s. 2 (w.e.f. 8-2-2012).
THE CONSTITUTION OF INDIA
(Part III.—Fundamental Rights)
10
(e) to reside and settle in any part of the territory of India; 1[and]
2[(f)* * * * *]
(g) to practise any profession, or to carry on any occupation, trade or
business.
3[(2) Nothing in sub-clause (a) of clause (1) shall affect the operation of
any existing law, or prevent the State from making any law, in so far as such
law imposes reasonable restrictions on the exercise of the right conferred by the
said sub-clause in the interests of 4[the sovereignty and integrity of India], the
security of the State, friendly relations with foreign States, public order,
decency or morality, or in relation to contempt of court, defamation or
incitement to an offence.]
(3) Nothing in sub-clause (b) of the said clause shall affect the operation
of any existing law in so far as it imposes, or prevent the State from making
any law imposing, in the interests of 4[the sovereignty and integrity of India or]
public order, reasonable restrictions on the exercise of the right conferred by
the said sub-clause.
(4) Nothing in sub-clause (c) of the said clause shall affect the operation
of any existing law in so far as it imposes, or prevent the State from making
any law imposing, in the interests of 4[the sovereignty and integrity of India or]
public order or morality, reasonable restrictions on the exercise of the right
conferred by the said sub-clause.
(5) Nothing in 5[sub-clauses (d) and (e)] of the said clause shall affect
the operation of any existing law in so far as it imposes, or prevent the State
from making any law imposing, reasonable restrictions on the exercise of any
of the rights conferred by the said sub-clauses either in the interests of the
general public or for the protection of the interests of any Scheduled Tribe.
______________________________________________
1. Ins. by the Constitution (Forty-fourth Amendment) Act, 1978, s. 2 (w.e.f. 20-6-1979).
2. Sub-clause (f) omitted by s.2, ibid. (w.e.f. 20-6-1979).
3. Subs. by the Constitution (First Amendment) Act, 1951, s. 3, for cl. (2) (with retrospective
effect).
4. Ins. by the Constitution (Sixteenth Amendment) Act, 1963, s. 2 (w.e.f. 5-10-1963).
5. Subs. by the Constitution (Forty-fourth Amendment) Act, 1978, s. 2, for "sub-clauses
(d), (e) and (f)" (w.e.f. 20-6-1979).
THE CONSTITUTION OF INDIA
(Part III.—Fundamental Rights)
11
(6) Nothing in sub-clause (g) of the said clause shall affect the operation
of any existing law in so far as it imposes, or prevent the State from making
any law imposing, in the interests of the general public, reasonable restrictions
on the exercise of the right conferred by the said sub-clause, and, in particular,
1[nothing in the said sub-clause shall affect the operation of any existing law in
so far as it relates to, or prevent the State from making any law relating to,—
(i) the professional or technical qualifications necessary for practising
any profession or carrying on any occupation, trade or business, or
(ii) the carrying on by the State, or by a corporation owned or
controlled by the State, of any trade, business, industry or service,
whether to the exclusion, complete or partial, of citizens or otherwise.]
20. Protection in respect of conviction for offences.—(1) No person
shall be convicted of any offence except for violation of a law in force at the
time of the commission of the Act charged as an offence, nor be subjected to a
penalty greater than that which might have been inflicted under the law in force
at the time of the commission of the offence.
(2) No person shall be prosecuted and punished for the same offence
more than once.
(3) No person accused of any offence shall be compelled to be a witness
against himself.
21. Protection of life and personal liberty.—No person shall be
deprived of his life or personal liberty except according to procedure
established by law.
2[21A. Right to education.—The State shall provide free and
compulsory education to all children of the age of six to fourteen years in such
manner as the State may, by law, determine.]
22. Protection against arrest and detention in certain cases.—(1) No
person who is arrested shall be detained in custody without being informed, as
soon as may be, of the grounds for such arrest nor shall he be denied the right
to consult, and to be defended by, a legal practitioner of his choice""")))