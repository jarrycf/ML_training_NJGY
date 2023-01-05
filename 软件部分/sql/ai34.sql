/*
 Navicat Premium Data Transfer

 Source Server         : 111111111111
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : ai34

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 01/12/2022 22:05:02
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version`  (
  `version_num` varchar(32) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL,
  PRIMARY KEY (`version_num`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = gbk COLLATE = gbk_chinese_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('ed798f493da5');

-- ----------------------------
-- Table structure for banji
-- ----------------------------
DROP TABLE IF EXISTS `banji`;
CREATE TABLE `banji`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET gbk COLLATE gbk_chinese_ci NULL DEFAULT NULL,
  `count` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = gbk COLLATE = gbk_chinese_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of banji
-- ----------------------------
INSERT INTO `banji` VALUES (1, '二班', 10);
INSERT INTO `banji` VALUES (2, '二班', 10);
INSERT INTO `banji` VALUES (3, '二班', 10);
INSERT INTO `banji` VALUES (4, '二班', 10);
INSERT INTO `banji` VALUES (5, '二班', 10);
INSERT INTO `banji` VALUES (6, '二班', 10);
INSERT INTO `banji` VALUES (7, '二班', 10);
INSERT INTO `banji` VALUES (8, '二班', 10);
INSERT INTO `banji` VALUES (9, '二班', 10);
INSERT INTO `banji` VALUES (10, '二班', 10);

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET gbk COLLATE gbk_chinese_ci NULL DEFAULT NULL,
  `age` int NULL DEFAULT NULL,
  `banji_id` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `banji_id`(`banji_id`) USING BTREE,
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`banji_id`) REFERENCES `banji` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = gbk COLLATE = gbk_chinese_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (1, '林青霞', 10, 1);
INSERT INTO `student` VALUES (2, '张无忌', 10, 1);
INSERT INTO `student` VALUES (3, '林青霞', 10, 2);
INSERT INTO `student` VALUES (4, '张无忌', 10, 2);
INSERT INTO `student` VALUES (5, '林青霞', 10, 3);
INSERT INTO `student` VALUES (6, '张无忌', 10, 3);
INSERT INTO `student` VALUES (7, '林青霞', 10, 4);
INSERT INTO `student` VALUES (8, '张无忌', 10, 4);
INSERT INTO `student` VALUES (9, '林青霞', 10, 5);
INSERT INTO `student` VALUES (10, '张无忌', 10, 5);
INSERT INTO `student` VALUES (11, '林青霞', 10, 6);
INSERT INTO `student` VALUES (12, '张无忌', 10, 6);
INSERT INTO `student` VALUES (13, '林青霞', 10, 7);
INSERT INTO `student` VALUES (14, '张无忌', 10, 7);
INSERT INTO `student` VALUES (15, '林青霞', 10, 8);
INSERT INTO `student` VALUES (16, '张无忌', 10, 8);
INSERT INTO `student` VALUES (17, '林青霞', 10, 9);
INSERT INTO `student` VALUES (18, '张无忌', 10, 9);
INSERT INTO `student` VALUES (19, '林青霞', 10, 10);
INSERT INTO `student` VALUES (20, '张无忌', 10, 10);

SET FOREIGN_KEY_CHECKS = 1;
