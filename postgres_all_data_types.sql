-- PostgreSQL Data Generation Script
-- Generated on: 2025-09-16T18:21:59.931649
-- Records: 15
-- Batch size: 5
-- NOT NULL columns: SMALLINT, CHAR, JSON
-- Always NULL columns: None

DROP TYPE IF EXISTS mood_enum CASCADE;
CREATE TYPE mood_enum AS ENUM ('happy', 'sad', 'neutral');

DROP TABLE IF EXISTS "all_types_table";

CREATE TABLE "all_types_table" (
  "id" SERIAL PRIMARY KEY,
  "col_smallint_0" SMALLINT NOT NULL,
  "col_integer_1" INTEGER,
  "col_bigint_2" BIGINT,
  "col_decimal_3" DECIMAL(10,2),
  "col_numeric_4" NUMERIC(8,3),
  "col_real_5" REAL,
  "col_double_precision_6" DOUBLE PRECISION,
  "col_serial_7" SERIAL,
  "col_smallserial_8" SMALLSERIAL,
  "col_bigserial_9" BIGSERIAL,
  "col_money_10" MONEY,
  "col_char_11" CHAR(10) NOT NULL,
  "col_varchar_12" VARCHAR(255),
  "col_text_13" TEXT,
  "col_bytea_14" BYTEA,
  "col_date_15" DATE,
  "col_time_16" TIME,
  "col_timetz_17" TIME WITH TIME ZONE,
  "col_timestamp_18" TIMESTAMP,
  "col_timestamptz_19" TIMESTAMP WITH TIME ZONE,
  "col_interval_20" INTERVAL,
  "col_boolean_21" BOOLEAN,
  "col_enum_22" mood_enum,
  "col_point_23" POINT,
  "col_line_24" LINE,
  "col_lseg_25" LSEG,
  "col_box_26" BOX,
  "col_path_27" PATH,
  "col_polygon_28" POLYGON,
  "col_circle_29" CIRCLE,
  "col_cidr_30" CIDR,
  "col_inet_31" INET,
  "col_macaddr_32" MACADDR,
  "col_macaddr8_33" MACADDR8,
  "col_bit_34" BIT(8),
  "col_varbit_35" BIT VARYING(16),
  "col_tsvector_36" TSVECTOR,
  "col_tsquery_37" TSQUERY,
  "col_uuid_38" UUID,
  "col_xml_39" XML,
  "col_json_40" JSON NOT NULL,
  "col_jsonb_41" JSONB,
  "col_int_array_42" INTEGER[],
  "col_text_array_43" TEXT[],
  "col_int4range_44" INT4RANGE,
  "col_tsrange_45" TSRANGE
);

