admission_attributes = [
            "Parity",
            "Ruptured membrane",
            "Fever",
            "Meconium",
            "Gestational Hypertension",
            "Preeclampsia",
            "Severe Preeclampsia",
            "Intraamniotic Infection"
            "Lupus",
            "Antiphospholipid Syndrome",
            "Asthma",
            "Gravidity",
            "Tobacco Usage",
            "Polyhydramnios",
            "Oligohydramnios",
            "Cholestasis",
            "Chronic Kidney Disease",
            "IVF",
            "Pregestational Diabetes",
            "Gestational Diabetes",
            "Fetal growth restriction",
            "Marginal Cord Insertion",
            "Velamentous Cord Insertion"
        ]
delivery_attributes = [
        "Gestational Age (weeks)",
        "Sex of Fetus",
        "Mother's Age (years)",
        "Parity",
        "Ruptured membrane",
        "Fever",
        "Meconium",
        "Gestational Hypertension",
        "Preeclampsia",
        "Severe Preeclampsia",
        "Intraamniotic Infection"
    ]

example_note = "Example note: Case was referred to SW by tx team as MOB has a h/o anxiety/PTSD/panic attacks. MOB is a 19yo G1P1 Hispanic female who gave birth to a baby girl via csection on [---]. Both are expected to be discharged home today. MOB is English speaking. SW met with MOB was appropriate, yet somewhat guarded. Role of SW was explained.CM comprehensive assessment was completed- please see for additional info.MOB denies any h/o mental illness including PTSD and panic attacks. Denies taking any psychotropic medication or being enrolled in therapy./n"
example_format = "Attribute, Value, Sentence/n Age of Mother, 19, MOB is a 19yo/n Gravidity, 1, MOB is a 19yo G1P1/n Parity, 1, MOB is a 19yo G1P1/n"
example_note1 = "Example note: Patient: [---], [---] MRN: [---] FIN: [---] Age: 32 years Sex: Female DOB: [---] Associated Diagnoses: None Author: [---] , [---] Basic Information Reason for admission: Scheduled induction. Informed consent obtained for anesthesia, procedure and blood transfusion. Gestational Age: * Note: EGA calculated as of [---]No EGA/EDD calculations have been recorded. Is the patient admitted with spontaneous labor?: No. Patient has no history of Cesarean Birth Chief Complaint IOL History of Present Illness 32 y/o G2P[---] at 37.6 wks by LMP consistent with [---] trimester U/S for EDD of [---]. PNC with VPLOW. C/b:1. GDMA2: on NPH 25 units nightly2. Obesity3. Ulcerative colitis: on mesalamine Patient presents for unscheduled IOL for oligohydramnios. Reports feeling well today, has no complaints.Denies any regular ctx, VB, LOF, or decrease in FM. Review of Systems Constitutional: Negative. Respiratory: Negative. Cardiovascular: Negative. Gynecologic: Negative. Health Status Allergies: Allergic Reactions (Selected)UnknownPenicillin- No reactions were documented.Sulfur- No reactions were documented., Allergies (2) ActiveReactionpenicillinNone DocumentedSulfurNone Documented Current medications: (Selected) PrescriptionsPrescribed1 cc BD insulin syringes with BD ultra-fine 6mm (15/64) x 31 G needles: 1 cc BD insulin syringes with BD ultra-fine 6mm (15/64) x 31 G needles, See Instructions, to use with humulin N at bedtime diagnosis code: 024.424, 1 box, 2 Refill(s), Pharmacy: CVS/pharmacy #[---], to use with humulin N at bedtime; diagnosis code: 0...BD insulin needles: BD insulin needles, See Instructions, 31G, 6mm, 30 ea, 2 Refill(s), Pharmacy: CVS/pharmacy #[---], 31G, 6mm, SupplyDiabetes Supplies: 1/2cc BDInsulin Syringes with BD UltraFine 6mm (15/64) X31G needle ___: Diabetes Supplies: 1/2cc BDInsulin Syringes with BD UltraFine 6mm (15/64) X31G needle ___, See Instructions, Use Daily as directed, 200 ea, 4 Refill(s), Pharmacy: CVS/pharmacy #[---], Use Daily as directed, SupplyDiabetes Supplies: Glucometer ___: Diabetes Supplies: Glucometer ___, See Instructions, Use as directed 4x/day, 1 ea, 0 Refill(s), Pharmacy: CVS/pharmacy #[---], Use as directed 4x/day, SupplyDiabetes Supplies: Lancets Delica One Touch: Diabetes Supplies: Lancets Delica One Touch, See Instructions, Use 4x Daily as directed, 200 ea, 2 Refill(s), Pharmacy: CVS/pharmacy #[---], Use 4x Daily as directed, SupplyDiabetes Supplies: Lancets ___: Diabetes Supplies: Lancets ___, See Instructions, Use 4x Daily as directed, 200 ea, 0 Refill(s), Pharmacy: CVS/pharmacy #[---], Use 4x Daily as directed, SupplyDiabetes Supplies: Test Strips One Touch: Diabetes Supplies: Test Strips One Touch, See Instructions, Use 4x Daily as directed, 200 ea, 2 Refill(s), Pharmacy: CVS/pharmacy #[---], Use 4x Daily as directed, SupplyDiabetes Supplies: Test Strips ___: Diabetes Supplies: Test Strips ___, See Instructions, Use 4x Daily as directed, 200 ea, 0 Refill(s), Pharmacy: CVS/pharmacy #[---], Use 4x Daily as directed, SupplyHumuLIN N 100 units/mL subcutaneous suspension: = 15 Units, SubCutaneous, Bedtime, diagnosis code: 024.424, # 10 mL, 2 Refill(s), [---], Pharmacy: CVS/pharmacy #[---], 15 Units SubCutaneous Bedtime,Instr:diagnosis code: 024.424HumuLIN N Pen 100 units/mL subcutaneous suspension: = 15 Units, SubCutaneous, Bedtime, # 10 mL, 4 Refill(s), [---], Pharmacy: CVS/pharmacy #[---], 15 Units SubCutaneous BedtimeNovoLIN N 100 units/mL subcutaneous suspension: = 15 Units, SubCutaneous, Bedtime, # 3 mL, 4 Refill(s), [---], Pharmacy: CVS/pharmacy #[---], 15 Units SubCutaneous BedtimeDocumented MedicationsDocumentedLialda: = 2.4 g =, Oral, Once daily, 0 Refill(s), [---]Prenatal Multivitamins: Oral, Once daily, 0 Refill(s), [---], No qualifying data available, PNV Problem list: All ProblemsObesity / SNOMED CT [---] / ConfirmedGroup A beta-hemolytic streptococci / SNOMED CT [---] / ConfirmedPregnant / SNOMED CT [---] / ConfirmedResolved: Ulcerative colitis / SNOMED CT [---] Histories Past Medical History: ResolvedUlcerative colitis ([---]): Resolved. Procedure history: no known procedures. Pregnancy History Pregnancy History G1 P0,0,0,0 No previous pregnancies history have been recorded Social History Social & Psychosocial HabitsAlcohol[---] Use: DeniesHome/Environment[---] Feels unsafe at home: NoSubstance Abuse[---] Use: DeniesTobacco[---] Use: Never smoker[---] Use: Never smoker. Family History: Breast cancer...Aunt Prenatal History Prenatal labs Blood type: Rh positive. Rapid plasma reagin: nonreactive. Hepatitis: Hepatitis B Surface Antigen Negative. Human immunodeficiency virus: negative. Group B Strep: positive. Chlamydia: negative. Gonorrhea culture: negative. Rubella: immune. Varicella: immune. No Data Available Physical Examination Vital Signs (last [---] hrs)_____Last Charted___________Temp Oral36.9 DegC ([---] [---])Resp Rate 16 br/min ([---] [---])SBP132 mmHG ([---] [---])DBP82 mmHG ([---] [---])SpO296 % ([---] [---])Weight2.8 kg ([---] [---])Height165 cm ([---] [---]) General: Alert and oriented. Respiratory: Lungs are clear to auscultation. Cardiovascular: Normal rate, Regular rhythm. Gastrointestinal: Soft, Normal bowel sounds. Musculoskeletal No tenderness. No swelling. SVE: _/_/_ [x] deferredMembranes: [x] intact [ ] ruptured [_] ferning [_] poolingEFW: 8 lbs by [x] [---] [_] sonoEFM: 140 bpm, mod var, pos accels, no decelsToco: [x] none [_] _Sono: cephalic, anterior placenta Review / Management OB Results Review Results review Impression and Plan Pt is a 32 yo G2P[---] at 37.6 weeks presenting for scheduled induction of labor for oligohydramnios1. Admit to L&D-Consents signed, all questions answered, pt expressed understanding-ordered for clears- will place cervidil when arrives to floor, remove 12 hours unless maternal fetal indications- encouraged patient on limited movement once bedrest-IV hydration, routine labs sent2. FHT: category 1, continue to monitor3. Pain: pt to receive epidural if becomes uncomfortable4. GBS pos: pt w/ PCN allergy, Vancomycin ordered5. GDMA2: RAISS ordered"
example_format1 = "Attribute, Value, Sentence/n Age of Mother, 32, 32 y/o G2P[---] at 37.6 wks.../n Gestational Age, 37.6, 32 y/o G2P[---] at 37.6 wks.../n Gravidity, 2, 32 y/o G2P[---] at 37.6 wks.../n Oligohydramnios, Yes, Patient presents for unscheduled IOL for oligohydramnios./n Gestational Diabetes, Yes, GDMA2: on NPH 25 units nightly"
example_note2 = "Example note: Patient: [---], [---] S MRN: [---] FIN: [---] Age: 26 years Sex: Female DOB: [---] Associated Diagnoses: None Author: [---] MD, [---] History of Present Illness 26-year-old G2P[---] at 39 weeks dated by LMP [---] c/w 7 week sono for EDD [---] Pregnancy c/b:1. Hx of PEC with SF in prior delivery- Patient on ASA 162 mg/day - Baseline 24hr urine protein: 139mg2. Rh neg- Received Rhogam for first trimester bleeding on [---]3. Mild intermittent asthma in childhood: one hopsitalization as a child, no intubations, no inhaler in years4. Former smoker: less than 1ppd, quit in early pregnancy5. Migraines: normal MRI, now improved 6. Obesity: BMI 377. Marginal cord insertion- AGA fetus on [---]CC: Patient presents with LOF. She reports that at 2am she was awoken by a contraction, went to the bathroom and had a large gush of yellow fluid. She reports that, at that point, she got in the car to come to the ED, and on the drive started having ctx q5 mins. She denies VB. +FM. Currently the patient stats that she is contracting q3mins, of moderate intensity, and is still leaking fluid. Denies HA, CP, SOB, fever, NV, RUQ pain. Prenatal labs:Blood type: A negative, neg antibody screenH/H: 12.8/38.0Plt: 291kGC: neg[---]: negRPR: NRRubella: immuneVaricella: immuneUrine Cx: negHepBsAg: negHep C: negHIV: negPap: NILM with BVCF screen: Genetic carrier screening: no mutationsNIPTs: 46 XYFirst Trimester Screen: negGBS: negative Histories PMH: deniesPSH: lap cholecystectomyObHx: G2P[---]SocHx: denies smoking, alcohol, illicit drug useAll: dilaudid- itchyMeds: Metformin 500mg qhsaspirin 81mg Pregnancy History Pregnancy History G2 [---],0,0,1 Pregnancy # 1 Baby 1Outcome Date: [---]Neonate Outcome: Live BirthOutcome or Result: VaginalGender: --[---] Age: 40 weeks 4 days Wt: [---] gHospital: --[---] Labor: --Child's Name: --Baby's Father: -- Problem list: All ProblemsAFP - Alpha-fetoprotein raised / SNOMED [---] [---] / ConfirmedObesity / SNOMED [---] [---] / PossibleGestational hypertension / ICD-9-CM 642.90 / ConfirmedRh negative / SNOMED [---] [---] / ConfirmedAt risk of venous thromboembolus / SNOMED [---] [---] / ConfirmedDecreased hemoglobin or hematocrit / ICD-9-CM 285.9 / PossibleFamily history of breast cancer in mother / SNOMED [---] [---] / ConfirmedHistory of cigarette smoking / SNOMED [---] [---] / ConfirmedPostpartum exam / SNOMED [---] [---] / ConfirmedGestational diabetes mellitus, class A>1< / SNOMED [---] [---] / ConfirmedRubella non-immune / SNOMED [---] [---] / ConfirmedPregnant / SNOMED [---] [---] / Confirmed Prenatal History No qualifying data available. Allergies: Allergic Reactions (Selected)ModerateDilaudid- No reactions were documented. Current medications: (Selected) PrescriptionsPrescribedPrenatal Multivitamins Folic Acid 1 mg oral tablet: = 1 tab, Oral, Once daily, # 30 tab, 2 Refill(s), [---] EDT, Pharmacy: CVS/pharmacy #[---], 1 tab Oral Once dailyaspirin 81 mg oral delayed release tablet: = 1 tab, Oral, Once daily, # 30 tab, 2 Refill(s), Indication: Antiplatelet, [---], Pharmacy: RITE AID-[---] [---] HIGHW, 1 tab Oral Once dailyglucometer: glucometer, See Instructions, check fsbg qid as directed, 1 Units, 0 Refill(s), Pharmacy: CVS/pharmacy #[---], check fsbg qid as directed, Supplylancets: lancets, See Instructions, check fsbg qid, 2 [---], 3 Refill(s), Pharmacy: CVS/pharmacy #[---], check fsbg qid, SupplymetFORMIN 500 mg oral tablet: = 1 tab, Oral, Bedtime, # 30 tab, 1 Refill(s), Indication: Endocrine, [---] EDT, Pharmacy: CVS/pharmacy #[---], 1 tab Oral Bedtimetest strips: test strips, See Instructions, check fs bg qid as directed, 2 [---], 3 Refill(s), Pharmacy: CVS/pharmacy #[---], check fs bg qid as directed, Supply Review of Systems ROS reviewed as documented in chart Physical Examination Vitals Signs (last [---] hrs)__Last Charted___Minimum_____MaximumTemp 36.8 ([---] [---])36.8 ([---] [---])36.8 ([---] [---])Heart Rate85 ([---] [---])85 ([---] [---])85 ([---] [---])SBP 119 ([---] [---])119 ([---] [---])119 ([---] [---])DBP 71 ([---] [---])71 ([---] [---])71 ([---] [---])MAP 87 ([---] [---])87 ([---] [---])87 ([---] [---]) General: in no acute distressHeart: RRR, nml S1S2. no mrgLungs: CTABObstetric exam:Copious green fluid on valsalva.SVE: 3/[---]/-2FHT: 145 bpm, moderate var, + accels, no decelsToco: ctx q3minSono: cephalic, anterior placentaImaging:Sono 7/1- cephalic, anterior placenta w/ marginal cord insertion, Estimated FW: [---] gm. 7 lb 1 oz 59 %Tile Impression and Plan Disposition: Patient has no history of Cesarean Birth. Disposition: Admit. Reason for admission: SROM - Spontaneous Rupture of Membranes. Is the patient admitted with spontaneous labor?: Yes. Diagnosis SROM. 26y/o G2P[---] at 39wks presenting with SROM and ctx q3mins, found to be 3/[---]/-2 on SVE, admitted to L&D in labor. 1. Admit to labor and delivery for expectant management- Patient grossly ruptured with thin meconium- Consents reviewed and signed in chart- Clears, IVF, continuous toco and FHT- Will initiate pitocin if ctx space- SVE prn2. FHT: Cat 1 tracing - Continue to monitor3. GBS negative: no abx indicated4. Rh negative5. Pain- Desires epidural 6: Gestational Diabetes - RAISS- FS q4hr in latent labor, q2hr in active labor. Discussed with Dr.[---]"
example_format2 = "Attribute,Value,Sentence" \
                              " Gestational Age (weeks),39,26-year-old G2P[---] at 39 weeks..." \
                              "Sex of Fetus,Not mentioned,Information about sex of fetus absent from excerpt." \
                              "Mother's Age (years),26,26-year-old G2P[---] at..." \
                              "Liq. praecox,Absent,Liq. praecox not mentioned." \
                              "Gravidity,2 (G2),26-year-old G2P[---] at..." \
                                "Parity,,26-year-old G2P[---] at..." \
                              " Ruptured membrane,Yes (SROM),Patient presents with SROM (Spontaneous Rupture of Membranes)." \
                              " Pyrexia/Severe Fever,Not mentioned,Pyrexia/Severe Fever absent from excerpt." \
                              " Meconium,Yes (thin),Patient grossly ruptured with thin meconium." \
                              " Gestational hypertension,Yes,Problem list: ...Gestational hypertension..." \
                              " Preeclampsia,Not explicitly mentioned,Preeclampsia not explicitly mentioned." \
                              " Lupus,Not mentioned,Lupus absent from excerpt." \
                              " Antiphospholipid Syndrome,Not mentioned,Antiphospholipid Syndrome absent from excerpt." \
                              " Asthma,Mild intermittent (past),Mild intermittent asthma in childhood." \
                              " Tobacco Usage,Former smoker (<1ppd),History of cigarette smoking..." \
                              " Oligohydramnios,Not mentioned,Oligohydramnios absent from excerpt." \
                              " Cholestasis,Not mentioned,Cholestasis absent from excerpt." \
                              " Chronic Kidney Disease,Not mentioned,Chronic Kidney Disease absent from excerpt." \
                              " IVF,Yes,Clears, IVF, Continuous toco" \
                              " Pregestational Diabetes,Not mentioned,Pregestational Diabetes absent from excerpt." \
                              " Gestational Diabetes,Yes,Gestational diabetes mellitus... / Confirmed"
