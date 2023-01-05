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

 Date: 02/12/2022 09:11:05
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for stu_score
-- ----------------------------
DROP TABLE IF EXISTS `stu_score`;
CREATE TABLE `stu_score`  (
  `sno` int NOT NULL AUTO_INCREMENT,
  `chinese` int NULL DEFAULT NULL,
  `math` int NULL DEFAULT NULL,
  `class` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '无',
  PRIMARY KEY (`sno`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 101 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of stu_score
-- ----------------------------
INSERT INTO `stu_score` VALUES (1, 78, 67, 'all low');
INSERT INTO `stu_score` VALUES (2, 100, 78, 'all good');
INSERT INTO `stu_score` VALUES (3, 99, 82, 'all good');
INSERT INTO `stu_score` VALUES (4, 79, 67, 'all low');
INSERT INTO `stu_score` VALUES (5, 67, 87, 'low chinese');
INSERT INTO `stu_score` VALUES (6, 94, 86, 'all good');
INSERT INTO `stu_score` VALUES (7, 62, 58, 'all low');
INSERT INTO `stu_score` VALUES (8, 74, 87, 'low chinese');
INSERT INTO `stu_score` VALUES (9, 78, 75, 'all low');
INSERT INTO `stu_score` VALUES (10, 100, 91, 'all good');
INSERT INTO `stu_score` VALUES (11, 82, 83, 'all good');
INSERT INTO `stu_score` VALUES (12, 64, 89, 'low chinese');
INSERT INTO `stu_score` VALUES (13, 60, 92, 'low chinese');
INSERT INTO `stu_score` VALUES (14, 97, 67, 'low math');
INSERT INTO `stu_score` VALUES (15, 55, 55, 'all low');
INSERT INTO `stu_score` VALUES (16, 100, 65, 'low math');
INSERT INTO `stu_score` VALUES (17, 76, 64, 'all low');
INSERT INTO `stu_score` VALUES (18, 64, 65, 'all low');
INSERT INTO `stu_score` VALUES (19, 90, 64, 'low math');
INSERT INTO `stu_score` VALUES (20, 85, 92, 'all good');
INSERT INTO `stu_score` VALUES (21, 87, 81, 'all good');
INSERT INTO `stu_score` VALUES (22, 65, 91, 'low chinese');
INSERT INTO `stu_score` VALUES (23, 55, 79, 'low chinese');
INSERT INTO `stu_score` VALUES (24, 97, 78, 'all good');
INSERT INTO `stu_score` VALUES (25, 78, 66, 'all low');
INSERT INTO `stu_score` VALUES (26, 70, 99, 'low chinese');
INSERT INTO `stu_score` VALUES (27, 83, 73, 'low math');
INSERT INTO `stu_score` VALUES (28, 70, 97, 'low chinese');
INSERT INTO `stu_score` VALUES (29, 77, 91, 'all good');
INSERT INTO `stu_score` VALUES (30, 92, 93, 'all good');
INSERT INTO `stu_score` VALUES (31, 83, 90, 'all good');
INSERT INTO `stu_score` VALUES (32, 90, 97, 'all good');
INSERT INTO `stu_score` VALUES (33, 93, 76, 'low math');
INSERT INTO `stu_score` VALUES (34, 60, 84, 'low chinese');
INSERT INTO `stu_score` VALUES (35, 77, 75, 'all low');
INSERT INTO `stu_score` VALUES (36, 100, 83, 'all good');
INSERT INTO `stu_score` VALUES (37, 60, 92, 'low chinese');
INSERT INTO `stu_score` VALUES (38, 75, 63, 'all low');
INSERT INTO `stu_score` VALUES (39, 67, 65, 'all low');
INSERT INTO `stu_score` VALUES (40, 59, 81, 'low chinese');
INSERT INTO `stu_score` VALUES (41, 70, 71, 'all low');
INSERT INTO `stu_score` VALUES (42, 57, 83, 'low chinese');
INSERT INTO `stu_score` VALUES (43, 62, 87, 'low chinese');
INSERT INTO `stu_score` VALUES (44, 82, 85, 'all good');
INSERT INTO `stu_score` VALUES (45, 85, 78, 'all good');
INSERT INTO `stu_score` VALUES (46, 96, 57, 'low math');
INSERT INTO `stu_score` VALUES (47, 70, 70, 'all low');
INSERT INTO `stu_score` VALUES (48, 78, 74, 'all low');
INSERT INTO `stu_score` VALUES (49, 61, 98, 'low chinese');
INSERT INTO `stu_score` VALUES (50, 97, 62, 'low math');
INSERT INTO `stu_score` VALUES (51, 58, 94, 'low chinese');
INSERT INTO `stu_score` VALUES (52, 81, 96, 'all good');
INSERT INTO `stu_score` VALUES (53, 87, 57, 'low math');
INSERT INTO `stu_score` VALUES (54, 89, 97, 'all good');
INSERT INTO `stu_score` VALUES (55, 73, 73, 'all low');
INSERT INTO `stu_score` VALUES (56, 93, 68, 'low math');
INSERT INTO `stu_score` VALUES (57, 73, 64, 'all low');
INSERT INTO `stu_score` VALUES (58, 64, 57, 'all low');
INSERT INTO `stu_score` VALUES (59, 73, 65, 'all low');
INSERT INTO `stu_score` VALUES (60, 93, 86, 'all good');
INSERT INTO `stu_score` VALUES (61, 57, 91, 'low chinese');
INSERT INTO `stu_score` VALUES (62, 89, 55, 'low math');
INSERT INTO `stu_score` VALUES (63, 65, 89, 'low chinese');
INSERT INTO `stu_score` VALUES (64, 85, 96, 'all good');
INSERT INTO `stu_score` VALUES (65, 70, 96, 'low chinese');
INSERT INTO `stu_score` VALUES (66, 57, 99, 'low chinese');
INSERT INTO `stu_score` VALUES (67, 88, 79, 'all good');
INSERT INTO `stu_score` VALUES (68, 73, 82, 'low chinese');
INSERT INTO `stu_score` VALUES (69, 63, 85, 'low chinese');
INSERT INTO `stu_score` VALUES (70, 58, 99, 'low chinese');
INSERT INTO `stu_score` VALUES (71, 73, 97, 'low chinese');
INSERT INTO `stu_score` VALUES (72, 93, 90, 'all good');
INSERT INTO `stu_score` VALUES (73, 100, 66, 'low math');
INSERT INTO `stu_score` VALUES (74, 56, 73, 'all low');
INSERT INTO `stu_score` VALUES (75, 78, 55, 'all low');
INSERT INTO `stu_score` VALUES (76, 91, 74, 'low math');
INSERT INTO `stu_score` VALUES (77, 87, 65, 'low math');
INSERT INTO `stu_score` VALUES (78, 64, 78, 'low chinese');
INSERT INTO `stu_score` VALUES (79, 85, 93, 'all good');
INSERT INTO `stu_score` VALUES (80, 84, 67, 'low math');
INSERT INTO `stu_score` VALUES (81, 70, 78, 'all low');
INSERT INTO `stu_score` VALUES (82, 57, 90, 'low chinese');
INSERT INTO `stu_score` VALUES (83, 86, 100, 'all good');
INSERT INTO `stu_score` VALUES (84, 99, 61, 'low math');
INSERT INTO `stu_score` VALUES (85, 78, 82, 'all good');
INSERT INTO `stu_score` VALUES (86, 96, 85, 'all good');
INSERT INTO `stu_score` VALUES (87, 59, 67, 'all low');
INSERT INTO `stu_score` VALUES (88, 69, 98, 'low chinese');
INSERT INTO `stu_score` VALUES (89, 60, 77, 'low chinese');
INSERT INTO `stu_score` VALUES (90, 92, 67, 'low math');
INSERT INTO `stu_score` VALUES (91, 61, 88, 'low chinese');
INSERT INTO `stu_score` VALUES (92, 92, 65, 'low math');
INSERT INTO `stu_score` VALUES (93, 75, 65, 'all low');
INSERT INTO `stu_score` VALUES (94, 74, 72, 'all low');
INSERT INTO `stu_score` VALUES (95, 87, 82, 'all good');
INSERT INTO `stu_score` VALUES (96, 91, 61, 'low math');
INSERT INTO `stu_score` VALUES (97, 82, 91, 'all good');
INSERT INTO `stu_score` VALUES (98, 83, 75, 'low math');
INSERT INTO `stu_score` VALUES (99, 82, 59, 'low math');
INSERT INTO `stu_score` VALUES (100, 100, 79, 'all good');

SET FOREIGN_KEY_CHECKS = 1;