INSERT INTO "all_types_table" ("col_smallint_0", "col_integer_1", "col_bigint_2", "col_decimal_3", "col_numeric_4", "col_real_5", "col_double_precision_6", "col_money_10", "col_char_11", "col_varchar_12", "col_text_13", "col_bytea_14", "col_date_15", "col_time_16", "col_timetz_17", "col_timestamp_18", "col_timestamptz_19", "col_interval_20", "col_boolean_21", "col_enum_22", "col_point_23", "col_line_24", "col_lseg_25", "col_box_26", "col_path_27", "col_polygon_28", "col_circle_29", "col_cidr_30", "col_inet_31", "col_macaddr_32", "col_macaddr8_33", "col_bit_34", "col_varbit_35", "col_tsvector_36", "col_tsquery_37", "col_uuid_38", "col_xml_39", "col_json_40", "col_jsonb_41", "col_int_array_42", "col_text_array_43", "col_int4range_44", "col_tsrange_45") VALUES
(20041, NULL, 1775136869596699998, 3781674.76, 51507.606, 106471290.847373, -472330836.647908, NULL, 'YzGjUObSPL', 'Past two tax better.', 'Born leader plan still change prevent.
After that most buy adult prove key. Hit go item together hope science step ready.
Cover most management mouth anything end marriage. Special poor daughter various above check charge. Whether term decade sell eight crime difference information.
Foreign message case note way important game manage.
Choose knowledge develop seem on rest myself same. Indeed agreement perform nor. Instead south actually.
Today generation effect director since issue. Style full catch really sing.
Option cut rate partner.
Use husband word. Coach art talk half hold model weight. Work box life tonight rather. Throughout wind say ball computer how marriage exactly.
On quality employee common. Ago environment large Republican simple full movement.
Manage recently end these. Official father hope media risk certainly grow day.
Pull friend head can group production few.', '\xa5d6deb4704a39eebdbf41242bea5add3276fa8d29417e8d8ed6aaa6d17d9d4a', '1985-05-08 00:00:00', '1900-01-01 02:43:59', '00:58:39.552151+00', '2022-09-30 04:28:27', '2023-01-03 20:45:49+00', '177 days', True, 'happy', '(8.085076,-85.364733)', '{-1198181362.51581,7511093283.45766,-62439418586.514}', '[(-59.025206,-68.295334),(109.281402,-23.8699275)]', NULL, NULL, NULL, '<(92.383911,62.1842235),70>', '140.228.0.0/24', NULL, '1e:0c:d7:bf:4e:27', '6e:7a:47:e9:bd:62:e9:66', B'11110111', NULL, '''experience:1 care:2''', '''Congress & especially''', 'c917b566-dceb-454e-8d07-63d22cc8a9cf', '<person><name>Keith Skinner</name><age>71</age></person>', '{"name": "Lee Silva", "age": 61, "city": "Rodriguezview"}', NULL, '{24,67,73}', '{"white","those","look"}', '[18,76)', '[2025-06-24 14:13:23,2025-08-13 13:46:36)'),
(-26241, -1179069306, 4751358723839187823, NULL, 36800.653, -96064107.1457805, -872750370.412297, '$88135.10', 'fVZaVYeqfB', 'Discuss each travel political spring future set.', 'Soon since leg. Practice determine play bit decade. Woman magazine cold land wife try. Suggest real Mrs.
Early however seek there. Positive agreement others particular field hope only. Force recently policy pretty admit they election. Attention unit opportunity fish see talk.
Wide rise might skin full word eat. Find people upon brother TV word anyone million. Focus lead safe it tonight.
Treatment along simply raise page management.
Tax reach key.
Popular very scientist training movement pick some offer. Enjoy almost art hotel. Walk beyond risk adult concern.
Citizen station hard question magazine walk just lose. Church star service plant anything policy.
Senior alone above each. Possible election large development item. Evidence old central. Mind door front American news modern.
Fall data look store end training. Place must ground recent which heart.
Article major not story hot. Skill commercial about although field. That near like already.', '\x2c2fbb40c40bb61cb617bd8b656cdc53fff18e6e9a3716ba49d1b587aedc236e', '1995-02-15 00:00:00', '1900-01-01 07:16:51', '04:12:53.855700+00', '2020-11-16 04:13:51', '2024-07-29 16:43:15+00', '120 days', False, 'sad', '(64.889355,68.3366925)', '{-7946.27458543759,6567556452407.15,-83.6879493507151}', '[(52.988152,87.063113),(107.750974,-52.2763725)]', '(44.250805,45.4129655),(-131.189343,-23.7153645)', '[(-141.033774,70.8841965),(15.060369,-52.4562025)]', '((6.163407,17.714094),(119.672321,-74.881229),(-103.787077,-74.793194))', '<(-162.904535,-9.7810295),64>', '69.107.0.0/24', '84.168.148.74', NULL, '88:cc:5b:ff:48:4e:4b:92', B'11101111', B'1100100101100001', '''eat:1 peace:2''', '''billion & word''', '96e18909-c6fe-4cb3-82bc-64ed7f52fbe9', '<person><name>Alyssa Johnson</name><age>51</age></person>', '{"name": "Roger Miller", "age": 44, "city": "Estesville"}', '{"id": 238, "data": "action", "active": true}', '{15,77,100}', '{"land","institution","stock"}', '[36,44)', '[2025-06-30 14:33:23,2025-08-15 10:11:11)'),
(8104, NULL, -3642388270108026813, 39376775.61, 86482.437, 7424.7759414895, 93555603.8823173, '$52700.60', 'XxddJtbEdJ', 'Professor society month myself discuss standard more tree.', 'Worker unit rather. Present significant throughout soldier together. Case future civil their.
Finally instead car. Particular however job land population true. Color set too identify subject. Green relate agreement when high would.
Behind including help police sure among. Within us serve range technology town.
Speech lay east fight long. Unit her personal foreign main. Suddenly open contain change.
Note region before poor however. Enough today charge success. Often sea attorney.
Expect any bag speech. Money popular response along week blood question.
Card war do offer culture. Eat sea sense security imagine. Possible simply interest at claim song.
Drug theory thank fish. Treat continue thousand hour customer.
When often building land production success. North conference special on sister history. Own peace door together win opportunity.
Here respond tax American late second lawyer. Site party or support.', '\x038201690bf17603aedf9ff1467b28794f3bd382011ec70b8c3d56943a2c2606', '1971-11-11 00:00:00', '1900-01-01 10:00:10', '11:48:41.623929+00', '2021-02-27 08:46:01', '2023-06-22 09:30:56+00', '177 days', False, 'neutral', '(140.800458,-14.7897375)', NULL, '[(46.054530,-72.221488),(36.310849,-39.0365055)]', '(95.592508,28.0648235),(104.771201,59.280642)', '[(98.705826,31.5511195),(30.041201,44.584959)]', '((-61.447690,85.4561255),(-83.674580,-43.225178),(46.965250,44.2593925))', '<(7.023618,-19.555878),83>', '130.193.0.0/24', '155.45.172.48', 'f0:da:c6:07:b8:5d', '0d:73:b2:ba:f1:e8:be:09', NULL, B'111001000001111', '''thus:1 doctor:2''', '''human & discussion''', 'eb5e8d26-b0e1-43ab-92ae-954dab09c733', '<person><name>Robert Wright</name><age>65</age></person>', '{"name": "Steven Perez", "age": 56, "city": "Lake Sarah"}', '{"id": 362, "data": "leave", "active": false}', '{94,91,78}', '{"product","agree","against"}', '[60,83)', '[2025-02-18 16:28:55,2025-05-31 09:18:03)'),
(8968, -1777979996, 7898144702359494629, NULL, 51881.650, -4.14096039609437, 439604501.787351, '$66687.54', 'ghtYAMtXym', 'Detail result above.', 'Style force eat management seat. Call beat music ability beautiful. These he situation early example realize manage such.
Decide option hour PM appear. Reach remain your. Account maybe financial including last cup than.
Possible treat anyone eat discussion.
Road his fill. Accept rise condition majority second.
Study far how remain manager.
Mrs physical tell site ball. Yes mission method black instead simply.
Necessary amount station current form. Discuss spend little follow.
Explain ok anyone. West could moment. Hear consumer event likely song plan cup yard. Important baby your score financial there.
Eight thank individual compare finally. Lay game south.
Maybe order entire age too dog woman institution. Six office method none yes alone. Population glass free response help.
Floor door citizen and reduce leader occur. Cost some ever game. Service how short determine stock perhaps.
Manage situation easy laugh. Management discuss treat race. Leg reveal quality father avoid fine suddenly.', '\xbe58c01c05ad1865e6e72b2df1ecd4809d78a1567368a1f3522d425c2ea5a525', '1983-03-08 00:00:00', '1900-01-01 14:09:02', '09:45:16.954281+00', NULL, '2020-04-16 00:24:52+00', '205 days', True, 'sad', '(-28.779677,22.560294)', '{-355671253471.572,-69910.8427513413,52423678261.664}', '[(159.223394,-26.4053565),(56.323099,72.489939)]', '(113.972534,-29.0395395),(-50.354321,-36.4722345)', '[(68.435602,-0.519142),(-38.224625,23.3864325)]', '((-179.301881,-5.4291185),(0.347955,-44.0181765),(-57.431770,-32.8146705))', '<(87.646234,-48.024201),8>', '62.168.0.0/24', '146.236.137.50', '6e:6e:10:b3:e4:7c', NULL, B'00010111', B'1010000110100100', '''agent:1 any:2''', '''open & stay''', '38fce2fe-711d-47af-883b-c07122f72e91', '<person><name>Lori Leonard</name><age>22</age></person>', '{"name": "Melissa Jordan", "age": 56, "city": "South Andrewstad"}', '{"id": 99, "data": "form", "active": true}', NULL, '{"yet","you","result"}', '[6,18)', '[2025-02-14 23:42:45,2025-05-24 02:48:57)'),
(-6273, -1525907512, 4204587390040541708, NULL, NULL, -1162965.35073199, -9487245959397.57, '$89322.12', 'XhjhEhyXGE', 'Good fast candidate real.', NULL, NULL, '1974-07-21 00:00:00', '1900-01-01 03:23:32', '02:35:10.723888+00', '2023-01-10 13:11:53', '2020-04-11 16:16:36+00', '141 days', NULL, 'sad', '(75.826286,-43.8267315)', '{6.87508798344985,273.21106836729,-43642.934869721}', '[(-124.211430,7.901321),(-153.159661,-5.9188875)]', '(171.736957,-88.320091),(112.909673,-13.305936)', NULL, '((162.554862,28.108888),(84.213655,35.8541995),(93.594051,-59.1957615))', '<(-45.952951,33.477721),44>', '181.146.0.0/24', '156.19.202.142', '32:2a:d8:78:a1:ff', '38:b5:fd:66:37:20:09:48', B'10010101', B'1010110011100011', '''explain:1 store:2''', NULL, '3fad8bee-fe2a-4d88-8b2a-03fd4663dd7a', '<person><name>Jessica Santos</name><age>80</age></person>', '{"name": "Thomas Smith", "age": 47, "city": "Lake Sean"}', '{"id": 195, "data": "quality", "active": true}', '{31,37,74}', NULL, '[53,70)', '[2025-01-22 18:59:55,2025-04-30 13:53:21)');

INSERT INTO "all_types_table" ("col_smallint_0", "col_integer_1", "col_bigint_2", "col_decimal_3", "col_numeric_4", "col_real_5", "col_double_precision_6", "col_money_10", "col_char_11", "col_varchar_12", "col_text_13", "col_bytea_14", "col_date_15", "col_time_16", "col_timetz_17", "col_timestamp_18", "col_timestamptz_19", "col_interval_20", "col_boolean_21", "col_enum_22", "col_point_23", "col_line_24", "col_lseg_25", "col_box_26", "col_path_27", "col_polygon_28", "col_circle_29", "col_cidr_30", "col_inet_31", "col_macaddr_32", "col_macaddr8_33", "col_bit_34", "col_varbit_35", "col_tsvector_36", "col_tsquery_37", "col_uuid_38", "col_xml_39", "col_json_40", "col_jsonb_41", "col_int_array_42", "col_text_array_43", "col_int4range_44", "col_tsrange_45") VALUES
(-20529, 798265722, NULL, 33997855.85, 12137.522, -21610361.24046, 9857.11828283239, '$95757.43', 'UNPQzAlufo', 'Sure meeting pick gun project ten almost southern.', 'Scientist year study interesting less. State nature ready keep. Bad and at rate tend friend.
Site bank community head quite.
Ever return poor paper join so. How always night society bag.
Each sister present provide color. Study attack vote since reveal possible group. Rate past real pattern.
Walk near by since. Military fight management ground top short know perhaps. Make chair believe break among music whatever. Easy specific force why make war stuff.
Opportunity up walk industry cup. Traditional wish follow increase the situation. Raise wish or.
Bed radio project black member top. Give popular simply behind start worry article.
Attack ask wide sign street Republican. Rather ground determine establish. Edge necessary west.
Hot send figure expert remember available need mother. Different scene benefit fill sense plant. Blue finally your significant happen night.
Local about me degree feeling ahead benefit. Heart them feeling guess challenge might type.', NULL, '1977-07-14 00:00:00', '1900-01-01 12:38:00', '02:07:42.949785+00', '2022-06-08 18:54:02', '2021-09-25 01:59:00+00', '265 days', False, 'sad', NULL, '{6330.6951061319,-30924.9632404472,4414.46221850186}', NULL, '(-8.981165,89.3930925),(66.460681,49.4439955)', NULL, '((-18.985141,-30.857141),(172.624289,-33.740021),(-63.968035,-86.334711))', '<(-101.017556,89.2673785),3>', '51.186.0.0/24', '151.148.101.180', 'de:4a:2f:f0:b2:03', '0a:b8:7c:16:5a:d5:0b:ed', NULL, B'1011011111010000', '''wife:1 other:2''', '''price & nice''', 'cd3917c4-7768-4ac0-8140-133718686f57', '<person><name>Matthew Davis PhD</name><age>62</age></person>', '{"name": "Matthew Edwards", "age": 20, "city": "Port Jeanne"}', '{"id": 679, "data": "stay", "active": false}', '{26,93,26}', '{"film","far","movement"}', '[51,89)', '[2025-02-25 14:02:19,2025-04-15 20:03:48)'),
(-26460, -1511601726, -7709170362527832233, 63472084.20, 79563.580, -8021633718.94514, -5842.3548309049, '$18520.45', 'KZqzsyAvVL', 'Seven determine despite low along quickly.', 'Under by by expert. Current foot action lawyer national current lay. Commercial drive project education fish.
Half guy north TV. Think finish smile heart road. Into news artist. Cell organization land general.
Probably exist them citizen believe huge. Red head field these race computer.
Physical tell serve fire dark. Evening conference event scene on several. Huge seek personal minute.
Resource watch there cost experience song notice. Its whether morning sometimes become everything. Technology your national occur lot suddenly project range.
Prepare here positive recently be game. Peace audience inside usually. And hand should couple middle physical beautiful new.
Major world chair vote recognize contain positive. Hear here so end successful. Affect able believe animal able south feel short.
Interest oil reduce city design partner require open.
Hit alone effect next face its. North spend environment fine specific threat. Class fine direction bad. Catch cultural lose by.', '\x1d229294a7237c7661e292b9694cf4de1199796396d65cf7e6fa21289dd3f675', '2014-12-01 00:00:00', '1900-01-01 23:09:57', '22:14:59.095166+00', '2024-08-26 20:50:08', '2024-06-11 21:18:01+00', '65 days', False, 'happy', '(96.729493,-19.4895425)', '{44929.601364997,8.8611529313734,-493356.566004462}', '[(27.140395,-34.106547),(-145.602157,-30.410418)]', '(104.325345,-47.3816135),(-25.144462,34.174110)', '[(86.216875,-14.715181),(-55.766906,-8.989413)]', NULL, '<(40.003447,22.001229),59>', '190.215.0.0/16', '64.135.169.111', 'b4:d6:d6:f8:5d:cf', 'f3:77:aa:2a:bb:1b:9b:b7', B'01101111', B'110100100111111', '''actually:1 entire:2''', '''even & finish''', 'e39cdc8f-09f7-456d-b205-f916514c323f', '<person><name>Nathaniel Briggs</name><age>58</age></person>', '{"name": "Mark Hill", "age": 29, "city": "Sherriside"}', '{"id": 168, "data": "today", "active": true}', '{9,39,16}', '{"none","compare","art"}', '[51,92)', '[2025-03-11 08:53:38,2025-05-28 04:01:41)'),
(12954, 416732131, -4996564574176913394, 9714596.97, 16561.447, -7764.11367241526, 693872217545.8, '$74657.32', 'qixUlpOEvr', 'Community member work maintain clear speak usually boy.', 'Game total lawyer. Tough everybody sister back. Carry during wrong data however church computer.
Worry there seat three policy. Read her drive research. Generation take chair boy article.
Effect know better gas carry myself recognize night. Practice nearly hospital test. Own follow none whose network upon care can.
Could them hear key worry building Democrat. Condition nor decision couple people. Determine finally a room before.
Popular safe industry rule. Year begin structure put technology series.
Million woman spring about light doctor fact. Make degree major.
Color control walk live teacher point hair under. Area race air ago different.
Technology girl information low view. Notice take where body direction inside assume. Wind for big else leader sort woman. Land lawyer run year Republican rise such.
Young college executive break by. Moment western bed show single.
Use age different drive forward. Responsibility laugh work five discuss media couple.', '\x9f0c35ce1b4a485d8f154eba171fad13edcd52e483ea5a0cde1432c6674a5aa2', '2009-06-13 00:00:00', '1900-01-01 02:57:54', '07:02:09.420476+00', '2022-05-23 21:48:03', '2023-09-19 14:20:41+00', '17 days', True, NULL, '(156.895379,63.7790655)', '{8023954953516.9,21245.7180408144,-918680.442184397}', '[(-17.849687,85.3925525),(-120.414663,-89.153368)]', '(-135.608867,-73.2730805),(-145.070393,88.2620915)', NULL, '((7.211521,89.5689395),(85.685611,56.9504455),(92.347870,51.523562))', '<(-71.337790,-5.460449),65>', NULL, NULL, 'bc:6a:b9:77:7f:9d', '16:85:56:f0:86:64:08:0b', NULL, B'100010110000101', '''suffer:1 across:2''', '''pass & research''', '11300198-cce6-445b-b9c2-eddc41e1dd67', '<person><name>Teresa Williams</name><age>18</age></person>', '{"name": "Ellen Watkins", "age": 35, "city": "New Gregoryshire"}', '{"id": 1000, "data": "style", "active": true}', '{41,14,10}', '{"computer","answer","opportunity"}', '[56,58)', '[2025-07-18 06:44:34,2025-08-04 14:05:03)'),
(21097, 2053606486, 267688602238474704, 65775725.10, 26510.365, -897098451552.87, 9004.96185266587, '$92767.07', 'RGXCGyMsyF', NULL, 'Almost at dream style. In trial detail officer doctor right.
Minute amount film turn see. Firm conference physical.
Card education bit of already own hundred past. Buy physical something in both. Pass even in idea focus.
Meeting inside bill building. Team mind forget blood. Red support call probably trip.
Onto mission remain seem piece.
Money force safe specific author especially. Base best magazine beat. Again grow color treatment song question.
Man rate quality hard debate address military. American loss yet west couple owner continue.
Detail continue computer land society mother. Push far above add on dark general fear.
Foot cell beat wind one example. Baby early scene meeting way opportunity matter.
In sound answer federal art. Father international suffer behind wear about.
Others none security blue arrive great strong. Challenge possible kind power machine sit debate still. Soon less protect candidate parent.
Admit hope about front. Food no prevent offer speak science manage.', '\x393c883b251e34fc4f0f9fbe271a6cccaafc17159020f89ac0b1c04d75a23f33', '1984-09-02 00:00:00', '1900-01-01 18:12:25', '13:32:28.548361+00', '2023-04-16 20:17:01', '2024-06-01 12:21:19+00', '3 days', True, 'sad', '(103.896930,-56.5757675)', '{-17908313907.669,86357.383482427,7268860282.52899}', '[(-50.898075,61.8884035),(15.335896,-65.2670215)]', '(-112.913393,81.355220),(-68.719430,-68.730610)', '[(7.983827,-52.3168095),(1.615367,-71.140501)]', '((-126.057371,-65.4296915),(69.329031,-25.0952975),(160.383182,-26.9577685))', NULL, '91.16.0.0/24', '78.252.89.247', '44:1e:13:dd:06:d5', '63:5a:53:d7:d5:7f:71:0f', B'11000001', B'1011100100111111', '''help:1 event:2''', '''never & across''', 'e476d902-3310-4f82-8c81-73db42c9250f', '<person><name>Jenna Marshall</name><age>24</age></person>', '{"name": "Melissa Maxwell", "age": 70, "city": "New Tiffany"}', '{"id": 341, "data": "run", "active": false}', '{17,55,66}', '{"near","leader","election"}', '[19,44)', '[2025-03-11 04:54:46,2025-04-14 22:10:14)'),
(-18297, 1563433084, 3089858671969797392, 31275857.22, 53637.815, 9.74390177878218, 43.7826845746661, '$68000.41', 'tirIuoNWGo', 'Person couple worker themselves might official finish.', 'But lay specific west exactly act. Project local rate reflect deal seven evening dinner. Thus me financial car.
Read city place position section better. Wonder war any particular manager myself.
City score important PM staff arrive sound. Boy security better make gun. Suddenly recently door prepare total respond with.
Whole teacher raise pass poor.
Forget line direction material security beat behavior.
Mission how voice factor card stock drop. Meet family serious local air grow. Off however usually picture.
Perhaps book your. Total language network number white consider campaign.
Three from condition discussion we quickly again. Become manager buy especially specific go. Individual free hand suffer record measure.
Agency for education. Hot common future gas money blood live authority. Catch unit hotel positive. Peace idea lose American.
Participant piece recognize push break. Particular world ten own stage technology manager. Bag civil party arm.', '\x5fd235778f9d22ae747440881e51ef59224b6ede209e5002fa6c8a29b1e7c86c', '2006-04-19 00:00:00', '1900-01-01 08:38:35', '10:08:58.865951+00', '2021-05-24 20:10:03', '2024-03-12 14:44:37+00', '154 days', True, 'happy', NULL, '{-46.3412620009506,-5867587584.61726,81188719235.1971}', '[(-25.915242,-34.253030),(-137.233148,38.1836135)]', '(-20.573344,-14.883961),(-14.138087,28.329242)', '[(-63.914578,23.515153),(-88.382558,-39.7401205)]', '((-106.259138,14.708047),(-154.343534,38.830258),(123.457392,-7.3111425))', '<(85.118755,31.532281),40>', '13.128.0.0/16', '106.55.44.241', 'f0:c4:e8:49:75:9b', '0e:e9:0c:bf:70:25:51:6a', B'10110110', B'1000010000001011', '''popular:1 more:2''', '''list & hear''', NULL, '<person><name>Stephanie Maxwell</name><age>74</age></person>', '{"name": "Jeffrey Edwards", "age": 60, "city": "East Joseborough"}', '{"id": 672, "data": "director", "active": false}', '{55,62,100}', '{"take","several","us"}', '[23,59)', '[2025-03-26 07:49:44,2025-05-31 17:44:11)');

INSERT INTO "all_types_table" ("col_smallint_0", "col_integer_1", "col_bigint_2", "col_decimal_3", "col_numeric_4", "col_real_5", "col_double_precision_6", "col_money_10", "col_char_11", "col_varchar_12", "col_text_13", "col_bytea_14", "col_date_15", "col_time_16", "col_timetz_17", "col_timestamp_18", "col_timestamptz_19", "col_interval_20", "col_boolean_21", "col_enum_22", "col_point_23", "col_line_24", "col_lseg_25", "col_box_26", "col_path_27", "col_polygon_28", "col_circle_29", "col_cidr_30", "col_inet_31", "col_macaddr_32", "col_macaddr8_33", "col_bit_34", "col_varbit_35", "col_tsvector_36", "col_tsquery_37", "col_uuid_38", "col_xml_39", "col_json_40", "col_jsonb_41", "col_int_array_42", "col_text_array_43", "col_int4range_44", "col_tsrange_45") VALUES
(-1248, -2092504516, -8613618355788057536, 46599067.38, NULL, 754183.268778072, 52.855838330508, '$78587.07', 'nqBYNVcZNr', 'Various natural see TV tonight sell offer.', 'Member success painting service morning. Require not she laugh other.
Stay tell sense break build free. And car relate son social. During camera sport trip simple turn.
Including hear store second analysis grow. When economy organization red reflect pick team bag. Knowledge factor yeah fall. Any significant industry state both second.
Bad above something indeed age Mr finish. Hope every people west theory writer. The trial arm second international painting.
Always PM shake recent. Throw doctor writer fund price within.
Item lawyer him surface quality. A thing economy like. Customer and like seat.
Only couple action us single for child. Leave church add. We and church special.
Can suffer glass say know physical. Natural democratic buy music. Price race knowledge democratic brother head pressure.
Above who medical prepare. Against rest form third allow assume.', '\x6d9437f2f4ffff357fee770150cb62af440edc58da5d4e42ecc374a73a88fac2', '1997-06-05 00:00:00', '1900-01-01 22:22:37', '09:56:42.487611+00', '2020-11-05 08:02:58', NULL, '280 days', True, NULL, '(-97.300960,-13.201839)', '{-99694657851.109,-5127980.8729557,61886194.56585}', '[(73.421670,44.0553735),(170.484427,11.7828495)]', '(11.026538,45.6852535),(-51.693775,82.3938925)', '[(-102.808874,-72.2428695),(-99.255379,34.0661185)]', '((-119.328829,14.8437575),(133.490459,78.4079605),(-100.436286,61.8485765))', '<(61.377609,-0.562633),63>', '175.186.0.0/16', '112.174.111.141', '4e:10:9d:81:4b:ee', '73:1d:20:a4:34:c0:0c:bd', B'01110010', B'1110000111101010', '''hand:1 anyone:2''', '''method & likely''', NULL, '<person><name>Christopher Alvarez</name><age>67</age></person>', '{"name": "Dr. Michelle Wallace", "age": 39, "city": "Mosesland"}', '{"id": 463, "data": "arrive", "active": true}', '{14,69,95}', '{"among","many","difficult"}', '[42,95)', NULL),
(-78, -275458410, 1104227389639410822, 2849165.39, 90128.794, -829738.894935068, -299806817.420041, '$73379.05', 'qTRrJeyXBR', 'Couple investment wide society.', 'Raise compare simply firm. Set hear do father artist.
Professor offer marriage truth soldier rate become. Become improve recent friend staff. Each key whose any new early follow play.
Research before base compare. Because drop himself design example.
Event help agreement key rock tell investment ten. Pm out student I. Ball step month society according with special.
Positive material me morning rather information business red.
Customer cultural add dinner professor yes. Be your case strong sister TV.
Sit office challenge feel money onto. Wait try east in ground over. Piece could meeting world father. They hit common condition effect respond staff.
Sense me church huge action. What author task simple me big society.
Guess nice between on office piece. Economic on thought increase so race.
Yet number table seem system add. Such social though page this drug. Small hit be level cold amount child where.
Military attorney peace recently environment see start.', '\xa9538e3843b9b5dc98faae58b83f15d02541272f554af87310a25c302736dc89', '2021-01-16 00:00:00', '1900-01-01 03:41:46', '20:48:50.049280+00', '2024-04-20 11:14:36', '2020-04-20 05:47:58+00', '47 days', NULL, 'neutral', NULL, '{-20094106400.3526,-78124.6851375592,713277463.1567}', NULL, '(-34.947592,30.5332125),(-8.056143,83.612987)', '[(-122.298778,62.212340),(172.744536,27.1715655)]', '((101.297805,36.5278725),(14.129611,-59.6620045),(108.066345,-14.8049855))', '<(40.344497,-10.4594145),66>', '107.59.0.0/24', NULL, '8a:48:c2:54:a3:7c', '4c:6c:78:18:61:99:ea:f9', B'00101111', B'1011101100010010', '''those:1 seat:2''', '''professional & challenge''', '6cc32f5f-6edf-430a-8165-5fb2248e25e0', '<person><name>Stephanie Garcia</name><age>58</age></person>', '{"name": "Shannon Wilson", "age": 18, "city": "West Colleen"}', '{"id": 653, "data": "region", "active": true}', '{39,38,16}', '{"thing","certain","available"}', '[19,22)', '[2025-02-10 03:30:26,2025-08-29 00:23:34)'),
(24145, -715931232, -2035248060720298310, 28111803.68, 16780.353, NULL, -67173.4774102149, '$94964.17', 'DIAATLEDCD', NULL, 'Organization the religious parent different.
Do already wind common of if hard. Need me room decade identify economy.
Week give green positive sure red quite interest.
Those use career voice want. Speech three soldier economy serve theory. South base name seem.
Sometimes growth almost give break go defense. Smile yard finish ten certainly consumer. Treatment home take allow interview.
Mouth second least. Seek green travel find task medical. Doctor front board right hour.
Year paper recently shoulder item people. Those part however authority majority fly.
Final evidence story team. Age letter leg join put.
Force course head issue. Tell radio consider low participant. Someone away fund.
Individual close policy game culture. Store kitchen health stock create call. Memory us view body sound leave.
Hundred degree bring control apply. Contain south kind during so specific.', '\xf9e4a30004cc4d965ae2c9a3c246adc39875d0f8442e5860d286cc783feab317', '1984-05-26 00:00:00', '1900-01-01 00:31:40', '23:13:50.047304+00', '2025-05-16 01:14:02', '2022-06-03 02:36:29+00', '201 days', True, 'sad', '(158.928447,-18.454012)', '{-50579.5721310716,8062768277.81602,71895183.834685}', '[(31.376523,-11.144119),(-170.793611,-36.0089745)]', '(79.732415,-11.4588545),(-17.299793,-19.8932145)', NULL, '((-117.548244,-27.185311),(160.519437,-49.958264),(-137.158418,-62.0234865))', '<(-173.131087,-86.9686585),20>', '39.72.0.0/24', '31.42.208.41', '6e:cf:9a:b1:27:eb', '3c:7c:03:0f:31:7a:9c:b3', B'11000001', B'110010010001101', '''sometimes:1 tonight:2''', '''ever & develop''', 'f6cb689c-e71e-4d01-93da-30a1982064d0', '<person><name>Anita Hart</name><age>52</age></person>', '{"name": "Terry Wilson", "age": 31, "city": "South John"}', '{"id": 807, "data": "party", "active": true}', '{88,73,95}', '{"actually","beautiful","around"}', '[39,95)', '[2025-01-31 05:10:10,2025-04-19 22:53:34)'),
(13813, -1554098635, 5371321145920123133, 90083363.76, NULL, -724.39780945187, NULL, '$88489.34', 'EIhqrmdYOz', 'Try type particularly success understand anyone number reduce.', 'Mind keep direction role heavy player. Loss card decide rule executive town. Laugh card provide. Where debate radio Congress.
Matter operation push hear. Our west way rest information defense for.
Series not market day option worker. Eye character seem.
Far think law short property five. Likely along gun evening dog. Nor line speak fund majority. Eat country debate and reason real.
Move fear significant understand necessary security shake wide. Its player remember network drive daughter. Visit way ever line.
Detail season wait west. Job organization indicate guy single fear partner.
Require bag activity evening cut happy against. Arrive despite foreign rest five conference begin wrong. Very along good responsibility Congress.
Apply person evidence color want since theory. Pressure around community once whole threat. Red sell dog clearly idea picture.
Similar learn expect low.
Option pass lose. Television attack appear born detail leave cell.', '\x42f527ce076501733dffafeda03e81eb2348fe19db13ff8bc49a70d8a69be9b0', '2002-03-24 00:00:00', '1900-01-01 22:54:01', '13:59:29.885802+00', NULL, '2023-11-15 16:43:08+00', '332 days', False, 'neutral', '(27.871694,65.0718085)', '{-9.57731710287077,9451817076.9473,27.34505961637}', '[(2.308202,27.4912675),(-118.866930,51.309340)]', '(-152.768596,-64.3771765),(-95.628415,15.473161)', '[(122.276986,-68.084966),(87.394312,65.150494)]', '((-21.919116,-16.822099),(5.457416,50.8455915),(36.082605,21.6781545))', '<(72.344352,39.8449455),30>', '146.170.0.0/16', NULL, '0c:a4:ac:76:a4:e0', '96:8f:7c:1e:08:bb:0f:cc', NULL, B'101110010100111', '''store:1 should:2''', '''particularly & decide''', '718e2649-f1a9-4d68-ba38-5c5fdee9ac5a', NULL, '{"name": "Rachel Brown", "age": 54, "city": "New Kristen"}', '{"id": 729, "data": "building", "active": false}', '{32,61,83}', '{"but","end","six"}', '[25,97)', '[2025-04-25 07:41:34,2025-08-26 19:51:11)'),
(-8280, 1616946626, 241249749346282362, 41635498.60, 11519.191, 8681.3860158988, 973177.8842038, '$96954.02', 'SNrunsfNuP', 'Go nearly structure along issue agent item onto.', 'A thought positive hand note. Level conference huge wide station compare.
Material himself firm.
Tax affect home herself lot daughter.
Without if well major for. Difference there citizen hour court first down. Gun religious firm be early.
Rich positive trouble employee good agent church. Remember outside push.
Home several project yeah. Field difficult clear ahead truth ahead project.
Ahead grow father where city mind. Sit service almost finish eat. Current store hear think. Over near site green.
Research back different economic year name. Special TV eat plant if sport animal. Anyone keep budget painting success.
Reach perform explain claim.
Three word role this second.
Trade hour half culture particularly model. Similar pick man marriage onto. Police base have image.
Someone home behind low always create. Remember join commercial increase my.
Fact most around local analysis. History discuss land street. Clearly trip suggest wish.', '\x4a9972a3298dc6877d669bb91de0e3580bd8b19e8c0db2ddbe8da708fc764b58', '1975-01-29 00:00:00', '1900-01-01 01:13:12', '07:28:42.157994+00', '2022-10-16 23:17:53', '2025-05-09 13:10:55+00', '328 days', False, 'happy', '(-36.602704,-59.208603)', '{8403936.5507648,-9684817.62999262,-2.20128703080614}', '[(13.048633,-89.041910),(-82.371458,38.537463)]', NULL, '[(-46.982202,58.7730675),(168.655288,-28.204890)]', '((169.152555,-24.5547575),(9.516698,25.383618),(175.676312,79.542995))', '<(146.598280,-26.982107),35>', '81.121.0.0/24', '188.238.149.171', '98:32:13:81:ec:49', NULL, B'00011110', B'10101001100011', '''civil:1 court:2''', '''opportunity & threat''', '33125d1c-f3c8-4a47-8db9-e626d67f3ef7', '<person><name>Michelle Brown</name><age>35</age></person>', '{"name": "Cindy Wilson", "age": 77, "city": "Torresborough"}', '{"id": 663, "data": "his", "active": false}', NULL, '{"including","receive","side"}', '[41,77)', '[2025-03-26 08:07:53,2025-05-30 07:34:26)');

