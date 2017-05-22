/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50529
Source Host           : 127.0.0.1:3306
Source Database       : fetcher_data

Target Server Type    : MYSQL
Target Server Version : 50529
File Encoding         : 65001

Date: 2017-05-21 22:18:04
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `dir_test`
-- ----------------------------
DROP TABLE IF EXISTS `dir_test`;
CREATE TABLE `dir_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(1000) NOT NULL,
  `title` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=136 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of dir_test
-- ----------------------------
INSERT INTO `dir_test` VALUES ('127', 'https://www.douban.com/note/620593810/', '真相在生活的缝隙里无所不在');
INSERT INTO `dir_test` VALUES ('128', 'https://www.douban.com/note/620437829/', '土澳三宝之自拍鼠！它真的爱笑爱自拍么？');
INSERT INTO `dir_test` VALUES ('129', 'https://www.douban.com/note/620001161/', '听歌时不要随机播放');
INSERT INTO `dir_test` VALUES ('130', 'https://www.douban.com/note/620430751/', '草木识小｜樱花落了，樱桃红了');
INSERT INTO `dir_test` VALUES ('131', 'https://www.douban.com/note/620727479/', '清单 | 糙汉茶の初夏ROUTINE');
INSERT INTO `dir_test` VALUES ('132', 'https://www.douban.com/note/620412184/', '“因为你是我的眼”：一个视障极客和他要改变的世界');
INSERT INTO `dir_test` VALUES ('133', 'https://www.douban.com/note/620349035/', '来富良野感受仓本聪创造的温柔时间吧');
INSERT INTO `dir_test` VALUES ('134', 'https://www.douban.com/note/614580469/', '巴黎之外的法国——从第戎到里昂');
INSERT INTO `dir_test` VALUES ('135', 'https://www.douban.com/note/620614133/', '克拉科夫与奥斯维辛');
