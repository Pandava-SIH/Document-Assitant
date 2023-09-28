import re

Bonds = {"Format for Simple Money Bond":"""DRAFT OF SIMPLE MONEY BOND 



I, X, son of __________ resident of _______________ confirm that I am indebted to Y son of __________ resident of __________________ to the extent of Rs. _________ ( Rupees __________________________ ) on account of the price of __________________ purchased by me from the said Y and I hereby agree and covenant to pay the said sum on demand of Rs. ________________ with interest at the rate of ____ percent per annum to Y.

Date: ____________

WITNESSES

1.

2.

Signature""",
"Format for Bond and Bail bond under CrPC 1973 after Arrest under a Warrant":"""Draft of Bond and Bail Bond under Criminal Procedure Code, 1973 after Arrest Under a Warrant



I (name),  ___________ of ___________ being brought before the District Magistrate of ______________ (or as the case may be) under a warrant issued to compel my appearance to answer to the charge of ____________ do hereby bind myself to attend in the court of ____________ on the _____ day of ________,20__ to answer to the said charge, and to continue to attend until otherwise directed by the court, and in case of my making default herein, 1 bind myself to forfeit to Government, the sum of Rs. _________.

Dated this ________ day of __________ 20__

(Signature)



I, do hereby declare myself surety for the above named ______________of ____________ that he shall attend before ________________ in the court of _______________ on the ____ day of __________, 20__, to answer to the charge on which he has been arrested, and shall continue to attend until otherwise directed by the court and in case of his making default therein, I bind myself to forfeit, to Government the sum of Rs. ___________.

Dated this ______ day of ____________, 20__

Signature""",
"Format for Employee Bond for Non Compete":"""DRAFT OF EMPLOYEE BOND OF NON-COMPETE



By this Bond Mr. A residing at ... binds himself to pay to Mr. B the sum of Rs... as liquidated damages.

WHEREAS A is a qualified ............ employed by B in his factory manufacturing some ............. viz. ………........ and in the course of employment Mr. B may come to know the secret........... adopted by B in the manufacture of such products.

AND WHEREAS as per the terms of employment A has promised to B not to misuse his position by disclosing to any person the knowledge acquired by him in the manufacture of the said products and has agreed to execute this Bond.

AND WHEREAS however, in the event of A misusing his position as herein stated, he has at the request of B agreed and hereby agrees to make good the loss by paying him the said B a sum of Rs ...... as compensation.

NOW the condition of this bond is that if during the course of employment of Mr. A with Mr. B, the said A will work faithfully and honestly and shall not disclose to any person the knowledge he may get regarding the manufacture of the said products and the formulae or manufacturing process thereof and shall not,after he ceases to be the employee of Mr. A due to his resignation or dismissal or removal or for any reason whatsoever, carry on any business similar to the business of manufacturing the said products or medicines or work with any other manufacturer carrying on similar business, either as an employee or on ad hoc basis or partially or otherwise directly or Indirectly within the city of... and for a period of ......years from the time he ceases to be in the service of the said B then this Bond will become void and of no effect but otherwise it will remain in full force and effect.

In WITNESS, WEREOF the said Mr. A has put his hand this day ...

Signed and delivered by the

withinnamed Mr.………….

WITNESSES;

1.""",
"Format for Bond to Secure the Performance of a Contract":"""DRAFT OF BOND TO SECURE THE PERFORMANCE OF A CONTRACT



By this Bond I Mr. A residing at ………………..... the Obligor acknowledge to be bound to pay to Mr. B the Obligee the sum of Rs... on demand by the said Obligee.

WHEREAS by a Contract entered into between the Obligee and the Obligor, the Obligee has appointed the Obligor as a contractor to construct a building on the plot of land of Obligee situated at ... in terms of the said contract.

AND WHEREAS as the said contract provides that the Obligor will execute a bond in the sum of Rs... for the proper performance of the said contract.

NOW The Condition of this Bond is that If the Obligor contractor or his legal representatives or permitted assigns shall and will and truly, perform and fulfill and keep all and every covenant, clause, provision, term or condition in the said contract and on the part of the Obligor (Contractor) to be observed and performed according to the true purport and intent or meaning thereof, then this Bond shall be treated as void but otherwise it shall remain in full force and effect.



In Witness Whereof the Obligor has put his hand this ... day of ………….., 20__.

Signed and delivered by the

with in named Mr.………….

WITNESSES;

1.

2.""",
"Format for Security Bond by a Surety":"""DRAFT OF SECURITY BOND BY  A SURETY



By this Bond Mr………….. residing at …………………………….... hereinafter referred to as the 'Surety' acknowledges himself to be bound to Mr. B hereinafter referred to as the 'Creditor' in the sum of Rs………………….. lent and advanced by the Creditor to Mr. C residing at ... the Debtor, with interest thereon at the rate of Rs... percent per annum from the date hereof till payment.

Whereas the Creditor has lent and advanced to Mr. C the Debtor above named a sum of Rs... repayable by him with interest thereon at the rate of Rs... per cent per annum.

And Whereas the said amount has been advanced against the surety giving a guarantee for repayment of the said amount by the said Debtor and against the said guarantee being secured by a mortgage of the property of the Surety described in the Schedule hereunder written and which the Surety has at the request of the Debtor agreed to do.

Now This Deed Witnesseth that in pursuance of there request made by the Debtor to the Surety the Surety doth hereby guarantor and covenants with the Creditor that in default of payment of the amount of Rs... with interest as aforesaid by the Debtor to the Creditor within the lime stipulated by him in the separate writing executed by the Debtor-for evidencing the said Debt, in favour of the Creditor, the surety shall pay to the Creditor the said amount of Rs... or any part thereof remaining unpaid with Interest at the rate of ... aforesaid till payment on demand made to the Creditor in writing

And This Deed Further Witnesseth that pursuant to the said agreement, the Surety as a security for payment of the said amount by the Surety, doth hereby grant and transfer by way of mortgage the said property described in the Schedule hereunder written TO HAVE and TO HOLD the same unto the Creditor subject to the covenant for redemption hereinafter contained And it is agreed and declared that in the event of the Surety being required to pay the said amount on default by the Debtor and on the surety so paying the said amount or any part thereof due and payable to the Creditor the Creditor shall release and recovery the said property to the Surety but at the costs of the Surety And it is further agreed that in the event of the Surety becoming liable and failing to pay the said amount or any part thereof as aforesaid, the Creditor will be entitled to sell the said property through a Court of law and to appropriate or apply the net sale proceeds thereof towards payment of the amount to the Creditor by the Surety and/ or the Debtor including costs of the suit and sale proceedings and to pay the balance if any to the Surety. And the Surety covenants with the Creditor that he has full right to mortgage the said property as aforesaid. And the condition of the Bond is that it will be void if the Debtor pays the said amount to the Creditor with interest as aforesaid, within the time stipulated otherwise, and failing which this Bond will remain in full force and effect.

The Schedule Above Referred To

Signed and delivered by the

withinnamed Surety Mr. A

WITNESSES;

1

2.""",
"Format for Security Bond for grant of Succession Certificate":"""Draft of Security Bond for Grant of Succession Certificate (Section 375, Indian Succession Act, 1925)


Know All Men that we,JN, s/o Late GP r/o ………………… and Mr NK, s/o …………………… r/o …………………… (Surety for Mr JN) bind ourselves jointly and severally to Shri JP, Distt. Judge, ……………………. for payment to him or his successor in office of the sum of Rs……………

We have signed this bond on this………day of…………at ………………….

Signature………………….

Administration

Signature………………….

Surety

WHEREAS, the Court of the said District Judge, Mr. JP, has passed the order on the day of………and has granted the succession certificates in favour of the said Mr. JN to the estate of Late JN deceased on the condition that said Mr. JN execute a bond with one surety of Rs………..

AND WHEREAS,the said Mr. JN has agreed to execute the bond for the said Rs………..and the said Mr. NK has agreed to enter into the above bond as surety for said Mr. JN.

NOW, This Bond Witnesses As Under:

NOW, the condition of the above bond is as under:

1.     That the said Mr. JN shall prepare an inventory of the property of the deceased within six months form the date of the execution of the bond.

2.     That the accounts of the debtor and creditor shall also be prepared by the said Mr. JN.

3.     That the said Mr. JN shall indemnify the person who may be entitled to the whole or any part of such debts.

4.     That if the above condition is satisfied then the bond shall remain in force, otherwise the bond shall be void.

We the above mentioned parties have signed this bond on this……….day of ………after fully understanding the contents of this bond in the presence of the following witnesses.

WITNESSES:

1. Name…………..                                                    Signature …………..

    Address…………                                                  Successor

2. Name…………..                                                    Signature ………..

    Address…………                                                  Surety""",
"Format for Lease Deed (for a term of years) Rent Agreement":"""Draft of Deed of Lease (for a Term of Years) Rent Agreement



This Deed of Lease is made at ..... this ..... day of ...... between A of ..... hereinafter called 'The Lessor' of the One Part and B also of ..... hereinafter called 'The Lessee' of the Other Part.

WHEREAS the Lessor is absolutely seized and possessed of or otherwise well and sufficiently entitled to the land and premises described in the Schedule hereunder written.

AND WHEREAS the Lessor has agreed to grant to the Lessee a lease in respect of the said land and premises for a term of .... years in the manner hereinafter appearing.

NOW  This Deed Witnesseth as Follows:

1.     In pursuance of the said agreement and in consideration of the rent hereby reserved and of the terms and conditions, convenants and agreements herein contained and on the part of the Lessee to be observed and performed the Lessor doth hereby demise unto the Lessee all that the said land and premises situated at.............…………..and described in the Schedule hereunder written (hereinafter for the brevity's sake referred to as 'the demised premises') to hold the demised premises unto the Lessee (and his heirs, executors, administrators and assigns) for a term of ....... years commencing from the 1st day of ...……….., 20___, but subject to the earlier determination of this demise as hereinafter provided and yielding and paying therefor during the said term the monthly ground rent of Rs ........ free and clear of all deductions and strictly in advance on or before the..... day of each and every calendar month. The first of such monthly ground rent shall be paid on the ___ day of ....... and the subsequent rent to be paid on or before the ___ day of every succeeding month regularly.

2.     The Lessee hereby for himself, his heirs, executors, administrators and assigns and to the intent that the obligations herein contained shall continue throughout the term hereby created covenants with the Lessor as follows:

a.     To pay the ground rent hereby reserved on the days and in the manner aforesaid clear of all deductions. The first of such monthly rent as hereinbefore provided shall be paid on the.... of ....... and the subsequent rent shall be paid on the.... day of every succeeding month regularly and If the-ground rent is not paid on the due dates the Lessee shall pay interest thereon at the rate of ....... % per annum from the due date till payment, though the payment of Interest shall not entitle the Lessee to make default in payment of rent on due dates.

b.    To bear pay and discharge the existing and future rates. taxes and assessment duties, cess, impositions, outgoing and burdens whatsoever which may at any time or from time to time during the term hereby created be Imposed or charged upon the demised land and the building or structures standing thereon and on the buildings or structures hereafter to be erected and for the time being standing on the demised land and payable either by the owners, occupiers or tenants thereof and to keep the Lessor and his estate and effects Indemnified against all such payment. The annual Municipal and other taxes at present are Rs…………...

c.     To keep the buildings and structures on the demised premises ,in good and tenantable repairs in the same way as the Lessor is liable to do under the law provided that if the Lessee so desires he shall have power to demolish any existing building or structure without being accountable to the Lessor for the building material of such building and structure and the Lessee shall have also power to construct any new buildings in their place.

d.    The Lessee shall be at liberty to carry out any additions or alterations to the buildings or structures at present existing on the demised premises or to put up any additional structures or buildings on the demised premises In accordance with the plans approved by the authorities at any time or from time to time during the subsistence of the term hereby created.

e.     Not to sell or dispose of any earth, gravel or sand from the demised land and not to excavate the same except so far as may be necessary for the execution of construction work.

f.     To use or permit to be used the buildings and structures to be constructed on the demised premises for any and all lawful purposes as may be permitted by the authorities from time to time.

3.     The Lessor doth hereby covenant with the Lessee that:

a.     the Lessor now has in himself good right full power and absolute authority to demise unto the Lessee the demised premises and the buildings and structures standing thereon In the manner herein appearing………..

b.    that on the Lessee paying the said monthly ground rent on the due dates thereof and in the manner herein provided and observing and performing the covenants,conditions, and stipulations herein contained and on his part to be observed and performed shall and may peaceably and quietly hold, possess and enjoy the demised premises together with the buildings and structures standing thereon during the term hereby created without any eviction, interruption, disturbance, claim and demand whatsoever by the Lessor or any person or persons lawfully or equitably claiming by, from, under or in trust for him.

4.     It is hereby agreed and declared that these presents are granted on the express condition that if the said monthly ground rent or any part thereof payable in the manner hereinbefore mentioned shall be an arrears for the space of ...... months after the same shall have become due and payable on any of the said days wherein the same ought to be paid as aforesaid whether the same shall or shall not be legally demanded or If any of the covenants and stipulations herein contained and on the part of the Lessee to be observed and performed shall not be so observed and performed by the Lessee or If the Lessee shall raise an objection to the amount of the monthly ground rent hereby fixed for any reason whatsoever then and in such event it shall be lawful for the Lessor or any person or persons duly authorised by him in that behalf at any time hereafter to enter into and upon the land and premises and the buildings and structures constructed or to he constructed thereon or any part or parts thereof in the name of the whole and the same to have, possess and enjoy and thereupon this demise shall absolutely determine but without prejudice to the right of action of the Lessor in respect of any breach of any of the covenants by the Lessee herein contained PROVIDED ALWAYS that, no re-entry shall be made under the foregoing power for breach of the covenants and stipulations herein contained and on the part of the Lessee to be observed and performed (save and except the covenant for payment of rent) unless and until the Lessor shall have given to the Lessee a notice in writing specifying the covenants and conditions or stipulations which require to be complied with or carried out and the Lessee shall have failed to comply with or carry out the same within ..... month from the date of the receipt of by such notice.

5.     And it is hereby expressly agreed and declared between the parties as follows-

a.     On the expiration of the term hereby created or earlier determination under the provisions hereof all the buildings and structures standing on the demised land shall automatically vest in the Lessor without payment of any compensation therefor by the Lessor to the Lessee.

b.    The Lessee shall not be entitled, without obtaining In writing the permission of the Lessor, to assign mortgage, sublet (except to the extent of creating monthly tenancies) or otherwise part with possession of the demised premises or any of them or any part thereof and the buildings and structure standing thereon though such permission shall not be unreasonably withheld.

IN WITNESS WHEREOF the Lessor and the Lessee have put their respective hands on the original and duplicate hereof the day and year first herein above written.

THE SCHEDULE ABOVE REFERRED TO

Signed and delivered by the

Withinnamed Lessor ........ in the presence of ........

Signed and delivered by the

Withinnamed Lessee ........ in the presence of ........""",
"Format for Deed of lease (for a term in perpetuity)":"""Draft of Deed of Lease (for a Term in Perpetuity)



This Deed Of Lease is made at ... this ... day of... between Mr. A of ... hereinafter called 'the Lessor' of the One Part AND Mr. B of... hereinafter called 'the Lessee' of the Other Part

Whereas the Lessor is absolutely seized and possessed of or otherwise well and sufficiently entitled to a large piece of land situate at... and described In the Schedule hereunder written.

And Whereas the Lessee has approached the Lessor and requested him to grant to him a lease of the said land in perpetuity as he wants to develop the same by constructing Industrial sheds thereon and establish an Industrial Estate.

And Whereas the Lessor has agreed to grant to the Lessee a lease in respect of the said land for a term in perpetuity in the manner hereinafter appearing.

Now This Deed Witnesseth as Follows:

1.     In pursuance of the said agreement and in consideration of the rent hereby reserved and of the terms and conditions, covenants and agreements herein contained and on the part of the Lessee to be observed and performed the Lessor doth hereby demise unto the Lessee all that the said piece of land situate at ... In the Registration Sub - District of ... and District of ... and described in the schedule hereunder written (hereinafter for the sake of brevity referred to as 'the demised Land') to hold the demised land unto the Lessee and his heirs, executors, administrators and assigns for a term in perpetuity commencing from the 1st day of... but subject to the earlier determination of this demise as hereinafter provided and yielding and paying therefor during the said term the yearly ground rent of Rs. ... free and clear of all deductions and strictly in advance on or before the 5th day of each and every calendar year, the first of such yearly ground rent shall be paid on the 5th day of the month of ... and the subsequent rent to be paid on or before the 5th day of that month in each and every succeeding year regularly.

2.     The Lessee hereby for himself, his heirs, executors, administrators and assigns and to the intent that the obligations herein contained shall continue throughout the term hereby created covenants with the Lessor as follows :-

a.     To pay the ground lease rent hereby reserved on the days and in the manner aforesaid clear of all deductions. If the Lease rent is not paid on the due dates, the Lessee shall pay interest thereon at the rate of ... % per annum from the due date till payment, though the payment of interest shall not entitle the Lessee to make default in payment of rent on due dates or dis-entitle the Lessor to exercise his other rights under these Presents or in law.

b.    To bear, pay and discharge the existing and future rates, taxes, and assessment duties, cess, impositions, outgoing and burdens whatsoever which may at any time or from time to tune during the term hereby created be imposed or charged upon the demised land and the buildings or structures that may be standing thereon and hereafter to be erected and for the time being standing on the demised land and payable either by the owners. occupiers or tenants thereof and to keep the Lessor and his estate and effects indemnified against all such payments.

c.     To keep the buildings and structures on the demised land in good and tenantable repairs In the same way as the Lessor would be liable to do under the law as the owner of the demised land and the buildings and structures thereon.

d.    Not to sell or dispose of any earth, gravel or sand from the demised land and not to excavate the same except so far as may be necessary for the execution of construction work of any building or structures.

e.     To use or permit to be used the said land and the buildings and structures to be constructed thereon for industrial purposes only as may be permitted by the authorities from time to time.

3.     The Lessee will be at liberty to prepare a layout of the said demised land and divide the same Into separate industrial plots, with the sanction of the local authority concerned and to construct Industrial sheds thereon suitable for carrying on small scale industries. The Lessee shall also be at liberty to sub-demise the said plots or any one of more of them and/or the sheds constructed thereon on such terms as the Lessee may think fit provided that such subleases shall not be for a period of more than... years at a time and they shall be subject to the terms, covenants and conditions of this demise. All such sheds shall be in accordance with the plans sanctioned by the Municipal or any other local authority competent to do so.

4.     The Lessee will be entitled to assign this lease in respect of the said demised land or any part or parts thereof with the previous consent of the Lessor In writing and which consent may be granted by the Lessor on such terms as he may think fit including the term of paying premium for each assignment, If It Is allowed by law, but such consent shall not be unnecessarily or unreasonably withheld.

5.     The Lessor doth hereby covenant with the Lessee that –

a.     the Lessor now has in himself good right, full power and absolute authority to demise unto the Lessee the demised land in the manner herein appearing;

b.    that on the Lessee, paying the said yearly ground rent on the due dates thereof and in the manner herein provided and observing and performing the covenants, conditions and stipulations herein contained and on his part to be observed and performed, shall and may peaceably and quietly hold, possess and enjoy the demised land together with the buildings and structures standing thereon during the term hereby created without any eviction, Interruption, disturbance, claim and demand whatsoever by the Lessor or any person or persons lawfully or equitably claiming by, from. under or In trust for him.

6.     It is hereby agreed and declared that these presents are on the express condition that if the said yearly ground lease rent or any part thereof payable in the manner hereinbefore mentioned shall be In arrears for the space of three months after the same shall have become due and payable on any of the said days wherein the same ought to be paid as aforesaid whether the same shall or shall not he legally demanded or if any of the covenants and stipulations herein contained and on the part of the Lessee to be observed and performed shall not be so observed and performed by the Lessee or any person claiming under him or If the Lessee shall raise an objection to the amount of the yearly ground lease rent hereby fixed for any reason whatsoever then and in such an event It shall be lawful for the Lessor or any person claiming under him or any person or persons duly authorised by him In that behalf at any time hereafter to enter Into and upon the land and premises and the buildings and structures to be constructed thereon or any part or parts thereof In the name of the whole and the same to have. possess and enjoy and thereupon this demise shall absolutely determine but without prejudice to the right of action of the Lessor In respect of any breach of Any of the covenants by the Lessee herein contained PROVIDED ALWAYS that no re-entry shall be made under the foregoing power for breach of the covenants and stipulations herein contained and on the part of the Lessee to be observed and performed (save and except t c covenant for payment of rent) unless and until the Lessor shall have given to the Lessee a notice in writing specifying the covenants and conditions or stipulations which require to be complied with or carried out and the Lessee shall have failed to comply with or carry out the same within one month from the date of the receipt of such notice.

7.     And It Is Hereby Expressly Agreed And Declared Between The Parties As Follows:-

a.     On the determination of this deed and the demise granted under the provisions hereof all the buildings and structures standing on the demised land shall be removed or caused to be removed by the Lessee, his heirs, executors, administrators and assigns or subleases within three months from the date of such determination failing which those which will not be so removed shall automatically stand forfeited to the Lessor without payment of any compensation therefor by the Lessor to the Lessee or to his assigns or subleases.

b.    The personal liability of the Lessee to pay the yearly lease rent will be absolute and will not be affected by the Lessee granting by sub-demise any portion of the demised land or any shed or structure thereon and notwithstanding the consent given to sub-lease or to the assignment of the demised land or any portion thereof. the said liability will continue unabated.

c.     That at any time or times during subsistence of this demise the Lessee shall have the option to purchase the reversion In respect of the demised land or any part or parts thereof on the payment to the Lessor of the market price therefor then prevailing and the Lessor shall in respect of the demised land or any portion therefor so purchased, execute a deed or conveyance and/or conveyances In respect thereof in favour of the Lessee and/or his nominee or nominees and that at the time of execution of each such conveyance the Lessor shall make out a marketable title in respect of the portion so to be purchased. Provided further that. the stamp and registration charges In respect of such conveyance shall be borne and paid by the Lessee alone. Provided further that, in the event of purchase of the reversion in respect of any portion of the demised premises the rent hereby agreed to be paid shall be proportionately reduced. In the event of any disagreement between the Lessor and Lessee regarding the market price of the demised land or any portion thereof the same shall be decided by arbitration of two arbitrators one to be appointed by each party and the arbitration will be governed by the Arbitration Act, 1940.

IN WITNESS WHEREOF the Lessor and the Lessee have put their respective hands on the original and duplicate thereof the day and year first hereinabove written.

THE SCHEDULE ABOVE REFERRED TO

Signed and delivered by the Withinnamed Lessor Mr... in the presence of ...

Signed and delivered by the Withinnamed Lessee Mr... in the presence of ...""",
"Format for Leave and License Agreement":"""Draft of Leave and License Agreement



This Agreement is made at ...... this ...... day of ……......., 20___, between Mr. A hereinafter referred to as 'the Licensor' of the One Part and Mr. B of …………… hereinafter referred to as the 'Licensee' of the Other Part, as follows;

Whereas the Licensor is the owner of a piece of land at ………………………………... bearing Survey No ... with a building consisting of …………. floor ...... having built up area of about ..... square feet.

And Whereas the Licensee has approached the licensor with a request to allow the Licensee to temporarily occupy and use a portion of the ...... floor of the said building, admeasuring about ...... square feet for carrying on his ...... business, on leave and license basis until the Licensee gets other more suitable accommodation.

And Whereas the Licensor has agreed to grant leave and license to the Licensee to occupy and use the said ground floor portion of the said building and which portion is shown on the plan hereto annexed by red boundary line on the following terms and conditions agreed to between the parties hereto;

Now it is agreed by and between the parties hereto as follows..

1.     The Licensor hereby grants leave and license to the Licensee to occupy and use the said portion of the ground floor/....... floor of the said building of the Licensor (hereinafter referred to as the Licensed Premises) for a period of eleven months from ...... The Licensee agrees to vacate the said premises even earlier If the Licensee secures any other accommodation in the locality where the said premises are situated.

2.     The Licensee shall pay to the Licensor a sum of Rs………..... per month (calculated at the rate of Rs………..... per square foot) as License fee or compensation to be paid in advance for each month on or before the ...... day of each month.

3.     All the Municipal taxes and other taxes and levies in respect of the licensed premises will be paid by the Licensor alone.

4.     The electric charges and water charges for electric and water consumption in the said licensed premises will be paid by the Licensee to the authorities concerned and the Licensor will not be responsible for the same. For the sake of convenience a separate electric and water meter if possible will be provided in the said premises.

5.     The Licensee will be allowed to use the open space near the entrance to the Licensed premises and shown on the said plan by green wash for parking cars during working hours of the Licensee and not for any other time and no car or other vehicle will be parked on any other part of the said plot.

6.     The licensed premises will be used only for carrying on business and for no other purpose.

7.     The licensed premises have normal electricity fittings and fixtures. If the Licensee desires to have any additional fittings and fixtures, the Licensee may do so at his cost and in compliance with the rules. The Licensee shall remove such fittings and fixtures on the termination of the license failing which they shall be deemed to be the property of the Licensor.

8.     The licensed premises are given to the Licensee on personal basis and the Licensee will not be entitled to transfer the benefit of this agreement to anybody else or will not be entitled to allow anybody else to occupy the premises or any part thereof. Nothing in this agreement shall be deemed to grant a lease and the licensee agrees and undertakes that no such contention shall be taken up by the Licensee at any time.

9.     The Licensee shall not be deemed to be in the exclusive occupation of the licensed premises and the Licensor will have the right to enter upon the premises at any time during working hours to inspect the premises.

10.  The Licensee shall maintain the licensed premises in good condition and will not cause any damage thereto. If any damage is caused to the premises or any part thereof by the Licensee or his employees, servants or agents the same will be made good by the Licensee at the cost of the Licensee either by rectifying the damage or by paying cash compensation as may be determined by the Licensor's Architect.

11.  The Licensee shall not carry out any work of structural repairs or additions or alterations to the said premises. Only such alterations or additions as are not of structural type or of permanent nature may be allowed to be made by the Licensee inside the premises with the previous permission of the Licensor.

12.  The Licensee shall not cause any nuisance or annoyance to the people-in the neighbourhood or store any hazardous goods on the premises.

13.  If the Licensee commits a breach of any term of this agreement then notwithstanding anything herein contained the Licensor will be entitled to terminate this agreement by fifteen days' prior notice to the Licensee.

14.  On the expiration of the said term or period of the License or earlier termination thereof, the Licensee shall hand over vacant and peaceful possession of the Licensed premises to the Licensor In the same condition In which the premises now exist subject to normal wear and tear. The Licensee's occupation of the premises after such termination will be deemed to be that of a trespasser.

IN WITNESS WHEREOF the parties hereto have put their hands the day and year first hereinabove written.

Signed by the withinnamed Licensor Shri ................

in the presence of ............

Signed by the within named Licensee Shri .......

in the presence of .........""",
"Format for Simple Mortgage Deed":"""Draft of Simple Mortgage Deed



This Deed of Mortgage made at ...................... this ................ day of ................... Between X, son of ............................... resident of ............................ hereinafter called as a mortgagor of the ONE PART and Y, son of ...................... resident of .................. hereinafter called as a mortgagee of the OTHER PART.

WHEREAS, the mortgagor is absolutely seized and possessed of or otherwise well and sufficiently entitled to the house bearing municipal no................ situated on ........................ Road, ....................... more particularly described in the Schedule hereunder written;

AND WHEREAS, the mortgagor has requested the mortgagee to lend him a sum of Rs. ........................ which the mortgagee has agreed on the mortgagor mortgaging his property.

NOW,This Deed Witnesseth That in pursuance to the said agreement and in consideration of the sum of Rs. .................. at or before the execution of these presents paid by the mortgagee to the mortgagor (the receipt whereof, the mortgagor doth hereby admit and acknowledge and of and from the same hereby release and discharge the mortgagee), the mortgagor hereby covenants with the mortgagee that he will pay on the ..................... day of ................. (hereinafter called "the said date"), the said sum of Rs. ................. with interest @ ........ % per annum from the date of these presents till the repayment of the said sum in full, every quarter the first instalment of interest to be paid on the ................... day of .......... 20___ and each subsequent instalment on the ................ day of July, October, January and April of each succeeding year until the said sum is repaid in full.

AND this deed further WITNESSETH that

In consideration aforesaid, the mortgagor doth hereby transfer by way of mortgage his house bearing municipal no ................. situated on .............. Road . ...................... and more particularly described in the Schedule hereunder written as a security for repayment of the said sum with interest @ ................ per annum with the condition that the mortgagor, his heirs, executors, administrators or assigns shall on the said the pay to the mortgagee, his heirs, executors, administrators or assigns the said sum of Rs .............. together with interest thereon at the rate mentioned above, the said mortgagee, his heirs, executors, administrators, or assigns shall at any time thereafter upon the request and at the cost of the mortgagor, his heirs, executors, administrators or assigns reconvey the said house, hereinbefore expressed to be mortgaged unto or to the use of the mortgagor, his heirs, executors, administrators or assigns or as he or they shall direct.

And It Is Hereby Agreed And Declared that if the mortgagor does not pay the said mortgage amount with interest when shall become due and payable under these presents, the mortgagee shall be entitled to sell the said house through any competent court and to realise and receive the said mortgage amount and interest, out of the sale proceeds of the house.

And It Is Further Agreed And Declared by the mortgagor that during the period, the mortgage amount is not paid and the said house remains as a security for the mortgage amount, the mortgagor shall insure the said house and take out an insurance policy in the joint names of the mortgagor and mortgagee and continue the said policy in full force and effect by paying premium and in case of default by the mortgagor to insure or to keep the insurance policy in full force and effect, the mortgagee can insure the said house and the premium paid by the mortgagee will be added to the mortgage amount, if not paid by the mortgagor on demand.

And It Is Further Agreed That the mortgagor can grant lease of the said house with the consent of the mortgagee in writing.

And It Is Further Agreed by the Mortgagor that he shall bear stamp duty, registration charges and other out of pocket expenses for the execution and registration of this deed and reconveyance deed but however each party will bear cost and professional charges of his Solicitor/Advocate.

IN WITNESS WHEREOF the parties have put their hands the day and year first hereunder written.

The Schedule above referred to

Signed and delivered by X the within named mortgagor

Signed and delivered by Y the within named mortgagee

WITNESSES;

1.

2""",
"Format for Agreement for Sale of a House (Sale Agreement)":"""   Draft of Agreement for Sale of a House



This Agreement of sale made at .................. on this .............. day of ................... 20___, between A son of ..................... resident of .................. hereinafter called the vendor of the ONE PART and B son of ............................... resident of .............................. hereinafter called the purchaser of the OTHER PART.

WHEREAS the vendor is absolutely seized and possessed of or well and sufficiently entitled to the house more fully described in the Schedule hereunder:

AND WHEREAS,the vendor has agreed to sell his house to the purchaser on the terms and conditions hereafter set-forth.

NOW this Agreement Witnesseth as Follows

1.     The vendor will sell and the purchaser will purchase that entire house No....................... Road ...................... more particularly described in the Schedule hereunder written at a price of Rs. ................. free from all encumbrances.

2.     The purchaser has paid a sum of Rs. ................. as earnest money on ......................... (the receipt of which sum, the vendor hereby acknowledges) and the balance amount of consideration will be paid at the time of execution of conveyance deed.

3.     The sale shall be completed within a period of......... months from this date and it is hereby agreed that time is the essence of the contract.

4.     The vendor shall submit the title deeds of the house in his possession or power to the purchaser's advocate within one week from the date of this agreement for investigation of title and the purchaser will intimate about his advocate's report within ................ days after delivery of title deeds to his advocate.

5.     If the purchaser's Advocate gives the report that the vendor's title is not clear, the vendor shall refund the earnest money, without interest to the purchaser within ................. days from the date of intimation about the advocate's report by the purchasers. If the vendor does not refund the earnest money within ................... days from the date of intimation about the advocate's report, the vendor will be liable to pay interest @ ................ p.m. upto the date of repayment of earnest money.

6.     The vendor declares that the sale of the house will be without encumbrances.

7.     The vendor will hand over the vacant possession of the house on the execution and registration of conveyance deed.

8.     If the purchaser commits breach of the agreement, the vendor shall be entitled to forfeit the earnest money paid by the purchaser to the vendor and the vendor will be at liberty to resell the property to any person.

9.     It the vendor commits breach of the agreement, he shall be liable to refund earnest money, received by him and a sum of Rs. ................. by way of liquidated damages.

10.  The vendor shall execute the conveyance deed in favour of the purchaser or his nominee as the purchaser may require, on receipt of the balance consideration.

11.  The vendor shall at his own costs obtain clearance certificate under section 230A, Income tax Act, 1961 and other permissions required for the completion of the sale.

12.  The expenses for, preparation of the conveyance deed, cost of stamp, registration charges and all other cut of pocket expenses shall be borne by the purchaser.

Schedule above referred to

IN WITNESS WHEREOF the parties have set their hands to this Agreement on the day and year first hereinabove written.

Signed and delivered by Shri A..............

the within named vendor

Signed and delivered by Shri B ………..

The within named purchaser

WITNESSES;

1.

2""",
"Format for Agreement between Independent Contractor and Service Provider":"""Draft of Agreement between Independent Contractor and Service Provider


This agreement is only a guideline it can be costumesied as per the requirement

This Agreement is entered into as of the ________ day of ________________, 20____, between [ABC company located at ______] (Hereinafter referred as "the Company") and [XYZ service provider's name] (Hereinafter referred as the "the Contractor" for the sake of brevity).

1.     Independent Contractor. Subject to the terms and conditions of this Agreement, the Company hereby engages the Contractor as an independent contractor to perform the services set forth herein, and the Contractor hereby accepts such engagement.

2.     Duties, Term, and Compensation. The Contractor's duties, term of engagement, compensation and provisions for payment thereof shall be as set forth in the estimate previously provided to the Company by the Contractor and which is attached as Exhibit A, which may be amended in writing from time to time, or supplemented with subsequent estimates for services to be rendered by the Contractor and agreed to by the Company, and which collectively are hereby incorporated by reference.

3.     Expenses. During the term of this Agreement, the Contractor shall bill and the Company shall reimburse [him or her] for all reasonable and approved out-of-pocket expenses which are incurred in connection with the performance of the duties hereunder. Notwithstanding the foregoing, expenses for the time spent by Contractor in traveling to and from Company facilities shall not be reimbursable.

4.     Written Reports. The Company may request that project plans, progress reports and a final results report be provided by Contractor on a monthly basis. A final results report shall be due at the conclusion of the project and shall be submitted to the Company in a confidential written report at such time. The results report shall be in such form and setting forth such information and data as is reasonably requested by the Company.

5.     Inventions. Any and all inventions, discoveries, developments and innovations conceived by the Contractor during this engagement relative to the duties under this Agreement shall be the exclusive property of the Company; and the Contractor hereby assigns all right, title, and interest in the same to the Company. Any and all inventions, discoveries, developments and innovations conceived by the Contractor prior to the term of this Agreement and utilized by [him or her] in rendering duties to the Company are hereby licensed to the Company for use in its operations and for an infinite duration. This license is non-exclusive, and may be assigned without the Contractor's prior written approval by the Company to a wholly-owned subsidiary of the Company.

6.     Confidentiality. The Contractor acknowledges that during the engagement [he or she] will have access to and become acquainted with various trade secrets, inventions, innovations, processes, information, records and specifications owned or licensed by the Company and/or used by the Company in connection with the operation of its business including, without limitation, the Company's business and product processes, methods, customer lists, accounts and procedures. The Contractor agrees that [he or she] will not disclose any of the aforesaid, directly or indirectly, or use any of them in any manner, either during the term of this Agreement or at any time thereafter, except as required in the course of this engagement with the Company. All files, records, documents, blueprints, specifications, information, letters, notes, media lists, original artwork/creative, notebooks, and similar items relating to the business of the Company, whether prepared by the Contractor or otherwise coming into [his or her] possession, shall remain the exclusive property of the Company. The Contractor shall not retain any copies of the foregoing without the Company's prior written permission. Upon the expiration or earlier termination of this Agreement, or whenever requested by the Company, the Contractor shall immediately deliver to the Company all such files, records, documents, specifications, information, and other items in his possession or under [his or her] control. The Contractor further agrees that he will not disclose his retention as an independent contractor or the terms of this Agreement to any person without the prior written consent of the Company and shall at all times preserve the confidential nature of his relationship to the Company and of the services hereunder.

7.     Conflicts of Interest; Non-hire Provision. The Contractor represents that he is free to enter into this Agreement and that this engagement does not violate the terms of any agreement between the Contractor and any third party. Further, the Contractor, in rendering his duties shall not utilize any invention, discovery, development, improvement, innovation, or trade secret in which he does not have a proprietary interest. During the term of this agreement, the Contractor shall devote as much of his productive time, energy and abilities to the performance of his duties hereunder as is necessary to perform the required duties in a timely and productive manner. The Contractor is expressly free to perform services for other parties while performing services for the Company. For a period of six months following any termination, the Contractor shall not, directly or indirectly hire, solicit, or encourage to leave the Company's employment, any employee, consultant,or contractor of the Company or hire any such employee, consultant, or contractor who has left the Company's employment or contractual engagement within one year of such employment or engagement.

8.     Right to Injunction. The parties hereto acknowledge that the services to be rendered by the Contractor under this Agreement and the rights and privileges granted to the Company under the Agreement are of a special, unique, unusual, and extraordinary character which gives them a peculiar value, the loss of which cannot be reasonably or adequately compensated by damages in any action at law, and the breach by the Contractor of any of the provisions of this Agreement will cause the Company irreparable injury and damage. The Contractor expressly agrees that the Company shall be entitled to injunctive and other equitable relief in the event of, or to prevent, a breach of any provision of this Agreement by the Contractor. Resort to such equitable relief, however, shall not be construed to be a waiver of any other rights or remedies that the Company may have for damages or otherwise. The various rights and remedies of the Company under this Agreement or otherwise shall be construed to be cumulative, and no one of the them shall be exclusive of any other or of any right or remedy allowed by law.

9.     Merger. This Agreement shall not be terminated by the merger or consolidation of the Company into or with any other entity.

10.  Termination. The Company may terminate this Agreement at any time within ".....working days''  by a written notice to the Contractor. In addition, if the Contractor is convicted of any crime or offense, fails or refuses to comply with the written policies or reasonable directive of the Company, is guilty of serious misconduct in connection with performance hereunder, or materially breaches provisions of this Agreement, the Company at any time may terminate the engagement of the Contractor immediately and without prior written notice to the Contractor.

11.  Independent Contractor. This Agreement shall not render the Contractor an employee, partner, agent of, or joint venture with the Company for any purpose. The Contractor is and will remain an independent contractor in [his/her] relationship to the Company. The Company shall not be responsible for withholding taxes with respect to the Contractor's compensation hereunder. The Contractor shall have no claim against the Company hereunder or otherwise for vacation pay, sick leave, retirement benefits, social security, worker's compensation, health or disability benefits, unemployment insurance benefits, or employee benefits of any kind.

12.  Insurance. The Contractor will carry liability insurance (including malpractice insurance, if warranted) relative to any service that [he or she] performs for the Company.

13.  Successors and Assigns. All of the provisions of this Agreement shall be binding upon and inure to the benefit of the parties hereto and their respective heirs, if any, successors, and assigns.

14.  Choice of Law. The laws of the state of [______________] shall govern the validity of this Agreement, the construction of its terms and the interpretation of the rights and duties of the parties hereto.

15.  Arbitration. Any controversies arising out of the terms of this Agreement or its interpretation shall be settled in [____________________] in accordance with the rules of the American Arbitration Association, and the judgment upon award may be entered in any court having jurisdiction thereof.

16.  Headings. Section headings are not to be considered a part of this Agreement and are not intended to be a full and accurate description of the contents hereof.

17.  Waiver. Waiver by one party hereto of breach of any provision of this Agreement by the other shall not operate or be construed as a continuing waiver.

18.  Assignment. The Contractor shall not assign any of [his or her] rights under this Agreement, or delegate the performance of any of [his or her] duties hereunder, without the prior written consent of the Company.

19.  Notices. Any and all notices, demands, or other communications required or desired to be given hereunder by any party shall be in writing and shall be validly given or made to another party if personally served, or if deposited in the United States mail, certified or registered, postage prepaid, return receipt requested. If such notice or demand is served personally, notice shall be deemed constructively made at the time of such personal service. If such notice, demand or other communication is given by mail, such notice shall be conclusively deemed given five days after deposit thereof in the United States mail addressed to the party to whom such notice, demand or other communication is to be given as follows:

If to the Contractor:

[ name and complete address]

If to the Company:

[ name & Complete Address]

Any party hereto may change its address for purposes of this paragraph by written notice given in the manner provided above.

20.  Modification or Amendment. No amendment, change or modification of this Agreement shall be valid unless in writing signed by the parties hereto.

21.  Entire Understanding. This document and any exhibit attached constitute the entire understanding and agreement of the parties, and any and all prior agreements, understandings, and representations are hereby terminated and canceled in their entirety and are of no further force and effect.

22.  Unenforceability of Provisions. If any provision of this Agreement, or any portion thereof, is held to be invalid and unenforceable, then the remainder of this Agreement shall nevertheless remain in full force and effect.

IN WITNESS WHEREOF the undersigned have executed this Agreement as of the day and year first written above. The parties hereto agree that facsimile signatures shall be as effective as if originals.

[Company name]

By:____________________

Its:____________________ [title or position]

[Contractor's name]

By:____________________

Its:____________________ [title or position]
 


SCHEDULE A

DUTIES, TERM, AND COMPENSATION

DUTIES: The Contractor will [describe here the work or service to be performed]. [____] will report directly to [name] and to any other party designated by [name] in connection with the performance of the duties under this Agreement and shall fulfill any other duties reasonably requested by the Company and agreed to by the Contractor.

TERM: This engagement shall commence upon execution of this Agreement and shall continue in full force and effect through [date] or earlier upon completion of the Contractor's duties under this Agreement. The Agreement may only be extended thereafter by mutual agreement, unless terminated earlier by operation of and in accordance with this Agreement.

COMPENSATION: (Choose A or B)

A.    As full compensation for the services rendered pursuant to this Agreement, the Company shall pay the Contractor at the hourly rate of [dollar amount] per hour, with total payment not to exceed [ amount] without prior written approval by an authorized representative of the Company. Such compensation shall be payable within 30 days of receipt of Contractor's monthly invoice for services rendered supported by reasonable documentation.

B.    As full compensation for the services rendered pursuant to this Agreement, the Company shall pay the Contractor the sum of ____________________ [ amount], to be paid _______________ [time and conditions of payment.]""",
"Format for Business Services Agreement":"""DRAFT OF BUSINESS SERVICE AGREEMENT



 AGREEMENT made at..........this ____ day of _______ 20____ BETWEEN ------------------ situated at ----------------- (hereinafter referred to as "the Centre") of the One Part AND -------------- a Company incorporated under _______________________ and having its corporate / registered office at ____________________________a Company hereinafter called "the Client") (which expression should include its successors and assigns) of the Other Part;

AND WHEREAS the Centre is a member of ________________ Society, having its registered address at____________ and hereinafter referred to as the "said Society" and is in possession, use and occupation of the premises _________________, hereinafter referred to as the "said Premises".

AND WHEREAS the Centre is carrying on the business of providing office services in the name and style of ------------------- at the said premises --------------------------------- and for that purpose has made arrangements to render office facilities and services to persons who require such facilities for their business temporarily and on contract;

AND WHEREAS the client is carrying on the business of ______________ and is desirous of availing certain office facilities to enable it to more conveniently carry on it's said business.

AND WHEREAS the Client has requested the Centre to grant to the Client such facilities;

AND WHEREAS Centre has agreed to grant the same on the terms and conditions mutually agreed upon;

AND WHEREAS the parties hereto are desirous of recording the said terms and conditions.

NOW THIS AGREEMENT WITNESSETH AS UNDER:

1.     The Centre hereby agrees to grant to the Client certain office facilities in the said premises as set out herein to more conveniently carry on its said business in the name and style of ------------------------ and as incidental to such office services the Centre has permitted the Client to use until otherwise decided, a portion of the said premises and also to make available other ancillary office facilities, amenities, conveniences and services therein.

2.     The Centre has agreed to render the following services to the Client:

                              i.   to occupy and use a portion of the Business Centre at the said premises for itself, its bonafide employees and visitors, for the purpose of carrying on the client's said business

                             ii.    to use furniture, fixtures and fittings provided in the said Centre.

                            iii.   to avail of a peon's facility as may be reasonably required to attend to the needs of the Client,

                            iv.  to avail the use of three telephone connections (two local and one with ISD facilities) in the Centre

                             v.    to avail the use of air-conditioner in the Centre.

                            vi.    Any further facilities which Centre at its discretion considers it necessary to provide to the Client.

                           vii.   It is hereby expressly agreed and declared that save as otherwise herein expressly provided, the office services to be provided under this agreement, the Centre may at it's sole discretion permit it's other clients to avail of or share in common any of the said office services hereby agreed to be provided.

3.     The Client further agrees and undertakes:

a.     to take all reasonable and good care of the said Centre and furniture, fixtures and fittings therein as per separate list prepared and signed by the Centre and the Client) therein and not to cause any damage thereto or to any part thereof. To keep and maintain the fixtures and fittings in good order and condition, reasonable wear and tear or an act of God or for the reasons beyond the Control of the Client being excepted. In the event of any damage thereto or destruction thereof, save for reasons excepted as aforesaid,the Client shall at its own cost and expense immediately repair and/or replace the same or at the option of the Centre, the client pay the cost of such repair or replacement that may be carried out by the Centre.

b.    to bring into the said Centre only office records and documents etc. but in any event no hazardous and inflammable items or things shall be brought into the office by the Client.

c. to use the said Centre only for commercial purpose as an office and in a lawful manner and in any event not to make any illegal use of the same and not to cause any disturbance, nuisance or annoyance to others in the said Centre.

d. In the event of the Client making use of the aforesaid facilities for any purpose other than confide commercial office purposes and the same resulting in any civil or criminal action, the Client shall keep Centre fully indemnified of and from and against all arise there from.

e. not to allow or permit any outsiders to use the premises or any part thereof.

f. to remove all their articles, belongings and things lying in the said Centre on expiry of the term of the arrangement or in the event of prior termination, upon the date of termination.

g. to observe and perform all the rules, regulations and bye-laws of the said Society wherein the center is situate, the client having made himself aware of all such rules, regulations and bye-laws and shall indemnify and keep indemnified the Centre against any loss or damage incurred by the Client for non-performance by the Client as aforesaid.

h.Not to do or suffer to be done anything in or around the said premises which is or is likely to cause prejudice to the rights and entitlements of the Centre as the member of the Society.

i. Not to make any structural or other alterations, modifications or additions in the said premises, except with the prior written consent of the Centre which shall not be unreasonably withheld.

j. Not to alter or change the original colour on the outer or inner wall of the said premises, except with the written consent of the Centre.

4.The Centre agrees to:

a.  keep the said Centre clean and tidy and provide electricity.

b. Provide a common peon facility entirely at its own discretion as may reasonably be required to attend to the needs of the Client.

c. Provide access to the NOC of the Centre's three telephone connections of which one shall have STD facility.

5. It is mutually agreed between the parties hereto as follows:

a.The term of this arrangement shall be for three months, commencing from the date of this agreement and the same shall be renewable for a further like terms, for a total period of....... commencing from the..... day of ......... and ending on ........... Provided, however that the Centre may at it's absolute discretion and without assigning any reason in that behalf refuse to grant any removal.

b.In consideration for the services to be rendered the Centre shall from time to time submit their Bill for quarterly Standard Services charges at the rate of Rs. _______/- (Rupees ________________ only) for the first four quarters, Rs.___________ (Rupees _______________ only) for the next four quarters and Rs._____________ (Rupees______________ only) for the last four quarters. The Client shall also be liable to pay for the telephone rentals and the telephone calls made by the Client, electricity consumed by the Client and also other services specifically utilised by the Client on actual. These bills shall be paid by the Client within a week and in any event before demanding refund of the security deposit amount deposited by the Client with the Centre.

c. The arrangement herein is purely temporary and personal and not transferable under any circumstances and the Client shall not be entitled to assign or transfer the benefit of this arrangement to any other person/persons on any basis whatsoever.

d.  No tenancy, leave and license or any other protected rights whatsoever permitting the Client or its employees to come upon and use the said premises or any part thereof is created or intended or sought to be created by these presents and the parties hereto shall not plead any oral variation to the provisions thereof. The variation if any hereto shall not be valid, binding upon or enforceable against the parties hereto unless the same are duly recorded in writing in the form of supplemental agreement signed by both the parties hereto.

e. The Client shall be allowed to display its name board outside the premises at the place allotted by the Centre.

f.  If the services charges/bills payable by the Client have been outstanding for ......... from the date of receipt of the bill, the arrangement herein shall not be extended and thereupon on expiry of the two weeks, the Centre shall be entitled to prevent access to the Client and its employees in to the said premises and every part thereof and allow the Client one day's time to remove its belongings. In the event of the Client refusing or neglecting to remove its belonging from the said premises, the Centre shall be entitled to open the premises or any part thereof allotted to the said Client using the original key in their possession and in the presence of witness remove the articles and things therein after making a list thereof. It is expressly agreed that the Centre shall not render itself liable for any civil or criminal action by so doing. This authority retained by the Centre and expressly agreed to by the Client is irrevocable and constitutes the basis for this agreement and the Client shall not be entitled to dispute, challenge or call into question the validity or reasonableness of this provision.

g. Any delay or indulgence by the Centre in enforcing the terms and conditions of this Agreement or any forbearance or giving of time to the Client shall not be construed as a waiver on the part of the Centre of any breach or non-observation and or non- compliance of any of the terms and conditions of this Agreement by the Client nor shall it in any manner prejudice the rights of the Centre against the Client.

h. All letters, receipts, notices or communications issued by the Centre or the Client and dispatched by Registered Post with Acknowledgement due or delivered by Hand Delivery to the address on the record of the other will be sufficient proof of receipt thereof by the other and shall be an effectual discharge on the part of the party forwarding the same and the same shall be deemed to have been received by the other party on the normal expiry period under post.

i. The Centre shall not be responsible or liable for any:

1. Theft, loss, damage or destruction of any property of the Client or any person living in or visiting the said premises or in the said building from any cause whatsoever.

2. For any personal or other injury caused to the person for the time being in the said premises on any account.

j.In the event of the Client committing any breach of the terms and conditions herein contained and failing within....... days of the receipt of a notice in writing in that behalf given by the Centre to remedy or make good such breach the Centre shall be entitled to forthwith revoke and or terminate the arrangement and/or the permission granted and in such an event the provisions of clause 5(g) of this Agreement shall apply mutatis mutandis.

k. Each party shall bear and pay the fees of their respective legal representatives.

6. As security for the due performance of the provisions hereof the Client shall deposit with Centre an interest free security deposit of a sum of Rs.-----/- (Rupees --- ). The said interest free security deposit, after deducting there from the amount of arrear or other dues if any from the Client shall be refunded by Centre to the Client without interest on the arrangement herein coming to an end, howsoever and when so ever, and upon the Client removing itself and all its belongings and things from the said premises.

7.The Centre shall be at liberty to terminate this Agreement or any renewal thereof by giving the Client three months notice in writing stating therein its desire to do so and on the expiry of such notice, and on the client removing itself, it's employees and belongings from the said premises and otherwise performing it's obligation under this agreement the Centre shall refund to the Client the interest free security deposit amount as contained in clause 6.

8. Upon the termination of this Agreement or sooner determination and upon the failure of the Client to remove itself, its employees and its belongings from the said premises. The Client shall be liable and hereby agrees to pay to the Centre liquidated damages of Rs._____________ (Rupees __________only) and compensation and/or manse profits of Rs.__________ (Rupees____________) per day for the wrongful and unauthorised use of the said premises and the facilities provided therein. The Centre shall be entitled without prejudice to its other rights to forfeit the security deposit in the event of any breach on the part of the client.

9.It is further agreed and declared between the parties hereto that the permission hereby granted by the Centre to the Client to use a portion of the said premises is incidental to the availing of office facilities, amenities and services provided by the Business Centre to the Client and the Client shall not be entitled to avail other facilities separately as the arrangement is composite, impartibly and indivisible.

10. Any dispute between the parties hereto shall be referred to the sole arbitration of Mr________________. Having his / its office at ______________and shall be subject to the provisions of the Arbitration and Conciliation Act, 1996.



IN WITNESS WHEREOF the parties hereto have hereunto set and subscribed their respective hands, the day and year first hereinabove written.

SIGNED AND DELIVERED by

_______________________ )

as partner / proprietor of the Centre.)

in the presence of _____________ )

SIGNED AND DELIVERED by the )

With in named ______________ )

in the presence of____________ )""",
"Format for Confidential Information and Non-Disclosure Agreement NDA":"""DRAFT OF CONFIDENTIAL AGREEMENT AND NON-DISCLOSURE AGREEMENT



This Agreement is made and entered into by and between _________________ ABC (hereinafter referred to as ABC) having offices at ___________ and DEF (hereinafter referred to as DEF) having offices at __________________

Subject of ABC Information: Business and technical information including but not limited to its ideas, products, proposed products, processes, services, capabilities, and materials, or any information which quantifies, classifies, or identifies any ideas, products, proposed products, processes, services, capabilities and materials to be employed including _________________________________________

Subject of DEF Information: Business and technical information including but not limited to its ideas, products, proposed products, processes, services, capabilities, and materials, or any information which quantifies, classifies, or identifies any ideas, products, proposed products, processes, services, capabilities and materials to be employed including ________________________________________

Purpose(s) of Disclosures: To exchange confidential information to enable the parties to discuss possible future business collaborations relating to the aforementioned business and technology.

The parties anticipate that technical and business information, and/or media samples, prototype parts or other tangible embodiments of information, may be disclosed or delivered between the parties, for the above stated Purpose(s), such information and tangible embodiments constituting confidential information, being considered by ABC and DEF to be proprietary (and being referred to hereinafter, collectively, as "Proprietary Material"). Any party furnishing Proprietary Material will be referred to as a "disclosing party" and a party receiving Proprietary Material will be referred to as a "receiving party." In order to provide for the protection of such Proprietary Material from unauthorized use and disclosure, the parties hereby agree that the disclosure of such Proprietary Material between them shall be subject to the following terms and conditions:

1.  Both parties agree that all Proprietary Material which relates to the above-stated Subject(s) and Purpose(s) and which is disclosed to the receiving party by the disclosing party, whether orally, or in written or other tangible form, will be maintained by the receiving party in confidence, provided, that: (a) disclosures in writing are expressly marked with a confidential or proprietary legend; (b) oral disclosures and tangible embodiments in a form other than written are identified as confidential or proprietary at the time of disclosure or delivery; and (c) oral disclosures are thereafter reduced to writing and marked with a confidential or proprietary legend, which writing is thereafter furnished to the receiving party within ...... days after the oral disclosure. The receiving party may, however, in furtherance of the aforesaid Purpose(s), disclose such Proprietary Material to its professional advisors, investment committee participants, and those of its employees and others under its control, all of whom will be advised of this Agreement and agree to accept the obligations there under. The receiving party further agrees not to reverse engineer any tangible embodiments of Proprietary Material furnished by the disclosing party, not to disclose any Proprietary Material to third parties and limit circulation of the Proprietary Material to such employees and others under its control having a direct "need to know" in connection with the above mentioned Purpose.

2. The receiving party additionally agrees to take reasonable care to safeguard the confidential nature of the foregoing Proprietary Material, and such reasonable care shall not be less than the degree of care used to prevent disclosure of its own proprietary material. However, the receiving party will not be liable for disclosure and use of such Proprietary Material: if the Proprietary Material is in, or becomes part of, the public domain other than through a breach of this Agreement by the receiving party; if the Proprietary Material is disclosed to the receiving party by a third party who is not known by the receiving party to be subject to any confidentiality obligation; if the Proprietary Material is disclosed by the receiving party with the disclosing party's prior written approval; or if disclosure of the Proprietary Material is required by any judicial order or decree or by any governmental law or regulation. Further, with respect to such Proprietary Material provided to the receiving party by the disclosing party, or rule of any stock exchange the receiving party shall not be liable for disclosure and use thereof if such Proprietary Material was of record in the files of the receiving party at the time of its disclosure to the receiving party by the disclosing party or if such Proprietary Material is developed by the receiving party completely independently of the disclosing party's Proprietary Material. Prior to disclosure to any third party of any Proprietary Material to which the receiving party determines the obligations of confidentiality, non-use and non-disclosure do not apply pursuant to this Agreement, the receiving party shall provide within....... days' prior written notice to disclosing party of the intent to disclose such Proprietary Material, stating the grounds upon which the exception is claimed and providing documentation in support thereof. The receiving party shall limit the scope of disclosure to only the portion of the Proprietary Material not protected.

3.  Proprietary Material identified and disclosed as provided in this Agreement shall be held in confidence for a period of ______years from the date of disclosure. During such period, such Proprietary Material shall be used only for the Purpose(s) stated above. Neither party acquires any intellectual property rights under this Agreement, except the limited rights to carry out the Purpose(s) above stated.

4.  Each party understands that the other is developing and acquiring technology for its own products, and that existing or planned technology independently developed or acquired by that party may contain ideas and concepts similar or identical to those contained in the disclosing party's proprietary information. The disclosing party agrees that entering this Agreement shall not preclude the receiving party from developing or acquiring technology similar to the disclosing party's, without obligation to the disclosing party, provided the receiving party does not use the disclosing party's proprietary information to develop such technology.

5.  All Proprietary Material received and identified in accordance with this Agreement shall remain the property of the disclosing party and shall be returned or destroyed upon request except that the receiving party may keep one copy of such proprietary material for its legal files which shall remain subject hereto. Nothing contained herein shall be construed as a right or license, express or implied, under any patent or copyright, or application therefore, of either party by or to the other party.

6.  Each disclosing party warrants that it has the right to make disclosures under this Agreement. NO OTHER WARRANTIES ARE MADE BY EITHER PARTY. ALL PROPRIETARY MATERIAL IS PROVIDED "AS IS".

7.  The receiving party agrees that no technical data furnished to it by the disclosing party shall be exported from the ________without first complying with all requirements of the concerned rules and regulations, including the requirement for obtaining any export license, if applicable. The receiving party shall first obtain the written consent of the disclosing party prior to submitting any request for authority to export any such technical data.

8. This Agreement

a.  will be effective as of the date of the signature by the last party to execute this Agreement, and may be terminated at any time upon written notice by either party;

b.  shall automatically terminate _______years from its effective date unless terminated sooner pursuant to provision (a) above;

c. does not obligate either party to deliver a purchase order for the performance of any service or for the supply of any article whatsoever;

d. does not obligate either party to perform any service or to furnish any proposal or comments;

e.  does not obligate either party to disclose Proprietary Material to the other; and

f.  will be binding upon the parties hereto and their successors, assignees, or personal representatives as the case may be. Any termination of this agreement shall not relieve the receiving party of any obligations herein incurred prior to the date of such termination or to be performed subsequent to the date of such termination.

9. The terms and conditions herein constitute the entire agreement and understanding of the parties and shall supersede all communications, negotiations, arrangements and agreements, either oral or written, with respect to the subject matter hereof. No amendments to or modifications of this Agreement shall be effective unless reduced to writing and executed by the parties hereto. The failure of either party to enforce any term hereof shall not be deemed a waiver of any rights contained herein.

10.This Agreement shall apply to any Proprietary Material that may have been provided to either party prior to the effective date hereof.

11.No rights or obligations other than those expressed and recited herein are to be implied from this Agreement. No other existing Agreement between the parties, if any, are modified or terminated by this Agreement. No warranty or representation is made by either party hereto that any information transmitted by it hereunder is patentable or copyrightable, or that any such information involves concepts or embodiments that are free of infringement of other rights. Neither party hereto shall be obligated to prosecute any such action or bring any suit against any person not a party hereto for infringement. Neither party shall indemnify the other party hereto for any liability resulting from infringement of patent, copyright or trademark of a third party caused by the use of any Proprietary Material transferred pursuant to the Agreement. Neither party hereto confers the right to the other to use in advertising, publicity, or otherwise any trademark or trade name of the other party, nor confers any authorization to the other party to act as an agent on its behalf for any purpose.

12.  This Agreement shall be governed and interpreted in accordance with the laws of the ___________, without giving effect to its internal principles of conflict of law.

IN WITNESS WHEREOF, the parties hereto have caused this Agreement to be executed in duplicate.

ABC DEF

By:_______________________ By:_____________________

(Authorized Signature) (Authorized Signature)

Name:______________________ Name:___________________

Title:__________________ Title:___________________

Date:""",
"Format for Employee Service Agreement":"""DRAFT OF EMPLOYEE-SERVICE-AGREEMENT



THIS EMPLOYEE SERVICE AGREEMENT executed at __________ on this the _______ day of ______________

BETWEEN

_______________, a company incorporated under the Companies Act, 1956 or Companies Act, 2013,represented by it's ________________Mr./Ms. _______________, son of / wife of/ daughter of Mr. ___________ having it's registered office at ________________________________________________, hereinafter referred to as the EMPLOYER (which expression shall, unless it is repugnant to the context, mean and include it's successors-in-interests, administrators and permitted assigns);

AND

Mr. /Ms. ______________, son of / wife of/ daughter of Mr. ____________, Indian, ______________, aged about _____________years, residing at ______________________________________________, hereinafter referred to as the EMPLOYEE.

WHEREAS

The EMPLOYER is carrying on the business of ________________.

The EMPLOYER called for applications from the eligible candidates for the post _________and in response thereto an application-dated ____________ was forwarded by the EMPLOYEE to the EMPLOYER.

On processing the application and the relevant documents, the EMPLOYER found the EMPLOYEE adequately qualified for the post and offered to appoint him as __________________________ in the Company.

The EMPLOYEE has accepted the said appointment on the terms and conditions herein after set out.

NOW THEREFORE IN CONSIDERATION OF THE MUTUAL OBLIGATIONS AND UNDER TAKINGS CONTAINED HEREIN THIS AGREEMENT WITNESSETH AS FOLLOWS

NAME OF THE POST:

The said EMPLOYEE is hereby appointed as ______________.

PROBATION AND CONFIRMATION:

The EMPLOYEE shall be on probation for a period of ________. The decision of the management on the performance of the EMPLOYEE during the period of probation is final and binding on the EMPLOYEE.

DURATION OF EMPLOYMENT:

On successful completion of probation, the EMPLOYEE shall be appointed as a permanent EMPLOYEE of the EMPLOYER for a period of ____________.

PLACE OF POSTING:

The EMPLOYEE shall report to work at ___________________, on ___________________.

HOURS OF WORK:

The EMPLOYEE is required to work from ___________ to ________ during the Weekdays. The weekly holiday would be on ________.

REMUNERATION

The EMPLOYER shall pay the EMPLOYEE a stipend of Rs. __________/- during the period of probation. On successful completion of probation the EMPLOYER shall pay the EMPLOYEE a basic salary of Rs. __________.

The EMPLOYER shall increase the basic salary of the EMPLOYEE as per the policy of the EMPLOYER.

PERQUISITIES & HOLIDAYS:

On confirmation, the EMPLOYEE shall be entitled to other benefits, monetary/leave, as is prevalent in the Company, from time to time, as per the ________________________.

ARBITRATION:

Any dispute arising under this Agreement or any matter incidental thereto, shall be submitted for arbitration as per the provisions of Arbitration and Conciliation Act, 1996.

IN WITNESS WHEREOF the parties hereto affixed their signatures on the day, month and year mentioned herein above.



SIGNATURE OF EMPLOYER



SIGNATURE OF THE EMPLOYEE



WITNESSES:

1.

2.""",
"Format for Franchise Agreement":"""DRAFT OF FRANCHISE AGREEMENT



This AGREEMENT entered into on the...............................day of......................., 20..............

BETWEEN:

....................................................Limited a Company incorporate under the Companies Act, 1956 or Companies Act, 2013, having its Registered Office at..........................., represented herein by its................................. Shri................................................. (hereinafter referred to as the ''XYZ Limited '', which expression shall, whenever the context so requires or admits mean and include its successors and assigns) of the ONE PART;

AND

M/s.................................................. a Partnership Firm, having its place of Business at.............................. represented herein by its Partner Shri............................. (hereinafter referred to as the ''AGENT'', which expression shall, unless the context so requires or admits mean and include its Partners for the time being, their heirs, legal representatives, executors and permitted assigns) of the OTHER PART;

WHEREAS XYZ Limited is engaged interalia in the business of marketing......products and are the owners of the trade name and trade mark ''XYZ'';

WHEREAS XYZ Limited is desirous of promoting........products under its trade name and trade mark by setting up chain or retail outlets all over the country on its own a also by appointing stockiest, retailers and franchises for the purpose of setting up of retail outlets;

WHEREAS the Agent has offered to set up one such Retail Outlet in the City of..... and has represented to XYZ Limited that it is in a position of invest necessary capital and is also possessed of a suitable premises to set up and carry on the Retail Outlet and XYZ Limited has accepted the said offer;

NOW THIS AGREEMENT WITNESSETH AS FOLLOWS

That in consideration of the foregoing, the Company hereby appoint M/s......... as its Agent in the City of......... upon the following terms and conditions:

1.     The retail outlet for marketing....... products under the name and style of ''XYZ'' shall be set up and run in the Premises made available by the Agent, which premises is more fully described in the Schedule Premises''. The premises will be made available free of cost or charges to XYZ Limited by the Agent during the subsistence of this Agreement.

2.     The Agent will meet and bear the entire cost of furnishing and decorating the interior and exterior of the Schedule-Premises in accordance with the specifications and requirements of XYZ Limited, particularly touching upon the following aspects -- elevation, décor and interior design, selection of furniture, fitting, counters and stands, lighting system, illumination, mannequins, window display, air conditioning, fire fighting equipment, furnishings, flooring, etc. the cost of which is estimated to be of the order of Rs.......................... (Rupees.........................................) He shall also provide necessary warehousing facilities and office space for the Company's' representations.

3.     The name of the Shop shall be promptly and clearly displayed as..........................;

4.     XYZ Limited will make available from time to time to the Agent ....... products and  shall be manufactured, sold or dealt in by XYZ Limited (hereinafter collectively referred to as ''Stockiest'') and the Agent will take the Stocks on consignment and sell the same in retail at prices fixed from time to time by the XYZ Limited. The stocks shall at all times be the property of the XYZ Limited and the Agent shall only be entrusted the Stocks for the purpose of enabling their retails sale.

5.     The Agent at his cost will employ necessary personnel to man and manage the Retail Outlet to the entire satisfaction of XYZ Limited.

THE AGENT COVENANTS WITH THE COMPANY AS FOLLOWS:

1.     It shall duly and promptly pay the owner of the Schedule Premises rents and other charges and keep the lease subsisting and valid and ensure that the Schedule Premises is always available for running of the Retail Outlet.

2.     That it shall not directly or indirectly or in Partnership or Association, with friends or relatives, or Companies engaged itself in business, which is same or similar to the one being, carried on by XYZ Limited.

3.     That it shall not sell, display or otherwise deal in any goods which are in any way similar to the goods sold or dealt in by XYZ Limited.

4.     That it shall not use the Company''s trade name and/or trademark in any manner other than that which is permitted by XYZ Limited.

5.     That all sales effected by the Agent shall be strictly for cash only.

6.     That it shall furnish to XYZ Limited at such intervals as they may required certified stocks statement of the stock of all goods held by the Agent giving full and correct particulars thereof.

7.     That it shall remit each day the entire sale proceeds of the preceding day to the credit of the designated account of XYZ Limited, which may be indicated from time to time and shall forthwith sent intimation of such remittances to XYZ Limited.

8.     That it shall not draw, accept or endorse any Bill on behalf of the XYZ Limited or in any way pledge the credit of XYZ Limited except with the previous written authorization of XYZ Limited.

9.     That it shall be at all times responsible to XYZ Limited for any damage occasioned to the Stock either on account of the improper or negligent conduct on the part of the Agent, its servants or agents or for any reason whatsoever and shall make goods such loss to the XYZ Limited as and when demanded without demur.

10.  That it shall furnish an irrevocable Bank Guarantee for a sum of Rs.................. (Rupees.......................................) in favour of XYZ Limited covering the value of the Stocks held by it on consignment and that the said Bank Guarantee shall be enhanced from time to time as may be required by XYZ Limited to bring it in conformity with the value of the Stocks held by the Agent.

11.  That it shall keep proper accounts of all Stocks received, sold, damaged and furnish to XYZ Limited each week full particulars of the Stocks and shall permit XYZ Limited, its agents and servants to inspect all Books of Account, Records and vouchers maintained in the Retail Outlet by it all reasonable times.

12.  That it shall be responsible for any loss or damage sustained to the Stock while in the custody of the Agent.

DURATION: The duration of this Agreement shall be for a period of.............. years commencing from..........On the expiry of this period of earlier, the Agreement may be extended for such further period and on such terms as the parties may be mutually agreed in writing.

This Agreement is however terminable as follows:

a.     by either party giving the other................. days notice in writing;

b.    by XYZ Limited unilaterally without assigning any reasons

                      i.        if the agent is found guilty of misconduct, or

                     ii.        commits a breach of any of the provisions of the Agreement, or

                    iii.        is dissolved, or

                    iv.        any suit or other proceedings are instituted for its dissolution or winding up, or

                     v.        commits any act of bankruptcy,

                    vi.        suffers any execution or distress.

CONSIDERATION: In consideration of the foregoing, the Agent shall be entitled to a commission at the rate of......% of the net sale price realized by it in the Retail Outlet by sale of the Stocks. The expression net sale price shall mean the selling price of the Stocks excluding Sales Tax, local taxes and other levies imposed upon the sale or purchase of the Stocks and/or on the total turnover, packing and forwarding charges and gift wrapping charges.

The commission shall be payable by XYZ Limited on or before the.......... Day of the succeeding month for which it is due upon receipt of the monthly statement of sales and realization of the sale proceeds.

ASSIGNMENT: This Agreement or the benefit there from shall not be assignable or transferable by the Agent in favour of anyone without prior written consent of the company.

SECURITY DEPOSIT: In order to ensure XYZ Limited the due performance of its obligations under this Agreement, the Agent has this day deposited a sum of Rs................. (Rupees.....................................) by Pay Order bearing No..........dated.......... drawn on............. Bank............... Branch,......................, in favour of XYZ Limited as Security Deposit. The said amount will be refundable upon the termination of this Agreement, free of interest, in the event of there being no outstanding claim against the Agent by XYZ Limited. XYZ Limited will however be entitled to appropriate and adjust and amounts which may be due to it from the Agent from out of the Security Deposit.

JURISDICTION: This Agreement is executed at.................City and it is hereby agreed that Court situated in............ city alone will have exclusive jurisdiction over any matter arising under this Agreement to the execution of Courts situated in any part of the country.

SCHEDULE

Premises bearing No...................................... situated at............................................................................ admeasuring and bounded as follows:

MEASUREMENTS

East to West:

North to South:

BOUNDARIES

ON THE EAST

WEST

NORTH

SOUTH

:

:

:

:

: By

: By

: By

: By

IN WITNESS WHEREOF the parties above named have executed these presents in the presence of the Witnesses attesting hereunder on the dates and place mentioned herein below:

Place:

Dated:

For XYZ Limited,

WITNESSES

1. ()

2. ()

Agent""",
"Format for Memorandum of Understanding MOU":"""DRAFT OF MEMORANDUM OF UNDERSTANDING



ABC and XYZ.

Re: ____________________________ Pvt. Ltd.

THIS MEMORANDUM OF UNDERSTANDING made on this ____________day of _____________between ABC having his office at__________________, India hereinafter referred to as "ABC" (which expression and the expression "ABC Group" shall unless it be repugnant to the context or meaning thereof mean and include himself and the present other shareholders of __________________Pvt. Ltd. and their respective heirs, executors, administrators and assigns) of the One Part and MR. XYZ having his office at_____________________. (Hereinafter referred to as "XYZ" which expression and the expression "XYZ Group" shall unless it be repugnant to the context or meaning thereof be deemed to mean and include himself and his nominees to the extent specified herein and their respective heirs, executors, administrators and assigns) of the SECOND PART;

WHEREAS, ABC is one of the founding shareholders and is Chairman and Director of a company incorporated in India known as ______________ Pvt. Ltd. hereinafter referred to as "the Company" which is in the process of setting up an internet portal, relating to ___________________, known as "__________________";

AND WHEREAS, ABC and certain other persons have advanced sums of money to the Company in respect of which shares have been/are to be issued to them and this group is for the sake of brevity referred to as the "XYZ Group";

AND WHEREAS, XYZ has agreed that he and his nominees (for the sake of brevity referred to as the "ABC Group") will invest an amount of Rs.__________________ /- (Rupees _______________Only) to acquire ____ of the Capital of the Company on certain terms and conditions and equity shares of the Company will be issued to the members of XYZ Group accordingly;

AND WHEREAS, the parties hereto are desirous of recording the terms and conditions of their agreement in writing

NOW THIS MEMORANDUM OF UNDERSTANDING WITNESSETH AS UNDER:-

1.     ABC Group has caused to be incorporated a Company known as ________ Pvt. Ltd. hereinafter referred to as "the Company" and has, since several months been working on establishing an internet portal relating to___________________.

2.     The paid up capital of the Company shall be Rs._________________ /- (Rupees________only) comprising __________(____________) equity shares of Rs._____ /- (Rupees_________) each.

3.     It has been agreed that XYZ group shall hold ....... of the paid-up capital of the Company and that XYZ Group shall hold........ of the paid-up capital of the Company.

4.     It is further agreed that......... shall be allotted by ABC Group as and by way of stock options at their discretion to employees, associates, content writers and Technology partners and other supporters on such terms as decided by the Group. It has however been agreed that...... out of this ........ shall be allotted to Mr. XYZ and........ to Mr. PQR leaving thereby........ to be allotted by ABC Group as described above.

5.     XYZ has agreed that for the.........to be allotted to the XYZ Group, the XYZ Group shall pay to the Company a total amount of Rs. __________________/- (Rupees _________________Only) to comprise share capital and premium of the total amount of Rs.__________/- (Rupees ______________Only) an amount of approximately Rs._________/- (Rupees _____________Only) being the equivalent of U.S. $ ____________/- has already been received by the Company by way of Foreign Inward Remittance received from XYZ. These amounts already received have been treated by the Company as advances against share capital and premium. The balance amount of Rs____________/- (Rupees ______________ Lakh Only) approximately is to be paid in the following manner.

a.     Rs.__________ /- (Rs______________ Only) by (date)

b.    Rs.__________ /- (Rupees ___________Only) by --/--/---

c.     Rs. __________/- (Rupees_________ __Only) by --/--/---.

d.    Rs. _________/- (Rupees ___________Only) by --/--/---

e.     Rs. _________/- (Rupees ___________Only) by --/--/---

f.     Rs. _________/- (Rupees ___________ Only) by --/--/---

g.    The balance to make up Rs_____________/- (Rupees ______ only) by (date)

6.     It has been mutually agreed that the Company shall not further dilute its equity or avail of finance from any other person nor shall it agree to allot any shares to any other person without the consent of XYZ. It has been further agreed that ABC Group shall not sell all or any of the shares allotted to them without the consent of XYZ Group until such time as there is an IPO or a second round of financing by mutual agreement. In the event of a second round of financing becoming necessary, it shall be done by mutual Agreement between the parties hereto and it is expected that an Initial Public Offering (IPO) will also be made and that shares will be issued to the public. The parties have agreed that for any future rounds of financing as mutually decided there will be a proportionate dilution of shares.

7.     XYZ shall have the right to be a Director of the Company and ABC shall cause XYZ to be appointed to the Board of Directors whenever XYZ desires.

8.     ABC shall cause this Memorandum of Understanding to be taken on the records of the Company and the Company will also agree to abide by all the terms and conditions hereof.

9.     The parties hereto record that this Memorandum of Understanding reflects the broad terms of their Agreement and they agree to execute and sign a detailed Shareholders Agreement and such further Agreements in writing as may be required from time to time to give effect to the development promotion and financing of the portal in the best possible way.

IN WITNESS WHEREOF the parties hereto have hereunto set and subscribed their respective hands the day and year first hereinabove written.

SIGNED AND DELIVERED by the Withinnamed

MR. ABC

In the presence of __________________

SIGNED AND DELIVERED by the Withinnamed

MR. XYZ

In the presence of________________________""",
"Format for Articles of Association for Public Companies":"""DRAFT MODEL ARTICLES OF ASSOCIATION FOR PUBLIC COMPANIES



PART 1: DEFINITIONS AND INTERPRETATION

1.       Defined terms

1.     The special meanings given to certain words and phrases in the articles are set out in the index of defined terms.

2.     Where a word or phrase is defined in the index of defined terms, other grammatical forms of that word or phrase used in the articles shall have a meaning which corresponds to that definition.

PART 2: DIRECTORS

DIRECTORS’ POWERS AND RESPONSIBILITIES

2.       Directors’ general authority

Subject to the Companies Acts and the articles, the directors:

a.       shall manage the company’s business; and

b.       may exercise all the powers of the company for any purpose connected with the company’s business.

3.       Members’ reserve power

1.     The members may, by special resolution, order the directors to act, or refrain from acting, in a particular way

2.     No such special resolution shall invalidate anything which the directors have already done.

DELEGATION OF DIRECTORS’ POWERS AND RESPONSIBILITIES

4.     Directors may delegate

1.     Subject to the articles, the directors may delegate any of their powers and responsibilities:

a.     to such persons;

b.    by such means;

c.     to such an extent;

d.    in relation to such matters or territories; and

e.     on such conditions or subject to such restrictions, as they think fit.

2.     Unless the directors specify otherwise, any such delegation authorises further delegation of the directors’ powers and responsibilities by any person to whom they are delegated, whether expressly or by virtue of this paragraph.

3.     The directors must not delegate to any person who is not a director any decision connected with:

a.     how the directors (or a committee of directors) take decisions;

b.    a director’s appointment or the termination of a director’s appointment; or

c.     the payment or declaration of a dividend.

4.     The directors may at any time withdraw or revoke any delegation in whole or part, or alter its terms.

5.     Committees of directors

1.     If the directors:

a.     delegate powers or responsibilities to two or more persons, at least one of whom is a director; and

b.    indicate that they should act together in respect of those powers or responsibilities, those persons are a “committee” for the purposes of the articles.

2.     The provisions of the articles about how the directors take decisions shall apply, as far as possible, to the taking of decisions by committees, but the directors may make rules of procedure which are binding on a committee.

DECISION-MAKING BY DIRECTORS

6.     Directors to take decisions collectively

1.     This article applies to any matter in respect of which the directors have not delegated their powers and responsibilities to a single director.

2.     Subject to the articles, the directors must not act in relation to any such matter unless they have taken a decision about it:

a.     at a directors’ meeting, or

b.    in the form of a directors’ written resolution, in accordance with the articles.

7.     Calling directors’ meetings

1.     Any director may call a directors’ meeting.

2.     The company secretary shall call a directors’ meeting if a director so requests.

3.     A meeting is not called unless reasonable notice of it has been given, indicating its proposed date, time, place and subject matter.

4.     Notice must be given to all the directors, except those:

a.     to whom it is not possible to give reasonable notice; or

b.    who waive their entitlement to notice, prospectively or retrospectively.

5.     Notice of a directors’ meeting need not be given in writing.

6.     The reasonableness of any notice period shall be determined by reference to:

a.     The urgency and importance of the meeting’s subject matter; and

b.    Individual directors’ ability to receive notice of or participate in the meeting.

8.     Participation in directors’ meetings

1.     Subject to the articles, directors participate in a directors’ meeting, or part of a director’s meeting, when:

a.     the meeting has been called and takes place in accordance with the articles;

b.    they are engaged, together, exclusively in the business of the meeting, or of that part of the meeting;

c.     no other directors are engaged on that business separately from them; and

d.    they can each communicate to the others any information or opinions they have on any particular item of that business.

2.     In determining whether directors are participating in a directors’ meeting, it is irrelevant where any director is or how they communicate with each other.

9.     Quorum for directors’ meetings

1.     At a directors’ meeting, unless a quorum is participating, no proposal shall be voted on, except a proposal to call another meeting.

2.     The quorum for directors’ meetings may be fixed from time to time by:

a.     a decision of the directors, or

b.    an ordinary resolution, but it shall never be less than two, and unless otherwise fixed it shall be two.

3.     Subject to the articles, a director who is interested in an actual or proposed transaction or arrangement with the company shall not be counted as participating in any directors’ meeting, or part of a directors’ meeting, relating to that transaction or arrangement.

4.     A person who is an alternate director but not a director shall be counted as participating for the purposes of determining whether a quorum is participating, but only if that person’s appoint tor is not participating. No alternate shall be counted as more than one director for such purposes.

10.  Total number of directors less than quorum

If the total number of directors for the time being is less than the quorum for directors’ meetings, then:

a.     all the directors, or

b.    as many of them as are not incapable of doing so by reason of illness or accident, may agree in writing either to appoint sufficient new directors to make up a quorum or to call a general meeting of the company to vote on a resolution that will appoint further directors or alter the quorum.

11.  Chairing of directors’ meetings

1.     The directors shall appoint a director to chair their meetings.

2.     The person so appointed for the time being shall be known as the chairman.

3.     The directors may terminate the chairman’s appointment at any time.

4.     If the chairman is not participating in a meeting within ten minutes of the time at which it is to start, the participating directors shall appoint one of themselves to chair it.

12.  Voting at directors’ meetings: general rules

1.     A decision is taken at a directors’ meeting when a majority of the participating directors vote in favour of a proposal.

2.     Subject to the articles:

a.     each director participating in such a decision shall have one vote; but

b.    if a director has an interest in an actual or proposed transaction or arrangement with the company, that director and that director’s alternate may not vote on any proposal relating to it.

13.  Chairman’s casting vote at directors’ meetings

If the numbers of votes for and against a proposal are equal, the chairman or other director chairing the meeting shall have a casting vote.

14.  Alternates voting at directors’ meetings

Directors who are also alternate directors each have an additional vote on behalf of each of their appointers when their appointers are:

a.     not participating, and

b.    would have been entitled to vote if they were participating.

15.  Conflict of interests: relaxation of restrictions

1.     In any of the circumstances specified for the purposes of this article, a director who is interested in an actual or proposed transaction or arrangement with the company:

a.     shall be counted as participating in a decision at a directors’ meeting, or part of a directors’ meeting, relating to it; and

b.    is entitled to vote on a proposal relating to it.

2.     The circumstances specified for the purposes of this article are when:

3.     the company by ordinary resolution disapplies the provision of the articles which would otherwise prevent a director from being counted as participating in, or voting at, a directors’ meeting;

4.     the director’s interest cannot reasonably be regarded as likely to give rise to a conflict of interest; or

5.     the director’s conflict of interest arises from a permitted cause.

3.     For the purposes of this article, the following are permitted causes:

a.     a guarantee given, or to be given, by or to a director in respect of an obligation incurred by or on behalf of the company or any of its subsidiaries;

b.    subscription, or an agreement to subscribe, for shares or other securities of the company or its subsidiaries, or to underwrite, sub-underwrite, or guarantee subscription for any such shares or securities; and

c.     a contract about benefits for employees and directors or former employees and directors of the company or its subsidiaries generally which does not provide special benefits for directors or former directors.

16.  Directors’ discretion to make further rules

1.     Subject to the articles, the directors may make any rule which they think fit about how they take decisions.

2.     The directors must ensure that any such rule is communicated to all persons who are directors while it remains in force.

17.  Directors’ written resolutions

1.     A directors’ written resolution is adopted when all the directors (or their alternates) sign a document setting out a decision.

2.     A directors’ written resolution is also adopted when:

a.     fewer than all of the directors sign a document setting out a decision;

b.    it is impracticable to have the document signed by those who have not signed it; and

c.     the document records the names of the directors who have not signed it and the reasons why they have not signed it.

3.     The practicability of a director signing such a document shall be determined by reference to:

a.     the urgency and importance of the decision to which it relates; and

b.    the director’s ability to receive and sign the document and send it to the company by the time when it is necessary or expedient for the directors to take that decision.

4.     References to a document in this article include copies of that document.

5.     The directors are responsible for ensuring that the company keeps a written record of all directors’ written resolutions for at least ten years from the date of their adoption.

APPOINTMENT OF DIRECTORS

18.    Minimum and maximum number of directors

Subject to the Companies Acts, the company may by ordinary resolution decide that it is to have:

a.     not more than, or

b.    not less than,

a specified number of directors.

19.  Methods of appointing directors

Any person who is willing to act as a director, and is permitted by law to do so, may be appointed to be a director:

a.     by ordinary resolution; or

b.    by a decision of the directors. 

20.  Appointments by directors to be confirmed by members

1.     Directors appointed by a decision of the directors must be confirmed in office by an ordinary resolution at the next annual general meeting following their appointment by the directors.

2.     Subject to the articles, the appointment of directors whose appointment is not so confirmed terminates at the end of that annual general meeting.

21.  Retirement of directors by rotation

1.     At the first annual general meeting all the directors shall retire from office.

2.     At every subsequent annual general meeting half of the directors (rounded up to the nearest whole number if there is an odd number of directors) shall retire from office and offer themselves for reappointment by the members.

3.     The directors to retire by rotation shall be those who have been longest in office since their last appointment or reappointment by a general meeting, but as between persons who were last appointed or reappointed on the same day those to retire shall be decided by lot.

4.     For the purposes of calculating which directors are required to retire by rotation, the following shall be disregarded:

a.     any directors whose appointment is required to be confirmed because they were appointed by the directors; and

b.    any directors who wish to retire and not be re-elected. 

22.  Appointment of directors at general meetings

1.     A person is only eligible to be appointed a director by a general meeting if that person:

a.     is a director retiring by rotation at that meeting under the articles; or

b.    has been nominated for appointment as a director at that meeting by the directors or by a member qualified to vote at that meeting.

2.     Members wishing to nominate a person for appointment as a director must do so by giving notice in writing to the company not less than.... or more than ...... days before the date of the meeting.

3.     The company must notify all those who are entitled to receive notice of the meeting of who is eligible to be appointed a director at any general meeting not less than seven or more than ..... days before the date of that meeting.

4.     Nominations or notices about the proposed appointment of a person as a director at a general meeting need not contain that person’s address, but must otherwise include the same information as an entry in the register of directors in respect of that person would contain if that person were appointed a director.

5.     Nominations of a person for appointment as a director at a general meeting must include a statement signed by the person nominated indicating that person’s willingness to be appointed a director.

6.     If, at the end of a general meeting, the company would otherwise have fewer than two directors, or such higher minimum number of directors as has been fixed in accordance with the articles, the persons who were directors at the start of the meeting shall be deemed to have been reappointed as directors, but they shall only act for the purposes of:

a.     calling general meetings; and

b.    performing such duties as are essential to maintain the company as a going concern.

23.  Termination of director’s appointment

1.     A person ceases to be a director as soon as:

a.     that person ceases to be a director by virtue of any provision of the Companies Acts, or is prohibited by law from being a director;

b.    that person becomes subject to a receiving order or compounds with that person’s creditors generally;

c.     in the opinion of all the other directors, mental disorder makes that person incapable of discharging the duties of a director;

d.    that person fails, without the directors’ permission, to participate in directors’ meetings for more than three months, and is not prevented from doing so by illness, accident, or some other cause which the directors consider sufficient;

e.     a notification to the company that that person is resigning or retiring from office as director takes effect in accordance with its terms (but if a contract with the company specifies a longer notice period, that person’s appointment shall not terminate until expiry of the contractual notice period);

f.     the directors decide to accept that person’s offer to resign from the office of director;

g.    an ordinary resolution is passed removing that person from office;

h.     a contract under which that person was appointed as a director of the company or undertakes personally to perform services for the company terminates, and the directors decide that that person should cease to be a director; or

i.      the directors decide that that person should be removed from office, after having given that person a reasonable opportunity to be heard at a directors’ meeting called on at least fourteen days notice.

2.     The termination of a person’s appointment as a director under the articles:

a.     terminates that person’s membership of any committee and any other employment which that person may have with the company;

b.    is without prejudice to any claim which that person may have for breach of contract.

24 Directors’ terms of service

1.     Directors may undertake any services for the company that the directors decide (except audit).

2.     Directors may undertake such services either as part of, or in addition to, their work as directors.

3.     Subject to the Companies Acts:

a.     directors shall be entitled to be remunerated for their services to the company as the directors determine; and

b.    the directors may decide any other terms of any contract relating to the services which a director undertakes personally to perform for the company.

4.     Subject to the articles, a director’s remuneration may:

a.     take any form;

b.    be contingent on or otherwise calculated by reference to any aspect of the company’s performance, however measured; and

c.     include any arrangements in connection with the payment of a pension, allowance or gratuity, or any death, sickness or disability benefits, to or in respect of that director.

5.     Directors’ remuneration which is determined by the directors must not include payments to or for the benefit of directors or former directors in connection with the cessation or the transfer to any person of the whole or part of the undertaking of the company or any of its subsidiaries.

6.     Unless the directors decide otherwise, directors’ remuneration shall accrue from day to day.

7.     Unless the directors decide otherwise, directors shall not be accountable to the company for any remuneration which they receive as directors of the company’s subsidiaries.

25.  Directors’ expenses

Subject to the Companies Acts, the company shall meet any reasonable expenses which the directors properly incur in connection with anything they do for the company.

ALTERNATE DIRECTORS

26.  Appointment and removal of alternates

1.     An alternate director (or “alternate”) is a person appointed by a director (the alternate’s “appointer”) to:

a.     exercise that director’s powers; and

b.    carry out that director’s responsibilities, at directors’ meetings as requested by that director.

2.     Alternate directors must be:

a.     directors, or

b.    persons approved by the directors and willing to act as their appointers’ alternates.

3.     Any director may appoint an alternate by notice in writing to the company specifying the duration of the alternate’s appointment.

27.  Rights and responsibilities of alternate directors

1.     Except as the articles specify otherwise, alternate directors shall, in relation to directors’ meetings:

a.     have the same rights, duties and liabilities under the articles as their appointers;

b.    be subject to the same restrictions as their appointers; and

c.     be deemed for all purposes to be directors.

2.     Alternate directors shall not be entitled to receive any remuneration from the company for their services as alternate directors except such part of their appointers’ remuneration as their appointers may direct in writing.

3.     Alternate directors are responsible for their own acts and omissions and shall not be deemed to be agents of or for their appointers.

28.  Termination of alternate directorship

Alternate directors’ appointments as alternates terminate:

a.     when their appointers revoke their appointments by notice to the company in writing specifying when their appointments are to terminate;

b.    on the occurrence in relation to them of any event which, if it occurred in relation to their appointers, would result in the termination of their appointers’ appointments as directors;

c.     when their appointers die; or

d.    when their appointers appointments as directors terminate, except that alternate directors’ appointments as alternates do not terminate if their appointers retire by rotation at a general meeting at which they are re-appointed as directors.""",
"Format for Formation Agreement to Convert a Partnership into a Limited Company":"""DRAFT OF FORMATION AGREEMENT TO CONVERT A PARTNERSHIP INTO A LIMITED COMPANY



 AGREEMENT is made at________on this_____ day of____________ between Mr. L s/o_______residing at ......... of the FIRST PART and Mr.M s/o_________residing at .......... of the SECOND PART and Mr. N s/o___________ residing at .......... Of the THIRD PART as follows:

The Parties are carrying on business of dealing in electronic goods in partnership in terms of the deed of partnership ____________ entered by and between them in the name of M/s. LMN & Co. and the parties now propose to convert the said partnership into a public company limited by shares under the Companies Act 1956  or Companies Act, 2013 , on the following terms agreed upon between them.

NOW IT IS AGREED BY AND BETWEEN THE PARTIES HERETO AS FOLLOWS:

1.     The Parties agree that they will form and register a public company limited by shares with a view to carry on the business carried on by them in partnership as aforesaid.

2.     The name of the company will be ABC & Co. Ltd., subject to approval by the Registrar of Companies or such other name as will be approved by the parties hereto and by the said Registrar of Companies.

3.     The Memorandum of Association and Articles of Association will be got prepared by the lawyer to be appointed by the parties hereto and to be approved by the parties hereto. The main object of the proposed company will be to deal in electronic goods by way of manufacture, sale and purchase thereof or acting as the agents for sale of such goods for any other Company or concern.

4.     The nominal or authorized capital of the company will be Rs.__________ to be divided into equity shares of Rs.100/- each and________preference shares of Rs.100/- each.

5.     The valuation of the business of the said partnership together with its assets, stock-in-trade and goodwill including book debts but subject to liabilities will be obtained from the Chartered Accountants of the said partnership firm and the amount of such valuation will be taken as paid to the parties hereto by allotting equity shares and preference shares of the face value of such valuation as fully paid up to each of the parties hereto. The valuation of the assets and the goodwill of the said partnership business will be made and shown separately. The equity and preference shares in the capital of the company will be allotted to the parties hereto in the ratio or in proportion in which shares of the parties in the capital and property of the said partnership firm are held.

6.     The parties shall subscribe to the Memorandum and Articles of Association, one share each to be paid in cash and they will also secure additional at least four persons to subscribe to the Memorandum and Articles by agreeing to take one share each.

7.     Besides, the minimum subscription to shares required to commence business will also be contributed by the parties hereto in cash in the same proportion as aforesaid.

8.     The initial expenses required for registration of the company will be contributed by the parties in equal shares and the same will be reimbursed to them by the company after registration of the company.

9.     The parties hereto will be the first Directors of the Company and the Board of Director will be constituted after the registration of the company in terms of the Articles of Association. The total number of Directors shall not be more than five.

10.  On the registration of the company the parties agree to transfer the business of their said partnership together with all assets and liabilities and together with its goodwill and the benefit of subsisting contracts entered into by the partnership, by executing a Deed of Assignment of the business as a going concern in terms of the draft that will be prepared by the legal adviser of the parties.

11.  No invitation to the public to apply for allotment of shares of the issued capital to be fixed by the Director will be made until the shares to be allotted to the parties in cash as well as fully paid are allotted to the parties hereto and other subscribers to the Memorandum of Association.

12.  This agreement is provisional only and shall not be binding on the company until the date on which company is entitled to commence business under S. 149 of the Companies Act and on that date it shall become binding on the company formally adopting the same. In case that event shall not happen this agreement will be treated as canceled.

13.  On the registration of the company and the company becoming entitled to commence business, the Board of Director to be constituted as aforesaid will adopt this agreement so as to be binding on the company. A formal agreement will be entered into between the company and the parties for adopting and confirming this agreement.

14.  After the business of the said partnership is assigned to the company as aforesaid, the said partnership will be treated as dissolved and no party will be liable to pay any amount to the other in respect of such partnership. It is, however agreed that if any of the creditors does not accept the company as debtor for the amount, due to him on any account, the amount due to such creditor or creditors will be payable and paid by the parties hereto in proportion of their respective shares in the partnership and the valuation of the said business will be increased to that extent. The consent of the creditors to the transfer of the liability of the partnership to the company will be obtained before the transfer of the business to the company. A formal Deed of Dissolution will be executed by the parties and intimation of dissolution will be filed with the Registrar of Firms and advertised as required by law.

15.  The parties agree that so long as they will be directors and share holders of the company, none of them will start a similar business or be directly or indirectly interested in a similar business as that of the company.

16.  The parties agree that none of them will exercise any vote for removal of any of them as director.

17.  The costs of and incidental to the execution of the Deed of Assignment of the business by the parties hereto will be borne by the company.

18.  The liability to pay capital gains tax on transfer of the said business will be that of the parties in proportion to their shares in the partnership and the parties will indemnify the company against such liability.

IN WITNESS WHEREOF the parties have put their hands the day and year first hereinabove written.

Signed and delivered by

Within named partners

Mr. L,

Mr.M

Mr. N

IN the presence of_________

Witnesses

1._____________

2._____________""",
"Format for Joint Venture / Share Holder’s Agreement":"""DRAFT OF JOINT VENTURE/SHARE HOLDERS AGREEMENT



MODEL OF A JOINT VENTURE/SHARE HOLDERS AGREEMENT BETWEEN TWO COMPANIES HOLDING EQUAL SHARES IN THE JOINT VENTURE COMPANY TO BE INCORPORATED FOR A PARTICULAR PROJECT

THIS AGREEMENT executed at_______________ on the day of___________________

BETWEEN: M/S. ABC PRIVATE LIMITED.

(herein after referred to as the "ABC", which expression shall, wherever the context so requires or admits, mean and include, its successors and assigns).

A N D: M/S.XYZ PRIVATE LIMITED,

(here in after referred to as the "XYZ ", which expression shall, wherever the context so requires or admits, mean and include, its successors-in-title and assigns);

WITNESSES AS FOLLOWS:

      I.        WHEREAS ABC is engaged in business of ____________________ and have the necessary experience and expertise in that field;

     II.        WHEREAS the XYZ are doing ____________________________________ and have the necessary experience and expertise in that field;

    III.        WHEREAS the parties hereto have decided to float a project of _______________________________ ( hereinafter referred to as the "PROJECT");

   IV.        WHEREAS ABC and XYZ both having the necessary infrastructure and the capabilities of providing the services required for the project have agreed to form a Joint Venture Company for the Project and ABC and XYZ are desirous of entering into an Agreement for constituting Joint Venture Company in terms hereof;

    V.        WHEREAS the Parties hereto for the said Project have decided to form a Joint Venture Company and whereas subject to all necessary consents, licences, permissions and authorities to be procured for the formation and incorporation of the joint venture Company in the State of India, with the principle object, inter alia, being that of ____________________;

   VI.        WHEREAS ABC and XYZ are desirous of recording the Agreement with regard thereto and the agreement arrived at between them;

  VII.        NOW THIS AGREEMENT WITNESSESTH AS FOLLOWS:

1.     It is agreed between the parties hereto to constitute a new Company which will be incorporated under the provisions of the Companies Act, 1956 or Companies Act, 2013 and the Parties further agree that the said Company shall carry on its business in the name and style of "XYZ - ABC PRIVATE LIMITED" or any other name as may be mutually agreed between the parties hereto, (hereinafter referred to as the "SAID COMPANY" or "JOINT VENTURE COMPANY")

2.     It is agreed that the terms and conditions of this Agreement shall govern the relationship of ABC and XYZ and the rendering of services under this Agreement and any subsequent Agreement;

3.     It is agreed between the Parties hereto that the share holdings of the said Company shall be held by XYZ and ABC in the ratio of _% belonging to XYZ and _% belonging to ABC;

4.     The Company shall be incorporated in the State of _________, after following all the provisions of the Companies Act, including any amendments from time to time, required for the incorporation thereof. The Registered Office of the Joint Venture Company shall be situated at "__________", ___, ________ Road, ___________________;

5.     It is agreed between the Parties hereto that the said Company shall have as its object of business recorded in the Memorandum of Association & Articles of Association inter alia _____________________________________________________________________;

6.     It is agreed between the Parties hereto that the authorised capital of the said Company shall be Rs.______ /- (Rupees _______only) divided into ______equity share of Rs.__________ /- (Rupees _________only) each;

7.     The Parties hereto shall jointly approve the Memorandum and Articles of Association of the said Company taking into consideration the principle objectives as set out in Paragraph 5 above;

8.     ABC shall on incorporation of the Joint Venture Company subscribe to ___% of the authorised share capital and the XYZ shall on the incorporation of the said Company subscribe to __% of the authorised share capital, and pay for such shares on call made by the said Company towards the said shares, within the period prescribed;

9.     The Parties further agree that the authorised capital of the said Company may be increased from time to time as per the Provisions of the Companies Act and as per the financial requirements of the said Company and as approved by the Board of Directors/General Body Meeting and it is further agreed that on the authorised capital being increased ABC and XYZ will be entitled to subscribe thereto in equal ratio and only after the other Party by written notice under acknowledgement rescinds the offer to apply for additional shares will the other be entitled to subscribe for those share not applied for;

10.  ABC and XYZ agree that till such time as the project is being handled by the Joint Venture Company, ABC and XYZ shall always have equal representation on the Board. Mr.____________ shall be the Nominee Director of ABC and Mr._________________ of XYZ Group being the First Directors who shall hold the Office for entire period of the project, save and except both of them will not be liable for retirement. The number of Directors will be ______in total, ___ from ABC and _____from XYZ;

11.  It is further agreed between the Parties that in the event of any of the Director from any of the group retiring/being removed/dying or becomes unable to perform the duties of a Director or for any reason ceases to be employed by the Party that nominated them then such party shall promptly by written notice served to the other party name in Successor thereof so that the strength of the Board of Directors remains same as before;

12.  Meetings of the Board of Directors for the transaction of business of the Joint Venture may be called, subject to reasonable notice by the Directors of either party.

13.  The Board of Directors shall have full responsibility and authority for the performance of the Company including but not limited to assignment of services between the Parties, preparation of the schedule of services, settlement of disputes and any other items affecting the performance of services under this Agreement;

14.  The Board of Directors shall constitute a committee being the Executive committee for the execution of the work of the Project Agreement and the said committee shall consist of one representative of ABC and another from XYZ and at all times there shall be equal representative on the said committee from ABC Group and the XYZ Group;

15.  The Executive Committee shall be:

a.     Responsible for the direction and management of the Work in accordance with the policies and procedures established by the Board of Directors;

b.    Responsible for the Co-ordination of the Work; and

c.     ____________________________________________ The Board of Directors may from time to time change the existing Executive Committee by replacing its representatives, however the representation of ABC and XYZ shall always be equal on such committee;

16.  Action and decisions of the Board of Directors shall be by unanimous vote and shall be final, and conclusive and binding upon both ABC and XYZ;

17.  In the event the Board of Directors is unable to reach any unanimous decision, ABC and XYZ agree that the matter in controversy shall be referred to Mr.__________ with regards to matter relating to _________________________ and _____ Mr._____ with regards to matter relating _________________________________ who shall make an interim decision which may be subject to arbitration if the parties hereto do not accept the decision;

18.  The Parties agree that the Board of Directors shall by and large conduct business of the said Company on the basis of the Agreement arrived at between them under this Agreement or mutually agreed between them in writing from time to time between them, giving effect to the understanding arrived at between them under this Agreement;

19.  The Parties further agree that until mutually agreed in writing by and between the parties hereto the said Company shall not:

a.     increase or re organise its authorised capital;

b.    amend the Memorandum of Association & Articles of Association;

c.     dissolve or liquidate the said Company;

d.    in any manner deal with and dispose off or create any charges with regards to the assets of the said Company or its business;

e.     Amalgamate with any other Company;

f.     to stand and guarantee in any manner for any other parties or any other person/s without the prior consent and without the Special Resolution of the General Body Meeting of the said Company;

20.  Each of the Parties hereto agree that they shall perform their obligations as set out in Clause 24, 25 and 26 with regards to the said Company so as to complete the project undertaken by the said Company as a successful venture;

21.  The Parties further agree that as the nature of business undertaken by the Parties is relating to the Project to date which will get transformed to the said Company, any business which has been set out in the Memorandum of Association of the said Company shall be done by XYZ and ABC through the said Company only;

22.  ABC and XYZ shall furnish all necessary know how experience, expertise, man power, managerial assistance to make success of the project undertaken by the said Company;

23.  The Joint Venture Company shall share, in the manner provided for in the Agreement, the obligations and responsibilities for the services to be performed for the Project as described in this Agreement. Both ABC and XYZ shall give strategic input to the Joint Venture Company to perform the specific services as given below:

24.  Both ABC and XYZ will give their input for:- Marketing, project management, i.e., monitoring of the execution of the project from the stage of commencement to completion and property management thereon; Identifying Consultants and Contractors, finalisation and awarding tenders to all Contractors and Consultants; Any other services required to fulfill the needs of the project;

25.  ABC shall give their inputs on procurement and work of all design and technical consultants;

26.  XYZ shall give their input in liasoning with local authorities, Government for obtaining permissions for Plan sanction including all the approvals required from various Governmental Agencies for the purpose of construction and completion of the Project.

27.  Neither ABC nor XYZ shall enter into any separate agreement/s with ______________ for services in connection with this Project as long as the association between ABC and XYZ with regards to the Project is in existence;

28.  The Services required of the parties to Joint Venture Agreement shall be limited to the performance of services required under this Agreement;

29.  ABC and XYZ intend that the responsibilities and obligations set out in this agreement shall be borne and performed by each of the party as stated herein and the financial contribution as and when required for the Company shall be in proportion of their participation as provided in clause 3 of this Agreement;

30.  It is agreed between ABC and XYZ that for the purposes of ------------------------------------ the same shall be done by ABC and XYZ together and for the said purpose ABC and XYZ will constitute and form another company in which both ABC and XYZ will have equal shares and XYZ and ABC will have equal representation on board at all times;

31.  The Parties agree that as the Parties shall be working in co-ordination with each other and for the furtherance of the interest of the said Company and during the course of work any information, expertise or knowledge material, documents or trade secret exchanged between the parties shall be kept secret and neither parties hereto shall divulge the same to any Third Party in any manner whatsoever and accordingly the parties shall on the incorporation of the said Company include a Clause in the Memorandum and Articles of Association to maintain the trade secret between the parties hereto/shareholder/Directors or anyone employed by the said Company and accordingly the parties shall also execute such document between them after incorporation of the said Company as may be necessary and as advised;

32.  It is agreed between the Parties that amounts received by the Joint Venture Company will be allotted to ABC and XYZ equally The distribution so made will be irrespective of the expenses that may be incurred by either XYZ or ABC towards their staff or expenses or any other head of accounts;

33.  It is agreed between the ABC and XYZ that for the compliance of their respective obligation to be fulfilled in terms of this Agreement and after meeting the basic expenses of the joint venture company, the amounts in hand of the Joint Venture Company will be distributed between ABC and XYZ in the respective proportion set forth in Clause 3 of this Agreement. Upon completion of this Agreement, funds remaining after payments of outstanding indebtedness of the Joint Venture Company shall be distributed to the respective Parties in the same proportion as set forth in Clause 3 above;

34.  Should the Board of Directors determine that additional funds are required for the performance of the Project Agreement for any reasons or to pay losses arising there from or to eliminate any deficits resulting from prior overpayments to the ABC or XYZ, the Parties shall within 14 working days after the decision of the Board of Directors contribute such funds in proportions set forth in Clause 3 of this Agreement;

35.  In the event of any of the Party does not contribute for any reasons such funds as may be determined under Clause 34 above the other party may at its discretion bring in the amounts to be contributed by the other party or any part thereof at its discretion and in this event the Other party will be liable for payment of the amounts to the Party contributing in excess along with interest at the rate of 22% per annum or any part thereof to be calculated from the date of contribution to repayment;

36.  It is agreed between the parties that the amounts that may become payable in terms of Clause 34 above by the Party failing to contribute in terms of Clause 34 the Party contributing the amounts will be entitled to the said amounts at the first instance from the amounts to be disbursed and out of the share of the Party defaulting in payment along with the interest as stipulated in para 35 and thereafter if any amounts are balance to the share of the party defaulting will be taken by him;

37.  It is agreed between parties hereto that the Joint Venture company will employ necessary persons for the purpose of services to be rendered for the project and for the purpose of the project and the said personnel will be employed by mutual consent of both XYZ and ABC. The salary and payment with regards to the said employees shall be borne by the said Joint Venture Company;

38.  It is agreed between XYZ and ABC that in the event that either XYZ or ABC or its personnel are required to render service to the Joint Venture company either in sales promotion or any other area of work of the project, then in that event, all the actual expenses incurred will be reimbursed to either XYZ and or ABC as the case may be. The nature of expenses permitted for reimbursement are set out in Annexure ______ hereto;

39.  The Parties hereto agree that on the incorporation of the said Company, the said Company in its first meeting shall ratify what has been agreed hereunder;

40.  The Parties after the execution of this agreement shall finalise between them the master plan charting out the plan for execution of the project, setting goals, time frames, manner and method of implementation of the project, the day to day operations and manner in which the said company would handle the entire project;

41.  The said Company shall appoint an independent Chartered Accountant who shall perform such duties as determined by the Board of Directors which shall include regular audit accounts of the said Company file all necessary forms, applications, accounts with the concerned authority as may be necessary and as per the Provisions of the Companies Act, or any other Statutory Authority with regards to the said Company. For the purpose of this agreement the certified figure of the independent Chartered Accountant shall be final conclusive and binding upon the parties;

42.  The Parties hereto agree that all the preliminary expenses with regards to the incorporation of the said Company including all the costs, charges, expenses, professional fees, out of pocket expenses that may be incurred during the incorporation and formation of the said Company and incidental to the establishment of the said Company shall be borne by and paid for by the said Company;

43.  The Board of Directors shall appoint an Accountant for the Joint Venture Company who shall maintain the day to day books of the Company on the generally accepted accounting principles;

44.  The Board of Directors may authorise one or more bank accounts in any bank nationalised or private and the said Bank account/s for all purposes shall be operative under the joint signature of the representative/s of ABC and XYZ;

45.  All payments received by the Joint Venture, in connection with this Agreement, shall be promptly deposited in the aforementioned Joint Account and invoices received by the Joint Venture shall be paid by Cheque drawn against the Joint account;

46.  Records of the Joint Venture which are required pursuant to law to be retained beyond the duration of this Agreement shall be retained at such place(s) as determined by the Board of Directors and the cost thereof shared by the parties in proportion to their respective interest as described in Clause 3 of this Agreement;

47.  Joint Venture property shall consist of the capital contributions described in Clause 8 of this Agreement and any other property obtained with the funds of the Joint Venture. The Joint Venture property shall be identified and recorded in the Joint Venture accounts;

48.  This Agreement represents the entire and integrated agreement between the Parties and supercedes all prior negotiations, representations and agreements, either written or oral. The Agreement may be amended only by written instrument signed by each Party to this Agreement;

49.  Neither party shall assign this Agreement without the written consent of the other;

50.  The right of any person, firm or corporation, claiming by, through or under any Party (including, but not limited to judgement or other creditors, receivers, trustees, assignees, executors and administrators), to assert any claim against the right of interests if any Party shall be limited in any event to the right to claim or receive after completion of the Project Agreement, and after the doing of the accounts of the Joint Venture, the proportional interest of such Party as described in Clause 3 of this Agreement, and then only subject to the equities of the other Party as set forth in this Agreement;

51.  The Parties to this Agreement, respectively bind themselves, their successors, assigns and legal representatives to the other Party with respect to all covenants of this Agreement;

52.  All public statements and releases, including the issuance of photographs, models and renderings, for all media for the duration of this Agreement, are subject to the prior approval of the Board of Directors;

53.  In subsequent presentations made by the Joint Venture, in any brochures publicity material in any form of media with regards to the Project and any logo mark devised by the Joint Venture Company or any development/drawing that can be and which constitutes any intellectual property shall be the intellectual property of the Joint Venture Company and will be dealt in the manner set out herein

54.  If determined by the Board of Directors or required under the Project Agreement, intellectual property, reports, analysis, contracts, designs, drawings, specifications and other instruments of service prepared pursuant to this Agreement shall be registered, patented, copyrighted and secured as intellectual property rights as per the provision of law and in the name of the Joint Venture. The Joint Venture Company shall have the ownership and rights and privileges of all intellectual property rights acquired in the course of the Project and in so far as it is consistent with this Agreement XYZ and ABC will be entitled to use such intellectual property for any of its purpose including to prepare documents for other projects based on such Project information without any payment thereof so long as they are equal shareholders of the Joint Venture Company in terms of this agreement and not otherwise;

55.  Neither of XYZ nor ABC shall assign or transfer the intellectual property rights and interest so acquired or established pursuant to this agreement by the Joint Venture Company in the course of its Project, nor permit reproduction of Project documents otherwise then stated in clause 53 above, in any manner resulting in infringement or violation of any of the intellectual property rights secured by the Joint Venture Company during the course of the Project except upon written consent of the other Party;

56.  Documents prepared specifically for this Project by one of the Parties to this Agreement may not be copyrighted solely by that Party. Each Party hereby grants the other and the Joint Venture a licence to use and reproduce such documents in furtherance of this Agreement and Project;

57.  The Parties further agree that as far as the registered Office of the Company is concerned, the same shall be at _________________________________________or at mutually agreed place provided always that the Registered Office shall be at __________ State of _________, India;

58.  It is further agreed between the Parties hereto that during the existence of this Agreement and the incorporation of the said Company if there being any change in Law which may affect the incorporation of the said Company as agreed between the Parties hereto then in that event, the Parties hereto may mutually agree to terminate this Agreement without any claim of damages by either party and in the event of there being any pre incorporation expenses incurred by the Parties hereto, the same shall be shared equally between the ABC and the XYZ;

59.  In the event of there being any dispute which may result into a dead lock situation between XYZ and ABC, the Parties before invoking the rights set out in Clause 59 of this Agreement, the Party expressing that the other Party is in breach shall give a written notice of any situation likely to result in dead lock, putting forth all the details of the nature of dispute and the Parties will resolve the said dispute between 14 days of such written notice being received after which period, the Parties may refer the dispute to Arbitration as per the provisions of Clause 70;

60.  It is agreed between the parties that in the event of there being a dead lock situation with regard to the management of Joint Venture Company then in that event it is agreed between the parties hereto that for the purposes of removing the dead lock any one of the parties hereto who may chose to value the share held by it and on such valuation done by that party the other party will have the first option to either acquire at that price the shares of the party valuing it or sell its shares to the valuing party and the party valuing the shares will have no option but to either sell its share at the valuation set, to the other party or to acquire the shares of the other party at that value as the case may be;

61.  No Party will be entitled to sell transfer, pledge, mortgage, charge, encumber or otherwise dispose off or create any lien on or interest in, any of its shares in the Joint Venture Company, save and except as per Clause 63 below;

62.  In the event of any one of the Party decides to dispose off its shareholding, which shall always be the entire shareholding, it shall give notice of its intent of disposal to the other Party, and the other Party will have the right to acquire the entire shareholding on the valuation of the shares done by an Independent Chartered Accountant appointed by both the Parties or identify a buyer for the purchase of the entire shareholding within a period of 12 weeks from the receipt of the written notice from the Party intending to sell, after which period, the Party intending to sell its shareholding will be entitled to dispose of the shares to any third party. Any notice with regards to intend to sell the shareholding or refusal to acquire the shareholding, shall be done through Registered Post Acknowledgement Due.

63.  Notwithstanding the provisions setout in Clause 61, either of the Parties to this agreement would be entitled to transfer its shareholdings to any of its subsidiary or affiliate Companies, may be one or more such subsidiary or affiliate Companies and the shareholding of such transferee shall be clubbed for the purpose of the total shareholding of XYZ or ABC as the case may be. The Transferee shall be bound by the terms and conditions of this Joint Venture Agreement. For the purpose this agreement parties hereto agree that the meaning subsidiary /affiliate companies shall mean such companies wherein the Party desiring to transfer the share holding in the Joint Venture Company should have at least 51% shares in such affiliate or subsidiary as the case may be

64.  In the event of the Project being completed and in the event of there being no other project being undertaken the XYZ shall be entitled to take over the Joint Venture Company at Book Value, however the name of the Joint Venture Company will stand changed and XYZ shall not use the name of the Joint Venture Company. If XYZ does not desire to acquire the Company, the XYZ and ABC shall jointly sell the Company to any Third Party and the sale proceeds to be shared equally. The Party shall not be permitted to use the name of XYZ ABC;

65.  The Parties hereto agree that the address set out in the title of this Agreement are the true addresses and the notice/s may be issued to them at the said address in the event of there being any change of address, the same shall be intimated to all the Parties failing which any notice/s served on the existing address shall be deemed to be good service on the addressee;

66.  Any amendments to this Agreement shall be done with the consent of the Parties and in writing. Otherwise nothing shall be binding on the Parties hereto;

67.  This Joint Venture will commence as of the date of this Agreement. It is further agreed that the terms and conditions of this Agreement shall be an agreement governing the shareholder of the Joint Venture Company including where ever it relates to the provisions of share holding its transfers, conduct of the business by the parties hereto and conduct of the Board of Directors and the constitution of the Board of the Joint Venture Company and the terms set out herein;

68.  This Agreement shall remain in full force and effect until terminated by written agreement of the Parties or until the Project has been completed and all Joint Venture Property and money has been distributed in accordance with this Agreement and even after the incorporation of the Joint Venture Company as a shareholders agreement;

69.  The obligation of each party to contribute in accordance with this Agreement to the satisfaction of all debts and liabilities of the Joint Venture shall survive the termination of this Agreement;

70.  It is further agreed between the Parties hereto that in the event of there being any dispute with regards to this Agreement or any of the terms hereof or the interpretation of any of the terms of the Agreement or any dispute arising under the said Agreement, the same shall be referred to the Arbitration of two Arbitrators appointed by each of the Parties hereto i.e., ABC and the XYZ and the Arbitration proceedings shall be as per the provisions of the Arbitration and Conciliation Act, 1996 and the venue of such Arbitration proceedings shall be held and conducted in _________________alone;

71.  This Agreement shall be binding upon the Parties hereto and their successors in title and all the shareholders of the Joint Venture Company and their respective heirs, executors, administrators, successors in title and assigns as the case may be;

72.  If any provision of this Agreement shall, under any circumstance, be deemed invalid/inoperative to an extent, such invalidity shall not invalidate the whole Agreement, but the said invalid or inoperative provision shall be construed as not to be contained in this Agreement;

73.  The provisions of the Companies Act, 1956 or companies Act, 2013  would apply with regard to the governing of the Joint Venture Company otherwise than what has been agreed by and between the Parties hereto;

74.  It is agreed by and between the Parties hereto that the Courts at____________________ alone shall have jurisdiction with regards to this Agreement and the seat of Arbitration shall be _________ and the Arbitration proceedings shall be in English; IN WITNESS WHEREOF, the PARTIES hereto have executed this AGREEMENT in the presence of the Witnesses attesting hereunder: SIGNED SEALED AND DELIVERED

BY THE WITHIN NAMED ABC

PRIVATE LIMITED REPRESENTED

BY ITS MANAGING DIRECTOR IN

THE PRESENCE OF THE FOLLOWING

ABC

WITNESSES:

1)

2)

SIGNED SEALED AND DELIVERED

BY THE WITHIN NAMED XYZ

PRIVATE LIMITED REPRESENTED

BY ITS MANAGING DIRECTOR IN

THE PRESENCE OF THE FOLLOWING

XYZ

WITNESSES:

1)

2)""",
"Format for Shareholders Agreement":"""DRAFT OF SHAREHOLDERS AGREEMENT



 BETWEEN



____________________

AND

____________________

RE: Shares of ----------------------Pvt. Ltd.

THIS AGREEMENT made the ____ day of ______, 20__ BETWEEN MR.B residing at _____________________ (hereinafter referred to as "A") (which expression shall, unless repugnant to the context or meaning hereof, mean and include his heirs, executors, administrators and assigns) of the First Part.

And

MR. B residing at __________________________(hereinafter referred to as "B") (which expression shall, unless repugnant to the context or meaning hereof, mean and include his heirs executors, administrators and assigns) of the Second Part.

And

________________________ (P) LTD., a Company incorporated under the Companies Act____ and having its registered office at _____________________ herein represented by its ___________ (hereinafter referred to as "XYZ") which expression shall, unless repugnant to the context or meaning hereof, include its successors and assigns) of the Third Part;

WHEREAS:

A.    A and B hereto have agreed to jointly manage a company in India named "XYZ Pvt Ltd ";

B.    A and B have agreed to become Equity Partners by investing in the shares of the Company subject to the condition that they shall enter into a Shareholders Agreement in terms of these presents;

C.    The Company "XYZ PVT. LTD. " has been requested to, and has agreed to, join in the execution of these presents and to take this Agreement on record so that it is aware of the rights and obligations of A AND B, the parties hereto and ensure that they comply with the same;

D.    The parties hereto are desirous of recording the terms and conditions of their Agreement in writing;

NOW IT IS HEREBY AGREED BY AND BETWEEN THE PARTIES HERETO AS FOLLOWS:-

1.      

a.     A and B shall jointly invest in the Company which is an existing company limited by shares under the Companies Act,____ and known as "XYZ PVT LTD".

b.    The registered office of the Company shall be situated at ________________, or at such other places as may be mutually agreed upon between the parties in writing.

c.     The Company shall carry on the business of running and managing restaurants and (Description of the business and complete address), either by itself or through other agencies or company industries and may carry on any other business as may be decided by B hereto and shall ensure that no other business activity is undertaken by the Company at any time without the consent of A hereto.

2.     The authorised share capital of the Company is Rs.________/- (Rupees ___________________ only) consisting of ______________ (________) equity shares of Rs.10/- (Rupees ten) each.

3.     The subscription by A hereto to the aforesaid authorised share capital of the Company shall be 1,00,000 (One lakh) equity shares of Rs.10/- (Rupees ten only) and the subscription by B to the aforesaid authorised share capital of the Company shall be 1,00,000 (One lakh) equity shares of Rs.10/-(Rupees ten only).

4.     There shall be no further issue of capital without the consent of both the parties hereto, and unless otherwise agreed upon in writing further investment shall be as mutually decided by both parties.

5.      

a.     The Board of Directors of the Company shall consist of A and B

b.    A shall have the right to nominate two (2) Additional Directors onto the Board and B shall have the right to nominate three or more Additional Directors on the Board. Both parties shall be entitled at any time to remove any of the representatives on the Board by written notice to the other party and to appoint another or other/s in their place.

c.     The day to day management of the Company shall be looked after by a Managing Director to be appointed with the consent of B hereto. Any major acquisition of property, substantial expansion of business activities or diversification or matters of policy shall be with the prior consent of B.

d.    It is agreed as between the parties hereto that the position of Chairperson of the Company shall be held by B or a nominee of B. The Chairman of the Board shall also be the Chairman of all general meetings of the Company.

6.     A and B hereto jointly and severally shall vote and act as members of the Company and with respect to the shares of the Company held by them, so as to ensure that Directors of the Company are at all times appointed and maintained in office in conformity with the provisions of this Agreement. If at any time the provisions of this Agreement are not fully complied with, A and B jointly and severally agree to promptly take all necessary steps to ensure that the provisions of this Agreement hereof are fully implemented in letter and spirit.

7.      

a.     The Auditors of the Company shall be M/s.______________________.

b.    The Auditors of the Company shall not be changed without the prior written consent of both A and B.

8.     Any sale or transfer of shares in the Company by either party shall be as provided in Clause 9. If at any time during the continuance of this Agreement either A or B, desire to sell or transfer all or any of their respective shares held by them in the Company, they shall do so strictly in accordance with the provisions hereinafter written.

9.     If either A or B desires at any time to sell the whole or part of their shares in the Company, he shall first offer such shares in writing to the other. If the other does not accept in writing the offer within 15 days of receipt of the offer, the first party shall then be at liberty within 30 days thereafter to sell the shares so offered to any other persons of its choice at the same price and on the same terms and conditions as contained in its written offer to the other party hereto in the first instance, failing which the procedure contained in this sub-clause will have to be repeated by a party desiring to sell his shares.

10.  B will bring in further working capital to run an F & B Unit(s) at (Address of registered office). __________ Bank had advanced loans of about Rs. 1,10,00,000/-(Rupees One Crore Ten Lakhs Only) to XYZ which loans have to be repaid by them. B will be bringing further moneys upto Rs. (Rupees Only) to repay the loan. The Balance Rs. ____/- has been secured with the collateral security provided B. XYZ have entered into a Management and Royalty Agreement with ------------- (P) Ltd., for the operation and management of the F & B unit(s) of XYZ and are entitled to receive their share of profit. A and B are equally entitled to this share of profit being equal share holders of XYZ. It is hereby agreed that A shall not be entitled to a percentage of the profit which shall not exceed Rs. ------/-(Rupees ________________ Only) per month from XYZ out of his share of profit subject to the terms contained herein and/or in any other document executed by him on behalf of XYZ. The balance money attributable to A shall be utilized to repay the loans and interest outstanding to ________ Bank, and the amount of Rs. ________ /- brought in by B and interest thereon, and towards the working capital brought in by B and interest thereon and any other loans of the XYZ. This arrangement will continue till the entire sums (liabilities) together with the interest thereon have been repaid. However B will be entitled to withdraw the profit attributable to his share.

11.  B will be entitled to interest at the rate of 12% per annum on the sums brought in by him or his Associates / concerns / businesses.

12.  A and B agree and undertake not to disclose or divulge directly or indirectly to any third party any trade or business secret or other secret or confidential information pertaining to the business, affairs or transactions of each other or of the Company or of their clients or customers, that may have been disclosed, imparted to or acquired by either of them from the other or from the Company.

13.  A and B jointly and severally undertake:-

a.     that they shall ensure that they, their representatives, proxies and agents representing them at general meetings of the shareholders of the Company shall at all times exercise their votes in such manner so as to comply with, and to fully and effectually implement, the provisions of this Agreement.

b.    That if any resolution is proposed contrary to the terms of this Agreement, the parties, their representatives, proxies and agents representing them shall vote against it. If for any reason such a resolution is passed, the parties will, if necessary, join together and convene an extraordinary, general meeting of the Company in pursuance of section 169 of the Companies Act, 1956 or  for implementing the terms of this Agreement.

14.  A and B shall jointly and severally procure and/or ensure that the Director or Directors of its choice on the board of the Company shall at all times fully and effectually implement and comply with (including by exercise of voting rights at meetings of the Board or resolutions by circulation and on resolutions passed at a meeting of any Companies of the Directors) the provisions of this Agreement.

15.  If either A or B shall commit a breach of any of the terms or provisions of this Agreement and shall fail to rectify such breach within Sixty (60) days from the receipt of written notice from the party complaining of the breach, then the latter shall be entitled, without prejudice to its other rights and remedies under this Agreement or at law, to terminate the Agreement recorded herein by written notice.

16.  No modification of alteration of this Agreement or any of its terms or provisions shall be valid or binding on A and/or B unless made in writing duly signed by both.

17.  This Agreement is personal to A and B and shall not be transferred or assigned in whole or in part by either party without the prior written consent of the other.

18.  If any dispute or difference shall at any time arise between A and B as to any terms, provisions or matters contained herein on as to their respective rights, claims, duties or liabilities hereunder or otherwise, howsoever in relation to or arising out of or concerning this Agreement, such dispute or difference shall be referred to the arbitration. The venue of such arbitration shall be in ........., unless otherwise agreed in writing. Such arbitration shall be held under and in accordance with the provisions of the Arbitration and Conciliation Act, 1996.

19.  This Agreement represents the entire agreement between the parties hereto on the subject matter hereof and cancels and supersedes all prior agreements, arrangements or understandings, if any, whether oral or in writing, between the parties hereto on the subject matter hereof.

IN WITNESS WHEREOF the parties hereto have executed these presents the day and year first hereinabove written.

SIGNED AND DELIVERD by )

MR. A)

in the presence of )

SIGNED AND DELIVERD by )

MR.B)

in the presence of )

SIGNED AND DELIVERD )

for and on behalf of

XYZ )

by its SHAREHOLDERS AND )

AUTHORISED DIRECTORS )

MR. A )

MR. B)

in the presence of )""",
"Format for Memorandum of Settlement of Industrial dispute between Employer and Employees":"""DRAFT OF FORM FOR MEMORANDUM OF SETTLEMENT OF INDUSTRIAL DUSPUTE BETWEEN EMPLOYERS AND EMPLOYEES



Names of Parties

Representing employer(s):

Representing workmen:

Short Recital of the Case

Terms of settlement

Signature of the parties

…………….................

....................................

Witness:

(1)

(2)

Conciliation Officer

Signature of ……………….

Board of Conciliation

Copy to:

1.     Assistant Labour Commissioner (Central) .................................. [Here enter the office address of the Assistant Labour Commissioner (Central) in the local area concerned].

2.     Regional Labour Commissioner (Central) ...................................

3.     Chief Labour Commissioner (Central), New Delhi.

4.     The Secretary to the Government of India, Ministry of Labour, New Delhi.

Conciliation Officer

In case of settlements effected by ………………..

Board of Conciliation

In case where settlements are arrived at between the employer and his workmen otherwise than in the course of conciliation proceeding.""",
"Format for Agreement of Amalgamation between two Companies":"""
DRAFT OF AGREEMENT OF AMALGAMATION BETWEEN TEO COMPANIES



SCHEME OF AMALGAMATION

BETWEEN

XYZ LIMITED AND ITS MEMBERS

AND

A & B LIMITED AND ITS MEMBERS

[For Amalgamation of XYZ Limited with A & B Limited under Section........of the Companies Act, 2013]

1.      Definitions: In this Scheme, unless inconsistent with the subject or context, the following expressions shall have the following meanings:

1.1   "the Act" means the Companies Act,____or any statutory modification or re-enactment thereof for the time being in force.

1.2   "the Appointed Date" means the...... date of.... or such other date as may be fixed or approved by the High Court at.....

1.3   "the Effective Date" means the last of the dates on which the sanctions, approvals or orders specified in Clause 15 of this Scheme ate obtained.

1.4   "the Scheme" means this Scheme of Amalgamation in its present form or with any modification(s) approved or imposed or directed by the High Court at.....

1.5   "the Transferor Company" means XYZ Limited, a Company incorporated under the Companies Act,2013 and having its Registered Office at

1.6   "the Transferee Company" means A & B Limited, a company incorporated under the Companies Act, 2013,and having its registered Office at

1.7   "Undertaking" means:

a.     All the assets and properties of the Transferor Company as on the Appointed Date (hereinafter referred to as "the said assets");

b.    All the debts, liabilities, duties and obligations of the Transferor Company including contingent liabilities as on the Appointed Date (hereinafter referred to as "the said liabilities");

c.     Without prejudice to the generality of sub-clause (a) above, the Undertaking of the Transferor Company shall include all the Transferor Company's reserves and the authorised share capital, movable and immovable properties including investments, claims, powers, authorities, allotments, approvals, consents, registrations, contracts, engagements, arrangements, rights, credits, titles, interests, benefits, club memberships, advantages, leasehold rights, brands, tenancy rights, other intangibles, industrial and other licences, permits, authorisations, quota rights, trade marks, patents and other industrial and intellectual properties including, know-how, domain names, import quotas, telephones, telex, facsimile and other communication facilities and equipment, rights and benefits of all agreements and all other interests, rights and powers of every kind, nature and description whatsoever, privileges, liberties, easements, advantages, benefits and approvals of whatsoever nature and where soever situate, belonging to or in the ownership, power or possession or control of the Transferor Company as on the Appointed Date and thereafter.

2.      Share Capital:

2.1   The authorised and the issued, subscribed and paid up share capital of the Transferor Company is as follows:

The authorised share capital is Rs........ (Rupees.....) divided into...... equity shares of Rs.... each. The issued, subscribed and paid-up share capital is Rs....... (Rupees.......) divided into........ equity shares of Rs...... each.

The Authorised Share Capital of the Transferee Company is Rs........ (Rupees.................) consisting of......... equity shares of Rs...... each aggregating to Rs...... and........ unclassified shares of Rs.....each aggregating to Rs............... The issued Capital of the Transferor Company is Rs........ and the subscribed and paid up capital is Rs.........

3.      Vesting of Undertaking:

3.1   With effect from the Appointed Date, the Undertaking shall, pursuant to the provisions contained in Section 394 and other applicable provisions of the Act, stand transferred to and vest in or be deemed to be transferred to and vested in the Transferee Company as a going concern without any further act, deed, matter or thing (save as provided in Clause 3.2 below) so as to become on the Appointed Date, the assets (subject to encumbrances and charges, if any, existing thereon) or liabilities of the Transferee Company. Provided always that the Scheme shall not operate to enlarge the scope of security for any loan, deposit or facility availed of by the Transferor Company and the Transferee Company shall not be obliged to create or provide any further or additional security therefor after the Effective Date or otherwise.

3.2   It is expressly provided that in respect of such of the said assets as arc movable in nature, including cash in hand, or otherwise capable of being transferred by manual delivery or by endorsement and delivery, the same shall be so transferred by the Transferor Company. In respect of movable assets, other than those specified in clause 3.1 above, including sundry debtors, outstanding loans and advances, if any, recoverable in cash or in kind or value to be received, bank balances and deposits, if any. the following modus operandi shall be followed:

The Transferor Company shall give notice in such form as they may deem fit and proper to each party, debtor or depositee as the case may be, that pursuant to the Orders of the High Court at..... sanctioning the Scheme, the said debts, loans, advances, etc. be paid or made good or held on account of Transferee Company as the person entitled thereto to the intent and purposes that the right of the Transferor Company to recover or realise the same stands extinguished. The Transferee Company may, if required, give notice in such form as it may deem fit and proper to each person, debtor or depositee that pursuant to the Orders of the High Court.... of sanctioning the Scheme, the said person, debtor or deposited should pay the debt, loan or advance or make good the same or hold the same to its account and that the right of the Transferee Company to recover or realise the same is in substitution of the right of the Transferor Company.

3.3   With effect from the Appointed Date all the debts, liabilities, contingent liabilities duties and obligations of the Transferor Company shall, pursuant to the Orders of the High Court of....... under Section..... and other applicable provisions of the Act and without any further act or deed, be also transferred or deemed to be transferred to and vest in and be assumed by the Transferee Company, so as to become as from the Appointed Date the debts, liabilities, duties and obligations of the Transferee Company on the same terms and conditions as were applicable to the Transferor Company.

4.      Accounting Treatment:

4.1   On the Scheme becoming effective, the Transferee Company shall account for the merger in its books as specified hereunder:

                       i.        all the assets and liabilities recorded in the books of the Transferor Company shall stand transferred to and vested in the Transferee Company pursuant to the Scheme and shall be recorded by the Transferee Company at their book values as appearing in the books of the Transferor Company;

                      ii.        On and from the Appointed Date and subject to any corrections and adjustments as may, in the opinion of the Board of Directors of the Transferee Company, be required, the reserves and the balance in the Profit and Loss Account of the Transferor Company will be merged with those of the Transferee Company in the same form as they appear in the financial statements of the Transferor Company;

                     iii.        The difference, if any, between the amount recorded as fresh share capital issued by the Transferee Company on amalgamation and the amount of share capital of the Transferor Company shall be reflected as General Reserves.

                     iv.        In case of any difference in accounting policy between the Transferor Company and the Transferee Company, the impact of the same till the amalgamation will be quantified and adjusted in the reserves of the Transferee Company to ensure that the financial statements of the Transferee Company reflect the financial position on the basis of consistent accounting policy.

5.      Contracts, Deeds, Bonds and Other Instruments:

Subject to the other provisions of the Scheme, all contracts, deeds, bonds, agreements including the contracts for tenancies and licence arrangements and other instruments of whatsoever nature to which the Transferor Company is a party subsisting or having effect immediately before or after the Effective Date shall remain in full force and effect against or in favour of the Transferee Company and shall be binding on and be enforceable against the Transferee Company or be enforceable by the transferee Company as fully and effectually as if it had at all material times been a party thereto.

6.      Date when the scheme comes into operation: The Scheme, though operative from the Appointed Date, shall be effective from the Effective Date.

7.      Conduct Of Business By The Transferor Company until The Effective Date: With effect from the Appointed Date and upto and including the Effective Date, the Transferor Company shall:

                i.        carry on and be deemed to carry on all its business and activities and stand possessed of its properties and assets for and on account of and in trust for the Transferee Company and all the profits accruing to the Transferor Company or losses arising or incurred by them shall for all purposes be treated as the profits or losses of the Transferee Company, as the case may be;

               ii.        carry on its business with reasonable diligence and shall not without the prior written consent of the Transferee Company alienate, charge or otherwise deal with or dispose of the Undertaking or any part thereof except in the ordinary course of its business;

              iii.        not vary the terms and conditions of service of its permanent employees except in the ordinary course of its business;

             iv.        not, without the prior written consent of the Transferee Company, undertake any new business or a substantial expansion of its existing business.

8.      Legal Proceedings: All suits, claims, actions and proceedings, by or against the Transferor Company pending and/ or arising on or before the Effective Date shall be continued and be enforced by or against the Transferee Company, as effectually as if the same had been pending and/ or arising against the Transferee Company.

9.      Issue and Allotment Of Shares By The Transferee Company:

9.1. Upon the Scheme becoming finally effective, in consideration of the transfer and vesting of the Undertaking in the Transferee Company in terms of the Scheme, the Transferee Company shall, without any further application, act or deed, issue and allot a( par....... equity shares of Rs......... each credited as fully Paid up in the capital of the Transferee Company to every equity shareholder of the Transferor Company whose name appears in the Register Members on a date ("Record Date ") to be fixed by the Board of Directors of the Transferee Company for every...... equity shares of Rs.... each held by the said shareholder in the Transferor Company, in the electronic form and by issue of share certificates for those share holders who hold the shares in physical form. The equity shares when issued and allotted by the Transferee Company in terms of the Scheme shall rank for diligence, voting rights and in all other respects pari passu with the existing equity shares of the Transferee Company.

9.2. No fractional Certificates/Coupons shall be issued by the Transferee Company in respect of the fractional entitlements, if any, to which the shareholders of the Transferor Company may be entitled on issue and allotment of the equity shares of the Transferee Company as aforesaid. The Board of Directors of the Transferee Company shall instead consolidate all such fractional entitlements to which the shareholders of the Transferor Company may be entitled on issue and allotment of the equity shares of the Transferee Company as aforesaid and thereupon issue and allot equity shares in lieu thereof to a Director or any Officer respectively of the Transferee Company with the express understanding that such Director or Officer to whom such equity shares are issued and allotted shall hold the same in trust for those entitled to the fractions and sell the same in the market at the best available price and pay to the Transferee Company, the net sale proceeds thereof whereupon the Transferee Company shall, subject to the approval of the Reserve Bank of India, wherever required, and subject to withholding tax, if any, distribute such net sale proceeds to the shareholders of the Transferor Company in proportion to their fractional entitlements. Holders of less than ... equity shares in the Transferor Company shall be entitled to receive proportionate number of shares in the Transferee Company, and for the remaining fractional entitlements, if any, they shall receive sale proceeds as mentioned above.

9.5. Upon this Scheme becoming finally effective and upon the new shares in the Transferee Company being issued and allotted by it to the shareholders of the Transferor Company whose names appear on the Register of Members of the Transferor Company on the Record Date fixed as aforesaid, the shares in the Transferor Company, both in electronic form and in the physical form, shall be deemed to have been automatically cancelled and be of no effect on and from the Record Date. Wherever applicable, the Transferee Company shall instead of requiring the surrender of the share certificates of the Transferor Company, directly issue and dispatch the new share certificates of the Transferee Company in lieu thereof.

9.6. For the purpose aforesaid, the Transferee Company shall, if and to the extent required, apply for and obtain the consent of the Reserve Bank of India and other concerned authorities, to the issue and allotment of equity shares to the non-resident shareholders of the Transferor Company in the aforesaid manner.

9.7. The issue and allotment of equity shares in the Transferee Company by the Transferee Company to the shareholders of the Transferor Company as provided in this Scheme as an integral part thereof, shall be deemed to have been carried out as if the procedure laid down under Section.... and any other applicable provisions of the Act were duly complied with.

9.8. Upon issue and allotment of Equity Shares in the Transferee Company to the members of the Transferor Company as provided in the Scheme, the existing Equity Shares held by members of the Transferor Company shall stand automatically cancelled/extinguished.

10.    Dividends, Profits, Bonus/Rights Shares:

10.1 Dividends (interim or final) in respect of the period commencing from the Appointed Date may be declared or paid by the Transferor Company or Transferee Company after mutual consultation with each other.

10.2 Except as envisaged under this Scheme, the Transferor Company and the Transferee Company shall not issue or allot after the Appointed Date any rights shares, bonus shares or other shares out of their respective authorised or unissued share capital for the time being, without the consent of the other.

11.    Employees of The Transferor Company:

11.1 All employees of the Transferor Company, who are in service on the date immediately preceding the Effective Date shall become the employees of the Transferee Company on the Effective Date.

11.2 On the Scheme finally taking effect as hereinafter provided:

a.     The employees of the Transferor Company shall become the employees of the Transferee Company, without any break or interruption in service and on terms and conditions not less favourable than those on which they are engaged by the Transferor Company as on the Effective Date. Services of all employees with the Transferor Company upto the Effective Date shall be taken into account for purposes of all retirement benefits for which they may be eligible. The Transferee Company further agrees that for the purpose of payment of any retrenchment compensation, such past services with the Transferor Company shall also be taken into account;

b.    The services of such employees shall not be treated as having been broken or interrupted for the purpose of Provident Fund or Gratuity or Superannuation or other statutory purposes and for all purposes will be reckoned from the date of their respective appointments with the Transferor Company;

c.     It is provided that as far as the Provident Fund, Gratuity Fund and Pension and/ or Superannuation Fund or any other special fund created or existing for the benefit of the staff, workmen and other employees of the Transferor Company are concerned, upon the Scheme becoming finally effective, the Transferee Company shall stand substituted for the Transferor Company in respect of the employees transferred with the Undertaking for all purposes whatsoever relating to the administration or operation of such Funds or Trusts or in relation to the obligation to make contribution to the said Pounds or Trusts in accordance with the provisions of such Funds or Trusts as provided in the respective Trust Deeds or other documents. The above shall include any trust created from the above mentioned funds for the staff and officers of the Transferor Company which shall be merged with such or similar funds of the Transferee Company. It is the aim and the intent of the Scheme that all the rights, duties, powers and obligations of the Transferor Company in relation to such Funds or Trusts shall become those of the Transferee Company.

12.    Applications to The High Court At......:

12.1 The Transferor Company shall make applications / petitions under Sections...... and other applicable provisions of the said Act to the High Court of...... for sanction of this Scheme and for dissolution of the Transferor Company without winding-up under the provisions of law.

12.2 The Transferee Company shall make applications/ petitions under Sections ........ and other applicable provisions of the said Act to the High Court........ for sanction of this Scheme under the provisions of law.

13.    Modifications / Amendments To The Scheme:

13.1 The Transferor Company and the Transferee Company through their respective Boards of Directors in their full and absolute discretion, may assent to any modification or amendment to the Scheme which the High Court... the shareholders of the Transferor Company and/or Transferee Company and/or any other competent authority may deem fit to approve /impose and effect any other modification or amendment which the Boards in the best interests of the Transferor Company or Transferee Company may consider necessary or desirable and give such directions as they may consider necessary or desirable for settling any question, doubt or difficulty arising under the Scheme or in regard to its implementation or in any matter connected therewith (including any question, doubt or difficulty arising in connection with any deceased or insolvent shareholder of the Transferor Company or the Transferee Company) and to do all acts, deeds and things as may be necessary, desirable or expedient for carrying the Scheme into effect. In the event that any modification or amendment to the Scheme is unacceptable to the Transferor Company and/ or the Transferee Company for any reason whatsoever, the Transferor Company and/or Transferee Company shall be at liberty to withdraw from the Scheme at any time.

13.2 For the purpose of giving effect to the Scheme or to carry out any modification or amendment thereto, the Boards of Directors of the Transferor Company and the Transferee Company or any Committee thereof is authorised to give such directions and/ or to take such steps as may be necessary or desirable including any directions for settling any question, doubt or difficulty whatsoever that may arise.

14.    Winding Up: On the Scheme becoming effective, the Transferor Company shall be dissolved without being wound up.

15.    Scheme Conditional On Approvals/ Sanctions: The Scheme is conditional on and subject to:

a.     the approval of and agreement to the Scheme by the requisite majorities in number and value of such classes of persons of the Transferee Company as may be directed by the High Court of....... and of the Transferor Company as may be directed by the High Court of....... on the applications made for directions under Section 391 of the Act for calling' meetings and necessary resolutions being passed under the Act for the purpose;

b.    the sanction of the High Court of........ under Sections........ of the said Act in favour of the Transferee Company and the sanction of the High Court of.........under the said provisions in favour of the Transferor Company and to the necessary Order or Orders under Section ......of the said Act being obtained;

c.     certified copies of the Orders of the High Court of...... sanctioning the Scheme being filed with the Registrar of Companies, at........ by the Transferee Company and the Transferor Company respectively.

16.    Effect Of Non Receipt Of Approvals/ Sanctions: In (he event of any of the said suctions and approvals referred to in the preceding Clause not being obtained and/ or the Scheme not being sanctioned by the High Court of...... and/ or the Order or Orders not being passed as aforesaid before the... day of..... or within such further period or periods as may be agreed upon between the Transferor Company and the Transferee Company by its Boards of Directors (and which the Boards of Directors of the Companies are hereby empowered and authorised to agree to and extend the Scheme from time to lime without any limitation), this Scheme shall stand revoked, cancelled and be of no effect, save and except in respect of any act or deed done prior thereto as is contemplated hereunder or as to any rights and/ or liabilities which might have arisen or accrued pursuant thereto and which shall be governed and be preserved or worked out as is specifically provided in the Scheme or as may otherwise arise in law. Each party shall bear and pay its respective costs, charges and expenses for and or in connection with the Scheme.

17.    Costs and Expenses: All costs, charges and expenses of the Transferor Company and of the Transferee Company in relation connection with the Scheme shall be respectively borne by the Transferor Company and the Transferee Company.""",
"Format for Simple compromise Agreement":"""DRAFT OF SIMPLE COMPROMISE AGREEMENT



This Agreement of compromise made at __________ on this ____ day of ___________, 20__ between A son of _____________ resident of ___________________ (hereinafter called Party No. 1) of the One Part and B son of ____________ resident of ___________________ (hereinafter called Party No. 2) of the Other Part.

WHEREAS, disputes and differences have arisen between the parties aforementioned regarding _____________________.

AND WHEREAS, the parties have agreed to settle their disputes and differences amicably between themselves without recourse to litigation and for that purpose are willing to abandon their claims in the manner hereinafter appearing.

NOW, This Deed Witnesseth That It Is Hereby Agreed As Follows:

1.

2.

IN WITNESS Whereof, the parties have hereunto set and subscribed their respective hands, the day, month and year first above written.

Signed and delivered by the Withinnamed  A

Witnesses

1.

2.

Signed and delivered by the Withinnamed B""",
"Format for Agreement for compromise between the employer and workman for payment of compensation under workmen's compensation act":"""Draft of Agreement for Compromise between the Employer and Workman for Payment of Compensation under Workmen's Compensation Act



This Agreement is made at __________ on this ______ day of ___________, 20___, between A B Co. Ltd., a company incorporated under the Companies Act,1956  or Companies Act, 2013, and having its registered office at ________________ hereinafter called "the Employer" (which expression shall unless repugnant to the context or meaning thereof include its successors and assigns) of the ONE PART and Shri X son of _________, resident of _______________ hereinafter called "the workman" (which expression shall unless repugnant to the context or meaning thereof, include his heirs, executors, administrators and assigns) of the Other Part.

Whereas the workman was employed by the employer in its factory in the capacity of ___________ and on ________ he was injured by an accident arising out of and in the course of his employment, in respect of which he claims that the employer is liable to pay him compensation under the Workmen's Compensation Act.

Whereas in order to avoid litigation in respect of the said claim, the parties hereto are desirous that the liability of the employer (if any), shall be satisfied by the compensation herein agreed to be made.

Now This Deed Witnesseth That It Is Hereby Agreed As Follows:

1.     The employer shall pay the workman the sum of Rs. __________ as compensation for such injury as aforesaid on __________.

2.     The employer shall also pay the workman the sum of Rs. _________in respect of the costs of his medical attendance and other expenses.

3.     The workman shall accept the before mentioned payments in full

discharge of all liability of the employer to pay compensation under the Workmen's Compensation Act or any law for the time being in force and doth hereby release the employer from any and all liability in respect of the injury caused to the workman and from any and all liability for any damages, which may result to the said workman in future on account of the said injury.

in witness whereof, the employer hereto has set its hands and seal and the workman has set his hands hereunto and to a duplicate hereof, the day and the year first hereinabove written.

The common seal of ABC Co. Ltd. has been

hereunto affixed pursuant to the Resolution of

its Board of Directors dated the _____ day of

__________, 20___, in the presence of S/Shri

______________ and _________________

Directors who have signed in token thereof.

Signed and delivered by A, the withinamed workman

WITNESSES;

1.

2.""",
"Format for Affidavit and Indemnity":"""DRAFT OF  AFFIDAVIT AND INDEMNITY



BY____________________

FAVOUR OF____________________

I, _______________ aged __ years, do hereby solemnly declare and say as follows:-

1. That I am employed with____________________. (Hereinafter referred to as "the bank").

2. That the Bank has presently taken residential premises being Situated at ______________ known as _________________(hereinafter referred to as "the said premises") situated at________________from _______________ on leave and license basis for the purpose of providing residential accommodation for me and my immediate family members.

3.  At my request, the Bank has permitted me to use the premises as per terms and conditions of the Agreement dated __________________, as perquisite to my service.

4. I do hereby declare, agree and undertake that:-

5  I shall vacate the said premises on the expiry or earlier determination of the said leave and license agreement dated ___________________ .

I shall use the premises only for the purpose of residence of myself and I shall not part with the possession of the premises or any part thereof to any one else.

I shall not commit any breach of any of the terms and conditions of the Agreement under which the Company has taken possession of the premises.

I confirm that I am aware of the terms and conditions of the Agreement under which the company has acquired the said premises on leave and licence basis.

I confirm that on happening of any of the following events, _____________shall be at liberty to demand and take possession of the said premises and I shall indemnify and keep ________________ indemnified against any loss or damage which __________________ may suffer or incur due to my non-compliance, intentioned or otherwise, with any of the following:-

                              i.                For not vacating the premises on termination of my employment with the company for any reasons whatsoever (whether any retirement, resignation or otherwise).

                             ii.                For not vacating the premises on my services being transferred from...... to any place outside........

6. On my committing breach of any of the terms and conditions of the Agreement under which the company holds the premises.

7. I further declare that the undertaking and assurance given by me in paragraph 4(d) above is and shall be binding on my family, my heirs, administrators, executors and legal representatives and any person staying in the said premises at the time of my death.

8. In the event of my committing any breach of any of the terms and conditions under which I have been allowed to use the premises ______________ shall be entitled without prejudice to his other rights to take such legal action of proceedings against me including criminal proceedings as ______________________ may lawfully be advised.

9. This undertaking-cum-indemnity shall be binding on me till I am occupying the said premises.

10 I confirm that what has been stated hereinabove is true to my own knowledge and that on the basis of the declaration made by me herein ___________________has permitted the bank the use of the premises.

Solemnly declared by the aforesaid

On this ____ day of ___________, 20__

Sworn Before me,

Dated this ___ day of _____ 20__""",
"Format for Agreement for Sale":"""DRAFT OF AGREEMENT FOR SALE



THIS AGREEMENT FOR SALE is made and executed on this the____________ day _____________ of ___________, 200-

BETWEEN

Mr. ____________s/o. ____________ aged_________________ years residing at _____________Hereinafter called "The SELLER" (which expression shall mean and include her legal heirs, successors, successors-in-interest, executors, administrators, legal representatives, attorneys and assigns) of ONE PART.

AND

Mr. ______________ s /o __________ aged­ ________ years residing at__________ ___Hereinafter referred as "The PURCHASER" (represented by his power of attorney) which expression shall mean and include his heirs, successors, executors, administrators, legal representatives, attorneys and assigns of the OTHER PART.

WHEREAS THE SELLER is the absolute owner in possession and enjoyment of the more fully described in the schedule hereunder and hereafter called the "SCHEDULE PROPERTY.

WHEREAS the property more fully described in the schedule hereunder is the self acquired property of the SELLER who purchased the same from Mr._____________ in and by sale deed dated _____________ and registered as Doct No._________of Book 1 Volume No______________Page No_____to_________, registered on and filed on the file of the Sub-Registrar,

WHEREAS the SELLER is the absolute owner of the property and he has been enjoying the same with absolute right and he has clear and marketable title to the Schedule Property

WHEREAS the SELLER being in need of funds for the purpose of ________________ has decided to sell the property more fully described in the Schedule hereunder and the PURCHASER has offered to purchase the same..

WHEREAS the SELLER offered to sell and transfer the schedule property to the PURCHASER for a sale consideration of Rs.___________(Rupees___________ only) and the PURCHASER herein has agreed to purchase the same for the aforesaid consideration on the following terms and conditions:

NOW THIS AGREEMENT WITNESSETH AS FOLLOWS:

The Sale consideration of the Schedule Property is fixed at Rs. __________ (Rupees________ only).

The PURCHASER has paid a sum of Rs.­­­­­­­­­­­­­___________(Rupees _________ only) by cash/ cheque /D.D. bearing No _________ drawn on ___________ dated________ as advance, the receipt of which sum the SELLER hereby acknowledges.

The balance payment of Rs._____________(Rupees _________ only) will be paid by the PURCHASER to the SELLER at the time of execution of the absolute Sale Deed and thus completing the Sale transaction.

The parties herein covenant to complete the Sale transaction and to execute the Absolute Sale Deed by the end of

The SELLER confirms with the PURCHASER that he/she has not entered into any agreement for sale, mortgage or exchange whatsoever with any other person relating to the Schedule Property of this Agreement.

The SELLER hereby assures the PURCHASER and he/she has absolute power to convey the same and there are no encumbrances, liens, charges, Government dues, attachments, acquisition, or requisition, proceedings etc.

The SELLER agrees to put the PURCHASER in absolute and vacant possession of the schedule property after executing the sale deed and registering the same in the jurisdictional Sub-Registrar's office.

The SELLER covenants with the PURCHASER that he/she shall not do any act, deed or thing creating any charge, lien or encumbrance in respect of the schedule property during the subsistence of this Agreement.

The SELLER has specifically agreed and covenants with the PURCHASER that he/she shall do all acts, deeds and things which are necessary and requisite to convey absolute and marketable title in respect of the schedule property in favour of the PURCHASER or his nominee.

IT IS AGREED between the parties that all expenses towards Stamp Duty and Registration charges shall be borne by the PURCHASER only.

 The PURCHASER shall have the right to nominate or assign his right under this agreement to any person / persons of his choice and the SELLER shall execute the Sale Deed as per terms and conditions of this Agreement in favour of the PURCHASER or his nominee or assignee.

  The SELLER has agreed to get consent deed duly executed to this Sale transaction from his wife/her husband, sons and daughters on or before date of registration of Sale Deed and assured that they all join to execute sale deed in favour of the purchaser.

It is hereby expressly provided and agreed by the parties here to that both parties are entitled to enforce specific performance of the agreement against each other in case of breach of any conditions mentioned in this Agreement.

The original of the "AGREEMENT" signed by both the parties shall be with the PURCHASER and copy of the same similarly signed shall be with the SELLER.

SCHEDULE

IN WITNESS WHEREOF the SELLER and the PURCHASER have signed this Agreement of Sale on the day month and year herein above mentioned in the presence of the witnesses:

WITNESSES:

1.

2.

Signed by SELLER_____________

In presence of

Signed by PURCHASER______________

In presence of""",
"Format for Deed Of Guarantee":""" DRAFT OF DEED OF GUARANTEE



THIS DEED OF GUARANTEE executed on the day of Two Thousand:

BY:

(hereinafter referred to as the "FIRST PARTY", which expression shall, wherever the context so requires or admits, mean and include, his heirs, executors, administrators and assigns).

IN FAVOUR OF:

(Here in after referred to as the "SECOND PARTY", which expression shall, wherever the context so requires or admits, mean and include, its successors-in-title and assigns)

WITNESSES AS FOLLOWS:

I.  WHEREAS by an Agreement dated ........20___, the Second Party has arrived at an arrangement to contribute its effort and economic strength in the development being done by M/s.________________ of the PropertybearingNo.______________________________________________, in terms set out therein;

II. WHEREAS a copy of the said Agreement is hereto annexed and marked as Annexure 'A';

III. WHEREAS the First Party is one of the Partners/Directors of _________________________________ and apart from the assurances given by M/s._______________________________________ the First Party herein has agreed to personally guarantee the performance and returns estimated of M/s._______________________________________________ under the said Agreement, failing which the First Party will make good the amounts guaranteed hereunder and the Parties hereto are desirous of recording the terms of the guarantee;

IV. NOW THIS DEED OF GUARANTEE WITNESSES AS FOLLOWS:

1. In the premises aforesaid and at the request of the Second Party, the First Party hereby agrees with and guarantees the Second Party the payment assured to the Second Party under the Agreement dated....20___ by M/s._______________________________ and in the event of the Second Party not receiving the amounts in terms of the Agreement dated......20____, irrespective of any reasons from M/s._________________________________________ the First Party Mr.________________________ hereby irrevocably and unconditionally agrees and covenants to pay to the Second Party the amounts to be received by the Second Party in terms of the annexed Agreement or any part or parts thereof with interest thereon as aforesaid and as set out in the Agreement dated _____ 20___ between the Second Party and M/s.___________________ upon demand in that behalf being made by the Second Party;

  2.  The First Party further agrees as follows:-

a. A notice of demand issued by the Second Party or on its behalf stating that any of the sums under the annexed Agreement dated....20___ have become receivable, in terms of the said Agreement dated ....20__and that M/s.______________________________________________________ have failed or neglected in its assurances and failure of the Second Party receiving the said sum or any part thereof or any interest thereon as agreed, shall be conclusive and binding on the First Party as to that fact and without any further proof. The First Party shall make payment hereunder to the Second Party without any demur or default or without any recourse or reference to M/s.___________________________________ as the case may be.

b.The First Party further agrees to pay the amounts mentioned hereunder or any part thereof as the case may be, notwithstanding that there may be any dispute or difference between the Second Party and M/s________ as to whether or not the said sums under the Agreement dated...20__ or any part thereof and interest thereon as aforesaid or any part thereof has or has not become due and receivable by the Second Party;

c. The First Party agrees that this Guarantee is in addition to and without prejudice to the existing security offered by and on behalf of M/s._________________________________ to the Second Party and that all rights and remedies in respect thereof be reserved;

d. The First Party agrees that this guarantee shall be a continuing guarantee and shall not be considered as wholly or partially satisfied or exhausted by any part received by the Second Party or any settlement of account between the Second Party and M/s._____________________________.

e. The First Party agrees that this guarantee shall continue and be in force notwithstanding the discharge of M/s._____________________________________ by operation of any law or insolvency /bankruptcy/winding up/ dissolution of M/s._____________________________ and shall cease only on payment of amount guaranteed hereunder either by M/s._____________________________________ or the First Party herein;

f. The First Party shall have no right to the benefit of any other security that may be held by the Second Party until the Second Party receives all the amounts in respect of the monies and of all other claims under the said Agreement dated. ...20___ and on any account whatsoever arising out of the said Agreement dated ....20__ shall have been fully satisfied;

g. The First Party agrees that the Second Party under notice to the First Party, shall be at liberty to take other securities for the said monies due to the Second Party or any part thereof and to release or forbear to enforce all or any of the Second Party's remedies upon or under such securities and any collateral security or securities now held or be held by the Second Party and that no such release or forbearance as aforesaid shall have the effect of releasing the First Party from his liability or of prejudicing the Second Party's rights against the First Party under this Guarantee provided the notice mentioned herein above has been duly served on the First Party;

h. The First Party shall have no right to the benefit of any other security that may be held by the Second Party until the Second Party receives all the amounts in respect of the monies and of all other claims under the said Agreement dated.....20___ and on any account whatsoever arising out of the said Agreement dated ..... .20__ shall have been fully satisfied and in respect of the amounts from M/s.__________________________________, this Guarantee shall come to an end and in the event of the First Party paying under this Guarantee, the First Party shall be entitled to the security held by the Second Party at the time of total discharge;

 3. The First Party agrees that demand for payment under this Guarantee shall be deemed to have been given to the First Party if made in writing and delivered at his address hereunder written and if sent by post shall be deemed to have been received by the Second Party 24 hours after posting thereof and in proving such services it shall be sufficient to prove that the letter containing the demand was properly addressed and put into post;

NAME:. ________________

Address for Notice:

4. It is agreed that this Guarantee shall be enforceable notwithstanding any change in the name of the Second Party Company and it shall ensure for the benefit of any company with which the Second Party may become amalgamated or to which the Second Party may assign its rights;

5. It is agreed that this Guarantee shall remain in force until the performance assured by M/s.___________________ ___________________________________ under the Agreement dated....20__ have been fulfilled and complied in terms thereof;

6. The First Party agrees that it shall not be discharged or released from this Guarantee by any arrangement made between the Second Party and M/s. _____________________ notice to him in writing with regards to any additional security given by M/s. ____________________ and/or M/s __________________, or release of any security at present given or may be given in addition nor will the First Party be discharged or released from this Guarantee by any alterations in the obligations save and except the quantum and returns agreed to be paid by M/s. _______, to the Second Party undertaken by M/s.__________________ or by any forbearance or waiver by the Second Party whether as to payment, time of performance or otherwise under notice to the First Party in writing. The First Party agrees that the reasons for such notice as set out in this Para is only for information and not to seek consent of the First Party;

IN WITNESS WHEREOF, the FIRST PARTY has executed this DEED OF GUARANTEE in the presence of the Witnesses attesting hereunder:

WITNESSES:

1)

FIRST PARTY

2)""",
"Format for Retainership Agreement":"""DRAFT OF  RETAINERSHIP AGREEMENT



THIS AGREEMENT is made at Bombay this __________ day of ___________________ 20___ between _____________________________ Co-operative Housing Society Ltd., having its registered office at ______________________________________ hereinafter referred to as "the party of the first part" and ABC, a legal portal having its registered office at______________________, hereinafter referred to as "the party of the second part".

WHEREAS the party of the first part is a co-operative housing society and requires the assistance of solicitors and legal advisors for drafting notices to be issued to members of the society, correspondence with the Bombay Municipal Corporation/ Registrar of Society, giving advice and solutions to internal problems of the members of the society in accordance with the Co-operative Societies Act, 1960 and the bye-laws of the society, etc.

AND WHEREAS the party of the first part has offered to appoint and retain the party of the second part to act for them as legal advisors and solicitors and the party of the second part have agreed to the said appointment and retainer ship;

AND WHEREAS the parties hereto have agreed to record the terms and conditions on which the party of the first part has agreed to appoint and retain the party of the second part to act for them as legal advisors and solicitors and the party of the second part has agreed to accept the said appointment and retainer ship;

NOW IT IS HEREBY AGREED BY AND BETWEEN THE PARTIES HERETO AS FOLLOWS:

1.     The party of the first part hereby appoints and retains the party of the second part for drafting notices to be issued to members of the society, correspondence with the Bombay Municipal Corporation/ Registrar of Society, giving advice and solutions to internal problems of the members of the society in accordance with the Co-operative Societies Act, 1960 and the bye-laws of the society and all ancillary and incidental matters.

2.     The party of the first part shall pay to the party of the second part fees of Rs. (Rupees ------------only) per month. The said fees will be in lieu of and in satisfaction of all professional charges and expenses including the office expenses of the party of the second part but excluding any out of pocket expenses and costs incurred in relation to the assignment.

3.     The party of the first part shall also pay to the party of the second part all out of pocket expenses incurred by them in payment of traveling expenses, registration charges, etc. in respect of documents in relation to each transaction etc.

4.     The above fee quote is based on the assumption that there will be no material change in the scope. In the event of any material deviation in the foregoing assumption the parties hereto agree to re-assess and mutually revise the fee quote.

5.     Invoices will be raised by the party of the second part on a monthly basis and will be payable within 15 days. A detailed narrative stating the nature of the work done will accompany the invoice. The invoice shall also include details of any out of pocket expenses and costs incurred in relation to the assignment.

6.     The scope of the above services would not include any regulatory compliance (such as filings, etc. with statutory authorities, etc.), or providing substantive opinions or memoranda on any specific legal issue and the same will be charged separately.

7.     This agreement will not extend to any litigation civil or criminal or arbitration whether arising out of any transaction entrusted to the party of the second part or otherwise. If any such matter of litigation or any legal proceedings in a court of law or tribunal or arbitrator is entrusted to them, the party of the second part will be entitled to charge fees according to their usual practice.

8.     The party of the second part shall maintain full secrecy and shall not disclose any confidential matter or communication between the party of the first part and themselves to anybody else.

9.     The party of the second part shall not act in any matter entrusted to them for any other party concerned or connected with such matter.

10.  This agreement may be terminated by any party hereto by giving one month''s prior notice to the other without assigning reason and on the expiry of the said period from receipt of the notice this agreement shall stand terminated except in respect of matters which are already entrusted to the party of the second part and are not completed.

IN WITNESS WHEREOF the parties hereto have put their hands the day and year first hereinabove written.

Signed by the with in named)

______________ Co-operative)

Housing Society by its Secretary)

Mr. ___________________________)

In the presence of)

______________________________)

Signed by the with in named)

_________________________ ( retainers)

by its ( concerned authority)

Ms. ___________________________)

In the presence of)

______________________________)""",
"Format for Hire Purchase Agreement":"""DRAFT OF HIRE AND PURCHASE AGREEMENT



This Agreement is made at ... this ... day of ... between M/s. AB & Co. Ltd., a Company having registered office at ... hereinafter referred to as 'the Company' of the One Part and Mr.... of... hereinafter referred to as 'the Hirer' of the Other Part.

WHEREAS, the Company is the owner of certain machinery and equipment Intended for manufacturing ... and which is more particularly described In the Schedule hereunder written.

AND WHEREAS, the Hirer has requested the Company to give the said machinery and equipment on hire to enable the Hirer to carry on the business of manufacturing ... with an option to the Hirer to purchase the same.

AND WHEREAS, the Company has agreed to do so on the following terms and conditions agreed upon between the parties.

NOW, It Is Agreed by And Between The Parties As Follows:

1.     The Company agrees to give and deliver over to the Hirer the said machinery and equipment described in the Schedule hereunder written on hire on the terms and conditions hereinafter mentioned and pursuant to the said Agreement the Company has delivered possession of the said machinery and equipment to the Hirer.

2.     The Hirer confirms that he has inspected the said machinery and equipment before taking possession and is satisfied that it is In good and working condition and acknowledges delivery of the same to him by the Company and agrees to hold it on the terms and conditions hereinafter mentioned.

3.     The hire-purchase price of the said machinery and equipment fixed at Rs. ... exclusive of the deposit amount mentioned in the next clause and the cost price fixed at Rs. ... is accepted by both the parties hereto.

4.     The Hirer has paid to the Company on the execution of this agreement a sum of Rs. ... as deposit or earnest which will be adjusted against the hire purchase price of the said machinery and equipment, If the Hirer exercises the option to purchase the same as hereinafter mentioned. If the Hirer does not exercise the said option or the agreement is terminated before the exercise of such option then the said amount of deposit will be returned to the Hirer by the Company on the expiration or sooner determination of this agreement, subject to deduction of any claim which the Company may have against the Hirer under or by virtue of this agreement or in law, including the cost price of the said machinery and equipment.

5.     During the pendency of this agreement the Hirer shall pay to the Company by equal monthly installments a sum of Rs. ... as hire charges, in advance, the first of such payments to be made on the execution of this agreement and each subsequent monthly payment will be made on or before the ... day of such each succeeding month hereafter. The payment will be made at the registered office of the Company by cash only or by cheque in the name of the Company.

6.     If the Hirer fails to pay any monthly installment of hire charges on the due date thereof then the Hirer shall be liable to pay interest thereon at the rate of ....... per cent per annum from the date of default till payment thereof. This is however, without prejudice to the right of the Company to terminate this agreement for default in payment of the monthly Installments as hereinafter provided.

7.     During the pendency of this agreement the Hirer shall keep the said machinery and equipment in good working condition and shall maintain It properly as a man of prudence would do and shall replace any of the parts thereof lost or disused or out-of-use or broken.

8.     The Hirer agrees to indemnify and keep Indemnified the Company against any loss the Company may suffer due to any damage done to the said machinery and equipment by any reason whatsoever.

9.     The Company through its authorised representative shall be entitled to inspect the said machinery and equipment during working hours at any time and for that purpose to enter Into the premises where the said machinery and equipment will be installed or kept and the Hirer shall allow the Company and its representative to do so.

10.  The Company does not give any warranty as to the quality or fitness of the mechanism of the said machinery and equipment and will not be responsible or liable for any defect found therein.

11.  The Hirer proposes to install the said machinery and equipment at ....... and agrees and undertakes not to remove the same to any other place without the prior written consent of the Company. The Hirer shall not remove the nameplates fixed to the machinery for the purpose of identification of the property of the Company during the pendency of this agreement.

12.  The Hirer shall keep the said machinery and equipment insured in the name of the Company with any recognised Insurance Company and shall pay the premium as and when due and payable regularly. The Policy of Insurance will be handed over to the Company and the Hirer shall produce the premium receipt or furnish true or Xerox copy thereof to the Company from time to time. If the Hirer fails to insure the said machinery and equipment or fails to pay the premium at any time the Company will be entitled to insure (without prejudice to Its other rights under this agreement) the same or to pay the premium as the case may be and the costs incurred by the Company will be paid by the Hirer to the Company as and when demanded.

13.  The Hirer shall use the said machinery and equipment for the manufacture of and not for any other purpose without the prior consent of the Company.

14.  The Hirer shall not give the said machinery and equipment on hire or on any other basis or to allow it to be used by any other person without the prior written consent of the Company and shall not hypothecate or pledge the same with any person to secure payment of any moneys.

15.  The ownership or property of the Company in the said machinery and equipment will continue to remain unaffected during the pendency of this agreement and the Hirer shall be considered as the bailee thereof with all the-duties and obligations of a bailee in law, until the Hirer exercises his option to purchase hereinafter provided.

16.  If any taxes or other dues are required to be paid in respect of the said machinery and equipment, the same will be paid by the Hirer and if any permit or licence to use the said machinery and equipment is required to be obtained from any Government or any local authority the same will be obtained by the Hirer at his costs and responsibility.

17.  If the said machinery and equipment or any part thereof goes out of order and requires repairs of a substantial nature the work of repairs will be carried only through a mechanic appointed by the Company and the Hirer shall pay his charges.

18.  The Hirer shall be liable to pay the hire charges every month not- withstanding whether the said machinery and equipment is working or remains idle for want of work or for any other reason.

19.  This agreement shall be deemed to have commenced from the date hereof and will remain in force for a period of... years from the date hereof that is up to the day of ... and (unless the Hirer exercises the option to purchase as hereinafter provided), on the expiration of the said period or earlier termination thereof as hereinafter provided the Hirer shall hand over back the said machinery and equipment in good working condition subject to normal wear and tear at his costs at the place of business of the Company or as may be directed by the Company provided that, the Hirer shall continue to be liable to pay hire charges until the said machinery and equipment is actually delivered over to or taken over by the Company.

20.  If the Hirer commits breach of any term of this Agreement or fails to pay any two monthly installments of hire charges, the Company will have the right to terminate this agreement by giving one month's prior notice to that effect and unless in the meanwhile the breach is remedied and the hire charges are paid as the case may be. this agreement shall, on the expiration of the notice period stand terminated. If the agreement is terminated as aforesaid the Hirer's option to purchase as hereinafter mentioned shall stand forfeited or cancelled.

21.  If the Hirer is adjudged insolvent or he allows the said machinery and equipment to be attached in execution of a decree or an order of a court or for recovery of any Government dues or if a Receiver thereof is appointed by Court or any creditor, this agreement, on the happening of any such event shall stand terminated.

22.  The Hirer shall have also a right to terminate this agreement at any time by giving not less thin fourteen days' prior notice to the company to that effect but in such a case the Hirer will be liable to pay to the Company the amounts which have accrued due towards hire charges have not been paid and the amount of hire charges payable for the period from the date of termination till the stipulated period of this agreement would expire as and by way of compensation for the loss suffered by the Company, subject to the provisions of S. 10 (2) of the Hire Purchase Act.

23.  On the termination of this agreement by efflux of time or earlier termination by the Company or the Hirer or otherwise as aforesaid, the Company shall return to the Hirer the amount of deposit less the amounts payable by the Hirer to the Company for hire charges or otherwise and the expenses to be paid or Incurred by the Hirer in terms of these presents and not paid by him.

24.  If the said machinery and equipment is lost or wholly destroyed or damaged beyond repairs by fire, floods or earthquake or for any other reason, the Hirer shall make good the loss suffered by the Company, the loss being the market price of the machinery and equipment then existing or the hire-purchase price mentioned in clause (3) above, whichever is more, Provided that, the amount of Insurance claim received if any will be adjusted against such price.

25.  The Hirer shall have the option to purchase the said machinery and equipment, and the option shall be exercised by giving one month's prior notice to the Company. The option to purchase can be exercised from the date of expiration of the stipulated period of this agreement or from any earlier date. In the former case the Hirer shall be liable to pay to the Company a sum equal to the Hire purchase price of the machinery and equipment mentioned in Clause (3) above, less the aggregate amount of installments paid up to that date or Rupee one whichever is higher. In the latter case that is if the option to purchase is exercised before the expiration of the period of this agreement, the Hirer shall be liable to pay a sum equal to the said Hire-Purchase price or the balance thereof payable by monthly installments of hire charges up to the date of the stipulated period of the agreement as reduced by a rebate which will be equal to two third of an amount which bears to the hire purchase charges the same proportion as the balance of the hire purchase price not due till then bears to the hire purchase price.

26.  On the Hirer exercising the option and paying the price of the machinery and equipment and other moneys as mentioned in clause (25) above to the Company the sale of the said machinery and equipment to the Hirer shall be deemed to be complete as on the date the option comes into operation. But until then, the Company will continue to be the owner thereof. If, however, the Hirer fails to pay the amount due and payable to the Company as aforesaid at or before the date from which the option is to become effective, this agreement shall stand terminated and the Hirer will return the machinery and equipment to the Company forthwith in good working condition as aforesaid.

27.  Notwithstanding the completion of sale of the machinery and equipment, the Company shall have a lien or charge on the same for all the moneys due and payable by the Hirer under this Agreement.

28.  The Company declares that

a.     The Hirer shall have and enjoy quiet possession of the said machinery and equipment during the subsistence of this agreement.

b.    That the said machinery and equipment is free from any charge or encumbrance in favour of any third person.

c.     The Company has a right to sell the said machinery and equipment.

d.    The said machinery and equipment is new/second hand.

29.  The Hirer shall not assign the benefits and rights under this Agreement to any other person without the prior written consent of the Company which consent shall not be unreasonably withheld or refused.

30.  If on the determination of this agreement by efflux of time or otherwise, the Hirer fails to deliver the said machinery and equipment to the Company, without there being any dispute the Company will be entitled to file a suit or take other proceedings to recover possession thereof and the Hirer will be liable to pay all the costs, charges and expenses incurred by the Company, in that behalf subject to any order of the Court.

31.  If any dispute arises between the parties out of or in connection with the agreement whether in the nature of interpretation or meaning of any term hereof or as to any claim by one against the other, or otherwise the same shall be referred to arbitration of a common arbitrator if agreed upon. otherwise to two arbitrators one to be appointed by each party hereto and the arbitration shall be governed by the Arbitration Act, 1940.

THE SCHEDULE ABOVE REFERRED TO

(List /Description of machinery & equipment)

Signed and delivered for and

on behalf of M/s. A B & Co. Ltd., by Mr. ... a Director of the

Company duly authorised by a Resolution of the Board of Directors dated ...

in the presence of ...

Signed and delivered by the with in named Hirer Mr. in the presence of ...""",
"Format for Partnership Deed":"""DRAFT OF PARTNERSHIP AGREEMENT



This Deed of Partnership is made at.................... on this .................... day of ............... by and between: Shri ............................... aged about .............. years, son of Shri .................................. resident of ………………………………………… (Hereinafter to be called the First Party); Shri ............................... aged about ............... years, son of Shri .................................. resident of ………………………………………(Hereinafter to be called the Second Party); Shri ............................. aged about ................ years, son of Shri .................................. resident of (Hereinafter to be called the Third Party); Shri .......................... aged about ................. years, son of Shri .................................. resident of (Hereinafter to be called the Fourth Party);

WHEREAS, the parties to this deed have been carrying on the business of ....................................... under the name and style of M/s. ......................... with its principal place of business at ............. on the terms and conditions incorporated in the Partnership Deed executed on .........................................

AND WHEREAS, vital amendments have been made by the Finance Act, 1992 in the procedure for assessment of firm. Consequent to the said amendment, the parties to this deed had a meeting and have orally and mutually agreed to amend and alter some of the terms and conditions contained in the aforesaid partnership deed with effect from ____.

AND FURTHER WHEREAS the parties to this deed have been carrying on the above said business in partnership on the terms and conditions orally and mutually agreed amongst themselves as aforesaid;

AND NOW WHEREAS, the parties to this deed desire that the terms and conditions on which they have been carrying on the above said business in partnership since ...................... and propose to continue in future be reduced to writing to avoid future difficulties or misunderstanding.

NOW, THEREFORE THIS DEED WITNESSETH as under, incorporating the aforesaid amendment/ alteration in the terms and conditions of the partnership:

1.     That the partnership business has been and shall continue to be carried on under the name and style of M/s. ....................................

2.     That the partnership business has been and shall continue to be that of ................ with its principal place of business at .............. The parties by mutual consent may carry on business at such other place or places, in such other name or names and of such other nature or natures, as they may deem fit and proper from time to time.

3.     That the amount lying to the credit of the partners as on ______shall be deemed as their capital investment. Further capital, loans or deposits looking to the needs/requirements of the partnership firm shall be arranged, invested or contributed by the partners.

4.     That interest at the rate of __ per annum or as may be prescribed under section 40(b)(iv) of the Income-tax Act, 1961 or any other applicable provisions as may be in force in the income-tax assessment of the partnership firm for the relevant accounting period or at a lower rate as may be agreed to by and between the parties from time to time shall be paid to the partners or credited to the partners on the amount standing to the credit of the account of the partners.Such interest shall be considered as an expenditure of the firm and shall be debited to the Profit & Loss Account of the firm before arriving at the divisible profit or loss. The interest to persons other than partners shall be paid or credited to their accounts at the rate or rates as may be agreed to by and between the partners and such persons from time to time.

5.     That Shri ................................ Shri ..................... and Shri ............................ the parties of the ....................... parts have agreed to keep themselves actively engaged in conducting the affairs of the business of the partnership firm. The said partners shall be working partners. It is hereby agreed to that in consideration of the said parties keeping themselves actively engaged in the business of the partnership firm and working as working partners, shall be entitled to remuneration.

The remuneration payable to the said working partners shall be computed in the manner laid down or deduction under section 40(b)(v), read with Explanation 3 of the Income-tax Act, 1961 or any other applicable provision as may be in force in the income-tax assessment of the partnership firm for the relevant accounting year. Such amount of remuneration shall be distributed between the said working partners in the following proportion:

A. Shri ................................ ....... per cent of such amount

B. Shri ................................ ....... per cent of such amount

C. Shri ................................ ....... per cent of such amount

The partners shall be entitled to increase or reduce the above remuneration and may agree to pay remuneration to other working partner or partners as the case may be. The partners may also agree to revise the mode of calculating the above said remuneration as may be agreed to by and between the partners from time to time.

6.     That the parties hereto shall be true and faithful to each other and shall not do or cause to be done anything which may be detrimental to the interest of the firm.

7.     That the parties shall keep or cause to be kept proper books of account and documents and shall make entries therein of all receipts, payments and other matters as is usually done and entered in the books of account kept by persons engaged in business similar to that of the firm. Each partner shall have a right to have access to and to inspect and take copy of the same.

8.     That the partnership has been and shall be a partnership at will.

9.     That the net profit of the partnership firm after deduction of all expenses including rent, salaries, other establishment expenses, interest and remuneration payable to the partners in accordance with this deed of partnership or any supplementary deed as may be executed by the partners from time, to time, shall be divided and distributed amongst the partners in the following proportion:

Sr. No. Name of Party Share in profits

1.

2.

3.

4.

The losses, if any, including loss of capital suffered in any year shall also be apportioned in the above said proportion.

10.  That the bank account or accounts have been and shall be maintained in the name of the firm and shall be operated singly or jointly by the partners.

11.  That the books of account shall be closed on 31st day of March each year. The net profit or loss after deducting all expenses, interest, remuneration, outgoings shall be divided between the parties in proportion to the sharing ratio referred to hereinabove.

12.  That notwithstanding anything contained in the Indian Partnership Act it is hereby mutually agreed to by and between the parties that in case of death of any one or more partners, the firm shall not be dissolved but shall continue to be carried on by and between the surviving partners and legal heirs and/or representatives of the deceased partner, as a continuing concern, on the same terms and conditions as incorporated in this Deed or on such terms and conditions as may be agreed to by and between them from time to time. It is hereby further clarified that it shall be deemed as change in constitution and not succession.

13.  That with respect to any matter connected with the affairs of the firm, which is not specifically provided for herein, the partners may make such agreements therefor and may set in such manner with regard thereto as may be agreed upon by and between themselves.

14.  That if the partners deem proper and in their interest, they may admit any other person or persons as partners on the terms and conditions as may be mutually agreed amongst themselves.

15.  That the partners to this deed are partners in their individual capacity/representing HUF styled as M/s. ..................................... The parties do not represent any other person.

16.  All bonds, bills, notes, bills of exchange, hundies or promissory notes or other securities given on behalf of the partnership (except cheques) shall be signed, endorsed, accepted or executed jointly by all the partners and any bond, bill, note, bill of exchange, etc. to which any partner may be a party contrary to this provision shall be deemed to have been on the personal account of such partner and he shall pay and discharge the same out of his own moneys and indemnify other partners and the firm against payment thereof and against all actions, proceedings, costs, charges, expenses, claims and demands in respect thereof.

17.  That the parties of ...................... part are not working partners but are only financing, dormant and sleeping partners. The parties of ....................... part need not be in charge of, responsible to the firm for the conduct of the business of the firm and need not take interest in day-to-day working and business of the partnership firm.

That the parties of the ............................ part shall not be liable to any criminal action for the business or working of the partnership firm or for the acts of the other partners or its employees or its representatives for and on behalf of or on account of the partnership firm or for the purposes of the partnership firm. The said partners shall not be liable for any liability, civil or criminal, against the partnership firm or other partners.

That the said partners shall not become and shall not be liable for any criminal action for any default or offence committed by other partners or employees or authorised representatives of the firm under the Income-tax Act, Customs Act, Foreign Exchange Regulation Act, Sales tax Laws or other Central or State Acts, laws, Rules or Regulations.

18.  That the partners shall be entitled to modify the above terms relating to remuneration, interest, etc. payable to partners by executing a supplementary deed and such deed when executed shall have effect unless otherwise provided from the first day of accounting period in which such supplementary deed is executed and the same shall form part of this deed of partnership.

19.  That all disputes and questions in ...................... connection with the partnership or this deed arising between the partners or between any one of them or their legal representatives and whether during or after the partnership, shall be referred to the arbitrator in accordance with the provisions of the Arbitration and Conciliation Act, 1996 then in force.

IN WITNESS WHEREOF the parties to this deed have set their hands on the day and year first above written and in the presence of:

First Party Second Party

Third Party Fourth Party

WITNESSES;

1.

2.""",
"Format for Legal Notice for Non-Payment of Salary":"""Legal Notice to a company for non-payment of salary and other interest and allowances



 

To,                                                                                                                                          Date:

 

XYZ. Company Private Limited

 

Through its Managing Director

 

Mr. ABC

 

Sir,

 

Under instruction and on behalf of my client Ms. A, Resident House No. 3/96, Gomti Nagar, I do hereby serve you with the following notice:-

 





That my client was appointed by your offer letter dated 20th November 2014 and the salary of my client was fixed at Rs. 25000 /- per month with respect to your offer letter dated 20th November 2014. But my client joined her duty on 20th December 2014 with you.




That my client did her duty diligently, regularly and with utmost punctuality and sincerity, and with full devotion by doing manual job with her own hands in accordance with the well-settled provisions of the law. You issued the offer letter in the name of my client and got printed the visiting cards also in the name of my client along with the Identity Card.




That on 4th October, 2015 when my client went to attend her duty then your office abruptly refused to allow to my client to attend her duty and told that services of my client are no more required by your office and thus the services of my client have been terminated by you in a most illegal and unlawful manner without any reasonable rhyme and cause. At the time of termination of the services of my client, you did not pay the salary for the month of August and 15 days salary for the month of September which comes to Rs. 37,500/- to my said client.




That my client visited your office from 9 a.m. to 4 p.m. from time to time and spent a huge amount of Rs. 4500/- on the charges of traveling but you refused to pay and also the amount of Rs. 10,000- my client spend while doing field work for your company. Lastly on 7th December, 2015 you clearly refused to pay the salary amount of Rs. 37500/- to my client along with traveling charges and amount spend on field work.




That you did not provide me statutory benefits i.e. Providential Fund. etc. You also did not pay amount of bonus and other service benefits which totally comes to Rs. 28000/-





I, therefore, call upon you through this Notice, to make the payment of the Rs. 80,000/- to my client along with interest up to date, under intimation to me, within the period of 15 days, failing which my client has given clear instructions to me to file criminal as well as civil suit and Suit for Recovery in the competent court of law and in that event you will be fully responsible for all costs, risks, responsibilities, expenses and consequences thereof. Please note well.

 

A copy of this Notice is kept in my office for record and further necessary action and you are also advised to keep the copy safe as you would be asked to produce in the court.

 

Advocate""",
"Format for Anticipatory Bail Petition Application Format (Sessions Court & High Court)":"""BEFORE THE HIGH COURT AT __________________________________



 

IN THE MATTER OF:

STATE

VS

_____________________

(FIR Number: _________)

Under Section: (_____________________)

Police Station: (______________________)

 



APPLICATION U/S 438 CRPC FOR GRANT OF ANTICIPATORY BAIL ON BEHALF OF THE ACCUSED (name of the applicant of the bail)



 

MOST RESPECTFULLY SUBMITTED AS UNDER:

 

1. That the present FIR has been registered on false and bogus facts. The facts stated in the FIR are fabricated, concocted and without any basis.

 

2. That the police has falsely implicated the applicant in the present case, the applicant is a respectable citizen of the society and is not involved in any criminal case.

 

3. That the facts stated in the complainant against the applicant are civil disputes and does not constitute any criminal offense at all.

 

4. That the applicant is not required in any kind of investigation nor any kind of custodial interrogation is required.

 

5. That the applicant is having very good antecedents, he belongs to a good family and there is no criminal case pending against them.

 

6. That the applicant is a permanent resident and there are no chances of his absconding from the course of justice.

 

7. That the applicant undertakes to present himself before the police/court as and when directed.

 

8. That the applicant undertakes that he will not, directly or indirectly make any inducement, threat or promise to any person acquainted with the facts of the case so as to dissuade him from disclosing such facts to the Court or to any police officer.

 

9. That the applicant further undertakes not to tamper with the evidence or the witnesses in any manner.

 

10. That the applicant shall not leave India without the previous permission of the Court.

 

11. That the applicant is ready and willing to accept any other conditions as may be imposed by the Court or the police in connection with the case.

 

12. That the Court below has failed to consider all the facts and circumstances of the case and has wrongly dismissed the anticipatory bail application.

 



PRAYER



It is therefore prayed that the court may direct the release the applicant on bail in the event of his arrest by the police.

 

Any other order which the court may deem fit and proper in the facts and circumstances of the case may be also passed in favor of the applicant.

 

APPLICANT

 

THROUGH

 

COUNSEL""",
"Format for Deed of family settlement for division of properties left by a deceased between son and daughters where son pays money to daughters":"""Draft of Deed of Family Settlement for Division of Properties Left by a Deceased Between Son and Daughters Where Son Pays Money to Daughters



This Deed of family arrangement is made at ........ on this ............ day of ..……...., 20___, between A son of Shri .............. resident of .......... (hereinafter called the FIRST PARTY) and Smt. B wife of Shri ........... resident of .......... (hereinafter called the Second Party ) and Smt. C wife of Shri .............. resident of ........... (hereinafter called the Third Party) and Shri D ........ son of ....... resident of ........ (hereinafter called the Fourth Party).

WHEREAS by his will dated ............ E son of late Shri .......... resident of ................. appointed the fourth party as the executors thereof and gave his movable and immovable assets unto his children the first party, second party and the third party in equal shares.

WHEREAS The said E died on ............ and the executors obtained the probate of the said will from the .............. District Court on ..............

WHEREAS the executor has paid the funeral and testamentary expenses of the testator and all his debts which have come to his knowledge out of the estate of the testator.

WHEREAS The estate of the said E now in the hands of the executors consists of the immovable property described in the First Schedule hereunder written and the investments, particulars whereof are  described in the Second and Third Schedules hereunder written respectively.

WHEREAS, the parties hereto of the first three parts are desirous that the first party shall receive the immovable property and the second party shall receive the investments specified in the Second Schedule hereunder written and that the third party shall receive the investments specified in the Third Schedule hereunder written as absolute owners.

NOW, This Deed Witnesseth As Follows:

1.     The first party shall pay to each of the second and third parties, the sum of Rs. .......…….

2.     On the making of payment as aforesaid, the executors shall assent to the vesting of the immovable property described in the First Schedule hereunder written in the first party as absolute owners.

3.     The executors shall transfer the investment specified in Second and Third Schedules to the second and third parties respectively and they will become the absolute owners of the said investments.

4.     It is expressly agreed by and between the parties hereto of the first three parts that they shall not claim any rights under the said will, save as hereinabove provided and they shall release and indemnity the executor from and against all actions, proceedings, claims and demands in respect of the assent and transfers hereinbefore agreed to be made.

In WITNESS Whereof the parties hereto have set and subscribed their hands to this writing, the day and year first hereinabove written.

The First Schedule above referred to;

(Description of immovable property)

The Second Schedule above referred to;

(Particulars of investments to be transferred to second party)

The Third Schedule above referred to;

(Particulars of investments to be transferred to third party)

Signed and delivered by the within named first party

Signed and delivered by the within named second party

Signed and delivered by the within named third party

Signed and delivered by the within named fourth party

Witnesses;

1.

2.                                                            """,
"Format for Separation Agreement between Husband and Wife":"""DRAFT OF SEPERATION AGREEMENT BETWEEN A HUSBAND AND WIFE



THIS AGREEMENT made at.......... on this.......... day of...............20___, between A, son of B, resident of........... (Hereinafter called "the husband") of the ONE PART and Mrs. A his wife (hereinafter called "the wife") of the OTHER PART.

WHEREAS the husband and wife are living separately due to differences and disputes having arisen between them; and

AND WHEREAS they want to live separate, apart from each other and intend to live separate at all times hereafter unless there is any reconciliation.

NOW THIS AGREEMENT WITNESSETH THAT:

1.     The parties shall live separately and apart from each other and no party shall have any right, authority over the other or shall institute any legal proceeding for restitution of conjugal rights or otherwise.

2.     The husband shall during the life time of the wife pay to her a sum of Rs............ p.m. for her maintenance and the maintenance of the children. However, if the wife does not lead a chaste life, the husband shall be entitled to stop the payment of maintenance allowance after giving her notice.

3.     The wife shall be entitled to the custody and guardianship of the children of the marriage, namely C and D now aged........ Years and.......... years, respectively. The wife shall maintain and educate the said children until they shall respectively attain the age of majority. The husband shall not be liable for any claim or demands of the children and the wife shall keep the husband indemnified from and against all claims and demands in respect of such children.

4.     The wife shall pay for and discharge all liabilities or debts incurred by her after the date of these presents, whether for maintenance, support or otherwise and the husband shall not be liable for the same. The wife indemnifies and keeps indemnified the husband against all claims, actions and demands on that account and if the husband has to pay any sum on account of the liabilities of debts incurred by the wife, he is entitled to deduct the same from the amount payable to the wife under this agreement.

5.     The wife may remove all her wearing apparel, jewelry and other personal effects, etc. belonging to her from the husband's place and retain the said goods as her separate properly.

6.     The husband may have the access to the children at every Sunday between ___A.M. to ___ P.M. He may have the sole society of the children in the said timings on the said day.

7.     Notwithstanding anything contained in this agreement, it is expressly agreed that if at any time hereafter, the parties live together as husband and wife with mutual consent, then in that case, the said sum payable to the wife-under this agreement shall no longer be payable and the agreements hereinabove contained shall become void.

8.     This agreement shall be revoked by the death of either the husband or wife.

9.     This agreement shall be executed in duplicate. The original shall be retained by the husband and duplicate by the wife.

IN WITNESS WHEREOF, the parties have set their respective hands to these presents and a duplicate hereof on the day and year first hereinabove written.

Signed and delivered by the within named husband Mr. A.

Signed and delivered by the within named wife Mrs. C

WITNESSES;

1.

2.""",
"Format for Deed of Adoption":"""DRAFT OF DEED OF ADOPTION



THIS DEED OF ADOPTION is made and entered into at ____ this ____ day of ______,20___BETWEEN MR.A N, Adult, Indian Inhabitant of ____, residing at_______, hereinafter referred to as the 'ADOPTIVE FATHER' (which term and expression shall unless it be repugnant to the context or meaning thereof shall mean and include his heirs, executors, administrators and assigns) of the ONE PART and MRS. B N, Adult, Indian Inhabitant of___, residing at _____________________,-, hereinafter referred to as the 'NATURAL MOTHER' (which term and expression shall unless it be repugnant to the context or meaning thereof shall mean and include her heirs. executors, administrators and assigns) of the SECOND PART and MASTER AD, a Minor, through her Natural Mother and Guardian, Mrs. B N, the Party of the Second Part herein, hereinafter referred to as the 'Adopted Son' of the THIRD PART.

WHEREAS the Party of the Second Part herein had married S R on at____ and after marrying Mr. S R, her name was Mrs. B R, hereinafter for the sake of brevity referred to as the 'Said Marriage'.

AND WHEREAS out of the Said Marriage, there has been a issue i.e. a Male Boy namely, "AD", born on___________, hereinafter for the sake of brevity referred to as the Said Boy.

AND WHEREAS due to their difference of opinion the Party of the Second Part and her the then husband i.e. Shri S. R preferred a Petition No. AA___/___for Divorce by Mutual Consent in the Family Court at ______ and the Honorable Court was pleased the dissolve the Said Marriage vide their order passed below Exh. 6 on ___________besides awarding the permanent custody of the Said Boy to the Party of the Second Part herein, hereinafter for the sake of brevity referred to as the 'Said Order'

AND WHEREAS Mr. S R the Ex-Husband of the Party of the Second Part herein did not prefer any Appeal and/or revision against the Said Order and Judgment.

AND WHEREAS the Party of the First Part herein has married the Party of the Second Part herein and have registered their marriage at the office of the Sub-Registrar of Assurances (Marriage Officer),___vide Their Receipt No.______/_______ dated__________, hereinafter for the sake of brevity referred to as the 'Said Second Marriage'.

AND WHEREAS the Party of the First Part has married the Party of the Second Part herein, has decided to Adopt the Party of the Third Part herein as he is issueless and has married the natural mother of the Said Boy.

AND WHEREAS the natural mother (the Party of the Second Part herein) consented for the said adoption and on ______________ the physical act of giving and taking of the boy in adoption was performed, namely the natural mother gave the third party in adoption and the adaptor took the boy as adopted son accompanied by performance of Datta Homam.

AND WHEREAS the parties considered it necessary and expedient that a Deed of Adoption be executed so as to be authentic record of the Adoption having already taken place.

NOW THEREFORE THIS INDENTURE WITNESSETH AS FOLLOWS;

1.     It is hereby declared that on _________ the party of the Second Part i.e. the Natural Mother of the Third Party gave in adoption her son "AD" to the Adopter who took the boy in Adoption. The Adopter took the boy in Adoption, the physical act of giving and taking was also accompanied by Datta Homam ceremony and in the presence of assembled brotherhood of the parties.

2.     As a result of the aforesaid adoption the Third Party was transferred legally from the Natural Mother to the Parties of the First and Second Part herein and Adopter became entitled to all the rights and obligations of his Adopted Son.

3.     The Adopted Boy by virtue of the Said Adoption has become member of the Coparcenary with his Adopted father and shall be entitled to inherit his self acquired property if indisposed of and shall be entitled to succeed to his Joint Ancestor's property by Survivorship except that if a legitimate son is born subsequent to his adoption, the right of inheritance of succession of the adopted son shall be regulated by Rule of the Hindu Law.

4.     The Adopter, first party, shall be responsible for the maintenance and education of the adopted son and agrees to bring him up according to his status in life.

5.     The Natural Father of the Said Boy having relinquished all his right, title, interest and claim over the said boy and Natural Mother having married the Party of the first part herein after her marriage having been dissolved by the Family Court,_____and being continue to remain as Natural Mother of the Said Boy, question of taking any consent from anybody does not arise at all.

6.     The Adopter shall not lay any claim hereinafter against the natural father for expenses incurred by him for the education and maintenance of the Said Boy/Adopted Son.

IN WITNESS WHEREOF the parties hereto have hereunto set and subscribed their respective hands to this on the day and year first hereinabove written

SIGNED, SEALED AND DELIVERED)

By the within-named Party of First Part)

In the presence of ____________________

SIGNED, SEALED AND DELIVERED)

By the within-named Party of Second Part)

In the presence of_________________ )

1)

2)

SIGNED, SEALED AND DELIVERED)

By the within-named Party of Third Part)

Through his Natural Mother

In the presence of_____________________)""",
"Format for Memorandum Recording Family Settlement":"""DRAFT OF MEMORANDUM RECORDING ORAL FAMILY SETTLEMENT



THIS MEMORANDUM RECORDING ORAL FAMILY SETTLEMENT is made at _________ this ________ day of ____________ between Shri ____________ an Indian inhabitant residing at __________ _________ _________ (hereinafter called "the Party of the First Part") of the FIRST PART, Shri ______________, an Indian inhabitant residing at _____________ _____________ (hereinafter called "the Party of the Second Part") of the SECOND PART and Shri _________, also an Indian inhabitant residing at ____________________________________ (hereinafter called "the Party of the Third Part") of the THIRD PART.

and reference to the parties hereto shall, unless repugnant to the context or meaning thereof mean and include their respective successors and assigns.

WHEREAS:-

1.     The parties hereto are related to each other, the party of the first part being the ____________ of the party of the Second Part etc;

2.     Serious disputes and differences have arisen between the parties hereto, relating to ___________, and which have disrupted the peace and harmony of the family and affected the business and family relations and threatened to resort to litigation;

3.     With the object of resolving the aforesaid disputes arising out of the conflicting claims made by the parties hereto as stated above and for effectuating a permanent solution of all the outstanding disputes once and for settlement was arrived at for ensuring family peace and harmony after considering what was best in the interest of the parties and in expectation that the settlement would result in achieving amity and goodwill among the Parties and it was agreed that the parties and it was agreed that the settlement arrived at would be final and binding upon all the parties hereto and avoid any further disputes and or differences amongst the parties hereto.

4.     The parties hereto, have come to a settlement after the aforesaid discussion with the help of mutual friends to resolve the disputes and differences, and a memorandum of settlement with certain terms and conditions was drawn with a view to avoid any future disputes and or differences amongst the parties hereto and that this memorandum has been entered into to record the said terms and conditions of the Family Settlement already agreed upon by the parties hereto.

NOW THEREFORE THIS MEMORANDUM OF FAMILY SETTLEMENT WITNESSETH THE SAID TERMS AND CONDITIONS AS FOLLOWS:

1.     In pursuance of the said agreement and in consideration of the premises, the parties hereto agree that the Party of the Third Part shall apply to the Court for grant of letters of administration with the will annexed of the estate of the late ___________, the deceased.

2.     Without prejudice to their right to get their shares in the estate of the deceased as hereinafter fixed and agreed to by the parties hereto, the heirs shall give their letters of consent to the Party of the Third Part for obtaining the letters of administration as aforesaid.

3.     In consideration of the premises, the Party of the Third Part shall immediately after the letters of administration have been obtained grant, deliver and transfer one-third of the said properties and assets (after setting apart a sum of Rs. ___________/- for discharging the liabilities of the late _____________ and also to meet the expenses for the grant of letters of administration in favour of the Party of the Third Part.) to each of the said heirs and retain the remaining one-third for himself.

4.     An inventory of the assets of the deceased and of the respective agreed values thereof, is listed in Part I of the annexure B, hereto. A list of the debts due and owing by the estate of the deceased is listed in Part II of the said Annexure B hereto. An estimated sum of Rs______ has been taken into consideration and set apart by the Parties in a separate Savings Bank Account no. with __________ Bank, _____________ Branch, towards the expenses of obtaining the Probate / Letters of Administration with the will annexed and the transfer / distribution of the estate of the deceased in accordance herewith and the said sum shall be utilized by the parties hereto, accordingly. In case of any deficit in meeting the debts of the deceased and/ or the expenses of proving the Will and distribution of the estate, the parties hereto, shall contribute equally to such deficit.

5.     After setting apart sums to meet the debts of the deceased and the estimated expenses of distribution of the estate, The assets allotted to the said the Party of the First Part pursuant to the Family Settlement arrived at are more particularly described in the First Schedule hereunder written. Similarly, The assets allotted to the said the Party of the Second Part pursuant to the Family Settlement arrived at are more particularly described in the Second Schedule hereunder written. The assets allotted to the Party of the Third Part pursuant to the Family Settlement arrived at are more particularly described in the Third Schedule hereunder written.

6.     All expenses of and incidental to the grant of letters of administration as also of transfer of the shares to the respective parties hereto shall come out of the estate of the deceased.

7.     It is expressly agreed by and between the parties hereto that the heirs shall not claim any rights under the said codicil and the Party of the Third Part shall not, after obtaining the letters of administration with the will annexed, claim any rights under the said will, save as hereinbefore provided.

8.     The parties hereto confirm and declare that all the disputes and differences between them are settled and that none of the parties has any further or other claim or demand of any nature whatsoever against the other or others of them.

9.     The parties hereto expressly agree and declare that they have arrived at this Family Arrangement in order to put an end to existing and future disputes between the parties and with a view to bring about amity and goodwill amongst them and with a view to maintaining peace and bring about harmony in the family. The parties hereto further agree and declare that the terms of the Memorandum of Family Settlement arrived at between them and recorded herein are fair and bona fide and in the interest of all the parties.

10.  The parties hereto shall sign and execute or cause to be signed and executed all such documents, deeds, writing and/or instructions as may be necessary to give effect to the Family Arrangement arrived at amongst the parties hereto. On ___________ and which is recorded in this Memorandum of Family Arrangement-cum-Compromise.

Annexure 'A'

(Copy to the Will)

Annexure 'B'

Part I:List of assets of the deceased and estimated agreed values

Thereof.

The first schedule hereinabove referred to

(The assets allotted to the said the Party of the First Part)

Part IV: List of Debts of the Deceased.

The Second schedule hereinabove referred to

(The assts allotted to the said the Party of the Second Part)

The third schedule hereinabove referred to

(The assets allotted to the said the Party of the Third Part)

IN WITNESSES WHEREOF the parties hereto have hereunto set and subscribed their respective hands the day and year first hereinabove written.

SIGNED AND DELIVERED by }

the Party of the First Part }

Shri.......................... }

in the presence of ___________ }

SIGNED AND DELIVERED by }

the Party of the Second Part }

Shri.......................... }

in the presence of ___________ }

SIGNED AND DELIVERED by }

the Party of the Third Part }

Shri......................... }

in the presence of ____________ }""",
"Format for Partition Deed":"""DRAFT OF PARTITION



THIS DEED OF PARTITION made at (city) this ___ day of __________, 20__,BETWEEN Mr. _____________,s/o____________, R/o ____________________________ Hereinafter called First Party of the First Part, Shri ____________,s/o_______________, R/o ____________________, hereinafter called Party of the Second Part, (3) Mr. __________s/o________________, r/o_______________________, hereinafter called Party of the Third Part

WHEREAS Shri ___________ is the Karta and Manager of the joint and undivided Hindu family, carrying on the activities under the name and style of "______________________" (hereinafter referred to as "the said ___", consisting of the said ___________, his wife, the said __________, and the said ____).

AND WHEREAS the said _______ owned and possessed immediately before the partition one telephones Nos. ________and _______, __ shares in ________ Ltd. Bank balance of Rs._______ with ________, _________, _____________ Bank The HUF had also incurred certain liabilities.

AND WHEREAS the parties hereto have agreed on the ___ day of _____ to have a total partition all the assets held by the said HUF on such partition:-

___ Shares of _____________ Ltd. Rs. _______/-

___ Shares of _____________ Ltd. Rs. _______/-

Total Rs.________/-

The above-named shares will be transferred to ________ on receipt of Rs.________/-

AND WHEREAS the net capital of the said HUF immediately before the full partition is Rs.________ consisting of Rs._______ as bank balance and Rs.____/-

AND WHEREAS the parties hereto are desirous of affecting the full partition of the said HUF by donating the entire amount to a charitable trust.

NOW THIS INDENTURE WITNESSETH AND IT IS HEREBY AGREED AND DECLARED BY and between the parties hereto as under:

1.     The parties hereto hereby declare that the said HUF has been fully partitioned on the ___ day of ______________.

2.     The parties hereto agree to donate the entire capital of Rs.______- held by the said ___ to ___ ____________ (a public charitable trust).

3.     The parties hereto agree to give further donation to _________________ as and when any refund is received from the income-tax department.

4.     The said ____ has been allotted telephone number _______.

IN WITNESS WHEREOF the parties hereto have set and subscribed their respective hands on the day and year first hereinabove written.

SIGNED SEALED AND DELIVERED by the within named

1.     ______________________

2.     ______________________

3.     ______________________

in the presence of............

WITNESSES:

1.

2.""",
"Format for Deed of Gift of Moveable Property/ Immovable Property":"""DRAFT OF DEED OF GIFT OF IMMOVABLE PROPERTY



This Deed Of Gift is made at ........ this ........ day of.. ..... between Mr. A of ....... hereinafter referred to as 'the Donor' of the One Part and Mr. B of ....... hereinafter referred to as 'the DONEE', of the Other Part.

WHEREAS the Donor is seized and possessed of the land and premises situated at ......... and more particularly described in the Schedule hereunder written.

AND WHEREAS the DONEE is related to the Donor as ........

AND WHEREAS the Donor desires to grant the said land and premises to the DONEE as gift in consideration of natural love and affection as hereinafter mentioned '

AND WHEREAS the DONEE has agreed to accept the gift as is evidenced by his executing these presents.

AND WHEREAS the market value of the said property his estimated to be Rs .....

NOW, this Deed Witnesseth that the Donor without any monetary consideration and in consideration of natural love and affection, which the Donor bears to the DONEE, doth hereby grant and transfer by way of gift the said land and premises situated at ..... and more particularly described in the Schedule hereunder written together with all and singular the buildings, and structures. thereon and all the things permanently attached thereto or standing thereon and all the liberties, privileges casements and advantages appurtenant thereto And all the estate, right, title, interest use, Inheritance, possession. benefit, claims and demand whatsoever of the Donor To Have And To Hold the same unto and to the use of the DONEE absolutely but subject to the payment of all taxes, rates, assessments, dues and duties now and hereafter chargeable thereon to the Government or Municipality or other Local Authority.

AND he the Donor doth hereby covenants with the DONEE;

a. That the Donor now has in himself, good right, full power and absolute authority to grant the said piece of land and other the premises hereby granted as gift in the manner aforesaid.

b. The DONEE may at all times hereafter peaceably and quietly enter upon have occupy, possess and enjoy the said piece of land and premises and receive the rents, Issues, and profits and rents thereof and every part thereof to and for his own use and benefit without any suit, lawful eviction, interruption, claim or demand whatsoever from or by the Donor or his heirs, executors, administrators and assigns or any person or persons lawfully claiming or to claim by, from, under or in trust for the Donor.

c.That the said land and premises are free and clear and freely and clearly and absolutely and forever released and discharged or otherwise by the Donor and well and sufficiently saved, kept harmless and Indemnified of and from and against all former and other estate, titles, charges and encumbrances whatsoever, had made, executed, occasioned or suffered by the Donor or by any other person or persons lawfully claiming or to claim by,from, under or in trust for the Donor.

d.And Further that the Donor and all persons having or lawfully claiming any estate or Interest whatsoever to the said land and premises or any part thereof from under or in trust for the Donor or his heirs, executors, administrators and assigns or any of them shall and will from time to time and at all times hereafter at the request and cost of the DONEE do and execute or cause to be done and executed all such further and other acts, deeds, things, conveyances and assurances in law whatsoever for better and more perfectly assuring the said land and premises and every part thereof unto and to the use of the DONEE in the manner aforesaid as by the DONEE, his heirs, executors, administrators and assigns or counsel in law shall be reasonably required.

IN WITNESS,WHEROF, the Donor as well as the DONEE (by way of acceptance of the said gift) have put their respective hands the day and year first hereinabove written.



THE SCHEDULE ABOVE REFERRED TO

Signed and Delivered by the withinnamed Donor ........ in the presence of .......

Signed by within named DONEE ........ In the presence of .......

1...............

2...............

 



 Draft of Deed of Gift of Moveable Property



I, Mr ............. residing at ............ do hereby make a gift of the ornaments and jewellery specified in the schedule hereinunder written to my daughter Miss ............ in consideration of natural love and affection on the occasion of her marriage.

SCHEDULE

SIGNED

DONOR

Witnesses.

1.............

2.............

Accepted

DONEE""",
"Format for General Power of Attorney (GPA)":"""Draft of General Power of Attorney



To All to Whom these presents shall come, I ........ of ......

WHEREAS, I am desirous of appointing some fit and proper person to look after all my immovable properties, business and other affairs and requested Mr. ...... of ........ (hereinafter called 'the Attorney') to act for me and manage and look after my affairs which the Attorney has consented to do

NOW KNOW YOU ALL AND THESE PRESENTS WITNESS that I, the said ... do hereby appoint the said ..... as my true and lawful Attorney with full power and authority to do and execute all acts, deeds, and things as hereinafter mentioned.

1.     To ask, receive and recover from all receivers, farmers, tenants and all other occupiers whatsoever whether holding under a written lease or agreement or otherwise, of my lands and buildings, all rents, arrears of rent, services. issues, profits, emoluments and sums of money now due owing and payable or at any time hereafter to become due, owing and payable in respect of the same in any manner whatsoever and also on non- payment thereof to take summary proceedings to distrain or distress according to law and to give notices to quit, and vacate and file suits and proceedings in ejectment and to recover rents and compensation for use and occupation and to make like and appropriate demands and take like and appropriate actions and proceedings against trespassers.

2.     To appoint any fit person to be steward, bailiff, receiver or servant for the management of my lands and premises and to recover rents thereof and the same or any of such stewards, bailiffs, receivers or servants at pleasure to remove and displace as the attorney shall think fit.

3.     To contract with any person for leasing for such period at such rent subject to such conditions as the attorney shall see fit, all or any of the said premises and any such person, to let into possession thereof and to accept surrenders of leases and for that purpose to make and execute any lease or grant or other lawful deed or instrument whatsoever which shall be necessary or proper in that behalf.

4.     To pay or allow all taxes, rates, assessments, charges. deductions, expenses and all other payments and outgoings whatsoever due and payable or to become due and payable for or on account of my said lands, estates and premises.

5.     To enter into and upon my lands and buildings and structures whatsoever and to view the state and defects for the reparation thereof and forthwith to give proper notices and directions for repairing the same and to let manage and Improve the same to the best advantage and to make or repair drains and roads thereon.

6.     To sell (either by public auction or private treaty) or exchange and convey transfer and assign any of my lands and buildings and other property for such consideration and subject to such covenants as the Attorney may think fit and to give receipts for all or any part of the purchase or other consideration money And the same or any of them with like power, to mortgage charge or encumber and also to deal with my immovable personal property or any part thereof as the Attorney may think fit for the purpose of paying off reducing consolidating, or making substitution for any existing or future mortgage. charge, encumbrance. hypothecation or pledge of the same or any part thereof as the Attorney shall think fit and in general to sanction any scheme for dealing with mortgages, charges hypothecations or pledges of any property or any part thereof as fully and effectually as I myself could have done.

7.     To purchase, take on lease or otherwise acquire such lands, houses, tenements and immovable property generally as the Attorney may think fit or desirable.

8.     To prepare a layout by sub-dividing any land into plots and obtain necessary approval of any local authority for the same if required.

9.     To develop any land or plot of land vacant or with any building or structure thereon by constructing new building or buildings thereon and on Flat ownership basis, to sell the flats and other premises therein on such terms as the Attorney may think fit and to transfer the land with such building to any co-operative housing society or company or on Apartment ownership basis and to execute necessary documents in that behalf.

10.  To enter into any development agreement with any developer or builder authorising him to develop any of my properties as mentioned above and to do and execute all acts and deeds as may be required to be done or executed.

11.  To sell or to concur in selling in private sale or In any other manner any of my stock, merchandise, goods, chattels and other effects, articles and things for such consideration and subject to such conditions as the Attorney may think fit and to receive the proceeds thereof and to give receipt for all, or any part of the sale proceeds or other consideration money.

12.  To pledge, hypothecate or charge or concur in pledging hypothecating or charging with, to or in favour of a Bank or Banks or any other financier body or Individual any personal or moveable properties, goods, chattels, merchandise, commodities, effects and things for such considerations and subject to such conditions as the Attorney may think fit and for that purpose to sign, execute and deliver all necessary instruments and deeds of mortgage, charge, hypothecation, pawn, pledge, lien and trust receipts and to receive the consideration money or otherwise for such pledge,pawn, hypothecation,charge, mortgage, lien and the like.

13.  Also to draw, make, sign, accept or endorse pledge, hypothecate or otherwise negotiate all or any foreign or Inland bills of exchange, hundi, cheques, orders for payment of money and promissory notes and to sign, seal, execute, deliver, endorse, accept, assign or transfer all mortgage deeds, bills of lading, delivery orders or other symbols or Andicia of or documents of title relating to goods or merchandise, policies of assurances, charter parties, ships certificates, bills of sale, securities of any Government, municipality or local authority wheresoever situate or other stocks, shares, debentures, mortgages, obligations, or other securities of any company or corporation whether commercial, municipal or otherwise and all and every other public or other securities, stocks or shares, foreign or otherwise and to deal with the same and to receive the proceeds thereof respectively.

14.  To purchase, take on hire, borrow or otherwise acquire machinery, tools, spare parts, raw materials, merchandise commodities, goods, wares, articles, effects and things and to deal in and with the same and to dispose of the same in such manner and for such consideration as the Attorney may think fit.

15.  To borrow any sum of money on such terms and with or without security as the Attorney may think fit for any of the purposes of these presents.

16.  To deposit any money which may come to his hands as such attorney with any banker,broker or other person and any of such money or any other money to which i am entitled which now or hereafter is or shall be deposited with any banker, broker or other person to withdraw and either employ as the Attorney shall think fit in the payment of any debts or the keeping down of interest payable by me or the creation of sinking fund for the liquidation of any charges or encumbrances affecting any moveable and immovable property or any part thereof or in or about any of the purpose mentioned in these presents or otherwise for my use and benefit or to invest in any such stocks, funds, shares or securities as the Attorney may think proper and to receive and give receipts for any Income or dividends arising from such investments and the same investments to vary or dispose of as the Attorney may think fit.

17.  To continue and or to open new, current and or overdraft accounts in my name with any Banks or Bankers and also to draw cheques and otherwise to operate upon any such accounts.

18.  To engage, employ and dismiss any agents, clerks, servants or other persons in and about the performance of the purposes of these presents as the Attorney shall think fit.

19.  To sell any of my present or future investments and for that purpose to employ and pay brokers and other agents in that behalf and to receive and give receipts for the purchase money payable in respect of such sales and to transfer any of my investments so sold to the purchaser or purchasers thereof or as he or they may direct and for these purposes to sign and execute all such contracts transfer deeds and other writings and do all such other acts as may be necessary for effectually transferring the same.

20.  To accept the transfer of any share, stocks, debentures stocks, annuities, bonds. obligations or other securities of whatever nature that may at any time be transferred to me.

21.  To attend, vote at and otherwise take part in all meetings held in connection with any company or corporation with which I am concerned as a member, shareholder or otherwise or In relation to any of my investments and to sign proxies for the purpose of voting thereat or for any other purpose connected therewith as freely as I myself could do.

22.  Out of any of my moneys in his hands or under his control to pay all calls that may be lawfully made upon me or other expenses that may be Incurred in relation to any of my Investments and to give security for payment of the same.

23.  To exercise all other rights and privileges and perform all other duties which now or hereafter may appertain to me as a holder of debentures or shares or stock in any company or corporation.

24.  To ask, demand, sue for. recover and receive from every person every body politic or corporate whom it shall or may concern all sums of money, rents, issues, profits, debts, dues, goods, wares,merchandise, chattels, effects and things of any nature or description whatsoever which now are or which at any time or times during the subsistence of these presents shall or may be or become due owing payable or belonging to me in or by any right, title, ways or means howsoever and upon receipt thereof or of any part thereof to make sign execute and deliver such receipts releases or other discharges for the same respectively as the Attorney shall think fit.

25.  To settle any account or reckoning whatsoever wherein i am now or at any time hereafter shall be in anywise interested or concerned with any person whomsoever and to pay or receive the balance thereof as the case may require.

26.  To receive every sum of money whatsoever which now is or at any time hereafter may be due arising or belonging to me upon or by virtue of any mortgage, charge, pledge hypothecation or other security whatsoever and on receipt thereof to make, sign. execute and give good and sufficient release or other discharges for the same and also to sign, execute, make and deliver all proper and sufficient reconveyances, releases and other assurances of the lands and premises which shall have been mortgaged or charged as security therefor and also to consent to any such alteration or modification of the nature or conditions of the said securities as the Attorney shall think fit.

27.  To compound with or make allowances to any person for or in respect of the aforesaid debts or any other debt or demand whatsoever which now is or shall or may at any time hereafter become due or payable to me and to make or receive any composition, dividend thereof or thereupon and to give receipts, releases or other discharges for the whole of the same debts, sums or demands or to settle compromise or submit to arbitration every such debt or demand and every other claim. right, matter or thing due to or concerning me as the Attorney shall think most advisable for my benefit and for that purpose enter into. make, sign, execute and deliver such bonds of arbitration or other deeds or instruments as are usual in like cases.

28.  To commence any suit, action or other proceedings In any Court of justice and before any public officer or Tribunal for the recovery or enforcement of any debt, sum of money, right, title, Interest, property matter or thing whatsoever now due or payable or to become due or payable or in anywise belonging to me by any means or on any account whatsoever and the same action, suit or proceedings to prosecute or discontinue or become non-suit therein If the Attorney shall see cause and also to take such other lawful ways and means including proceedings in execution. distress, distrain and the like for recovering or getting in any such sum of money or other thing whatsoever which shall by the attorney be conceived to be due owing, belonging or payable to me by any person whosoever and also to appoint any advocates, solicitors and legal advisers to prosecute or defend In the premises aforesaid or any of them as occasion may require And from time to time, them or any of them to remove and other or others to appoint In their place and to pay them such fees and remuneration as the Attorney shall think fit or be advised and for all or any of the purposes aforesaid to sign, execute, deliver. file all necessary vakalatnamas, war- rants to act, plaints, petitions, applications, defences, statements, ac- counts, declarations, affidavits, and other documents, papers and writings.

29.  To defend any suit or legal proceedings taken against me in any court of law and to do all acts and things as are mentioned above.

30.  To accept service of any writ of summons or other legal processes or notice in any suit or legal proceedings and any person to represent in such court civil or criminal, or revenue court or tribunal or before any officer or other Tribunal whatsoever.

31.  To make any declaration or affidavit in proof of any debt or debts due or claimed to be due to me in any proceedings taken or hereafter to be taken by or against any person firm or company under any Act or Ordinance for the time being in force for the relief or otherwise of insolvent debtors or the winding up of companies and to attend all meetings of creditors under any such proceedings and to propose, second or vote for or against any resolution at any such meeting and generally to act for me in all proceedings whether by way of bankruptcy or liquidation by arrangement or by composition which may be taken against or for the relief of any debtor as the Attorney shall think fit.

32.  To exercise any power and any duty vested in me whether solely or jointly with another or others as executor, administrator, trustee or in any other fiduciary capacity (including powers and trusts to sell or lease land or to receive and give good receipts for money) so far as such power or duty Is capable of being validity delegated.

33.  And also to appear before the Registrar or Sub - Registrar of any District or Sub-District appointed or to be appointed under any Act or law for the time being in force or otherwise for the registration of deeds, assurances, contracts or other Instruments and then and there or at any time thereafter to present and register or cause to be registered any deeds, assurances. contracts or other instruments In which i am or may be by the Attorney deemed to be Interested and to pay such fees as shall be necessary for the registration.

34.  To enter into, make, sign, seal, execute, deliver, acknowledge, perform all engagements, contracts, agreements, deeds, declarations, bonds, assurances and other documents, papers, writings and things that may be necessary or proper to be entered into, made signed, executed, delivered, acknowledged and performed for any of the purposes of these presents or to or in which I am or may be party or in any way Interested.

35.  To appear on my behalf and to represent my interest before the Income tax, Wealth-tax and Gift-tax and/or other Taxing Authorities in respect of my Income tax. Wealth-tax, Gift-tax, as also before any Tribunal, or Court.

36.  To sign on my behalf Income-tax, Wealth-tax and Gift-tax returns and to submit the same on my behalf to the respective Taxing Authorities,

37.  To sign, declare and affirm on my behalf all the applications, documents. declarations and affidavits as may be necessary for the purposes of the Income-tax, Wealth- tax and Gift -tax affairs and to submit and file the same with the respective Taxing Authorities, to file appeals and references as the Attorney may be advised and as he may deem fit and proper against the orders and decisions of the Income-tax, Wealth-tax and Gift-tax Authorities in respect of my assessment proceedings. to appoint on my behalf such Auditors, Accountants and Advocates as the said Attorney shall deem fit and proper for representing me before the Income-tax, Wealth-tax and Gift-tax and/or Taxing Authorities or any other Tribunal or Court in respect of the Income-tax, Wealth-tax and Gift-tax Assessments and to discharge them and appoint new Auditors, Accounts and Advocates as the case may be An their place, to compound, compromise and settle with the Income-tax, Wealth-tax and Gift-tax Authorities the orders and assessments made by them, to apply for time for payment and to apply for instalments for the payment of the amount assessed and to be paid by me to the Income-tax, Wealth-tax and Gift-tax or other Taxing Authorities, and to do all acts and- things regarding the said matters.

38.  And also for the better and more effectually doing, effecting and performing the several matters and things aforesaid to appoint from time to time or generally such person or persons as the Attorney may think fit as his substitute or substitutes to do, execute and perform all or any such matters and things as aforesaid and any such substitute or substitutes at pleasure to remove and to appoint another or other in his or their place.

39.  In general to do all other acts, deeds. Matters and things whatsoever in or about my estate, property and affairs or concur with persons jointly Interested with myself therein in doing all acts, deeds, matters and things herein either particularly or generally described as amply and effectually to all Intents and purpose as I could do in my own proper person if these presents had not been made.

AND I, the abovenamed ........... do hereby undertake to ratify whatever the Attorney or any substitute or agent appointed by him under the power In that behalf hereinbefore contained may lawfully do or cause to be done in and by virtue of these presents.

IN WITNESS WHEREOF I, the abovenamed ........... have hereunto set my hand this ........... day of. .......... in the .........

Signed, sealed and delivered by the withinnamed

in the presence of ..........""",
"Format for Revocation of the Power of Attorney":"""Draft of Revocation of the Power of Attorney



Let is be known to all men through these presents that I…………….s/o………………..r/o……………….do hereby remove and cancel all the powers and authorities given by me to Shri……….s/o……….r/o……….by virtue of a power of attorney dated……….

I further declare that all or any of the act done or executed by aforesaid Shri…………s/o………….r/o…………under or in pursuance of the aforesaid power of attorney dated…………shall not be deemed to be my acts nor done in my name or on my behalf, after the execution of this present deed.

IN WITNESS WHEREOF act……….""",
"Format for Irrevocable Power of Attorney":"""Draft of Irrevocable Power of Attorney



Know All Men by These Presents That We/ M/s………………a public/private ltd. Company incorporated under the Companies Act,____ with its registered office at…………….through Shri………….authorised by the Board of Directors of the Company vide Resolution dated or Constituted as a Sole/Proprietor ship Concern /Firm under the Indian Partnership Act, 1932 with its principal place of business at……………….through its partners/Namely Shri…………..having executed in favour of the Uttar Pradesh Financial Corporation a Statutory body incorporated under the State Financial Corporation an agreement a deed of hypothecation for Rs……..Rupees…………………………………..only and secured the repayment thereof by deposit of the Corporation empowering the corporation to execute a deed of mortgage in the form of an English Mortgage and have the same registered at the cost of the Company /Firm Concern if and wherever the Corporation find it advisable to do so during the pendency of the liability of the company firm concern to the corporation. Do hereby appoint the Corporation to be its attorney for its and in its name and on its behalf for otherwise for the Company/Firm/Concern for the purpose hereinafter mentioned.

To execute a mortgage in the form know as English Mortgage of the whole of the assets of the company/firm sole proprietor including and building machinery a electric fittings both present and future in favour of the corporation on terms and condition contained in the agreement and deed of hypothecation.

To sign the said deed of mortgage for and behalf of the Company/Firm concern and to have it registered with proper registering authority by admitting its execution and passing of consideration on behalf of the company/firm/concern and for the company/firm/concern.

And also execute and to do all such other acts and things as our said attorney shall deem fit for the purpose of securing the said repayment of the loan by the company /firm concern aforesaid.

To perform and obtain the Income-tax clearance certificate under Section 230-A (I) of Income-tax Act, for and on behalf of the borrower.

To apply and obtain the necessary permission/exemption under Urban Land Ceiling and Regulation Act, 1976 for and on behalf of the borrower, if necessary.

To perform the above functions either through himself for through lawfully constituted authority.

And the company/firm/concern hereby do agree to ratify and confirm whatever its said attorney shall do here under.

IN WITNESS WHEREOF, I/WE…………………………have hereunto set my/our hand(s) this………….day of…………..in the year ………...

(…………….)

(…………….)

Signature

THIS POWER OF ATTORNEY was this………..day of……… produced and executed before me and the within named………….who is ./are known to me has/have acknowledged it to be their/his act and execution.

SIGNATURE AND SEAL OF

THE PUBLIC NOTARY""",
"Format for Sample Letter to Builder for Delay in Handing Over the Possession":"""Date ______

To,

Builder/ Builder Company

Official Address

Contact Info

 

Sub: Delayed Possession of Unit no. ______

 

Dear Mr._________ (Authorized representative of the builder company),

This is to bring to your kind notice that I am the buyer of Unit no. _____ of your __________ (Project name) and it is of huge concern to me that I have not received any official communication from ________ (Builder Company) regarding the confirmed date of handing over of the possession of the said Unit.



I have signed the Buyer’s Agreement with ________ (Builder Company) on _______ (Date). It was a commitment by the company that possession will be handed over in ___ months. Thereafter, it was told that by the end of _______ (Extension date, if any), the possession will be given. However, the possession of the unit was never delivered even after the expiry of the extension date.



I am sorry to say but the company has failed to keep its commitment and has lost the customer's faith as it has delayed the possession of the said unit innumerable times and there seems to be no deadline to this project. I have paid 80% of the amount and paying interest on it every month to the bank which is causing me a substantial financial burden.



Kindly let me know the final date of delivery of possession of my unit or else I would have to resort to taking appropriate legal actions against the company on account of the delays caused by you.

Looking forward to a favorable reply.



Regards,

_________ (Sender’s Name)""",
"Format for Sample Gift Deed for gifting cash to son/daughter":"""GIFT DEED



 



This deed of gift made this ______ Day of __________(month) ____________ (year) between;

       Mr. __________________, Age ____years,

       Resident of _____________________

       (Hereinafter called the “Donor”) of the One part



        And,



        Mr/Miss ___________________, Age ____ years,

        Resident of __________________

        (Hereinafter called the “Donee”) of the other part.

 

Witnesseth as follows:





In consideration of natural love and affection being the son/daughter of Donor, the donor hereby assigns to the donee a sum of Rs._____________ (amount) to be held by the donee absolutely.




The possession of the Rs._____________(amount) vide cheque No. ________Drawn on _____________________ , _____________ Branch dated _/_/__ hereinabove donated unto the donee and has been physically handed over to the donee as absolute owner before execution of this Gift Deed.




The said gift of Rs.______________(amount) has been accepted by Mr/Miss ___________________________.




The donor from this date reserves no right or interest on the said sum hereby gifted which shall from this day be the sole and exclusive property of the donee.




 The property hereby gifted is the donor’s self-acquired property accumulated out of income earned and has full right and authority to dispose of the same in any manner he may think fit.





 

In witness whereof, the parties hereto have put their respective signatures on this deed of gift in presence of witnesses.

                         

                   

 

                         SIGNATURE, NAME AND                                                          Donor

                       ADDRESS OF THE WITNESS                                    ________________________

                        ______________________                                         (______________________)

                        ______________________

                        ______________________

                        ______________________                                         _________________________

                       _______________________                                      (__________________________)""",
"Format for Sample Gift Deed for Immovable Property":"""GIFT DEED (FORMAT)



 

_____________________, son of ________________, by faith Hindu, by Nationality Indian, by occupation – __________, residing at _______________________________________. (Donor includes successors-in-interest and assigns).



AND



__________________, son of ________________, by faith Hindu, by Nationality Indian, by occupation – __________, residing at ____________________. (Donee, includes successors-in-interest and assigns).



 

Now this Deed of gift witnesses as follows-





Subject matter of the gift







THE SUBJECT LAND: ALL THAT piece or parcel of land hereditaments and premises measuring _________________on ALL THAT piece or parcel of land hereditaments and premises measuring ______________ be the same a little more or less out of the total land _________________ situate and lying at and being Municipal Holding No. _________, Ward No. _____, within the limit of ________ Municipality and having Postal Address ____________.




The Structure: __________storied brick built dwelling ________(house/flat/building), having built up area of ____________ Square feet, be the same a little more or less, standing on the Subject Land (The Structure).




Other Rights: Easements and all other rights, liberties, privileges, and benefits appurtenant to the Subject Land and The Structure and all equipment, installations, fittings, fixtures, etc. in or about The Structure.

 







BACKGROUND:







Description of the Title: Chain of title is to be described in detail here.




Sale to Donor: By a Deed of Sale dated _______, registered in the Office of the Sub-Registrar, ________, in Book No. I, Volume No. ____, Pages __ to ___, Being No. ______ for the year __________ (Said Deed), said _______ (Name of the previous owner) sold the aforesaid plot of land measuring about __________________ more or less comprised in Dag No. ______ as aforesaid to the Donor hereto.




Ownership of the Donor: In the circumstances, the Donor hereto became the sole and absolute owner of ALL THAT piece or parcel of land measuring _______________ be the same a little more or less including the common passage situate and lying at ____________________ and comprised in _____________.




Construction by the Donor: Subsequently, the Donor constructed a _______ storied brick built dwelling (house/flat/building) on his acquired property as aforesaid in accordance with the building plan duly sanctioned by the appropriate authority.




Said Property: Thus the Donor has become the sole and absolute owner in respect of the land and the structure as referred above (Said Property). The Subject Property is the part and portion of the Said Property.

 







Representations and Warranties of the Donor:







Absolute Ownership: The Donor is the absolute owner of the Subject Property.




Right, Power and Authority to Sell: The Donor has good right, full power, absolute authority and indefeasible title to gift and/or alienate the Subject Property.




Free from Encumbrances: The Subject Property is free from all claims, demands, encumbrances, mortgages, charges, liens, attachments, lis pendens, uses, debutters, trusts, prohibitions, Income Tax Attachment, Financial Institution Charges and liabilities whatsoever or howsoever made or suffered by the Donor or any person claiming through the Donor and the title of the Donor to the Subject Property is free, clear and marketable.




No Prejudicial Act by the Donor: The Donor has not at any time done or executed or knowingly suffered or been party or privy to any act, deed, matter or thing whereby the Subject Property or any part thereof can or may be impeached, encumbered or affected in title.




No Personal Guarantee:  The Subject Property is not affected by or subject to any personal guarantee for securing any financial accommodation.




No Bar by Court Order: There is no order of the Court or any other statutory authority prohibiting the Donor from transferring and/or alienating the Subject Property or any part thereof.




Basic Understanding: The Donee is the _________(relationship) of the Donor and the Donor bears natural love and affection for the Donee. The Donor has expressed his desire of gifting the Subject Property in favour of the Donee and the Donee has agreed to accept such gift.

 







Terms of Gift







Salient terms: The gift of the Subject Property being affected by this Deed is:







Gift: A gift within the meaning of the Transfer of Property Act, 1882.




Absolute: Absolute, irreversible and forever.




Free from Encumbrances: Free from all encumbrances of any and every nature whatsoever including but not limited to lis pendens, attachments, liens, charges, mortgages, trusts, debutters, reversionary rights, residuary rights, claims and statutory prohibitions.




Other Rights:  Together with Easements and all other rights, liberties, privileges and benefits appurtenant to the Subject Property.

 




Miscellaneous







Delivery of Possession: Simultaneously with the execution of these presents khas, vacant and peaceful possession of the Subject Property is handed over by the Donor to the Donee  on _____________(Possession Date).




Outgoings:  All Municipal and other taxes, penalties, surcharge, outgoings, liabilities and levies on or relating to the Subject Property till the Possession Date, whether as yet demanded or not, shall be borne, paid and discharged by the Donor and thereafter that shall be borne, paid and discharged by the Donee.




Holding Possession: The Donor hereby covenant that the Donee shall and may, from time to time and at all times hereafter, peacefully and quietly enter into, hold, possess, use and enjoy the Subject Property and every part thereof and receive rents, issues and profits thereof and all other benefits, rights and properties hereby gifted or expressed or intended so to be unto and to the Donee, without any lawful eviction, hindrance, interruption, disturbance, claim or demand whatsoever from or by the Donor or any persons lawfully or equitably claiming any right or estate therein from under or in trust from the Donor.




Further Acts: The Donor hereby covenants that the Donor or any person claiming under him, shall and will from time to time and at all times hereafter, upon every request and at the cost of the Donee and/or successors-in-interest of the Donee, do and execute or cause to be done and executed all such acts, deeds and things for further or more perfectly assuring the title of the Donee to the Subject Property.




Production of Said Deed: As referred hereinbefore, the Said Deed and all other title documents in respect of the Said Property shall be lying with the custody of the Donor and unless prevented by fire or other unavoidable accidents from time to time and at all times hereinafter at like request and cost of the Donee, the Donor or his successors-in-interest will produce or cause to be produced the Said Deed and/or the said documents for reasonable requirement as may be required from time to time.




Assessment of Value for the purpose of Advalorem Stamp Duty: For the computation of stamp duty, the value of the Subject Property is assessed at Rs. _______________/- (Rupees ________) only.





 



Schedule above referred to

(Subject Property)

[Subject Matter of Gift]



 

Detail of the Subject Property with boundary description …………

The Plot is shown on the Plan annexed hereto





Execution and Delivery:





In Witness Whereof the Donor has executed and delivered this Deed of Gift on the day, month and year mentioned above.







 

 

                                                                                      (Donor)

 

I accept the Gift mentioned hereto with pleasure:

 

                                                                                      (Donee)

  

Witnesses:





Signature:_____________




Name:______________





 





Signature: _____________




Name:______________""",
"Format for Agreement of License between Trade Mark Owner and a Manufacturer":"""DRAFT OF AGREEMENT LICENSE BETWEEN TRADEMARK OWNER AND A MANUFACTURER



 AGREEMENT is made this _____________day of ________ between __________M/s ______________, a Company registered under the Companies Act,____, and having its registered office at ___________ hereinafter referred to as `the Licensor' of the One Part and Mr. ._________________carrying on business of ­­­­­­­­­­­­________________ Hereinafter referred has `the Licensee' of the Other Part

WHEREAS

1.     The Licensor is the proprietor of a trade mark more particularly described in the schedule hereunder written and which is duly registered under the Trade and Merchandise Marks Act 1958.

2.     The Licensor is manufacturing and selling the goods viz ____________________ under the said trade mark.

3.     The Licensee who is running a small scale industry has requested the Licensor to grant him a license to manufacture the said goods with the trade mark embossed or printed thereon as is being done by the Licensor and which the Licensor has agreed to do on the following terms and conditions agreed to between the parties hereto.

NOW IT IS AGREED BY AND BETWEEN THE PARTIES AS FOLLOWS:

1.     The Licensor hereby grants to the Licensee a license to manufacture the said goods as a job work by applying the said trade mark, particulars of which are described in the Schedule hereunder written.

2.     The Licensee agrees and undertakes that all of the said goods manufactured by the Licensee in his factory at ______________or elsewhere shall be sold to the Licensor and not to anybody else at the price of Rs __________per item or article. The Licensee undertakes to manufacture and supply to the Licensor a quantity of not less than _________________every month.

3.     The goods so manufactured with the said trade mark applied to them will be supplied and delivered by the Licensee to the Licensor at the latter s business premises at _______ at his own costs of transport.

4.     The price of the said goods so supplied will be paid by the Licensor against delivery after deducting there from the royalty payable by the Licensee to the Licensor as hereinafter provided.

5.     The Licensor shall have the right to reject any goods supplied if they are not as per specifications or quality which are made known to the Licensee and in the event of such rejection the Licensee shall take back the rejected goods from the Licensor's premises at his own costs and until such removal they will be at the risk of the Licensee. The Licensor agrees that during the subsistence of this agreement, the Licensor will not get the said goods manufactured from anybody else.

6.     The ownership of the said trademark will always remain with the Licensor and the Licensee will not pass off the said goods as if he is the owner of the said trademark.

7.     The Licensee will be at liberty to put a label or advertise that the said goods are manufactured by him but it will also be mentioned that the trade mark belongs to the Licensor and that the goods are manufactured for the benefit of the Licensor.

8.     In consideration of the Licensor allowing the Licensee to manufacture the said goods with the said trade mark the Licensee agrees to pay to the Licensor by way of royalty a sum equal to ______________per cent of the price of the goods at which they will be sold to the Licensor by the Licensee as aforesaid.

9.     The Licensee shall keep an account of the goods manufactured and sold to the Licensor and the price received by him and royalty paid in respect thereof and such account shall be open to inspection by the Licensor from time to time as may be required by the Licensor. The Licensor will also have the right to enter upon the premises of the Licensee where the goods are manufactured and to take inspection of the goods manufactured.

10.  This agreement will remain in force for a period of ______ years from the date hereof and on the expiration of the said period or earlier termination thereof as herein provided, the Licensee shall stop manufacturing the said goods under the said trade mark and all the goods till then manufactured and lying undelivered to the Licensor will be delivered to the Licensor in terms of this agreement as aforesaid.

11.  If the Licensee commits breach of any term of this agreement, the Licensor will be entitled to terminate this agreement by fifteen days prior notice in writing to the Licensee and on the expiration of the notice period, this agreement shall stand terminated unless in the mean while the breach complained of is remedied to the satisfaction of the Licensor.

12.  The Licensee may get himself registered as a registered user under the provisions of the Trade & Merchandise Marks Act 1958 subject to the terms of this agreement.

13.  If the Registrar of Trade Marks while registering the Licensee as a registered user puts any condition which is not acceptable to the Licensor, the Licensee will withdraw the application for registration or the Licensor will have the option to terminate this agreement.

14.  If any person is found by the Licensee to infringe the said trade mark either by passing off or otherwise, the Licensee will bring that fact to the notice of the Licensor to enable him to take necessary legal action against such person and in that event the Licensee will give all cooperation to the Licensor in prosecuting such action and all the costs thereof will be borne and paid by the parties hereto in equal shares.

15.  If the Licensee himself infringes the said trade mark by passing off or otherwise, then notwithstanding anything provided in clause 16 hereof it will be open to the Licensor to take legal action against him and in such case the Licensee will not be entitled to challenge the ownership of the Licensor in respect of the said trade mark.

16.  In the event of any dispute arising out of this agreement, the same will be referred to arbitration of a common Arbitrator if agreed upon or in the absence of such agreement, to two Arbitrators one to be appointed by each party hereto and the Arbitration will be governed by the Arbitration Act for the time being in force.

IN WITNESS WHEREOF the parties have put their respective hands the day and year first hereinabove written.

THE SCHEDULE ABOVE REFERRED TO

Signed and delivered for and on behalf of

Within named Licensor ____________Company

By its Managing Director

In the presence of _____________

 

Signed and delivered by the

Within named Licensee Mr.______________

In the presence of ____________""",
"Format for Agreement of License to Publish on Royalty Basis":"""DRAFT OF AGREEMENT OF LICENSE TO PUBLISH ON ROYALTY BASIS



Agreement is made at __________ this _________ day of _________ between Mr................r/o.......... Hereinafter referred to as `the Author' of the One Part and________________________ carrying on business at ______________ Hereinafter referred to as `the Publisher' of the Other Part

WHEREAS

1.     The Author has written a book on the subject of...................... and desires to publish the same.

2.     The Publisher has offered to publish the said book on the following terms and conditions, which are also agreed to by the Author.

NOW IT IS AGREED BETWEEN THE PARTIES HERETO AS FOLLOWS:

1.     The Publisher agrees to publish the said book entitled __________ within a period of __________months from the date hereof. The printing and publishing will be done by the Publisher at his own costs.

2.     The Author has delivered the manuscript of the book on the execution of this Agreement to the Publisher and the Publisher acknowledges receipt thereof.

3.     The Author grants to the Publisher the right to print and publish the said book subject to the terms and conditions herein contained.

4.     The Author hereby warrants that the said book does not infringe the copy right of any other person and he is the sole copyright owner of the said book. He also warrants that he has not given license to publish the said book to any other person. The Author agrees to indemnify the Publisher against any claim made by reason of infringement of copyright of any other person or by reason of the Author having given any right in respect of the book to any other person.

5.     The Publisher shall print and publish the book at his own entire costs and expenses and he will also advertise the publication of the work at his own cost.

6.     The Publisher shall, in consideration of the said right of publication hereby given, pay to the Author as and by way of royalty a sum equal to _________per cent of the price less the cost of printing of each copy of the book actually sold. The amount of royalty accrued on sales, shall be paid within __________weeks from the expiration of every six months commencing from the publication of the book.

7.     The Publisher shall submit to the Author every ________months, commencing from the publication of the book, a statement of the copies sold by the Publisher and his agents and shopkeepers. And such statement shall be sent along with the amount of royalty payable as aforesaid. Acceptance of any payment of royalty will not be construed as acceptance by the Author of the correctness of the statement and the Author will be entitled to verify the statement with the books of account, vouchers and other papers relating to sale and the Publisher shall offer such inspection to the Author or his agent whenever demanded by the Author. The Publisher shall with every such statement disclose the total number of copies printed by him.

8.     The Publisher shall supply ____________copies of the Book to the Author free of costs and without any royalty being payable thereon. The Publisher shall also supply free copies not exceeding ___________to such newspapers, periodicals or law Reporters as the Publisher may think fit.

9.     The Publisher shall not give benefit of this license by way of transfer or otherwise to any other person.

10.  The Publisher shall print only............ copies of the book and no more and the price of the book will not be more than Rs..................... per copy.

11.  The Publisher shall show the final proof of the print to the Author for his verification and the Author will be entitled to make any formal changes therein and to correct mistakes. The cover of the book will be got approved by the Author.

12.  This license is granted only for the publication of the First Edition of the Book.

13.  If the Author proposes to bring out a new edition of the book he will give the first option to the Publisher on such terms as may be agreed upon. In the event of any disagreement as to such fresh terms, the Author will be entitled to publish a new edition by himself or through any other publisher. But in no event the book will be reprinted or republished unless and until at least 90% of the copies of the first edition are sold out.

14.  The Author warrants that the said book is his original and does not infringe the copy right of any person. The Author agrees to indemnify and keep indemnified the Publisher against any claim made on account of infringement of any copyright. The author also warrants that he has not given the right of publication to any other person.

15.  The Publisher undertakes to mention on the cover page or any other following page of the book that the copyright in the book belongs to the Author.

16.  This agreement is executed in duplicate and one copy thereof will remain with the Author and the other with the Publisher.

17.  If the Publisher commits breach of any term of this Agreement, the Author will be entitled to cancel the same by giving fifteen days' notice to that effect to the Publisher and on the expiration of the said notice period this agreement will come to an end. On the termination of this agreement for any reason the Author shall have the option to take back all the unsold copies and the Publisher shall hand over them to the Author on payment of the proportionate cost of printing thereof but if the Author fails or refuses to exercise the option and to pay the costs, the unsold copies will be retained by the Publisher and sold.

18.  In the event of any dispute or difference arising between the parties hereto out of or in connection with the agreement the same shall be referred to arbitration of a common arbitrator if agreed upon, otherwise to two arbitrators, one to be appointed by each party to the arbitration and the Arbitration will be governed by the Arbitration Act for the time being in force.

IN WITNESS WHEREOF the parties have put their hands the day and year first hereinabove written.

Signed and delivered by...................

Within named Author.............

In the presence of.........................

Signed and delivered by ...................

Within named Publisher

In the presence of......................""",
"Format for Licence to use Copyright":"""DRAFT OF LICENSE TO USE COPYRIGHT AGREEMENT



I ………….s/o………………. r/o………………...., the owner of the copyright, to Award the LICENCE to s/or/o for using the said for the purpose of for a period of in lieu of the consideration of already paid to me on.., and I hereby acknowledge the receipt of said amount.

Date.      """,
"Format for Public Charitable Trust":"""DRAFT OF PUBLIC CHARITABLE TRUST



THIS INDENTURE made at ......... this ------- day of -----------  BETWEEN ____________________ called "the Settlor" (which expression shall unless it be repugnant to the context or meaning thereof be deemed to include his heirs, executors or administrator) of the One Part AND (1) ____________________ AND (2) _______________________ hereinafter called "the Trustees" (which expression shall unless repugnant to the context or meaning thereof be deemed to include the survivor of them and the Trustees or Trustee for the time being of these presents and the heirs, executors and administrators of the last surviving Trustee their, his or her assigns) of the second Part;

WHEREAS the 'Settlor' is desirous of settling for Public Charitable purpose a sum of Rs. _____(Rupees _________________only);

AND WHEREAS the Trustees have agreed to act as the Managing Trustees for life of the said Trust;

NOW THIS INDENTURE WITNESSEH that with a view to perpetuate the said desire and in consideration of the premises and for other diverse good causes and consideration him thereunto moving he the 'Settlor' doth hereby grant, assign transfer and hand over to the Trustees and the Trustees do hereby accept and take possession of the said sum of Rs. -------/- Rupees ---------- only) (hereinafter for brevity's sake called "the Trust Estate" which expression shall include all accretions thereto by way of donations or otherwise and the investments for the time being representing the same) to HOLD the Trust Estate upon the trusts and with and subject to the powers, provisions, agreements and declarations hereinafter contained of and concerning the same i.e.

a.     for relief of the poor

b.    education

c.     Medical relief

d.    the advancement of any other object of general public utility;

e.     to collect and receive funds and donations for the above objects,

f.     to do all acts, deeds and things as are incidental and conducive to the furtherance of the above objects.

AND IT IS HEREBY DECLARED that the charitable objects hereinabove mentioned shall not be limited or restricted to any particular caste or creed and will not involve any element of profit making.

AND IT IS HEREBY FURTHER DECLARED THAT THE Trustees shall be entitled to utilise and disburse either the net income of the Trust Estate and/or parts of the corpus thereof for maintaining and/or conducting establishments for the charitable purposes and trusts hereinabove set out;

1.     The Trustees shall have power and shall be entitled to collect, recover and receive dividends, rents and profits and other income of the Trust Estate (hereinafter referred to as `as the Trust income`) and to pay there out all taxes, rates, assessments, expenses and outgoings for collection in respect thereof and for the management of the Trust Estate and for administering and carrying out the Trust hereof.

2.     The Trustees shall be entitled from time to time to accept from any person or persons desiring to make gifts or donations upon the trusts and subject to the terms, provisions and powers and conditions contained herein, such moneys or properties as the Donors desire from time to time to give on the aforesaid trusts and on the terms and conditions herein contained.

3.     The Trust hereby declared shall be designated as ----------------.

4.     The Registered Office of the Trust shall be at ----------------------.

5.     The Trusts hereby declared shall be irrevocable.

6.     It shall be lawful for the Trustees at any time and from time to time to borrow moneys as well as to sell, mortgage, assign, transfer, demise or let on lease for any period however long or otherwise dispose of and deal with the Trust Estate including any immovable properties comprised therein or any part thereof either by publication or by private contract and on such terms and conditions as they the Trustees think fit with liberty to the Trustees to buy in rescind or vary any contracts for sale, mortgage, transfer, assignment, lease or other disposition as aforesaid and to resell the same or enter into a fresh contract for transfer, assignment, lease or other dispositions without being answerable for any loss occasioned thereby and with power also to execute all necessary assignments, conveyances, mortgages, transfers, leases, sub-leases and their counter-parts, and other deeds and assurances for the same and to give receipts and discharges for the consideration moneys and all other moneys. All moneys arising from any such sale, mortgage, transfer or other dispositions shall be deemed to be part of the Trust Estate and shall be dealt with accordingly.

7.     The receipt of the Trustees for the purchase money of any property hereby directed or authorised to be sold, or for any other moneys, stocks, funds, shares, securities or investments paid, delivered or transferred to them or him by virtue of these presents or in the execution of the Trusts or powers hereof shall effectually discharge the person or persons paying, delivering or transferring the same therefrom and/or from being bound to see to the application or being answerable for the loss or mis-application thereof.

8.     The Trustees for the time being of these presents shall be respectively chargeable only for such moneys and securities as they shall respectively actually receive, notwithstanding their signing any receipt for the sake of conformity and shall respectively be answerable and responsible only for their own respective acts, receipts, omissions, neglect and defaults and not for those of each other, nor for that of any banker, broker, auctioneer, or other person with whom or into whose hands any trust moneys or securities shall be deposited or come, nor the insufficiency in title or deficiency in value of any investments nor any other loss, unless the same shall happen through their own willful default respectively AND ALSO that the Trustees or Trustee for the time being may reimburse themselves, herself or himself or pay and discharge out of the Trust estate all expenses incurred in or about the execution of the Trusts or powers under these presents.

9.     The Trustees for the time being of these presents shall have full power to compromise or compound all actions suits and other proceedings and all differences and demands and to adjust, settle and approve all accounts relating to the Trust Estate and to execute, release and to do all other things relating thereto without being answerable or accountable for any loss occasioned thereby.

10.  The Trustees shall be entitled to employ any person or persons and pay them remuneration for the effective management and implementation of the Trust, including expert and technical qualified or experienced personnel.

11.  If and so often as any of the Trustees hereunder appointed or any future Trustees or Trustee of these presents shall die or shall leave India for more than one year or shall desire to retire from or refuse or become incapable to act in the Trust of these presents or otherwise, it shall be lawful for the surviving or continuing Trustees for the time being of these presents for this purpose to act in the execution of this power or for the proving executors or administrators of the last surviving Trustees to appoint a new Trustee or Trustees in place of the Trustee or Trustees so dying or leaving India or desiring to retire from the Trust or otherwise to appoint new or additional Trustees or Trustee and upon every or any such appointment the number of Trustees may be augmented or reduced and upon every such appointment the Trust Estate shall be transferred so that the same be vested in the Trustee or Trustees for the time being of these presents AND the Trustee or Trustees so appointed as aforesaid may as well before or after such transfer of the Trust Estate, act or assist in the Execution of the Trusts and powers of these presents as fully and effectually as if he / they had been hereby appointed as Trustee or Trustees PROVIDED THAT the number of Trustees of these presents shall not be less than two nor more than, seven PROVIDED HOWEVER AND IS HEREBY AGREED and declared for the sake of clarification that the present Trustees who have executed these presents shall remain Trustees during their lifetime or until such time as they retire or become disqualified to act as such.

12.  Any Trustee may at any time resign by giving a month's notice to his co-trustees and upon expiry of such period, he shall be deemed to have vacated his office.

13.  The Trustees shall have the right to make necessary resolutions by circulars instead of by meeting and any resolutions as agreed to by a majority of the Trustees shall be as valid and effectual as a resolution of the Trustees at a meeting duly convened.

14.  The Trustees shall determine all questions and matters of doubt in the execution of the Trusts, including the meaning and construction of any of the articles and provisions herein contained and do all acts and execute all the trusts, powers and authorities appertaining to these presents unanimously, and in case of disagreement, by majority, each Trustee shall have one vote only. The Trustees shall be at liberty to make rules or bye-laws which are not inconsistent with what is herein contained.

15.  For the purpose mentioned above or any of them, the Trustees shall be at liberty to enter into, sign, execute and deliver all such contracts, deeds, assurances and writings as they may deem necessary or expedient. The Trustees shall also be entitled in incur all legitimate expenses which they consider to be beneficial to and in the interests of the Trust.

16.  The Trustees shall be entitled to invest the Trust estate or such other funds of the Trust as are not immediately required, in any of the investments authorised by the Bombay Public Trusts Act, 1950 and/or the statutory amendments, modifications or reenactment thereof for the time being in force or the rules made there under and the Trustees shall also be at liberty to invest the Trust Estate or any part thereof on the mortgage of any immovable property situated in any part of the Republic of India (either of freehold or leasehold or any other tenure) and the Trustees shall also be entitled to purchase vacant land of any tenure and to construct buildings and other structures thereon as the Trustees may consider necessary and in the interest of the Trust and they shall also be entitled to pull down and demolish to rebuild any building or erection as they may consider necessary and in the interest of the Trust AND the Trustees shall have power to alter, vary or transfer the investments from time to time in such manner as the Trustees may think fit proper and in the interests of the Trust.

17.  The Trustees shall be entitled to obtain tenancy in and/or take on lease any premises and/or properties as they may consider proper, and also give them on leave and licence and receive deposits and/or advance compensation.

18.  Complete accounts of the Trust shall be properly kept in ....., or at such other place or places as the Trustees may from time to time decide and all the accounts, records, and documents of the trust shall be maintained at the office of the Trust. The accounts of the Trust shall be duly audited.

19.  The Trustees shall be entitled to open and maintain bank account or accounts as they may consider necessary or proper and such account or accounts may be operated on the signatures of any of two of the Trustees.

IN WITNESS WHEREOF the Settlor and the Trustees have hereunto set and subscribed their respective hands the day and year first hereinabove written.

SIGNED AND DELIVERED by the within-

named Settlor....................

in the presence of

SIGNED AND DELIVERED by the within-

named Trustees (1)...............

......... and (2)..............

............ in the presence of""",
"Format for Deed of Family Trust":"""DRAFT OF DEED OF FAMILY TRUST



This Deed of Trust made at.......................... this.......................... day of................ between (1)......................... (2)............................... (3)....................... (4).................... (5)................................ (6).................... (7)..................... all of..................... hereinafter referred to as the SETTLORS of the One Part and (I)................ (2)................... (3)..................... hereinafter referred to as the Trustees of the other part.

WHEREAS

1.     The settlors are the erstwhile members of a Joint family consisting of..............,.............. &............. as brothers and the remaining............. to............. as their respective sons and grandsons, all being majors and they are the only members of the family apart from their respective wives.

2.     The said Joint Family owns an ancestral House together with the land apartment in village/town of................. in Dist............ in State of.........................

3.     ................,............... &............... and their respective sons and grandsons are living separate at different Towns/Cities and earning in their own way independently and have their respective properties

4.     The said Family House is the only common property belonging to the said family

5.     The said house cannot be physically divided and partitioned and the parties also do not propose to do so nor do the settlers desire to sell the same but desire to keep and preserve it as a common unit and as a memorial of the ancestors and also to avoid any dispute regarding the same among the members of the said family.

6.     The said family has a family Deity of Goddess............... and the family has installed the same in one of the rooms of the said house.

7.     The Settlers have therefore proposed to dedicate the said house and premises to the said Deity and to continue to worship the same and with these objects they have decided to create a private Trust of the said property.

8.     The Settlers have also collected a Fund of Rs............... as the initial fund or Corpus to meet the expenses of maintaining the said house and to worship the said idol.

9.     It is proposed that...........,...........,..........., will act as the first Trustees of the Trust and the settlers have proposed to transfer the said property to...........,........... &........... as Trustees to hold the property for the benefit of the said family in the manner aforesaid.

NOW this Deed witnesseth that pursuant to the said desire of the settlers and in the premises aforesaid the settlers do and each of them doth hereby grant and transfer the said house with the land appurtenant thereto situate at........... and more particularly described in the Schedule hereunder written and all the rights liberties, privileges and easements appurtenant to the said house and the land and all the estate right, title and interest of the settlers in or to the said property hereby granted unto the Trustees and also transfer the Fund of Rs............ Collected by the settlers TO HOLD the same to the use of and on the terms

Herein below mentioned and with all the powers and provisions herein contained subject however to the payment of all taxes and other public dues payable to the Government or any local authority in respect of the family house and the land.

1.     This Trust will be known as............................................................ Family Trust.

2.     The Trustees will protect, preserve and worship the idol of Goddess.............installed in the said house and for that purpose make all arrangements for the same and appoint a PUJARI if available.

3.     The Trustees shall invest the said Fund or Corpus hereinafter referred to as the Trust Fund(which will include also all the contributions made by the members of the family from time to time and all other moneys received by the Trustees by way of gifts, donations or otherwise) in authorized securities and spend the income realized there from in the maintenance of the said property and in the worship of the said Deity.

4.     The Trustees will arrange and carry out the daily worship of the said deity as far as possible and shall hold the necessary religious Festivals or functions according to the custom of the family thereto followed.

5.     The Trustees will be entitled to collect or receive from the members of the family for the time being or any of them such periodical payments or occasional donations so as to increase the Corpus of the Trust Fund and will also be entitled to receive donations or gifts from others without creating or agreeing to create in them any right or privilege in respect of the trust property or Trust Fund or in the management of the Trust.

6.     The Trustees will be entitled to carry out necessary repairs or renovations to the said property so as to preserve the same in good condition and also to provide all necessary amenities for reasonably comfortable living in the said house to the extent the income of the Trust Fund permits.

7.     Any member of the Family will be entitled to occasionally stay in the said family house or any part thereof free of any charges, such stay not extending beyond a month continuously except in any exceptional circumstances as the Trustees may think proper. In the event of more than one member and his family desiring to occupy the said house at the same time the Trustees shall decide as to who should be given preference and what should be done for convenience of both and their decision shall be final. However the expenses for living will be borne by the member occupying the same and not by trust, The object of this provision is that the house should be available for temporary use and occupation by any member of the family and which use and occasion will also help in the upkeep and preservation of the house.

8.     The Trustees shall not make any substantial changes in the house or additions thereto except with the consent of all the major members of the different branches of the said family for the time being.

9.     The Trustees shall not be entitled to sell the said house property or any part thereof nor to mortgage the same or to let out any portion thereof.

10.  The Trustees will be entitled to engage a permanent or occasional watchman to safeguard the property from encroachments or any damage to the property and pay his salary out of the income of the Trust Fund.

11.  The number of trustees of this Trust will be minimum three and maximum five and the Trustee for the time being will be entitled to appoint any additional trustee so that the total number does not exceed five. The Trustees of the trust to be appointed in future will always be from among the members of the said family fit to be appointed and not any outsider.

12.  If any of the trustees for the time being dies or is disqualified to be a trustee for any reason prescribed by law, the remaining trustees will be entitled to appoint a new Trustee in his place and the Trust Property and Trust Fund will be transferred to his name along with the other Trustees as and in the manner required by law.

13.  The Trustee shall open one or more accounts in one or more banks in their names and such account will be operated by any two of the Trustees. All moneys received will be credited to such accounts and such amount as may not be required for immediate expenses can be invested in temporary deposits with any of the Banks.

14.  The Trustees shall have all other powers as are conferred on a Trustee by law.

15.  The Trustees shall keep accounts of the Trust Funds and the same shall be made available for inspection by any member of the family as and when required.

16.  The senior most Trustee in age will act as a managing Trustee and will be in charge of the day to day management of the trust. However all policy decisions and any item of work involving an expenditure of more than Rs.........../- will have to be approved by all the trustees or a majority of them in any meeting called for that purpose or by circulating resolution. The Trustees will keep written minutes of the meetings held and decisions taken. Any one Trustee can call a meeting of the Trustees as and when occasion arises.

17.  If for any reason or under any circumstances the trustees unanimously think that it is impossible to carry on with the Trust, they will be entitled to revoke the same and shall be entitled to deal with and dispose the Trust property and the Trust Fund as the majority of the members of the said family for the time being will agree to, failing which the Trustees will be entitled to apply to the competent Court of law for necessary directions.

IN WITNESS WHEREOF THE SETTLORS AND THE TRUSTEES HAVE PUT THEIR HANDS THE DAY AND YEAR FIRST HEREUNDER WRITTEN

THE SCHEDULE ABOVE REFERRED TO

Signed by the within named

Settlors.....................

...................,

...................,

...................,

...................,

....................,

..................,

..............................,

...................,

...............,

in the presence of............

Signed by the within named

Trustees....................

...................,

................... &

in the presence of............""",
"Format for Simple will":"""DRAFT OF WILL



 I, ______________, son of Shri _______________, aged __ years, resident of _____________________________, do hereby revoke all my former Wills, Codicils and Testamentary dispositions made by me. I declare this to be my last Will and Testament.

I maintain good health, and possess a sound mind. This Will is made by me of my own independent decision and free volition. Have not be influenced, cajoled or coerced in any manner whatsoever.

I hereby appoint my ________________, as the sole Executor of this WILL.

The name of my wife is _________________. We have two children namely, (1) __________________ (2) ________________, I own following immovable and movable assets.

1.     One Flat No.___ in _______________________.

2.     Jewellery, ornaments, cash, National Saving Certificate, Public Provident Fund, shares in various companies, cash in hand and also with certain banks.

All the assets owned by me are self-acquired properties. No one else has any right, title, interest, claim or demand whatsoever on these assets or properties. I have full right, absolute power and complete authority on these assets, or in any other property which may be substituted in their place or places which may be Acquired or received by me hereafter.

I hereby give, devise and bequeath all my properties, whether movable or immovable, whatsoever and wheresoever to my wife, _____________________, absolutely forever.

IN WITNESS WHEREOF I have hereunto set my hands on this ____ day of ____, 20__ at ____________.

TESTATRIX

SIGNED by the above named Testatrix as his last WILL and Testament in our presence, who appear to have perfectly understood & approved the contents in the presence of both of us presents, at the same time who in his presence and in the presence of each other have hereunto subscribed our names as Witnesses.

WITNESSES :

1.

2.""",
"Format for Deed of Hypothecation HP":"""DRAFT OF DEED OF HYPOTHECATION



THIS DEED OF HYPOTHECATION executed at ________ on this the ___________ day of _________ between

Mr.________________, son of_____________, aged about ___________ years, residing at _____________________, hereinafter called the CREDITOR (which expression shall, unless it is repugnant to the context mean and include his legal representatives, executors, administrators, and assigns)

And

Mr.________________, son of_____________, aged about ___________ years, residing at _____________________, hereinafter called the BORROWER (which expression shall, unless it is repugnant to the context mean and include his legal representatives, executors, administrators and assigns);

WHEREAS

The BORROWER has placed an order for the purchase of, a ___________, namely________________, {valued at Rs.____________ (Rupees ____________), (Details of the same are set out in the schedule 'A' hereunder) (hereinafter referred to as the asset), with the ________________, namely ________________, having its office at __________, and has remitted an amount of Rs.______________(Rupees _____________only}, with the said _________________ as advance towards the sale consideration.

The BORROWER has approached the CREDITOR for a loan of Rs.______________, (Rupees _____________only), for the payment of the balance price of the schedule 'A' mentioned asset. The CREDITOR and BORROWER have agreed that the CREDITOR shall finance the purchase of the schedule 'A' mentioned asset, on the condition that the BORROWER hypothecates the schedule mentioned asset with the CREDITOR as security for the due repayment of the said loan. The parties have agreed to reduce their agreement to writing

NOW THEREFORE IN CONSIDERATION OF THE MUTUAL OBLIGATIONS AND UNDERTAKINGS CONTAINED HEREIN THIS AGREEMENT WITNESSETH AS FOLLOWS:

Payment by the CREDITOR

The CREDITOR shall pay to the said manufacturer, on behalf of the BORROWER, a sum of Rs. ____________/-, (Rupees _______), towards the balance price of the said asset and shall retain possession of the original invoice of the said asset till the debt is fully discharged by the BORROWER.

HYPOTHECATION

The BORROWER hereby hypothecates and creates a charge on the asset more fully described in the schedule 'A' hereunder to and in favour of the CREDITOR as security for the repayment of the loan with interest.

Obligations of the BORROWER

The BORROWER hereby undertakes to repay the loan amount within a period of ______ months commencing from________ along with interest. The BORROWER shall pay interest at the rate of ______________ on the principal per month, at Rs._____________/-, (Rupees ____________only). The Interest and principal are payable in monthly instalments as per schedule-B hereto.

Rights of the CREDITOR

If the BORROWER defaults in payment of the amount as per schedule-B hereto then such defaulted instalment will carry interest as if the defaulted instalment is the principal, until it is paid. If the BORROWER fails to pay any ______ instalments then the CREDITOR shall be entitled to claim the principal and interest amount due, and the same shall become payable forthwith, on the CREDITOR calling upon the BORROWER to make payment of such defaulted principal amount.

The BORROWER shall not remove or take the said asset, outside the State without prior intimation to the CREDITOR.

The BORROWER agrees and undertakes to insure the asset against all hazards, and shall produce the relevant receipts, and other documents, whenever called upon by the CREDITOR so to do.

Any dispute arising under this Deed or any matter incidental thereto, shall be submitted to arbitration as per the provisions of the Arbitration and Conciliation Act 1996 and the venue of the arbitration shall be at .........

IN WITNESS WHEREOF the parties hereto affixed their signatures on the day month and year mentioned hereinabove

SCHEDULE 'A'

(Describe the Asset)

SCHEDULE-B

(Describe the payment schedule)

CREDITOR

BORROWER

WITNESSES

1.

2.""",
"Format for Loan Agreement":"""DRAFT OF LOAN AGREEMENT



LOAN AGREEMENT BETWEEN



________________________

AND ______________________

THIS AGREEMENT made and entered into at _______ this ____ day of_______, ______ BETWEEN __________________ hereinafter called "the Lender" AND ________________________ hereinafter called "the Borrower" and reference to the parties hereto shall mean and include their respective heirs, executors, administrators and assigns;

WHEREAS the Borrower is in need of funds and hence has approached the Lender to grant her an interest-free loan of Rs.________/- (Rupees ____________________ only) for a period of ____ years;

AND WHEREAS the Lender has agreed to grant a loan to the Borrower, free of interest, as the Lender and the Borrower have known each other since several years;

AND WHEREAS the parties hereto are desirous of recording the terms and conditions of this loan in writing;

NOW THIS AGREEMENT WITNESSETH and it is hereby agreed by and between the parties hereto as under:-

1.     The Borrower hereto, being in need of money, has requested the Lender to give her an interest-free loan of Rs.___________/- (Rupees _________________________ only) to enable her to purchase a residential flat, to which the Lender has agreed.

2.     The said loan is required by the Borrower for a period of ____ years, commencing from __/__/___ and terminating on __/__/_____.

3.     The Borrower hereby agrees and undertakes to return the loan of Rs.___________/- (Rupees ____________________only), in instalments, within the aforesaid period of ____ years and gives her personal guarantee for the same.

4.     The terms and conditions of this Agreement are arrived at by the mutual consent of the parties hereto.

IN WITNESS WHEREOF the parties hereto have hereunto set and subscribed their respective hands the day and year first hereinabove written.

SIGNED AND DELIVERED by the Within-

named Lender in the presence 

SIGNED AND DELIVERED by the Within-

named Borrower in the presence of""",
"Format for Loan Agreement with Security":"""DRAFT OF  LOAN AGREEMENT WITH SECURITY



 THIS AGREEMENT is made at ________on this ____ day of _______, 200__

BETWEEN

___________LTD, a Company incorporated under the Companies Act, 1956 or Companies Act ,2013 having its Registered Office at ___________________________ (hereinafter referred to as "The Lender") which term or expression shall unless excluded by or repugnant to the subject or context hereof shall mean and include its heirs, successors and assigns of the One Part

AND

      i.        M/S ABC LIMITED, a Company incorporated under the Companies Act, 1956 or Companies Act ,2013 having its Registered Office at ____________________ (hereinafter referred to as "The Borrower") which terms or expression shall unless excluded by or repugnant to the subject or context hereof shall mean and include its heirs, successors and assigns of the SECOND PART and

     ii.        M/S CDE LIMITED, a Company incorporated under the Companies Act, 1956 or Companies Act ,2013 having its Registered Office at __________________ (hereinafter referred to as "The Lender") which terms or expression shall unless excluded by or repugnant to the subject or context hereof shall mean and include its heirs, successors and assigns of the THIRD PART.

WHEREAS

A. The Borrower is one of the entities in the group of Companies, ABC LIMITED, a Company incorporated under the provisions of the Companies Act, 1956 or Companies Act, 2013 having its Registered Office at ___________________________ hereinafter referred to as "The Borrower" has a paid up capital of Rs. ______ lacs as on _________ (date).

B. The Borrowers has approached "The Lender" for grant of inter corporate deposit of Rs. _______/- (Rupees __________ only) for a period of _____ days beginning from the date of disbursal of loan i.e._________.

C. The Lender has favourably considered the request of the Borrower and has agreed to lend and advance a secured interest carrying inter-corporate deposit of Rs. _________ (Rupees _________ only) to the Borrower on the terms and conditions and covenants as follows.

D. The Lender has agreed to secure the timely repayment of the loan along with interest by creating in favour of the Lender Pledge with the securities fully stated in the Annexure Annexed hereto and treated as an integral part of this Agreement.

NOW THIS AGREEMENT WITNESSETH AS FOLLOWS:

1.  At the request of the Borrower the Lender lends an advance to the Borrower an inter corporate deposit of Rs. ____________ (Rupees ___________only) for a period of _______ days beginning from the date of disbursal i.e.________

2. The said inter corporate deposit shall carry an interest @ _____% per annum payable with ________ rests. In case of delay or default in payment, whether of the principal or of the interest or any part thereof the Lender shall be entitled and the borrower shall be liable to pay a penal interest @ _% per annum over and above the interest mentioned hereinabove.

3.  As a security towards timely repayment of loan along with interest, the Lender has agreed to pledge in favour of the Lender, fully paid up equity shares, standing in the name of Lender as stated in the Annexure annexed hereto and treated as an integral part of the agreement in the equity capital of ABC Limited, a company incorporated under the provisions of the Companies Act, 1956 or Companies Act, 2013 having its Registered Office at _____________________________. The Equity shares of Equity International Ltd are listed at _______ Stock Exchange and the current market price of shares is agreed to be Rs. ____/- per share.

4. In case the Lender sends the notice to the Borrower to make good the margin in the securities (_____% in this case) and the Borrower fails and/or neglects to make good the margin within the stipulated period as mentioned in the notice the Borrower shall be deemed to have committed default of the terms of this agreement and in that event it shall be lawful for the Lender (but not compulsory) to demand from the Borrower repayment of the loan along with the interest then outstanding and the Borrower shall be liable to repay the loan in full along with interest thereon without any objection and/or demur.

5. It is expressly agreed by and between the parties hereto that in case of downward revision in the market price of the equity shares of ABC LTD, the Borrower/ Lender shall on its own, pledge in favour of the Lender such other shares of ABC LTD so as to ensure ______ % margin between the amount of loan along with interest and the securities.

6. In case the Borrower fails and/or neglects to repay the amount of loan or the amount of interest on the due date it shall be lawful for the Lender to sell or dispose off, at the cost and expenses of the borrower, all or some of the equity shares of ABC LTD either by way of private arrangement or in the open market and to apply the net proceeds thereof towards satisfaction of the amount of loan or the interest, then outstanding.

7. The Borrower agrees that any accretion the securities pledged with the Lender by way of dividend, bonus/rights issue etc. accruing from time to time shall be deemed to be pledged with the Lender and the Borrower shall, on its own take expeditious steps to create a pledge in favour of the Lender.

8. It is agreed that the Borrower shall execute a Demand Promissory Note in favour of the Lender.

9. The Borrower/ Lender agree and undertake to execute in favour of the Lender all such documents/papers, including fresh transfer deeds, as may be required by the Lender from time to time.

10.The Borrower/ Lender have agreed to constitute nominate and appoint the Lenders as its true and lawful attorney to do all such deeds and things in respect of the said ______(No. of Shares) Equity Shares of ABC LTD as may be pledged/hypothecated by the Borrower to the Lender.

11. It is agreed that the liability of the Lender is jointly and severally along with the liabilities of the Borrower and the same is co-extensive.

IN WITNESS WHEREOF the parties herein have signed this agreement in acceptance of all terms stated above on the date and place mentioned hereinabove.

THE BORROWER

THE PLEDGER

THE LENDER""",
"Format for Cheque Bounce Notice Format":"""Sample Cheque Bounce Notice Format




To,                                                                                                                               Date: __/__/2019

Name of the party/parties

Address

Contact info.



Sub: Legal notice under section 138 of Negotiable Instrument Act for dishonour of cheque.



Dear Sir/Madam,



Under instructions and authority from my client M/s. ______ we serve upon you the following legal notice.





That my client is a Private Limited Company engaged in trading of computers, laptops, computer parts and accessories the name of ________ having office at _________.




That in the year ______ you have approached my client through E-mail communication of your employee ________ to purchase _______ for your office. Subsequently you have issued purchase order dated _______ amounting to rupees ______ for _______.




That you have promised our client to pay the cost of the product in the form of Current Dated Cheque as mentioned in the purchase order.




That our client had relied on your promise and as instructed by you delivered the ________ at your office at ______ vide Invoice No. _______ dated _______.




That you have issued Cheque No. ____dated ________ for Rs. ______/- (Rupees ____________only) drawn ____________________ towards payment against the Invoice.




That the aforesaid cheques No. _____dated ________for Rs. _______/- was presented by our client M/s. _______ on ____ to your bankers i.e. ______________.




That to our clients' shock and surprise the said cheque had been dishonored by your bankers with the reason “Fund Insufficient” which was intimated to our client by their _______ through their cheque return memo dated _________.




That thereafter in spite of many telephonic reminders by my client, you failed to make the payment due to my client.




That it is now clear that you had the dishonest intention at the time of purchasing ______ from my client and deceived my client to the tune of _________.




My client states that you have issued the above said cheques only with an intention to cheat our client which amounts to an offence punishable under section 138 of Negotiable Instruments Act.




Under the circumstances, we call upon you to pay of Rs. ____________ /- within a period of 15 (fifteen) days from the date of receipt of this notice, failing which our client will be constrained to take legal action against you in a court of law for an offence punishable under section 138 of Negotiable Instruments Act for which you will be liable for all costs and consequences.




This is without prejudice to all other legal rights and remedies available to our client for the above-stated purpose.




You are liable to pay a sum of Rs. _______/- as necessary cost and expenses of sending the present legal notice to you.




Copy of this legal notice is also kept at my office for further ready reference if required in the future.







Yours faithfully,

Signature

(Advocate)""",
"Format for Legal Notice for Recovery of Money":"""Legal Notice



Ref. No……………. Dated ____, __________



REGD.A.D.



LEGAL NOTICE



To,



_____________



Dear Sir,



Pursuant to the instructions from and on behalf of my client ___________________, through its _____________, I do hereby serve you with the following Legal Notice: -



1- That my client is a ___________ firm/individual under the name and style of M/s ______________________.



2- That my client is engaged in the business of __________ of the ___ etc.



3- That against your valid and confirmed order my client did your job work from time to time on credit basis as you have running credit account in the account books of my client operated in due course of business.



4- That my client-raised bills of each and every work performed for payment, although you have acknowledged the receipt of such bills raised by my client.



5- That inspite of acknowledging the liability of payment of principal balance of Rs. _________/- you have been miserably failed to make payment of the said amount due to my client from you deliberately with malafide intent, hence you are liable to pay the said principal balance amount of Rs. __________/- alongwith interest @ __% p.a. from the date of due till actual realization of the said sum as is generally and customarily prevailing in the trade usages, which comes to Rs. __________/-



6- That thus you are liable to pay the total amount of Rs. ________/- to my above named client and my above named client is entitled to recover the same from you.



7- That my client requested you several times through telephonic message and by sending personal messenger to your office for release of the said outstanding payment, but you have always been dilly delaying the same on one pretext or the other and so far have not paid even a single paisa out of the said outstanding undisputed amount.



I, therefore, through this Notice finally call upon you to pay to my client Rs. __________/-. along with future interest @ __ % p.a. from the date of notice till actual realization of the said amount, together with notice fee of Rs. ____/- to my client either in cash or by demand draft or Cheque which ever mode suits you better, within clear 30 days from the date of receipt of this notice, failing which my client has given me clear instructions to file civil as well as criminal lawsuit for recovery and other Miscellaneous proceedings against you in the competent court of law and in that event you shall be fully responsible for the same.



A copy of this Notice has been preserved in my office for record and future course of action.



(____________)



ADVOCATE"""}


new_Bonds = {key.lower():value for key, value in Bonds.items()}

user_input = input()
    
match = []
for key, value in new_Bonds.items():
    if key.lower() in user_input.lower() or user_input.lower() in key.lower():
        match.append({key})
print(match)