example_note3 = "Example note: Patient: [---], [---] N MRN: [---] FIN: [---] Age: 38 years Sex: Female DOB: [---] Associated Diagnoses: None Author: [---] MD , [---] Subjective Pain well controlled. Objective Vital Signs and Measurements: Vital Signs (last [---] hrs)__Last Charted____Temp Oral36.5 DegC ([---] [---])SBPL 107mmHG ([---] [---])DBP60 mmHG ([---] [---])SpO2100 % ([---] [---])Weight79.2 kg ([---] [---])Height154.41 cm ([---] [---]). Obstetric Exam Pelvic 5 cm dilated. 100 % effaced. -1 station. Membrane status: ruptured. Amniotic fluid: thinly meconium stained. Baby A fetal evaluation Decelerations: decel to 60s x 4 minutes s/p epidural placement, hands and knees, AROM performed with thin meconium noted, FSE placed, FHR recovered. Tocometer Every 2 minutes. Review / Management Medications: None. Antibotics: None. Pain Relief: Epidural. Assessment and Plan Assessment Plan 38yo G3P[---] at 40+1wk admitted in early labor/oligohydramnios1. Labor- expectant management as contracting on own and making cervical change- SVE q3-4hr or earlier PRN for maternal-fetal indication2. Fetus: deceleration s/p epidural placement, likely from hypotension. now cat I tracing, will continue to monitor3. GBS Positive, ordered for Pen G4. Pain-epidural in placeDiscussed with Dr. [---]"
example_format3 = "Attribute, Value, Sentence/n" \
" Gestational Age (weeks), 40+1, 38yo G3P[---] at 40+1wk admitted.../n" \
" Mother's Age (years), 38, 38yo G3P[---] at.../n" \
" Gravidity, 3 (G3), 38yo G3P[---] at.../n" \
" Parity, Not mentioned, Parity information absent from the excerpt./n" \
" Liq. praecox, Not mentioned, Liq. praecox absent from excerpt./n" \
" Ruptured membrane, Yes, Membrane status: ruptured /n" \
" Pyrexia/Severe Fever, Not mentioned, Pyrexia/Severe Fever absent from excerpt./n" \
" Meconium, Yes (thinly stained), Amniotic fluid: thinly meconium stained./n" \
" Gestational Hypertension, Not mentioned, Gestational Hypertension not mentioned./n" \
" Preeclampsia, Not mentioned, Preeclampsia not mentioned./n" \
" Lupus, Not mentioned, Lupus absent from excerpt./n" \
" Antiphospholipid Syndrome, Not mentioned, Antiphospholipid Syndrome absent from excerpt./n" \
" Asthma, Not mentioned, Asthma absent from excerpt./n" \
" Tobacco Usage, Not mentioned, Tobacco Usage absent from excerpt./n" \
" Oligohydramnios, Yes, admitted in early labor/oligohydramnios/n" \
" Cholestasis, Not mentioned, Cholestasis absent from excerpt./n" \
" Chronic Kidney Disease, Not mentioned, Chronic Kidney Disease absent from excerpt./n" \
" IVF, Not mentioned, IVF not mentioned in excerpt./n" \
" Pregestational Diabetes, Not mentioned, Pregestational Diabetes absent from excerpt./n" \
" Gestational Diabetes, Not mentioned, Gestational Diabetes not mentioned./n"

