
import sqlite3


df = [
    (1, "AETA"), (2, "AGLIPAYAN"), (3, "AGUTAYNEN"), (4, "AKLANON"), (5, "ALANGAN"),
    (6, "APPLAI"), (7, "ATA"), (8, "BADJAO"), (9, "BAGOBO"), (10, "BAKUN"),
    (11, "BALANGAO"), (12, "BANTUAS"), (13, "BANTOANON"), (14, "BATAK"), (15, "BICOLANO"),
    (16, "BLAAN"), (17, "BONTOK"), (18, "BUHID"), (19, "BUKIDNON"), (20, "BUTUANON"),
    (21, "CAPIZNON"), (22, "CEBUANO"), (23, "CHAVACANO"), (24, "CUYUNON"), (25, "GADDANG"),
    (26, "HANUNUO"), (27, "HIGAONON"), (28, "IBALOI"), (29, "IBANAG"), (30, "IBATAN"),
    (31, "IFUGAO"), (32, "IGOROT"), (33, "ILOCANO"), (34, "ILONGGO"), (35, "IRANUN"),
    (36, "IRAYA"), (37, "ISNAG"), (38, "ISNEG"), (39, "ITAWIS"), (40, "ITNEG"),
    (41, "IVATAN"), (42, "IWAK"), (43, "JAMA MAPUN"), (44, "KALAGAN"), (45, "KALINGA"),
    (46, "KANKANAEY"), (47, "KAPAMPANGAN"), (48, "KINARAY-A"), (49, "MAGUINDANAON"), (50, "MAMANWA"),
    (51, "MANDAYA"), (52, "MANGYAN"), (53, "MANOBO"), (54, "MANSAKA"), (55, "MARANAO"),
    (56, "MASBATEÑO"), (57, "MATIGSALUG"), (58, "MOLBOG"), (59, "PALA'WAN"), (60, "PANGASINENSE"),
    (61, "ROMBLOMANON"), (62, "SAMA"), (63, "SANGIL"), (64, "SUBANEN"), (65, "SURIGAONON"),
    (66, "TADYAWAN"), (67, "TAGABAWA"), (68, "TAGAKAULO"), (69, "TAGALOG"), (70, "TAGBANWA"),
    (71, "TAUSUG"), (72, "TBOLI"), (73, "TIRURAY"), (74, "WARAY"), (75, "YAKAN"),
    (76, "YOGAD"), (77, "ZAMBAL")
]


db=sqlite3.connect("./BIMS/db/db.sqlite3")
cur=db.cursor()



for i in df:
   sql=f'Insert into rbi_ethnicity (description,code) values (?,?)'
   cur.execute(sql,(i[1],i[0]))
   db.commit()
print('DOne')