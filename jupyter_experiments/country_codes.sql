CREATE DATABASE	countries_db;
USE countries_db;

CREATE TABLE country_codes (
iso_alpha2 CHAR(2) PRIMARY KEY,
iso_alpha3 CHAR(3),
iso_numeric INT,
fips CHAR(3),
country VARCHAR(50),
capital VARCHAR(50),
area_km2 FLOAT,
population FLOAT,
continent CHAR(2)
);

INSERT INTO country_codes 
VALUES 
('AF','AFG',4.0,'AF','Afghanistan','Kabul',647500.0,37172386.0,'AS'),
('AL','ALB',8.0,'AL','Albania','Tirana',28748.0,2866376.0,'EU'),
('DZ','DZA',12.0,'AG','Algeria','Algiers',2381740.0,42228429.0,'AF'),
('AS','ASM',16.0,'AQ','American Samoa','Pago Pago',199.0,55465.0,'OC'),
('AD','AND',20.0,'AN','Andorra','Andorra la Vella',468.0,77006.0,'EU'),
('AO','AGO',24.0,'AO','Angola','Luanda',1246700.0,30809762.0,'AF'),
('AI','AIA',660.0,'AV','Anguilla','The Valley',102.0,13254.0,'NA'),
('AQ','ATA',10.0,'AY','Antarctica',NULL,14000000.0,0.0,'AN'),
('AG','ATG',28.0,'AC','Antigua and Barbuda','St. John''s',443.0,96286.0,'NA'),
('AR','ARG',32.0,'AR','Argentina','Buenos Aires',2766890.0,44494502.0,'SA'),
('AM','ARM',51.0,'AM','Armenia','Yerevan',29800.0,2951776.0,'AS'),
('AW','ABW',533.0,'AA','Aruba','Oranjestad',193.0,105845.0,'NA'),
('AU','AUS',36.0,'AS','Australia','Canberra',7686850.0,24992369.0,'OC'),
('AT','AUT',40.0,'AU','Austria','Vienna',83858.0,8847037.0,'EU'),
('AZ','AZE',31.0,'AJ','Azerbaijan','Baku',86600.0,9942334.0,'AS'),
('BS','BHS',44.0,'BF','Bahamas','Nassau',13940.0,385640.0,'NA'),
('BH','BHR',48.0,'BA','Bahrain','Manama',665.0,1569439.0,'AS'),
('BD','BGD',50.0,'BG','Bangladesh','Dhaka',144000.0,161356039.0,'AS'),
('BB','BRB',52.0,'BB','Barbados','Bridgetown',431.0,286641.0,'NA'),
('BY','BLR',112.0,'BO','Belarus','Minsk',207600.0,9485386.0,'EU'),
('BE','BEL',56.0,'BE','Belgium','Brussels',30510.0,11422068.0,'EU'),
('BZ','BLZ',84.0,'BH','Belize','Belmopan',22966.0,383071.0,'NA'),
('BJ','BEN',204.0,'BN','Benin','Porto-Novo',112620.0,11485048.0,'AF'),
('BM','BMU',60.0,'BD','Bermuda','Hamilton',53.0,63968.0,'NA'),
('BT','BTN',64.0,'BT','Bhutan','Thimphu',47000.0,754394.0,'AS'),
('BO','BOL',68.0,'BL','Bolivia','Sucre',1098580.0,11353142.0,'SA'),
('BQ','BES',535.0,NULL,'Bonaire, Sint Eustatius, and Saba',NULL,328.0,18012.0,'NA'),
('BA','BIH',70.0,'BK','Bosnia and Herzegovina','Sarajevo',51129.0,3323929.0,'EU'),
('BW','BWA',72.0,'BC','Botswana','Gaborone',600370.0,2254126.0,'AF'),
('BV','BVT',74.0,'BV','Bouvet Island',NULL,49.0,0.0,'AN'),
('BR','BRA',76.0,'BR','Brazil','Brasilia',8511965.0,209469333.0,'SA'),
('IO','IOT',86.0,'IO','British Indian Ocean Territory','Diego Garcia',60.0,4000.0,'AS'),
('VG','VGB',92.0,'VI','British Virgin Islands','Road Town',153.0,29802.0,'NA'),
('BN','BRN',96.0,'BX','Brunei','Bandar Seri Begawan',5770.0,428962.0,'AS'),
('BG','BGR',100.0,'BU','Bulgaria','Sofia',110910.0,7000039.0,'EU'),
('BF','BFA',854.0,'UV','Burkina Faso','Ouagadougou',274200.0,19751535.0,'AF'),
('BI','BDI',108.0,'BY','Burundi','Gitega',27830.0,11175378.0,'AF'),
('CV','CPV',132.0,'CV','Cabo Verde','Praia',4033.0,543767.0,'AF'),
('KH','KHM',116.0,'CB','Cambodia','Phnom Penh',181040.0,16249798.0,'AS'),
('CM','CMR',120.0,'CM','Cameroon','Yaounde',475440.0,25216237.0,'AF'),
('CA','CAN',124.0,'CA','Canada','Ottawa',9984670.0,37058856.0,'NA'),
('KY','CYM',136.0,'CJ','Cayman Islands','George Town',262.0,64174.0,'NA'),
('CF','CAF',140.0,'CT','Central African Republic','Bangui',622984.0,4666377.0,'AF'),
('TD','TCD',148.0,'CD','Chad','N''Djamena',1284000.0,15477751.0,'AF'),
('CL','CHL',152.0,'CI','Chile','Santiago',756950.0,18729160.0,'SA'),
('CN','CHN',156.0,'CH','China','Beijing',9596960.0,1411778724.0,'AS'),
('CX','CXR',162.0,'KT','Christmas Island','Flying Fish Cove',135.0,1500.0,'OC'),
('CC','CCK',166.0,'CK','Cocos (Keeling) Islands','West Island',14.0,628.0,'AS'),
('CO','COL',170.0,'CO','Colombia','Bogota',1138910.0,49648685.0,'SA'),
('KM','COM',174.0,'CN','Comoros','Moroni',2170.0,832322.0,'AF'),
('CG','COG',178.0,'CF','Congo Republic','Brazzaville',342000.0,5244363.0,'AF'),
('CK','COK',184.0,'CW','Cook Islands','Avarua',240.0,21388.0,'OC'),
('CR','CRI',188.0,'CS','Costa Rica','San Jose',51100.0,4999441.0,'NA'),
('HR','HRV',191.0,'HR','Croatia','Zagreb',56542.0,3871833.0,'EU'),
('CU','CUB',192.0,'CU','Cuba','Havana',110860.0,11338138.0,'NA'),
('CW','CUW',531.0,'UC','Curaçao','Willemstad',444.0,159849.0,'NA'),
('CY','CYP',196.0,'CY','Cyprus','Nicosia',9250.0,1189265.0,'EU'),
('CZ','CZE',203.0,'EZ','Czechia','Prague',78866.0,10625695.0,'EU'),
('CD','COD',180.0,'CG','DR Congo','Kinshasa',2345410.0,84068091.0,'AF'),
('DK','DNK',208.0,'DA','Denmark','Copenhagen',43094.0,5797446.0,'EU'),
('DJ','DJI',262.0,'DJ','Djibouti','Djibouti',23000.0,958920.0,'AF'),
('DM','DMA',212.0,'DO','Dominica','Roseau',754.0,71625.0,'NA'),
('DO','DOM',214.0,'DR','Dominican Republic','Santo Domingo',48730.0,10627165.0,'NA'),
('EC','ECU',218.0,'EC','Ecuador','Quito',283560.0,17084357.0,'SA'),
('EG','EGY',818.0,'EG','Egypt','Cairo',1001450.0,98423595.0,'AF'),
('SV','SLV',222.0,'ES','El Salvador','San Salvador',21040.0,6420744.0,'NA'),
('GQ','GNQ',226.0,'EK','Equatorial Guinea','Malabo',28051.0,1308974.0,'AF'),
('ER','ERI',232.0,'ER','Eritrea','Asmara',121320.0,6209262.0,'AF'),
('EE','EST',233.0,'EN','Estonia','Tallinn',45226.0,1320884.0,'EU'),
('SZ','SWZ',748.0,'WZ','Eswatini','Mbabane',17363.0,1136191.0,'AF'),
('ET','ETH',231.0,'ET','Ethiopia','Addis Ababa',1127127.0,109224559.0,'AF'),
('FK','FLK',238.0,'FK','Falkland Islands','Stanley',12173.0,2638.0,'SA'),
('FO','FRO',234.0,'FO','Faroe Islands','Torshavn',1399.0,48497.0,'EU'),
('FJ','FJI',242.0,'FJ','Fiji','Suva',18270.0,883483.0,'OC'),
('FI','FIN',246.0,'FI','Finland','Helsinki',337030.0,5518050.0,'EU'),
('FR','FRA',250.0,'FR','France','Paris',547030.0,66987244.0,'EU'),
('GF','GUF',254.0,'FG','French Guiana','Cayenne',91000.0,195506.0,'SA'),
('PF','PYF',258.0,'FP','French Polynesia','Papeete',4167.0,277679.0,'OC'),
('TF','ATF',260.0,'FS','French Southern Territories','Port-aux-Francais',7829.0,140.0,'AN'),
('GA','GAB',266.0,'GB','Gabon','Libreville',267667.0,2119275.0,'AF'),
('GE','GEO',268.0,'GG','Georgia','Tbilisi',69700.0,3731000.0,'AS'),
('DE','DEU',276.0,'GM','Germany','Berlin',357021.0,82927922.0,'EU'),
('GH','GHA',288.0,'GH','Ghana','Accra',239460.0,29767108.0,'AF'),
('GI','GIB',292.0,'GI','Gibraltar','Gibraltar',6.5,33718.0,'EU'),
('GR','GRC',300.0,'GR','Greece','Athens',131940.0,10727668.0,'EU'),
('GL','GRL',304.0,'GL','Greenland','Nuuk',2166086.0,56025.0,'NA'),
('GD','GRD',308.0,'GJ','Grenada','St. George''s',344.0,111454.0,'NA'),
('GP','GLP',312.0,'GP','Guadeloupe','Basse-Terre',1780.0,443000.0,'NA'),
('GU','GUM',316.0,'GQ','Guam','Hagatna',549.0,165768.0,'OC'),
('GT','GTM',320.0,'GT','Guatemala','Guatemala City',108890.0,17247807.0,'NA'),
('GG','GGY',831.0,'GK','Guernsey','St Peter Port',78.0,65228.0,'EU'),
('GN','GIN',324.0,'GV','Guinea','Conakry',245857.0,12414318.0,'AF'),
('GW','GNB',624.0,'PU','Guinea-Bissau','Bissau',36120.0,1874309.0,'AF'),
('GY','GUY',328.0,'GY','Guyana','Georgetown',214970.0,779004.0,'SA'),
('HT','HTI',332.0,'HA','Haiti','Port-au-Prince',27750.0,11123176.0,'NA'),
('HM','HMD',334.0,'HM','Heard and McDonald Islands',NULL,412.0,0.0,'AN'),
('HN','HND',340.0,'HO','Honduras','Tegucigalpa',112090.0,9587522.0,'NA'),
('HK','HKG',344.0,'HK','Hong Kong','Hong Kong',1092.0,7451000.0,'AS'),
('HU','HUN',348.0,'HU','Hungary','Budapest',93030.0,9768785.0,'EU'),
('IS','ISL',352.0,'IC','Iceland','Reykjavik',103000.0,353574.0,'EU'),
('IN','IND',356.0,'IN','India','New Delhi',3287590.0,1352617328.0,'AS'),
('ID','IDN',360.0,'ID','Indonesia','Jakarta',1919440.0,267663435.0,'AS'),
('IR','IRN',364.0,'IR','Iran','Tehran',1648000.0,81800269.0,'AS'),
('IQ','IRQ',368.0,'IZ','Iraq','Baghdad',437072.0,38433600.0,'AS'),
('IE','IRL',372.0,'EI','Ireland','Dublin',70280.0,4853506.0,'EU'),
('IM','IMN',833.0,'IM','Isle of Man','Douglas',572.0,84077.0,'EU'),
('IL','ISR',376.0,'IS','Israel','Jerusalem',20770.0,8883800.0,'AS'),
('IT','ITA',380.0,'IT','Italy','Rome',301230.0,60431283.0,'EU'),
('CI','CIV',384.0,'IV','Ivory Coast','Yamoussoukro',322460.0,25069229.0,'AF'),
('JM','JAM',388.0,'JM','Jamaica','Kingston',10991.0,2934855.0,'NA'),
('JP','JPN',392.0,'JA','Japan','Tokyo',377835.0,126529100.0,'AS'),
('JE','JEY',832.0,'JE','Jersey','Saint Helier',116.0,90812.0,'EU'),
('JO','JOR',400.0,'JO','Jordan','Amman',92300.0,9956011.0,'AS'),
('KZ','KAZ',398.0,'KZ','Kazakhstan','Nur-Sultan',2717300.0,18276499.0,'AS'),
('KE','KEN',404.0,'KE','Kenya','Nairobi',582650.0,51393010.0,'AF'),
('KI','KIR',296.0,'KR','Kiribati','Tarawa',811.0,115847.0,'OC'),
('XK','XKX',0.0,'KV','Kosovo','Pristina',10908.0,1845300.0,'EU'),
('KW','KWT',414.0,'KU','Kuwait','Kuwait City',17820.0,4137309.0,'AS'),
('KG','KGZ',417.0,'KG','Kyrgyzstan','Bishkek',198500.0,6315800.0,'AS'),
('LA','LAO',418.0,'LA','Laos','Vientiane',236800.0,7061507.0,'AS'),
('LV','LVA',428.0,'LG','Latvia','Riga',64589.0,1926542.0,'EU'),
('LB','LBN',422.0,'LE','Lebanon','Beirut',10400.0,6848925.0,'AS'),
('LS','LSO',426.0,'LT','Lesotho','Maseru',30355.0,2108132.0,'AF'),
('LR','LBR',430.0,'LI','Liberia','Monrovia',111370.0,4818977.0,'AF'),
('LY','LBY',434.0,'LY','Libya','Tripoli',1759540.0,6678567.0,'AF'),
('LI','LIE',438.0,'LS','Liechtenstein','Vaduz',160.0,37910.0,'EU'),
('LT','LTU',440.0,'LH','Lithuania','Vilnius',65200.0,2789533.0,'EU'),
('LU','LUX',442.0,'LU','Luxembourg','Luxembourg',2586.0,607728.0,'EU'),
('MO','MAC',446.0,'MC','Macao','Macao',254.0,631636.0,'AS'),
('MG','MDG',450.0,'MA','Madagascar','Antananarivo',587040.0,26262368.0,'AF'),
('MW','MWI',454.0,'MI','Malawi','Lilongwe',118480.0,17563749.0,'AF'),
('MY','MYS',458.0,'MY','Malaysia','Kuala Lumpur',329750.0,31528585.0,'AS'),
('MV','MDV',462.0,'MV','Maldives','Male',300.0,515696.0,'AS'),
('ML','MLI',466.0,'ML','Mali','Bamako',1240000.0,19077690.0,'AF'),
('MT','MLT',470.0,'MT','Malta','Valletta',316.0,483530.0,'EU'),
('MH','MHL',584.0,'RM','Marshall Islands','Majuro',181.3,58413.0,'OC'),
('MQ','MTQ',474.0,'MB','Martinique','Fort-de-France',1100.0,432900.0,'NA'),
('MR','MRT',478.0,'MR','Mauritania','Nouakchott',1030700.0,4403319.0,'AF'),
('MU','MUS',480.0,'MP','Mauritius','Port Louis',2040.0,1265303.0,'AF'),
('YT','MYT',175.0,'MF','Mayotte','Mamoudzou',374.0,279471.0,'AF'),
('MX','MEX',484.0,'MX','Mexico','Mexico City',1972550.0,126190788.0,'NA'),
('FM','FSM',583.0,'FM','Micronesia','Palikir',702.0,112640.0,'OC'),
('MD','MDA',498.0,'MD','Moldova','Chisinau',33843.0,3545883.0,'EU'),
('MC','MCO',492.0,'MN','Monaco','Monaco',1.9,38682.0,'EU'),
('MN','MNG',496.0,'MG','Mongolia','Ulaanbaatar',1565000.0,3170208.0,'AS'),
('ME','MNE',499.0,'MJ','Montenegro','Podgorica',14026.0,622345.0,'EU'),
('MS','MSR',500.0,'MH','Montserrat','Plymouth',102.0,9341.0,'NA'),
('MA','MAR',504.0,'MO','Morocco','Rabat',446550.0,36029138.0,'AF'),
('MZ','MOZ',508.0,'MZ','Mozambique','Maputo',801590.0,29495962.0,'AF'),
('MM','MMR',104.0,'BM','Myanmar','Nay Pyi Taw',678500.0,53708395.0,'AS'),
('NA','NAM',516.0,'WA','Namibia','Windhoek',825418.0,2448255.0,'AF'),
('NR','NRU',520.0,'NR','Nauru','Yaren',21.0,12704.0,'OC'),
('NP','NPL',524.0,'NP','Nepal','Kathmandu',140800.0,28087871.0,'AS'),
('NC','NCL',540.0,'NC','New Caledonia','Noumea',19060.0,284060.0,'OC'),
('NZ','NZL',554.0,'NZ','New Zealand','Wellington',268680.0,4885500.0,'OC'),
('NI','NIC',558.0,'NU','Nicaragua','Managua',129494.0,6465513.0,'NA'),
('NE','NER',562.0,'NG','Niger','Niamey',1267000.0,22442948.0,'AF'),
('NG','NGA',566.0,'NI','Nigeria','Abuja',923768.0,195874740.0,'AF'),
('NU','NIU',570.0,'NE','Niue','Alofi',260.0,2166.0,'OC'),
('NF','NFK',574.0,'NF','Norfolk Island','Kingston',34.6,1828.0,'OC'),
('KP','PRK',408.0,'KN','North Korea','Pyongyang',120540.0,25549819.0,'AS'),
('MK','MKD',807.0,'MK','North Macedonia','Skopje',25333.0,2082958.0,'EU'),
('MP','MNP',580.0,'CQ','Northern Mariana Islands','Saipan',477.0,56882.0,'OC'),
('NO','NOR',578.0,'NO','Norway','Oslo',324220.0,5314336.0,'EU'),
('OM','OMN',512.0,'MU','Oman','Muscat',212460.0,4829483.0,'AS'),
('PK','PAK',586.0,'PK','Pakistan','Islamabad',803940.0,212215030.0,'AS'),
('PW','PLW',585.0,'PS','Palau','Melekeok',458.0,17907.0,'OC'),
('PS','PSE',275.0,'WE','Palestine','East Jerusalem',5970.0,4569087.0,'AS'),
('PA','PAN',591.0,'PM','Panama','Panama City',78200.0,4176873.0,'NA'),
('PG','PNG',598.0,'PP','Papua New Guinea','Port Moresby',462840.0,8606316.0,'OC'),
('PY','PRY',600.0,'PA','Paraguay','Asuncion',406750.0,6956071.0,'SA'),
('PE','PER',604.0,'PE','Peru','Lima',1285220.0,31989256.0,'SA'),
('PH','PHL',608.0,'RP','Philippines','Manila',300000.0,106651922.0,'AS'),
('PN','PCN',612.0,'PC','Pitcairn Islands','Adamstown',47.0,46.0,'OC'),
('PL','POL',616.0,'PL','Poland','Warsaw',312685.0,37978548.0,'EU'),
('PT','PRT',620.0,'PO','Portugal','Lisbon',92391.0,10281762.0,'EU'),
('PR','PRI',630.0,'RQ','Puerto Rico','San Juan',9104.0,3195153.0,'NA'),
('QA','QAT',634.0,'QA','Qatar','Doha',11437.0,2781677.0,'AS'),
('RO','ROU',642.0,'RO','Romania','Bucharest',237500.0,19473936.0,'EU'),
('RU','RUS',643.0,'RS','Russia','Moscow',17100000.0,144478050.0,'EU'),
('RW','RWA',646.0,'RW','Rwanda','Kigali',26338.0,12301939.0,'AF'),
('RE','REU',638.0,'RE','Réunion','Saint-Denis',2517.0,776948.0,'AF'),
('BL','BLM',652.0,'TB','Saint Barthélemy','Gustavia',21.0,8450.0,'NA'),
('SH','SHN',654.0,'SH','Saint Helena','Jamestown',410.0,7460.0,'AF'),
('LC','LCA',662.0,'ST','Saint Lucia','Castries',616.0,181889.0,'NA'),
('MF','MAF',663.0,'RN','Saint Martin','Marigot',53.0,37264.0,'NA'),
('PM','SPM',666.0,'SB','Saint Pierre and Miquelon','Saint-Pierre',242.0,7012.0,'NA'),
('WS','WSM',882.0,'WS','Samoa','Apia',2944.0,196130.0,'OC'),
('SM','SMR',674.0,'SM','San Marino','San Marino',61.2,33785.0,'EU'),
('SA','SAU',682.0,'SA','Saudi Arabia','Riyadh',1960582.0,33699947.0,'AS'),
('SN','SEN',686.0,'SG','Senegal','Dakar',196190.0,15854360.0,'AF'),
('RS','SRB',688.0,'RI','Serbia','Belgrade',88361.0,6982084.0,'EU'),
('SC','SYC',690.0,'SE','Seychelles','Victoria',455.0,96762.0,'AF'),
('SL','SLE',694.0,'SL','Sierra Leone','Freetown',71740.0,7650154.0,'AF'),
('SG','SGP',702.0,'SN','Singapore','Singapore',692.7,5638676.0,'AS'),
('SX','SXM',534.0,'NN','Sint Maarten','Philipsburg',21.0,40654.0,'NA'),
('SK','SVK',703.0,'LO','Slovakia','Bratislava',48845.0,5447011.0,'EU'),
('SI','SVN',705.0,'SI','Slovenia','Ljubljana',20273.0,2067372.0,'EU'),
('SB','SLB',90.0,'BP','Solomon Islands','Honiara',28450.0,652858.0,'OC'),
('SO','SOM',706.0,'SO','Somalia','Mogadishu',637657.0,15008154.0,'AF'),
('ZA','ZAF',710.0,'SF','South Africa','Pretoria',1219912.0,57779622.0,'AF'),
('GS','SGS',239.0,'SX','South Georgia and South Sandwich Islands','Grytviken',3903.0,30.0,'AN'),
('KR','KOR',410.0,'KS','South Korea','Seoul',98480.0,51635256.0,'AS'),
('SS','SSD',728.0,'OD','South Sudan','Juba',644329.0,8260490.0,'AF'),
('ES','ESP',724.0,'SP','Spain','Madrid',504782.0,46723749.0,'EU'),
('LK','LKA',144.0,'CE','Sri Lanka','Colombo',65610.0,21670000.0,'AS'),
('KN','KNA',659.0,'SC','St Kitts and Nevis','Basseterre',261.0,52441.0,'NA'),
('VC','VCT',670.0,'VC','St Vincent and Grenadines','Kingstown',389.0,110211.0,'NA'),
('SD','SDN',729.0,'SU','Sudan','Khartoum',1861484.0,41801533.0,'AF'),
('SR','SUR',740.0,'NS','Suriname','Paramaribo',163270.0,575991.0,'SA'),
('SJ','SJM',744.0,'SV','Svalbard and Jan Mayen','Longyearbyen',62049.0,2550.0,'EU'),
('SE','SWE',752.0,'SW','Sweden','Stockholm',449964.0,10183175.0,'EU'),
('CH','CHE',756.0,'SZ','Switzerland','Bern',41290.0,8516543.0,'EU'),
('SY','SYR',760.0,'SY','Syria','Damascus',185180.0,16906283.0,'AS'),
('ST','STP',678.0,'TP','São Tomé and Príncipe','Sao Tome',1001.0,197700.0,'AF'),
('TW','TWN',158.0,'TW','Taiwan','Taipei',35980.0,23451837.0,'AS'),
('TJ','TJK',762.0,'TI','Tajikistan','Dushanbe',143100.0,9100837.0,'AS'),
('TZ','TZA',834.0,'TZ','Tanzania','Dodoma',945087.0,56318348.0,'AF'),
('TH','THA',764.0,'TH','Thailand','Bangkok',514000.0,69428524.0,'AS'),
('GM','GMB',270.0,'GA','The Gambia','Banjul',11300.0,2280102.0,'AF'),
('NL','NLD',528.0,'NL','The Netherlands','Amsterdam',41526.0,17231017.0,'EU'),
('TL','TLS',626.0,'TT','Timor-Leste','Dili',15007.0,1267972.0,'OC'),
('TG','TGO',768.0,'TO','Togo','Lome',56785.0,7889094.0,'AF'),
('TK','TKL',772.0,'TL','Tokelau',NULL,10.0,1466.0,'OC'),
('TO','TON',776.0,'TN','Tonga','Nuku''alofa',748.0,103197.0,'OC'),
('TT','TTO',780.0,'TD','Trinidad and Tobago','Port of Spain',5128.0,1389858.0,'NA'),
('TN','TUN',788.0,'TS','Tunisia','Tunis',163610.0,11565204.0,'AF'),
('TR','TUR',792.0,'TU','Turkey','Ankara',780580.0,82319724.0,'AS'),
('TM','TKM',795.0,'TX','Turkmenistan','Ashgabat',488100.0,5850908.0,'AS'),
('TC','TCA',796.0,'TK','Turks and Caicos Islands','Cockburn Town',430.0,37665.0,'NA'),
('TV','TUV',798.0,'TV','Tuvalu','Funafuti',26.0,11508.0,'OC'),
('UM','UMI',581.0,NULL,'U.S. Outlying Islands',NULL,0.0,0.0,'OC'),
('VI','VIR',850.0,'VQ','U.S. Virgin Islands','Charlotte Amalie',352.0,106977.0,'NA'),
('UG','UGA',800.0,'UG','Uganda','Kampala',236040.0,42723139.0,'AF'),
('UA','UKR',804.0,'UP','Ukraine','Kyiv',603700.0,44622516.0,'EU'),
('AE','ARE',784.0,'AE','United Arab Emirates','Abu Dhabi',82880.0,9630959.0,'AS'),
('GB','GBR',826.0,'UK','United Kingdom','London',244820.0,66488991.0,'EU'),
('US','USA',840.0,'US','United States','Washington',9629091.0,327167434.0,'NA'),
('UY','URY',858.0,'UY','Uruguay','Montevideo',176220.0,3449299.0,'SA'),
('UZ','UZB',860.0,'UZ','Uzbekistan','Tashkent',447400.0,32955400.0,'AS'),
('VU','VUT',548.0,'NH','Vanuatu','Port Vila',12200.0,292680.0,'OC'),
('VA','VAT',336.0,'VT','Vatican City','Vatican City',0.4,921.0,'EU'),
('VE','VEN',862.0,'VE','Venezuela','Caracas',912050.0,28870195.0,'SA'),
('VN','VNM',704.0,'VM','Vietnam','Hanoi',329560.0,95540395.0,'AS'),
('WF','WLF',876.0,'WF','Wallis and Futuna','Mata Utu',274.0,16025.0,'OC'),
('EH','ESH',732.0,'WI','Western Sahara','El-Aaiun',266000.0,273008.0,'AF'),
('YE','YEM',887.0,'YM','Yemen','Sanaa',527970.0,28498687.0,'AS'),
('ZM','ZMB',894.0,'ZA','Zambia','Lusaka',752614.0,17351822.0,'AF'),
('ZW','ZWE',716.0,'ZI','Zimbabwe','Harare',390580.0,14439018.0,'AF'),
('AX','ALA',248.0,NULL,'Åland','Mariehamn',1580.0,26711.0,'EU');

SELECT * INTO OUTFILE '/country_codes.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM countries_db.country_codes;