example_format_admission = "Attribute,Value,Sentence" \
                              "Gravidity,2 (G2),26-year-old G2P[---] at..." \
                                "Parity,,26-year-old G2P[---] at..." \
                              " Ruptured membrane,Yes (SROM),Patient presents with SROM (Spontaneous Rupture of Membranes)." \
                              " Fever,Not mentioned,Fever absent from excerpt." \
                              " Meconium,Yes (thin),Patient grossly ruptured with thin meconium." \
                              " Gestational hypertension,Yes,Problem list: ...Gestational hypertension..." \
                              " Severe Preeclampsia,Not explicitly mentioned,Severe Preeclampsia not explicitly mentioned." \
                              " Intraamniotic Infection,Not explicitly mentioned,Intraamniotic Infection not explicitly mentioned." \
                              " Preeclampsia,Not explicitly mentioned,Preeclampsia not explicitly mentioned." \
                              " Lupus,Not mentioned,Lupus absent from excerpt." \
                              " Antiphospholipid Syndrome,Not mentioned,Antiphospholipid Syndrome absent from excerpt." \
                              " Asthma,Mild intermittent (past),Mild intermittent asthma in childhood." \
                              " Tobacco Usage,Former smoker (<1ppd),History of cigarette smoking..." \
                              " Oligohydramnios,Not mentioned,Oligohydramnios absent from excerpt." \
                              " Polyhydramnios,Not mentioned,Polyhydramnios absent from excerpt." \
                              " Cholestasis,Not mentioned,Cholestasis absent from excerpt." \
                              " Chronic Kidney Disease,Not mentioned,Chronic Kidney Disease absent from excerpt." \
                              " IVF,Yes,Clears, IVF, Continuous toco" \
                              " Pregestational Diabetes,Not mentioned,Pregestational Diabetes absent from excerpt." \
                              " Gestational Diabetes,Yes,Gestational diabetes mellitus... / Confirmed" \
                              " Fetal growth restriction,Not mentioned,Fetal growth restriction absent from excerpt." \
                              " Marginal Cord Insertion,Not mentioned,Marginal Cord Insertion absent from excerpt." \
                              " Velamentous Cord Insertion,Not mentioned,Velamentous Cord Insertion absent from excerpt."

example_format_delivery = "Attribute,Value,Sentence" \
                              " Gestational Age (weeks),39,26-year-old G2P[---] at 39 weeks..." \
                              " Sex of Fetus,Not mentioned,Information about sex of fetus absent from excerpt." \
                              " Mother's Age (years),26,26-year-old G2P[---] at..." \
                              " Parity,,26-year-old G2P[---] at..." \
                              " Ruptured membrane,Yes (SROM),Patient presents with SROM (Spontaneous Rupture of Membranes)." \
                              " Fever,Not mentioned,Fever absent from excerpt." \
                              " Meconium,Yes (thin),Patient grossly ruptured with thin meconium." \
                              " Gestational hypertension,Yes,Problem list: ...Gestational hypertension..." \
                              " Severe Preeclampsia,Not explicitly mentioned,Severe Preeclampsia not explicitly mentioned." \
                              " Intraamniotic Infection,Not explicitly mentioned,Intraamniotic Infection not explicitly mentioned." \
                              " Preeclampsia,Not explicitly mentioned,Preeclampsia not explicitly mentioned."