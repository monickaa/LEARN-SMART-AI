-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 22, 2024 at 10:11 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1studenmarkanadb`
--

-- --------------------------------------------------------

--
-- Table structure for table `answertb`
--

CREATE TABLE `answertb` (
  `id` bigint(10) NOT NULL auto_increment,
  `RegNo` varchar(250) NOT NULL,
  `subject` varchar(250) NOT NULL,
  `mark1` decimal(10,2) NOT NULL,
  `mark2` decimal(10,2) NOT NULL,
  `mark3` decimal(10,2) NOT NULL,
  `mark4` decimal(10,2) NOT NULL,
  `mark5` decimal(10,2) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `Result` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `answertb`
--

INSERT INTO `answertb` (`id`, `RegNo`, `subject`, `mark1`, `mark2`, `mark3`, `mark4`, `mark5`, `total`, `Result`) VALUES
(1, '844101', 'BASICCS', '1.00', '0.69', '0.72', '0.90', '0.73', '4.05', 'fail'),
(2, '21MCA083', 'IYear', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', 'fail'),
(3, '844101', 'Java', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', 'fail'),
(4, '844101', 'Java', '0.28', '0.24', '0.00', '0.00', '0.00', '0.10', 'fail');

-- --------------------------------------------------------

--
-- Table structure for table `coursetb`
--

CREATE TABLE `coursetb` (
  `id` bigint(10) NOT NULL auto_increment,
  `Department` varchar(250) NOT NULL,
  `Batch` varchar(250) NOT NULL,
  `Year` varchar(250) NOT NULL,
  `Cname` varchar(500) NOT NULL,
  `Curl` varchar(500) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `coursetb`
--

INSERT INTO `coursetb` (`id`, `Department`, `Batch`, `Year`, `Cname`, `Curl`) VALUES
(1, 'CSE', '2021-2023', 'IYear', 'Java', 'https://www.youtube.com/embed/eIrMbAQSU34?si=YZtfmNKnnjbcx8PO'),
(3, 'CSE', '2021-2023', 'IYear', 'AI', 'https://www.youtube.com/embed/JMUxmLyrhSk?si=FUYBp0ur2j68IbGX');

-- --------------------------------------------------------

--
-- Table structure for table `questiontb`
--

CREATE TABLE `questiontb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Department` varchar(250) NOT NULL,
  `Batch` varchar(250) NOT NULL,
  `Year` varchar(250) NOT NULL,
  `Q1` varchar(500) NOT NULL,
  `A1` varchar(500) NOT NULL,
  `Q2` varchar(500) NOT NULL,
  `A2` varchar(500) NOT NULL,
  `Q3` varchar(500) NOT NULL,
  `A3` varchar(500) NOT NULL,
  `Q4` varchar(500) NOT NULL,
  `A4` varchar(500) NOT NULL,
  `Q5` varchar(500) NOT NULL,
  `A5` varchar(500) NOT NULL,
  `Subject` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `questiontb`
--

INSERT INTO `questiontb` (`id`, `Department`, `Batch`, `Year`, `Q1`, `A1`, `Q2`, `A2`, `Q3`, `A3`, `Q4`, `A4`, `Q5`, `A5`, `Subject`) VALUES
(1, 'CSE', '2022-2024', 'IIIYear', 'Define computer', 'Computer is a fast operating device which processes the input data into desired information.', 'Define RAM?', 'RAM is a volatile memory that contains temporary data that can be accessed at high speed.', 'Define system software', 'A set of program that governs the operation of a computer system and makes the hardware works. It controls the internal operations of the computer.\r\n\r\n', 'What is application software?', 'Software which is used to solve a specific task is called application software.', 'What is Algorithm?', 'Algorithm means the logic of a program. It is a step by step description of a program.', 'BASICCS'),
(2, 'CSE', '2021-2023', 'IYear', 'Define computer', 'Computer is a fast operating device which processes the input data into desired information.', 'Define RAM?', 'RAM is a volatile memory that contains temporary data that can be accessed at high speed.', 'Define system software', 'A set of program that governs the operation of a computer system and makes the hardware works. It controls the internal operations of the computer', 'What is application software?', 'Software which is used to solve a specific task is called application software.', 'What is Algorithm?', 'Algorithm means the logic of a program. It is a step by step description of a program.', 'Java');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `Name`, `Mobile`, `Email`, `UserName`, `Password`) VALUES
(1, 'sangeeth Kumar', '9486365535', 'sangeeth5535@gmail.com', 'san', 'san'),
(2, 'akash', '9486365535', 'sangeeth5535@gmail.com', 'akash', 'akash'),
(3, 'ahamad', '9486365535', 'sangeeth5535@gmail.com', 'ahamad', 'ahamad');

-- --------------------------------------------------------

--
-- Table structure for table `studenttb`
--

CREATE TABLE `studenttb` (
  `id` bigint(20) NOT NULL auto_increment,
  `RegisterNo` varchar(250) NOT NULL,
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `Department` varchar(250) NOT NULL,
  `Batch` varchar(250) NOT NULL,
  `Year` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `studenttb`
--

INSERT INTO `studenttb` (`id`, `RegisterNo`, `Name`, `Gender`, `Mobile`, `Email`, `Address`, `Department`, `Batch`, `Year`) VALUES
(1, '844101', 'sangeeth', 'male', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'CSE', '2021-2023', 'IYear'),
(4, '21MCA083', 'ahamad', 'male', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'CSE', '2022-2024', 'IYear');

-- --------------------------------------------------------

--
-- Table structure for table `temptb`
--

CREATE TABLE `temptb` (
  `id` bigint(10) NOT NULL auto_increment,
  `regno` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `temptb`
--

