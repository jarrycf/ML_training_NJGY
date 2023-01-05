/*
 Navicat Premium Data Transfer

 Source Server         : 111111111111
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : aitrain

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 06/12/2022 08:11:09
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for home_score
-- ----------------------------
DROP TABLE IF EXISTS `home_score`;
CREATE TABLE `home_score`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `house_age` float NULL DEFAULT NULL,
  `nearest_mrt` float NULL DEFAULT NULL,
  `stores` float NULL DEFAULT NULL,
  `price_area` float NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of home_score
-- ----------------------------
INSERT INTO `home_score` VALUES (2, 32, 84.8788, 10, 50.061);
INSERT INTO `home_score` VALUES (3, 55, 84.8788, 10, 104.184);
INSERT INTO `home_score` VALUES (4, 32, 84.8788, 10, 50.061);
INSERT INTO `home_score` VALUES (5, 19.5, 306.595, 9, 42.3664);
INSERT INTO `home_score` VALUES (6, 13.3, 561.984, 5, 40.31);
INSERT INTO `home_score` VALUES (7, 33.6, 371.25, 8, 41.1632);
INSERT INTO `home_score` VALUES (8, 3.5, 56.4743, 7, 56.1349);
INSERT INTO `home_score` VALUES (9, 30.3, 4510.36, 1, 21.8849);
INSERT INTO `home_score` VALUES (10, 13.3, 336.053, 5, 45.0255);
INSERT INTO `home_score` VALUES (11, 11, 1931.21, 2, 28.1052);
INSERT INTO `home_score` VALUES (12, 32, 84.8788, 10, 50.061);
INSERT INTO `home_score` VALUES (13, 19.5, 306.595, 9, 42.3664);
INSERT INTO `home_score` VALUES (14, 13.3, 561.984, 5, 40.31);
INSERT INTO `home_score` VALUES (15, 13.3, 561.984, 5, 40.31);
INSERT INTO `home_score` VALUES (16, 5, 390.568, 5, 48.9198);
INSERT INTO `home_score` VALUES (17, 7.1, 2175.03, 3, 28.4017);
INSERT INTO `home_score` VALUES (18, 34.5, 623.473, 7, 38.03);
INSERT INTO `home_score` VALUES (19, 20.3, 287.603, 6, 40.7397);
INSERT INTO `home_score` VALUES (20, 31.7, 5512.04, 1, 19.9908);
INSERT INTO `home_score` VALUES (21, 17.9, 1783.18, 3, 24.9527);
INSERT INTO `home_score` VALUES (22, 34.8, 405.213, 1, 36.4996);
INSERT INTO `home_score` VALUES (23, 6.3, 90.4561, 9, 54.2971);
INSERT INTO `home_score` VALUES (24, 13, 492.231, 5, 41.8801);
INSERT INTO `home_score` VALUES (25, 20.4, 2469.65, 4, 21.6198);
INSERT INTO `home_score` VALUES (26, 13.2, 1164.84, 4, 32.0038);
INSERT INTO `home_score` VALUES (27, 35.7, 579.208, 2, 36.99);
INSERT INTO `home_score` VALUES (28, 0, 292.998, 6, 52.4247);
INSERT INTO `home_score` VALUES (29, 17.7, 350.852, 1, 41.8003);
INSERT INTO `home_score` VALUES (30, 16.9, 368.136, 8, 40.6049);
INSERT INTO `home_score` VALUES (31, 1.5, 23.3828, 7, 58.1069);
INSERT INTO `home_score` VALUES (32, 4.5, 2275.88, 3, 29.7364);
INSERT INTO `home_score` VALUES (33, 10.5, 279.173, 7, 46.0801);
INSERT INTO `home_score` VALUES (34, 14.7, 1360.14, 1, 30.3546);
INSERT INTO `home_score` VALUES (35, 10.1, 279.173, 7, 46.3467);
INSERT INTO `home_score` VALUES (36, 39.6, 480.698, 4, 42.4911);
INSERT INTO `home_score` VALUES (37, 29.3, 1487.87, 2, 26.6633);
INSERT INTO `home_score` VALUES (38, 3.1, 383.862, 5, 50.0141);
INSERT INTO `home_score` VALUES (39, 10.4, 276.449, 5, 48.3139);
INSERT INTO `home_score` VALUES (40, 19.2, 557.478, 4, 38.257);
INSERT INTO `home_score` VALUES (41, 7.1, 451.244, 5, 46.3993);
INSERT INTO `home_score` VALUES (42, 25.9, 4519.69, 0, 16.7764);
INSERT INTO `home_score` VALUES (43, 29.6, 769.403, 7, 33.484);
INSERT INTO `home_score` VALUES (44, 37.9, 488.573, 1, 37.0966);
INSERT INTO `home_score` VALUES (45, 16.5, 323.655, 6, 42.0553);
INSERT INTO `home_score` VALUES (46, 15.4, 205.367, 7, 44.5078);
INSERT INTO `home_score` VALUES (47, 13.9, 4079.42, 0, 23.092);
INSERT INTO `home_score` VALUES (48, 14.7, 1935.01, 2, 26.0334);
INSERT INTO `home_score` VALUES (49, 12, 1360.14, 1, 31.8253);
INSERT INTO `home_score` VALUES (50, 3.1, 577.961, 6, 44.8536);
INSERT INTO `home_score` VALUES (51, 16.2, 289.325, 5, 44.2006);
INSERT INTO `home_score` VALUES (52, 13.6, 4082.01, 0, 23.3689);
INSERT INTO `home_score` VALUES (53, 16.8, 4066.59, 0, 20.7267);
INSERT INTO `home_score` VALUES (54, 36.1, 519.462, 5, 38.8778);
INSERT INTO `home_score` VALUES (55, 34.4, 512.787, 6, 37.824);
INSERT INTO `home_score` VALUES (56, 2.7, 533.476, 4, 47.9331);
INSERT INTO `home_score` VALUES (57, 36.6, 488.819, 8, 43.508);
INSERT INTO `home_score` VALUES (58, 21.7, 463.962, 9, 39.7895);
INSERT INTO `home_score` VALUES (59, 35.9, 640.739, 3, 37.2771);
INSERT INTO `home_score` VALUES (60, 24.2, 4605.75, 0, 16.3671);
INSERT INTO `home_score` VALUES (61, 29.4, 4510.36, 1, 21.0725);
INSERT INTO `home_score` VALUES (62, 21.7, 512.549, 4, 37.9227);
INSERT INTO `home_score` VALUES (63, 31.3, 1758.41, 1, 25.3157);
INSERT INTO `home_score` VALUES (64, 32.1, 1438.58, 3, 28.5878);
INSERT INTO `home_score` VALUES (65, 13.3, 492.231, 5, 41.6931);
INSERT INTO `home_score` VALUES (66, 16.1, 289.325, 5, 44.2638);
INSERT INTO `home_score` VALUES (67, 31.7, 1160.63, 0, 26.2198);
INSERT INTO `home_score` VALUES (68, 33.6, 371.25, 8, 41.1632);
INSERT INTO `home_score` VALUES (69, 3.5, 56.4743, 7, 56.1349);
INSERT INTO `home_score` VALUES (70, 30.3, 4510.36, 1, 21.8849);
INSERT INTO `home_score` VALUES (71, 13.3, 336.053, 5, 45.0255);
INSERT INTO `home_score` VALUES (72, 11, 1931.21, 2, 28.1052);
INSERT INTO `home_score` VALUES (73, 5.3, 259.661, 6, 50.7037);
INSERT INTO `home_score` VALUES (74, 17.2, 2175.88, 3, 23.0661);
INSERT INTO `home_score` VALUES (75, 2.6, 533.476, 4, 47.9726);
INSERT INTO `home_score` VALUES (76, 17.5, 995.755, 0, 30.3856);
INSERT INTO `home_score` VALUES (77, 40.1, 123.743, 8, 50.1085);
INSERT INTO `home_score` VALUES (78, 1, 193.585, 6, 54.5153);
INSERT INTO `home_score` VALUES (79, 8.5, 104.81, 5, 53.8708);
INSERT INTO `home_score` VALUES (80, 30.4, 464.223, 6, 36.3391);
INSERT INTO `home_score` VALUES (81, 12.5, 561.984, 5, 40.7996);
INSERT INTO `home_score` VALUES (82, 6.6, 90.4561, 9, 54.0955);
INSERT INTO `home_score` VALUES (83, 35.5, 640.739, 3, 37.0135);
INSERT INTO `home_score` VALUES (84, 32.5, 424.544, 8, 39.9177);
INSERT INTO `home_score` VALUES (85, 13.8, 4082.01, 0, 23.1825);
INSERT INTO `home_score` VALUES (86, 6.8, 379.557, 10, 51.4864);
INSERT INTO `home_score` VALUES (87, 12.3, 1360.14, 1, 31.6595);
INSERT INTO `home_score` VALUES (88, 35.9, 616.4, 3, 37.5254);
INSERT INTO `home_score` VALUES (89, 20.5, 2185.13, 3, 22.2178);
INSERT INTO `home_score` VALUES (90, 38.2, 552.437, 2, 38.9166);
INSERT INTO `home_score` VALUES (91, 18, 1414.84, 1, 28.2396);
INSERT INTO `home_score` VALUES (92, 11.8, 533.476, 4, 43.0116);
INSERT INTO `home_score` VALUES (93, 30.8, 377.796, 6, 37.6227);
INSERT INTO `home_score` VALUES (94, 13.2, 150.935, 7, 47.2233);
INSERT INTO `home_score` VALUES (95, 25.3, 2707.39, 3, 21.7061);
INSERT INTO `home_score` VALUES (96, 15.1, 383.28, 7, 40.9601);
INSERT INTO `home_score` VALUES (97, 0, 338.968, 9, 52.5376);
INSERT INTO `home_score` VALUES (98, 1.8, 1455.8, 1, 36.0474);
INSERT INTO `home_score` VALUES (99, 16.9, 4066.59, 0, 20.6556);
INSERT INTO `home_score` VALUES (100, 8.9, 1406.43, 0, 31.4986);
INSERT INTO `home_score` VALUES (101, 23, 3947.95, 0, 18.1776);
INSERT INTO `home_score` VALUES (102, 0, 274.014, 1, 50.2381);
INSERT INTO `home_score` VALUES (103, 9.1, 1402.02, 0, 31.4245);
INSERT INTO `home_score` VALUES (104, 20.6, 2469.65, 4, 21.6184);
INSERT INTO `home_score` VALUES (105, 31.9, 1146.33, 0, 26.3579);
INSERT INTO `home_score` VALUES (106, 40.9, 167.599, 5, 47.3869);
INSERT INTO `home_score` VALUES (107, 8, 104.81, 5, 54.1932);
INSERT INTO `home_score` VALUES (108, 6.4, 90.4561, 9, 54.23);
INSERT INTO `home_score` VALUES (109, 28.4, 617.442, 3, 35.2666);
INSERT INTO `home_score` VALUES (110, 16.4, 289.325, 5, 44.0748);
INSERT INTO `home_score` VALUES (111, 6.4, 90.4561, 9, 54.23);
INSERT INTO `home_score` VALUES (112, 17.5, 964.75, 4, 32.5229);
INSERT INTO `home_score` VALUES (113, 12.7, 170.129, 1, 48.0721);
INSERT INTO `home_score` VALUES (114, 1.1, 193.585, 6, 54.4744);
INSERT INTO `home_score` VALUES (115, 0, 208.391, 6, 54.5168);
INSERT INTO `home_score` VALUES (116, 32.7, 392.446, 6, 38.1458);
INSERT INTO `home_score` VALUES (117, 0, 292.998, 6, 52.4247);
INSERT INTO `home_score` VALUES (118, 17.2, 189.518, 8, 43.8092);
INSERT INTO `home_score` VALUES (119, 12.2, 1360.14, 1, 31.7147);
INSERT INTO `home_score` VALUES (120, 31.4, 592.501, 2, 35.4031);
INSERT INTO `home_score` VALUES (121, 4, 2147.38, 3, 30.4542);
INSERT INTO `home_score` VALUES (122, 8.1, 104.81, 5, 54.1292);
INSERT INTO `home_score` VALUES (123, 33.3, 196.617, 7, 41.3043);
INSERT INTO `home_score` VALUES (124, 9.9, 2102.43, 3, 26.9862);
INSERT INTO `home_score` VALUES (125, 14.8, 393.261, 6, 41.6219);
INSERT INTO `home_score` VALUES (126, 30.6, 143.838, 8, 41.991);
INSERT INTO `home_score` VALUES (127, 20.6, 737.916, 2, 35.4831);
INSERT INTO `home_score` VALUES (128, 30.9, 6396.28, 1, 11.2018);
INSERT INTO `home_score` VALUES (129, 13.6, 4197.35, 0, 23.2904);
INSERT INTO `home_score` VALUES (130, 25.3, 1583.72, 3, 25.2308);
INSERT INTO `home_score` VALUES (131, 16.6, 289.325, 5, 43.9498);
INSERT INTO `home_score` VALUES (132, 13.3, 492.231, 5, 41.6931);
INSERT INTO `home_score` VALUES (133, 13.6, 492.231, 5, 41.5069);
INSERT INTO `home_score` VALUES (134, 31.5, 414.948, 4, 38.1388);
INSERT INTO `home_score` VALUES (135, 0, 185.43, 0, 46.3959);
INSERT INTO `home_score` VALUES (136, 9.9, 279.173, 7, 46.4799);
INSERT INTO `home_score` VALUES (137, 1.1, 193.585, 6, 54.4744);
INSERT INTO `home_score` VALUES (138, 38.6, 804.69, 4, 38.8188);
INSERT INTO `home_score` VALUES (139, 3.8, 383.862, 5, 49.6831);
INSERT INTO `home_score` VALUES (140, 41.3, 124.991, 6, 48.7389);
INSERT INTO `home_score` VALUES (141, 38.5, 216.833, 7, 45.3518);
INSERT INTO `home_score` VALUES (142, 29.6, 535.527, 8, 37.3232);
INSERT INTO `home_score` VALUES (143, 4, 2147.38, 3, 30.4542);
INSERT INTO `home_score` VALUES (144, 26.6, 482.758, 5, 36.1942);
INSERT INTO `home_score` VALUES (145, 18, 373.394, 8, 39.9952);
INSERT INTO `home_score` VALUES (146, 33.4, 186.969, 6, 41.2777);
INSERT INTO `home_score` VALUES (147, 18.9, 1009.23, 0, 29.58);
INSERT INTO `home_score` VALUES (148, 11.4, 390.568, 5, 45.0514);
INSERT INTO `home_score` VALUES (149, 13.6, 319.071, 6, 43.971);
INSERT INTO `home_score` VALUES (150, 10, 942.466, 0, 34.7502);
INSERT INTO `home_score` VALUES (151, 12.9, 492.231, 5, 41.9426);
INSERT INTO `home_score` VALUES (152, 16.2, 289.325, 5, 44.2006);
INSERT INTO `home_score` VALUES (153, 5.1, 1559.83, 3, 33.3463);
INSERT INTO `home_score` VALUES (154, 19.8, 640.607, 5, 35.4298);
INSERT INTO `home_score` VALUES (155, 13.6, 492.231, 5, 41.5069);
INSERT INTO `home_score` VALUES (156, 11.9, 1360.14, 1, 31.8807);
INSERT INTO `home_score` VALUES (157, 2.1, 451.244, 5, 48.9512);
INSERT INTO `home_score` VALUES (158, 0, 185.43, 0, 46.3959);
INSERT INTO `home_score` VALUES (159, 3.2, 489.882, 8, 46.3712);
INSERT INTO `home_score` VALUES (160, 16.4, 3780.59, 0, 21.3058);
INSERT INTO `home_score` VALUES (161, 34.9, 179.454, 8, 43.9086);
INSERT INTO `home_score` VALUES (162, 35.8, 170.731, 7, 43.2325);
INSERT INTO `home_score` VALUES (163, 4.9, 387.772, 9, 48.9947);
INSERT INTO `home_score` VALUES (164, 12, 1360.14, 1, 31.8253);
INSERT INTO `home_score` VALUES (165, 6.5, 376.171, 6, 47.2586);
INSERT INTO `home_score` VALUES (166, 16.9, 4066.59, 0, 20.6556);
INSERT INTO `home_score` VALUES (167, 13.8, 4082.01, 0, 23.1825);
INSERT INTO `home_score` VALUES (168, 30.7, 1264.73, 0, 25.3871);
INSERT INTO `home_score` VALUES (169, 16.1, 815.931, 4, 35.4391);
INSERT INTO `home_score` VALUES (170, 11.6, 390.568, 5, 44.9222);
INSERT INTO `home_score` VALUES (171, 15.5, 815.931, 4, 35.7592);
INSERT INTO `home_score` VALUES (172, 3.5, 49.661, 8, 56.12);
INSERT INTO `home_score` VALUES (173, 19.2, 616.4, 3, 38.0162);
INSERT INTO `home_score` VALUES (174, 16, 4066.59, 0, 21.3223);
INSERT INTO `home_score` VALUES (175, 8.5, 104.81, 5, 53.8708);
INSERT INTO `home_score` VALUES (176, 0, 185.43, 0, 46.3959);
INSERT INTO `home_score` VALUES (177, 13.7, 1236.56, 1, 32.0614);
INSERT INTO `home_score` VALUES (178, 0, 292.998, 6, 52.4247);
INSERT INTO `home_score` VALUES (179, 28.2, 330.085, 8, 38.9717);
INSERT INTO `home_score` VALUES (180, 27.6, 515.112, 5, 35.6453);
INSERT INTO `home_score` VALUES (181, 8.4, 1962.63, 1, 29.8317);
INSERT INTO `home_score` VALUES (182, 24, 4527.69, 0, 16.648);
INSERT INTO `home_score` VALUES (183, 3.6, 383.862, 5, 49.7797);
INSERT INTO `home_score` VALUES (184, 6.6, 90.4561, 9, 54.0955);
INSERT INTO `home_score` VALUES (185, 41.3, 401.881, 4, 45.2427);
INSERT INTO `home_score` VALUES (186, 4.3, 432.039, 7, 46.6121);
INSERT INTO `home_score` VALUES (187, 30.2, 472.174, 3, 37.384);
INSERT INTO `home_score` VALUES (188, 13.9, 4573.78, 0, 22.5349);
INSERT INTO `home_score` VALUES (189, 33, 181.077, 9, 45.3671);
INSERT INTO `home_score` VALUES (190, 13.1, 1144.44, 4, 32.3162);
INSERT INTO `home_score` VALUES (191, 14, 438.851, 1, 42.4397);
INSERT INTO `home_score` VALUES (192, 26.9, 4449.27, 0, 17.2457);
INSERT INTO `home_score` VALUES (193, 11.6, 201.894, 8, 47.0465);
INSERT INTO `home_score` VALUES (194, 13.5, 2147.38, 3, 24.7787);
INSERT INTO `home_score` VALUES (195, 17, 4082.01, 0, 20.5651);
INSERT INTO `home_score` VALUES (196, 14.1, 2615.47, 0, 23.9073);
INSERT INTO `home_score` VALUES (197, 31.4, 1447.29, 3, 28.0955);
INSERT INTO `home_score` VALUES (198, 20.9, 2185.13, 3, 22.1671);
INSERT INTO `home_score` VALUES (199, 8.9, 3078.18, 0, 27.5165);
INSERT INTO `home_score` VALUES (200, 34.8, 190.039, 8, 43.7248);
INSERT INTO `home_score` VALUES (201, 16.3, 4066.59, 0, 21.0934);
INSERT INTO `home_score` VALUES (202, 35.3, 616.573, 8, 41.4657);
INSERT INTO `home_score` VALUES (203, 13.2, 750.07, 2, 39.2276);
INSERT INTO `home_score` VALUES (204, 43.8, 57.5895, 7, 54.2936);
INSERT INTO `home_score` VALUES (205, 9.7, 421.479, 5, 45.4603);
INSERT INTO `home_score` VALUES (206, 15.2, 3771.9, 0, 22.1912);
INSERT INTO `home_score` VALUES (207, 15.2, 461.102, 5, 41.1572);
INSERT INTO `home_score` VALUES (208, 22.8, 707.907, 2, 35.0225);
INSERT INTO `home_score` VALUES (209, 34.4, 126.729, 8, 44.0876);
INSERT INTO `home_score` VALUES (210, 34, 157.605, 7, 42.194);
INSERT INTO `home_score` VALUES (211, 18.2, 451.642, 8, 38.6383);
INSERT INTO `home_score` VALUES (212, 17.4, 995.755, 0, 30.4354);
INSERT INTO `home_score` VALUES (213, 13.1, 561.984, 5, 40.4319);
INSERT INTO `home_score` VALUES (214, 38.3, 642.698, 3, 39.2241);
INSERT INTO `home_score` VALUES (215, 15.6, 289.325, 5, 44.5822);
INSERT INTO `home_score` VALUES (216, 18, 1414.84, 1, 28.2396);
INSERT INTO `home_score` VALUES (217, 12.8, 1449.72, 3, 30.0679);
INSERT INTO `home_score` VALUES (218, 22.2, 379.557, 10, 45.0262);
INSERT INTO `home_score` VALUES (219, 38.5, 665.064, 3, 39.2311);
INSERT INTO `home_score` VALUES (220, 11.5, 1360.14, 1, 32.1021);
INSERT INTO `home_score` VALUES (221, 34.8, 175.629, 8, 43.8677);
INSERT INTO `home_score` VALUES (222, 5.2, 390.568, 5, 48.8131);
INSERT INTO `home_score` VALUES (223, 0, 274.014, 1, 50.2381);
INSERT INTO `home_score` VALUES (224, 17.6, 1805.67, 2, 25.5257);
INSERT INTO `home_score` VALUES (225, 6.2, 90.4561, 9, 54.364);
INSERT INTO `home_score` VALUES (226, 18.1, 1783.18, 3, 24.8844);
INSERT INTO `home_score` VALUES (227, 19.2, 383.713, 8, 39.3197);
INSERT INTO `home_score` VALUES (228, 37.8, 590.929, 1, 36.1576);
INSERT INTO `home_score` VALUES (229, 28, 372.624, 6, 37.2699);
INSERT INTO `home_score` VALUES (230, 13.6, 492.231, 5, 41.5069);
INSERT INTO `home_score` VALUES (231, 29.3, 529.777, 8, 37.237);
INSERT INTO `home_score` VALUES (232, 37.2, 186.51, 9, 49.3573);
INSERT INTO `home_score` VALUES (233, 9, 1402.02, 0, 31.476);
INSERT INTO `home_score` VALUES (234, 30.6, 431.111, 10, 47.3796);
INSERT INTO `home_score` VALUES (235, 9.1, 1402.02, 0, 31.4245);
INSERT INTO `home_score` VALUES (236, 34.5, 324.942, 6, 39.9782);
INSERT INTO `home_score` VALUES (237, 1.1, 193.585, 6, 54.4744);
INSERT INTO `home_score` VALUES (238, 16.5, 4082.01, 0, 20.9256);
INSERT INTO `home_score` VALUES (239, 32.4, 265.061, 8, 41.324);
INSERT INTO `home_score` VALUES (240, 11.9, 3171.33, 0, 25.0084);
INSERT INTO `home_score` VALUES (241, 31, 1156.41, 0, 26.0754);
INSERT INTO `home_score` VALUES (242, 4, 2147.38, 3, 30.4542);
INSERT INTO `home_score` VALUES (243, 16.2, 4074.74, 0, 21.1595);
INSERT INTO `home_score` VALUES (244, 27.1, 4412.77, 1, 19.7032);
INSERT INTO `home_score` VALUES (245, 39.7, 333.368, 9, 52.6404);
INSERT INTO `home_score` VALUES (246, 8, 2216.61, 4, 26.8509);
INSERT INTO `home_score` VALUES (247, 12.9, 250.631, 7, 45.1221);
INSERT INTO `home_score` VALUES (248, 3.6, 373.839, 10, 53.4345);
INSERT INTO `home_score` VALUES (249, 13, 732.853, 0, 35.5302);
INSERT INTO `home_score` VALUES (250, 12.8, 732.853, 0, 35.6331);
INSERT INTO `home_score` VALUES (251, 18.1, 837.723, 0, 31.6978);
INSERT INTO `home_score` VALUES (252, 11, 1712.63, 2, 29.5546);
INSERT INTO `home_score` VALUES (253, 13.7, 250.631, 7, 44.5968);
INSERT INTO `home_score` VALUES (254, 2, 2077.39, 3, 31.8986);
INSERT INTO `home_score` VALUES (255, 32.8, 204.171, 8, 42.2105);
INSERT INTO `home_score` VALUES (256, 4.8, 1559.83, 3, 33.5072);
INSERT INTO `home_score` VALUES (257, 7.5, 639.62, 5, 42.3284);
INSERT INTO `home_score` VALUES (258, 16.4, 389.822, 6, 40.7381);
INSERT INTO `home_score` VALUES (259, 21.7, 1055.07, 0, 27.9659);
INSERT INTO `home_score` VALUES (260, 19, 1009.23, 0, 29.5332);
INSERT INTO `home_score` VALUES (261, 18, 6306.15, 1, 11.9417);
INSERT INTO `home_score` VALUES (262, 39.2, 424.713, 7, 44.756);
INSERT INTO `home_score` VALUES (263, 31.7, 1159.45, 0, 26.2266);
INSERT INTO `home_score` VALUES (264, 5.9, 90.4561, 9, 54.5639);
INSERT INTO `home_score` VALUES (265, 30.4, 1735.59, 2, 25.7906);
INSERT INTO `home_score` VALUES (266, 1.1, 329.975, 5, 52.0833);
INSERT INTO `home_score` VALUES (267, 31.5, 5512.04, 1, 19.7374);
INSERT INTO `home_score` VALUES (268, 14.6, 339.229, 1, 43.8147);
INSERT INTO `home_score` VALUES (269, 17.3, 444.133, 1, 40.459);
INSERT INTO `home_score` VALUES (270, 0, 292.998, 6, 52.4247);
INSERT INTO `home_score` VALUES (271, 17.7, 837.723, 0, 31.8986);
INSERT INTO `home_score` VALUES (272, 17, 1485.1, 4, 26.802);
INSERT INTO `home_score` VALUES (273, 16.2, 2288.01, 3, 23.0052);
INSERT INTO `home_score` VALUES (274, 15.9, 289.325, 5, 44.3907);
INSERT INTO `home_score` VALUES (275, 3.9, 2147.38, 3, 30.5159);
INSERT INTO `home_score` VALUES (276, 32.6, 493.657, 7, 37.5514);
INSERT INTO `home_score` VALUES (277, 15.7, 815.931, 4, 35.6516);
INSERT INTO `home_score` VALUES (278, 17.8, 1783.18, 3, 24.9875);
INSERT INTO `home_score` VALUES (279, 34.7, 482.758, 5, 38.2393);
INSERT INTO `home_score` VALUES (280, 17.2, 390.568, 5, 41.4153);
INSERT INTO `home_score` VALUES (281, 17.6, 837.723, 0, 31.9492);
INSERT INTO `home_score` VALUES (282, 10.8, 252.582, 1, 47.5266);
INSERT INTO `home_score` VALUES (283, 17.7, 451.642, 8, 38.8479);
INSERT INTO `home_score` VALUES (284, 13, 492.231, 5, 41.8801);
INSERT INTO `home_score` VALUES (285, 13.2, 170.129, 1, 47.7848);
INSERT INTO `home_score` VALUES (286, 27.5, 394.017, 7, 36.9277);
INSERT INTO `home_score` VALUES (287, 1.5, 23.3828, 7, 58.1069);
INSERT INTO `home_score` VALUES (288, 19.1, 461.102, 5, 38.9746);
INSERT INTO `home_score` VALUES (289, 21.2, 2185.13, 3, 22.1365);
INSERT INTO `home_score` VALUES (290, 0, 208.391, 6, 54.5168);
INSERT INTO `home_score` VALUES (291, 2.6, 1554.25, 3, 34.6724);
INSERT INTO `home_score` VALUES (292, 2.3, 184.33, 6, 54.183);
INSERT INTO `home_score` VALUES (293, 4.7, 387.772, 9, 49.112);
INSERT INTO `home_score` VALUES (294, 2, 1455.8, 1, 35.9767);
INSERT INTO `home_score` VALUES (295, 33.5, 1978.67, 2, 27.2492);
INSERT INTO `home_score` VALUES (296, 15, 383.28, 7, 41.0186);
INSERT INTO `home_score` VALUES (297, 30.1, 718.294, 3, 34.0439);
INSERT INTO `home_score` VALUES (298, 5.9, 90.4561, 9, 54.5639);
INSERT INTO `home_score` VALUES (299, 19.2, 461.102, 5, 38.9246);
INSERT INTO `home_score` VALUES (300, 16.6, 323.691, 6, 41.9951);
INSERT INTO `home_score` VALUES (301, 13.9, 289.325, 5, 45.6899);
INSERT INTO `home_score` VALUES (302, 37.7, 490.345, 0, 33.1);
INSERT INTO `home_score` VALUES (303, 3.4, 56.4743, 7, 56.1916);
INSERT INTO `home_score` VALUES (304, 17.5, 395.675, 5, 41.1369);
INSERT INTO `home_score` VALUES (305, 12.6, 383.28, 7, 42.4823);
INSERT INTO `home_score` VALUES (306, 26.4, 335.527, 6, 37.9395);
INSERT INTO `home_score` VALUES (307, 18.2, 2179.59, 3, 22.7359);
INSERT INTO `home_score` VALUES (308, 12.5, 1144.44, 4, 32.6418);
INSERT INTO `home_score` VALUES (309, 34.9, 567.035, 4, 37.5404);
INSERT INTO `home_score` VALUES (310, 16.7, 4082.01, 0, 20.7791);
INSERT INTO `home_score` VALUES (311, 33.2, 121.726, 10, 50.6879);
INSERT INTO `home_score` VALUES (312, 2.5, 156.244, 4, 56.5892);
INSERT INTO `home_score` VALUES (313, 38, 461.785, 0, 33.4785);
INSERT INTO `home_score` VALUES (314, 16.5, 2288.01, 3, 22.8914);
INSERT INTO `home_score` VALUES (315, 38.3, 439.711, 0, 33.8151);
INSERT INTO `home_score` VALUES (316, 20, 1626.08, 3, 25.4485);
INSERT INTO `home_score` VALUES (317, 16.2, 289.325, 5, 44.2006);
INSERT INTO `home_score` VALUES (318, 14.4, 169.98, 1, 47.0821);
INSERT INTO `home_score` VALUES (319, 10.3, 3079.89, 0, 26.3278);
INSERT INTO `home_score` VALUES (320, 16.4, 289.325, 5, 44.0748);
INSERT INTO `home_score` VALUES (321, 30.3, 1264.73, 0, 25.3055);
INSERT INTO `home_score` VALUES (322, 16.4, 1643.5, 2, 27.2266);
INSERT INTO `home_score` VALUES (323, 21.3, 537.797, 4, 37.6396);
INSERT INTO `home_score` VALUES (324, 35.4, 318.529, 9, 46.651);
INSERT INTO `home_score` VALUES (325, 8.3, 104.81, 5, 54.0005);
INSERT INTO `home_score` VALUES (326, 3.7, 577.961, 6, 44.5517);
INSERT INTO `home_score` VALUES (327, 15.6, 1756.41, 2, 26.7575);
INSERT INTO `home_score` VALUES (328, 13.3, 250.631, 7, 44.8584);
INSERT INTO `home_score` VALUES (329, 15.6, 752.767, 2, 37.8222);
INSERT INTO `home_score` VALUES (330, 7.1, 379.557, 10, 51.3088);
INSERT INTO `home_score` VALUES (331, 34.6, 272.678, 5, 40.8604);
INSERT INTO `home_score` VALUES (332, 13.5, 4197.35, 0, 23.3874);
INSERT INTO `home_score` VALUES (333, 16.9, 964.75, 4, 32.8024);
INSERT INTO `home_score` VALUES (334, 12.9, 187.482, 1, 47.619);
INSERT INTO `home_score` VALUES (335, 28.6, 197.134, 6, 40.1997);
INSERT INTO `home_score` VALUES (336, 12.4, 1712.63, 2, 28.7586);
INSERT INTO `home_score` VALUES (337, 36.6, 488.819, 8, 43.508);
INSERT INTO `home_score` VALUES (338, 4.1, 56.4743, 7, 55.7873);
INSERT INTO `home_score` VALUES (339, 3.5, 757.338, 3, 44.0895);
INSERT INTO `home_score` VALUES (340, 15.9, 1497.71, 3, 28.0483);
INSERT INTO `home_score` VALUES (341, 13.6, 4197.35, 0, 23.2904);
INSERT INTO `home_score` VALUES (342, 32, 1156.78, 0, 26.3274);
INSERT INTO `home_score` VALUES (343, 25.6, 4519.69, 0, 16.7301);
INSERT INTO `home_score` VALUES (344, 39.8, 617.713, 2, 39.8248);
INSERT INTO `home_score` VALUES (345, 7.8, 104.81, 5, 54.3204);
INSERT INTO `home_score` VALUES (346, 30, 1013.34, 5, 30.398);
INSERT INTO `home_score` VALUES (347, 27.3, 337.602, 6, 37.8362);
INSERT INTO `home_score` VALUES (348, 5.1, 1867.23, 2, 31.9989);
INSERT INTO `home_score` VALUES (349, 31.3, 600.86, 5, 35.1288);
INSERT INTO `home_score` VALUES (350, 31.5, 258.186, 9, 43.7526);
INSERT INTO `home_score` VALUES (351, 1.7, 329.975, 5, 51.8572);
INSERT INTO `home_score` VALUES (352, 33.6, 270.889, 0, 33.8485);
INSERT INTO `home_score` VALUES (353, 13, 750.07, 2, 39.3421);
INSERT INTO `home_score` VALUES (354, 5.7, 90.4561, 9, 54.6962);
INSERT INTO `home_score` VALUES (355, 33.5, 563.285, 8, 39.8063);
INSERT INTO `home_score` VALUES (356, 34.6, 3085.17, 0, 24.849);
INSERT INTO `home_score` VALUES (357, 0, 185.43, 0, 46.3959);
INSERT INTO `home_score` VALUES (358, 13.2, 1712.63, 2, 28.3168);
INSERT INTO `home_score` VALUES (359, 17.4, 6488.02, 1, 10.7451);
INSERT INTO `home_score` VALUES (360, 4.6, 259.661, 6, 51.1019);
INSERT INTO `home_score` VALUES (361, 7.8, 104.81, 5, 54.3204);
INSERT INTO `home_score` VALUES (362, 13.2, 492.231, 5, 41.7554);
INSERT INTO `home_score` VALUES (363, 4, 2180.25, 3, 30.3415);
INSERT INTO `home_score` VALUES (364, 18.4, 2674.96, 3, 21.4238);
INSERT INTO `home_score` VALUES (365, 4.1, 2147.38, 3, 30.3924);
INSERT INTO `home_score` VALUES (366, 12.2, 1360.14, 1, 31.7147);
INSERT INTO `home_score` VALUES (367, 3.8, 383.862, 5, 49.6831);
INSERT INTO `home_score` VALUES (368, 10.3, 211.447, 1, 48.5683);
INSERT INTO `home_score` VALUES (369, 0, 338.968, 9, 52.5376);
INSERT INTO `home_score` VALUES (370, 1.1, 193.585, 6, 54.4744);
INSERT INTO `home_score` VALUES (371, 5.6, 2408.99, 0, 30.0707);
INSERT INTO `home_score` VALUES (372, 32.9, 87.3022, 10, 50.6674);
INSERT INTO `home_score` VALUES (373, 41.4, 281.205, 8, 51.451);
INSERT INTO `home_score` VALUES (374, 17.1, 967.4, 4, 32.6706);
INSERT INTO `home_score` VALUES (375, 32.3, 109.946, 10, 50.0851);
INSERT INTO `home_score` VALUES (376, 35.3, 614.139, 7, 38.8847);
INSERT INTO `home_score` VALUES (377, 17.3, 2261.43, 4, 22.3934);
INSERT INTO `home_score` VALUES (378, 14.2, 1801.54, 1, 27.2969);
INSERT INTO `home_score` VALUES (379, 15, 1828.32, 2, 26.5562);
INSERT INTO `home_score` VALUES (380, 18.2, 350.852, 1, 41.5123);
INSERT INTO `home_score` VALUES (381, 20.2, 2185.13, 3, 22.2631);
INSERT INTO `home_score` VALUES (382, 15.9, 289.325, 5, 44.3907);
INSERT INTO `home_score` VALUES (383, 4.1, 312.896, 5, 51.1855);
INSERT INTO `home_score` VALUES (384, 33.9, 157.605, 7, 42.1384);
INSERT INTO `home_score` VALUES (385, 0, 274.014, 1, 50.2381);
INSERT INTO `home_score` VALUES (386, 5.4, 390.568, 5, 48.705);
INSERT INTO `home_score` VALUES (387, 21.7, 1157.99, 0, 27.0928);
INSERT INTO `home_score` VALUES (388, 14.7, 1717.19, 2, 27.4901);
INSERT INTO `home_score` VALUES (389, 3.9, 49.661, 8, 55.8783);
INSERT INTO `home_score` VALUES (390, 37.3, 587.888, 8, 44.1472);
INSERT INTO `home_score` VALUES (391, 0, 292.998, 6, 52.4247);
INSERT INTO `home_score` VALUES (392, 14.1, 289.325, 5, 45.5581);
INSERT INTO `home_score` VALUES (393, 8, 132.547, 9, 52.1907);
INSERT INTO `home_score` VALUES (394, 16.3, 3529.56, 0, 21.5708);
INSERT INTO `home_score` VALUES (395, 29.1, 506.114, 4, 36.4948);
INSERT INTO `home_score` VALUES (396, 16.1, 4066.59, 0, 21.2453);
INSERT INTO `home_score` VALUES (397, 18.3, 82.8864, 10, 49.8048);
INSERT INTO `home_score` VALUES (398, 0, 185.43, 0, 46.3959);
INSERT INTO `home_score` VALUES (399, 16.2, 2103.55, 3, 23.754);
INSERT INTO `home_score` VALUES (400, 10.4, 2251.94, 4, 25.3539);
INSERT INTO `home_score` VALUES (401, 40.9, 122.362, 8, 51.3074);
INSERT INTO `home_score` VALUES (402, 32.8, 377.83, 9, 43.8559);
INSERT INTO `home_score` VALUES (403, 6.2, 1939.75, 1, 31.2643);
INSERT INTO `home_score` VALUES (404, 42.7, 443.802, 6, 48.6623);
INSERT INTO `home_score` VALUES (405, 16.9, 967.4, 4, 32.765);
INSERT INTO `home_score` VALUES (406, 32.6, 4136.27, 1, 24.8244);
INSERT INTO `home_score` VALUES (407, 21.2, 512.549, 4, 38.1353);
INSERT INTO `home_score` VALUES (408, 37.1, 918.636, 1, 33.2949);
INSERT INTO `home_score` VALUES (409, 13.1, 1164.84, 4, 32.0573);
INSERT INTO `home_score` VALUES (410, 14.7, 1717.19, 2, 27.4901);

SET FOREIGN_KEY_CHECKS = 1;
